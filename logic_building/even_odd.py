def even_odd(n):
    """Return 'Even' if n is even, 'Odd' if n is odd."""
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage:
print(even_odd(4))  # Output: Even
print(even_odd(7))  # Output: Odd

