from functools import cache

@cache  # Simple caching with unlimited size
def fibonacci(n):
    """
    Compute the nth Fibonacci number using recursion.
    Cached results will speed up repeated calls.
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test the function
if __name__ == "__main__":
    print("Fibonacci numbers:")
    for i in range(10):
        print(f"fibonacci({i}) = {fibonacci(i)}")
