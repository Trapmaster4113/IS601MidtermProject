from abc import ABC, abstractmethod
from decimal import Decimal
from app.exceptions import ValidationError
from typing import Dict
class Operation(ABC): 
    @abstractmethod
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        pass
    def validateOperands(self, a: Decimal, b: Decimal) -> None:
        pass
    def __str__(self) -> str:
        return self.__class__.__name__
    
class add(Operation):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        self.validateOperands(a,b)
        return a + b
class sub(Operation):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        self.validateOperands(a,b)
        return a - b
class mult(Operation):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        self.validateOperands(a,b)
        return a * b
class div(Operation):
    def validateOperands(self, a, b) -> None:
        super().validateOperands(a, b)
        if b == 0:
            raise ValidationError("Division by zero is not allowed")
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        self.validateOperands(a,b)
        return a / b
class exp(Operation):
    def validateOperands(self, a, b) -> None:
        super().validateOperands(a, b)
        if b < 0:
            raise ValidationError("Negative exponents are not supported")
    def execute(self, a, b) -> Decimal:
        return Decimal(pow(float(a),float(b)))
class root(Operation):
    def validateOperands(self, a, b) -> None:
        super().validateOperands(a, b)
        if a < 0:
            raise ValidationError("Cannot calculate root of negative number")
        if b == 0:
            raise ValidationError("Zero root is undefined")
    def execute(self, a, b) -> Decimal:
        self.validate_operands(a, b)
        return Decimal(pow(float(a), 1 / float(b)))
class operationFactory:
    _Operation: Dict[str, type] = {
        'add': add,
        'subtract': sub,
        'multiply': mult,
        'divide': div,
        'power': exp,
        'root': root
    }
    @classmethod
    def register_operation(cls, name: str, operation_class: type) -> None:
        """
        Register a new operation type.

        Allows dynamic addition of new Operation to the factory.

        Args:
            name (str): Operation identifier (e.g., 'modulus').
            operation_class (type): The class implementing the new operation.

        Raises:
            TypeError: If the operation_class does not inherit from Operation.
        """
        if not issubclass(operation_class, Operation):
            raise TypeError("Operation class must inherit from Operation")
        cls._Operation[name.lower()] = operation_class

    @classmethod
    def create_operation(cls, operation_type: str) -> Operation:
        """
        Create an operation instance based on the operation type.

        This method retrieves the appropriate operation class from the
        _Operation dictionary and instantiates it.

        Args:
            operation_type (str): The type of operation to create (e.g., 'add').

        Returns:
            Operation: An instance of the specified operation class.

        Raises:
            ValueError: If the operation type is unknown.
        """
        operation_class = cls._Operation.get(operation_type.lower())
        if not operation_class:
            raise ValueError(f"Unknown operation: {operation_type}")
        return operation_class()