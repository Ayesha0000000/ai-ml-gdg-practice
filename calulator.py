def add(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Only integers allowed")
    print("Debug: Adding numbers")
    return a + b