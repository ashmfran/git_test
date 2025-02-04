def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def main():
    user_input = int(input("Enter a nonnegative integer: "))
    if user_input < 0:
        print("Please enter a nonnegative integer.")
    else:
        result = calculate_factorial(user_input)
        print(f"The factorial of {user_input} is {result}.")

if __name__ == "__main__":
    main()
