########################
# Calculator REPL       #
########################

from decimal import Decimal
from app.logger import Logger
from app.calculator import Calculator
from app.exceptions import OperationError, ValidationError
from app.history import AutoSaveObserver, LoggingObserver
from app.operations import OperationFactory
from app.color import Color
from colorama import Fore, Back, Style, init
from termcolor import colored
def Calculator_repl(): 
    """
    Command-line interface for the calculator.

    Implements a Read-Eval-Print Loop (REPL) that continuously prompts the user
    for commands, processes arithmetic operations, and manages calculation history.
    """
    try:
        # Initialize the Calculator instance
        calc = Calculator()
        # Register observers for logging and auto-saving history
        calc.add_observer(LoggingObserver())
        calc.add_observer(AutoSaveObserver(calc))

        Color.printColorOutput("Calculator started. Type 'help' for commands.", "yellow", "bright")

        while True:
            try:
                # Prompt the user for a command
                command = Color.printColorInput("\nEnter command: ", "white") 

                if command == 'help':
                    # Display available commands
                    Color.printColorOutput("\nAvailable commands:", "blue")
                    Color.printColorOutput("  add, subtract (sub), multiply (mult), divide (div), power (exp), root, integer division (idiv),\n\n  modulus (mod), percentage(perc), absolute difference (absv) - Perform calculations","blue", "bright")
                    Color.printColorOutput("  undo - Undo the last calculation","yellow")
                    Color.printColorOutput("  redo - Redo the last undone calculation","yellow")
                    Color.printColorOutput("  history - Show calculation history","green")
                    Color.printColorOutput("  save - Save calculation history to file","green")
                    Color.printColorOutput("  load - Load calculation history from file","green")
                    Color.printColorOutput("  clear - Clear calculation history", "red")
                    Color.printColorOutput("  exit - Exit the calculator", "red")
                    continue

                if command == 'exit':
                    # Attempt to save history before exiting
                    try:
                        calc.save_history()
                        Color.printColorOutput("History saved successfully.", "green", "bright")
                    except Exception as e: 
                        Color.printError(f"Warning: Could not save history: {e}")
                    Color.printColorOutput("Goodbye!", "white", "dim")
                    break

                if command == 'history': 
                    # Display calculation history
                    history = calc.show_history()
                    if not history:
                        Color.printColorOutput("No calculations in history", "red")
                    else:
                        Color.printColorOutput("\nCalculation History:", "green")
                        for i, entry in enumerate(history, 1):
                            Color.printColorOutput(f"{i}. {entry}", "green")
                    continue

                if command == 'clear': 
                    # Clear calculation history
                    calc.clear_history()
                    Color.printColorOutput("History cleared", "red")
                    continue

                if command == 'undo': 
                    # Undo the last calculation
                    if calc.undo():
                        Color.printColorOutput("Operation undone", "yellow")
                    else:
                        Color.printColorOutput("Nothing to undo", "red")
                    continue

                if command == 'redo': 
                    # Redo the last undone calculation
                    if calc.redo():
                        Color.printColorOutput("Operation redone", "yellow")
                    else:
                        Color.printColorOutput("Nothing to redo","red")
                    continue

                if command == 'save': 
                    # Save calculation history to file
                    try:
                        calc.save_history()
                        Color.printColorOutput("History saved successfully", "green")
                    except Exception as e:
                        Color.printError(f"Error saving history: {e}")
                    continue

                if command == 'load': 
                    # Load calculation history from file
                    try:
                        calc.load_history()
                        Color.printColorOutput("History loaded successfully","green")
                    except Exception as e:
                        Color.printError(f"Error loading history: {e}")
                    continue

                if command in ['add', 'sub', 'mult', 'div', 'exp', 'root', 'idiv', 'exp','mod', 'perc','absv']: 
                    # Perform the specified arithmetic operation
                    try:
                        Color.printColorOutput("\nEnter numbers (or 'cancel' to abort):", "yellow")
                        a = Color.printColorInput("First number: ", "white")
                        if a.lower() == 'cancel':
                            Color.printError("Operation cancelled")
                            continue
                        b = Color.printColorInput("Second number: ", "white")
                        if b.lower() == 'cancel':
                            Color.printError("Operation cancelled")
                            continue

                        # Create the appropriate operation instance using the Factory pattern
                        operation = OperationFactory.create_operation(command)
                        calc.set_operation(operation)

                        # Perform the calculation
                        result = calc.perform_operation(a, b)

                        # Normalize the result if it's a Decimal
                        if isinstance(result, Decimal):
                            result = result.normalize()

                        Color.printColorOutput(f"\nResult: {result}", "blue","bright")
                    except (ValidationError, OperationError) as e:
                        # Handle known exceptions related to validation or operation errors
                        Color.printError(f"Error: {e}")
                    except Exception as e:
                        # Handle any unexpected exceptions
                        Color.printError(f"Unexpected error: {e}")
                    continue

                # Handle unknown commands
                Color.printError(f"Unknown command: '{command}'. Type 'help' for available commands.")

            except KeyboardInterrupt:
                # Handle Ctrl+C interruption gracefully
                Color.printError("\nOperation cancelled")
                continue
            except EOFError:
                # Handle end-of-file (e.g., Ctrl+D) gracefully
                Color.printError("\nInput terminated. Exiting...")
                break
            except Exception as e:
                # Handle any other unexpected exceptions
                Color.printError(f"Error: {e}")
                continue

    except Exception as e:
        # Handle fatal errors during initialization
        Color.printError(f"Fatal error: {e}")
        Logger.errorLog(f"Fatal error in calculator REPL: {e}")
        raise