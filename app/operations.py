from abc import ABC, abstractmethod
from decimal import Decimal
from app.exceptions import ValidationError
from typing import Dict
class Operation(ABC): #pragma: no cover
    """
    Abstract base class for calculator operations.

    Defines the interface for all arithmetic operations. Each operation must
    implement the execute method and can optionally override operand validation.
    """
    @abstractmethod
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """
        Execute the operation.

        Performs the arithmetic operation on the provided operands.

        Args:
            a (Decimal): First operand.
            b (Decimal): Second operand.

        Returns:
            Decimal: Result of the operation.

        Raises:
            OperationError: If the operation fails.
        """
        pass
    def validate_operands(self, a: Decimal, b: Decimal) -> None:
        """
        Validate operands before execution.

        Can be overridden by subclasses to enforce specific validation rules
        for different operations.

        Args:
            a (Decimal): First operand.
            b (Decimal): Second operand.

        Raises:
            ValidationError: If operands are invalid.
        """
        pass
    def __str__(self) -> str:
        """
        Return operation name for display.

        Provides a string representation of the operation, typically the class name.

        Returns:
            str: Name of the operation.
        """
        return self.__class__.__name__
    
class add(Operation):
    """
    Addition operation implementation.

    Performs the addition of two numbers.
    """
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """
        Add two numbers.

        Args:
            a (Decimal): First operand.
            b (Decimal): Second operand.

        Returns:
            Decimal: Sum of the two operands.
        """
        self.validate_operands(a,b)
        return a + b
class sub(Operation):
    """
    Subtration operation implementation.

    Performs the subtraction of two numbers.
    """
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """
        Subtracts two numbers.

        Args:
            a (Decimal): First operand.
            b (Decimal): Second operand.

        Returns:
            Decimal: Difference of the two operands.
        """
        self.validate_operands(a,b)
        return a - b
class mult(Operation):
    """
    Multiplication operation implementation.

    Performs the Multiplication of two numbers.
    """
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """
        Multiplies two numbers.

        Args:
            a (Decimal): First operand.
            b (Decimal): Second operand.

        Returns:
            Decimal: Produce of the two operands.
        """
        self.validate_operands(a,b)
        return a * b
class div(Operation):
    """
    Division operation implementation.

    Performs the Division of two numbers.
    """
    def validate_operands(self, a, b) -> None:
        """
        Validate operands, checking for division by zero.

        Overrides the base class method to ensure that the divisor is not zero.

        Args:
            a (Decimal): Dividend.
            b (Decimal): Divisor.

        Raises:
            ValidationError: If the divisor is zero.
        """
        super().validate_operands(a, b)
        if b == 0:
            raise ValidationError("Division by zero is not allowed")
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """
        Divide one number by another.

        Args:
            a (Decimal): Dividend.
            b (Decimal): Divisor.

        Returns:
            Decimal: Quotient of the division.
        """
        self.validate_operands(a,b)
        return a / b
    
class exp(Operation):
    """
    Power (exponentiation) operation implementation.

    Raises one number to the power of another.
    """
    def validate_operands(self, a, b) -> None:
        """
        Validate operands for power operation.

        Overrides the base class method to ensure that the exponent is not negative.

        Args:
            a (Decimal): Base number.
            b (Decimal): Exponent.

        Raises:
            ValidationError: If the exponent is negative.
        """
        super().validate_operands(a, b)
        if b < 0:
            raise ValidationError("Negative exponents not supported")
    def execute(self, a, b) -> Decimal:
        """
        Calculate one number raised to the power of another.

        Args:
            a (Decimal): Base number.
            b (Decimal): Exponent.

        Returns:
            Decimal: Result of the exponentiation.
        """
        self.validate_operands(a,b)
        return Decimal(pow(float(a),float(b)))
    
