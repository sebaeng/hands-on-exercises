from enum import Enum


class Operation(str, Enum):
    SUM = "sum"
    SUB = "sub"
    MUL = "mul"
    DIV = "div"


OPERATIONS = {
    Operation.SUM: lambda a, b: a + b,
    Operation.SUB: lambda a, b: a - b,
    Operation.MUL: lambda a, b: a * b,
    Operation.DIV: lambda a, b: a / b,
}


def calc(a: float, b: float, op: Operation) -> float:
    """Perform a binary arithmetic operation on two numbers.

    Args:
        a: Left operand.
        b: Right operand.
        op: Operation to perform.

    Returns:
        Result of the operation.

    Raises:
        ZeroDivisionError: If op is Operation.DIV and b is zero.
    """
    if op is Operation.DIV and b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")

    return OPERATIONS[op](a, b)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Usage: python function.py <a> <b> <operation>")
        print(f"Supported operations: {', '.join(o.value for o in Operation)}")
        sys.exit(1)

    raw_a, raw_b, raw_op = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        a = float(raw_a)
        b = float(raw_b)
    except ValueError:
        print(f"Error: '{raw_a}' and '{raw_b}' must both be valid numbers")
        sys.exit(1)

    try:
        op = Operation(raw_op)
    except ValueError:
        print(f"Error: unknown operation '{raw_op}'. Supported: {', '.join(o.value for o in Operation)}")
        sys.exit(1)

    try:
        result = calc(a, b, op)
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        sys.exit(1)
