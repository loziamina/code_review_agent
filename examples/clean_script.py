def multiply(a, b):
    """Multiplie deux nombres."""
    return a * b

def divide(a, b):
    """Divise deux nombres."""
    if b == 0:
        raise ValueError("La division par zéro n'est pas autorisée")
    return a / b

print(multiply(2, 3))  # 6
print(divide(6, 2))     # 3.0
