def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def calculator():
    print("\n=== Simple Calculator ===")
    print("Available Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
            
            print("\nChoose operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            
            choice = input("Enter choice (1-4): ")
            
            if choice in ['1', '2', '3', '4']:
                if choice == '1':
                    result = add(num1, num2)
                    print(f"\n{num1} + {num2} = {result}")
                
                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"\n{num1} - {num2} = {result}")
                
                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"\n{num1} * {num2} = {result}")
                
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"\n{num1} / {num2} = {result}")
            else:
                print("\nInvalid input! Please enter a number between 1 and 4")
                
            again = input("\nDo you want to perform another calculation? (yes/no): ")
            if again.lower() != 'yes':
                print("\nThank you for using the calculator!")
                break
                
        except ValueError:
            print("\nError: Please enter valid numbers!")
        except Exception as e:
            print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    calculator()