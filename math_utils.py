# Math Utility Functions
# Common mathematical operations and calculations

import math

def factorial(n):
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    return math.factorial(n)

def gcd(a, b):
    """Find greatest common divisor."""
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    """Find least common multiple."""
    return abs(a * b) // gcd(a, b) if a and b else 0

def is_prime(n):
    """Check if number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_divisors(n):
    """Find sum of all divisors of n."""
    return sum(i for i in range(1, n + 1) if n % i == 0)

def fibonacci(n):
    """Generate first n fibonacci numbers."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fibs = [0, 1]
    for _ in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[:n]

def power(base, exp):
    """Calculate base raised to exp."""
    return base ** exp

if __name__ == '__main__':
    # Test cases
    print(f"Factorial of 5: {factorial(5)}")  # 120
    print(f"GCD of 48 and 18: {gcd(48, 18)}")  # 6
    print(f"LCM of 12 and 18: {lcm(12, 18)}")  # 36
    print(f"Is 17 prime: {is_prime(17)}")  # True
    print(f"Sum of divisors of 12: {sum_of_divisors(12)}")  # 28
    print(f"First 8 fibonacci numbers: {fibonacci(8)}")
    print(f"2 raised to power 10: {power(2, 10)}")  # 1024
