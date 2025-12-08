print("here is main branch")
print("addition math3way.py")

def greet(name):
    """사용자에게 인사합니다"""
    if not name:
        return "Hello, Guest!"
    return f"Hello, {name}!"

def main():
    print(greet("World"))
    print(greet(""))  # 빈 이름 테스트

if __name__ == "__main__":
    main()
