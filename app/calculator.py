########################
# Calculator Class      #
########################

from decimal import Decimal
import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

import pandas as pd

from app.calculation import Calculation
from app.calculator_config import CalculatorConfig
from app.calculator_momento import CalculatorMemento
from app.exceptions import OperationError, ValidationError
from app.history import HistoryObserver
from app.input_validators import InputValidator
from app.operations import Operation
from app.logger import Logger

Number = Union[int,float,Decimal]
CalculationResult = Union[Number, str]

class Calculator:
    def __init__(self,config: Optional[CalculatorConfig] = None):
        if config is None:
            current_file = Path(__file__)
            project_root = current_file.parent.parent
            config = CalculatorConfig(base_dir=project_root)
        Logger._setup_logging(config)
        self.config = config
        self.config.validate()
        self.history: List[Calculation] = []
        self.operation_strategy: Optional[Operation] = None
        self.observers: List[HistoryObserver] = []

        self.undo_stack: List[CalculatorMemento] = []
        self.redo_stack: List[CalculatorMemento] = []

        self._setup_directories()
        try:
            self.load_history()
        except Exception as e:
            Logger.warnLog(f"Could not load existing history: {e}")
        Logger.infoLog("Calculator initialized with configuration")
    def _setup_directories(self) -> None:
        self.config.history_dir.mkdir(parents=True, exist_ok=True)
    def add_observer(self, observer: HistoryObserver) -> None:
        self.observers.append(observer)
        Logger.infoLog(f"Added observer: {observer.__class__.__name__}")
    
    def remove_observer(self, observer: HistoryObserver) -> None:
        self.observers.remove(observer)
        Logger.infoLog(f"Removed observer: {observer.__class__.__name__}")
    def notify_observers(self, calculation: Calculation) -> None:
        for observer in self.observers:
            observer.update(calculation)
    def set_operation(self, operation: Operation) -> None:
        """
        Set the current operation strategy.

        Assigns the operation strategy that will be used for performing calculations.
        This is part of the Strategy pattern, allowing the calculator to switch between
        different operation algorithms dynamically.

        Args:
            operation (Operation): The operation strategy to be set.
        """
        self.operation_strategy = operation
        Logger.infoLog(f"Set operation: {operation}")
    def perform_operation(
            self,
            a: Union[str, Number],
            b: Union[str, Number],
    ) -> CalculationResult:
        if not self.operation_strategy:
            raise OperationError("No operation set")
        try: 
            validated_a = InputValidator.validate_number(a, self.config)
            validated_b = InputValidator.validate_number(b, self.config)
            result = self.operation_strategy.execute(validated_a, validated_b)
            calculation = Calculation(
                operation = str(self.operation_strategy),
                operand1 = validated_a,
                operand2 = validated_b,
            )
            self.undo_stack.append(CalculatorMemento(self.history.copy()))

            self.redo_stack.clear()

            self.history.append(calculation)
            return result
        except ValidationError as e:
            Logger.errorLog(f"Operation failed: {str(e)}")
            raise
        except Exception as e:
            Logger.errorLog(f"Operation failed: {str(e)}")
            raise OperationError(f"Operation failed: {str(e)}")
    def save_history(self) -> None:
        try:
            self.config.history_dir.mkdir(parents=True, exist_ok=True)

            history_data = []
            for calc in self.history:
                history_data.append({
                    'operation': str(calc.operation),
                    'operand1': str(calc.operand1),
                    'operand2': str(calc.operand2),
                    'result': str(calc.result),
                    'timestamp': calc.timestamp.isoformat()
                })
            if history_data: 
                df = pd.DataFrame(history_data)
                df.to_csv(self.config.history_file, index=False)
                Logger.infoLog(f"History saved successfully to {self.config.history_file}")
            else: #pragma: no cover
                pd.DataFrame(columns =['operation','operand1','operand2','result','timestamp']
                             ).to_csv(self.config.history_file, index=False)
                Logger.infoLog("Empty history saved")
        except Exception as e: #pragma: no cover
            Logger.errorLog(f"Failed to save history: {e}")
            raise OperationError(f"Failed to save history: {e}")
    def load_history(self) -> None:
        """
        Load calculation history from a CSV file using pandas.

        Reads the calculation history from a CSV file and reconstructs the
        Calculation instances, restoring the calculator's history.

        Raises:
            OperationError: If loading the history fails.
        """
        try:
            if self.config.history_file.exists():
                # Read the CSV file into a pandas DataFrame
                df = pd.read_csv(self.config.history_file)
                if not df.empty:
                    # Deserialize each row into a Calculation instance
                    self.history = [
                        Calculation.from_dict({
                            'operation': row['operation'],
                            'operand1': row['operand1'],
                            'operand2': row['operand2'],
                            'result': row['result'],
                            'timestamp': row['timestamp']
                        })
                        for _, row in df.iterrows()
                    ]
                    Logger.infoLog(f"Loaded {len(self.history)} calculations from history")
                else:
                    Logger.infoLog("Loaded empty history file") 
            else: #pragma: no cover
                # If no history file exists, start with an empty history
                Logger.infoLog("No history file found - starting with empty history")
        except Exception as e: 
            # Log and raise an OperationError if loading fails
            Logger.errorLog(f"Failed to load history: {e}")
            raise OperationError(f"Failed to load history: {e}")
    def get_history_dataframe(self) -> pd.DataFrame: #pragma: no cover
        """
        Get calculation history as a pandas DataFrame.

        Converts the list of Calculation instances into a pandas DataFrame for
        advanced data manipulation or analysis.

        Returns:
            pd.DataFrame: DataFrame containing the calculation history.
        """
        history_data = []
        for calc in self.history:
            history_data.append({
                'operation': str(calc.operation),
                'operand1': str(calc.operand1),
                'operand2': str(calc.operand2),
                'result': str(calc.result),
                'timestamp': calc.timestamp
            })
        return pd.DataFrame(history_data)

    def show_history(self) -> List[str]:
        """
        Get formatted history of calculations.

        Returns a list of human-readable strings representing each calculation.

        Returns:
            List[str]: List of formatted calculation history entries.
        """
        return [
            f"{calc.operation}({calc.operand1}, {calc.operand2}) = {calc.result}"
            for calc in self.history
        ] #pragma: no cover

    def clear_history(self) -> None:
        """
        Clear calculation history.

        Empties the calculation history and clears the undo and redo stacks.
        """
        self.history.clear()
        self.undo_stack.clear()
        self.redo_stack.clear()
        Logger.infoLog("History cleared")
    def undo(self) -> bool:
            """
            Undo the last operation.

            Restores the calculator's history to the state before the last calculation
            was performed.

            Returns:
                bool: True if an operation was undone, False if there was nothing to undo.
            """
            if not self.undo_stack:
                return False
            # Pop the last state from the undo stack
            memento = self.undo_stack.pop()
            # Push the current state onto the redo stack
            self.redo_stack.append(CalculatorMemento(self.history.copy()))
            # Restore the history from the memento
            self.history = memento.history.copy()
            return True

    def redo(self) -> bool:
            """
            Redo the previously undone operation.

            Restores the calculator's history to the state before the last undo.

            Returns:
                bool: True if an operation was redone, False if there was nothing to redo.
            """
            if not self.redo_stack:
                return False
            # Pop the last state from the redo stack
            memento = self.redo_stack.pop()
            # Push the current state onto the undo stack
            self.undo_stack.append(CalculatorMemento(self.history.copy()))
            # Restore the history from the memento
            self.history = memento.history.copy()
            return True