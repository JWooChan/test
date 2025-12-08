from math_ops import power, factorial

def test_power():
    assert power(2, 3) == 8
    assert power(5, 2) == 25
    print("✓ Power tests passed")

def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    print("✓ Factorial tests passed")

if __name__ == "__main__":
    test_power()
    test_factorial()
    print("\n모든 테스트 통과!")