OPERATIONS = {
    "sum": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a / b,
}


def calc(a: float, b: float, op: str) -> float:
    """Perform a binary arithmetic operation on two numbers.

    Args:
        a: Left operand.
        b: Right operand.
        op: Operation key — one of 'sum', 'sub', 'mul', 'div'.

    Returns:
        Result of the operation.

    Raises:
        ValueError: If op is not a supported operation.
        ZeroDivisionError: If op is 'div' and b is zero.
    """
    if op not in OPERATIONS:
        raise ValueError(f"Unknown operation '{op}'. Supported: {', '.join(OPERATIONS)}")

    if op == "div" and b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")

    return OPERATIONS[op](a, b)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Usage: python function.py <a> <b> <operation>")
        print(f"Supported operations: {', '.join(OPERATIONS)}")
        sys.exit(1)

    raw_a, raw_b, op = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        a = float(raw_a)
        b = float(raw_b)
    except ValueError:
        print(f"Error: '{raw_a}' and '{raw_b}' must both be valid numbers")
        sys.exit(1)

    try:
        result = calc(a, b, op)
        print(f"Result: {result}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
        sys.exit(1)