class root(Operation):
    """
    Root operation implementation.

    Calculates the nth root of a number.
    """
    def validate_operands(self, a, b) -> None:
        """
        Validate operands for root operation.

        Overrides the base class method to ensure that the number is non-negative
        and the root degree is not zero.

        Args:
            a (Decimal): Number from which the root is taken.
            b (Decimal): Degree of the root.

        Raises:
            ValidationError: If the number is negative or the root degree is zero.
        """
        super().validate_operands(a, b)
        if a < 0:
            raise ValidationError("Cannot calculate root of negative number")
        if b == 0:
            raise ValidationError("Zero root is undefined")
    def execute(self, a, b) -> Decimal:
        """
        Calculate the nth root of a number.

        Args:
            a (Decimal): Number from which the root is taken.
            b (Decimal): Degree of the root.

        Returns:
            Decimal: Result of the root calculation.
        """
        self.validate_operands(a, b)
        return Decimal(pow(float(a), 1 / float(b)))
    
class mod(Operation):
    """
    Modulus Remainder operation implementation.

    Calculates the remainder of the first number divided by the second.
    """
    def validate_operands(self, a, b) -> None:
        """
        Validate operands, checking for division by zero.

        Overrides the base class method to ensure that the divisor is not zero.

        Args:
            a (Decimal): Dividend.
            b (Decimal): Divisor.

        Raises:
            ValidationError: If the divisor is zero.
        """
        super().validate_operands(a, b)
        if b == 0:
            raise ValidationError("Division by zero is not allowed")
    def execute(self, a, b) -> Decimal:
        """
        Divide one number by another.

        Args:
            a (Decimal): Dividend.
            b (Decimal): Divisor.

        Returns:
            Decimal: Remainder of the division.
        """
        self.validate_operands(a, b)
        return a % b
    
class idiv(Operation):
    """
    Integer Division operation implementation.

    Performs the Division of two numbers.
    """
    def validate_operands(self, a, b) -> None:
        """
        Validate operands, checking for division by zero.

        Overrides the base class method to ensure that the divisor is not zero.

        Args:
            a (Decimal): Dividend.
            b (Decimal): Divisor.

        Raises:
            ValidationError: If the divisor is zero.
        """
        super().validate_operands(a, b)
        if b == 0:
            raise ValidationError("Division by zero is not allowed")
    def execute(self, a, b) -> int:
        """
        Divide one number by another.

        Args:
            a (Decimal): Dividend.
            b (Decimal): Divisor.

        Returns:
            Decimal: Integer Quotient of the division.
        """
        self.validate_operands(a, b)
        return int(a)//int(b)
    
class perc(Operation):
    """
    Percentage operation implementation.

    Performs the Percentage of one number on another.
    """
    def validate_operands(self, a, b) -> None:
        """
        Validate operands, checking for division by zero.

        Overrides the base class method to ensure that the divisor is not zero.

        Args:
            a (Decimal): Dividend.
            b (Decimal): Divisor.

        Raises:
            ValidationError: If the divisor is zero.
        """
        super().validate_operands(a, b)
        if b == 0:
            raise ValidationError("Division by zero is not allowed")
    def execute(self, a, b) -> Decimal:
        """
        Divide one number by another. Then, multiply by 100

        Args:
            a (Decimal): Dividend.
            b (Decimal): Divisor.

        Returns:
            Decimal: Percentage of dividing a by b and then multiplying by 100
        """
        self.validate_operands(a, b)
        return (a / b) * 100
    
class absv(Operation):
    """
    Absolute Difference operation implementation.

    Performs the Absolute Difference of one number on another.
    """
    def execute(self, a, b) -> Decimal:
        """
        Subtracts two numbers and then takes the absolute value of the difference

        Args:
            a (Decimal): First operand.
            b (Decimal): Second operand.

        Returns:
            Decimal: Absolute Difference of the two operands.
        """
        return abs(a-b)
class OperationFactory:
    """
    Factory class for creating operation instances.

    Implements the Factory pattern by providing a method to instantiate
    different operation classes based on a given operation type. This promotes
    scalability and decouples the creation logic from the Calculator class.
    """
    _Operation: Dict[str, type] = {
        'add': add,
        'sub': sub,
        'mult': mult,
        'div': div,
        'exp': exp,
        'root': root,
        'mod' : mod,
        'idiv': idiv,
        'perc' : perc,
        'absv' : absv,
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