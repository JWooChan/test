def factorial(n):
    """팩토리얼을 계산합니다"""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result