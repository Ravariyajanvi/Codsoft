import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    # Define character sets
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    
    # Create character pool based on user preferences
    char_pool = ''
    if use_letters:
        char_pool += letters
    if use_numbers:
        char_pool += numbers
    if use_symbols:
        char_pool += symbols
        
    # Ensure at least one character set is selected
    if not char_pool:
        return "Error: Please select at least one character type!"
    
    # Generate password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    print("\n=== Password Generator ===")
    
    while True:
        try:
            # Get password length
            length = int(input("\nEnter desired password length: "))
            if length <= 0:
                print("Password length must be greater than 0!")
                continue
            
            # Get character type preferences
            print("\nPassword character types:")
            use_letters = input("Include letters? (yes/no): ").lower() == 'yes'
            use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
            use_symbols = input("Include special characters? (yes/no): ").lower() == 'yes'
            
            # Generate and display password
            password = generate_password(length, use_letters, use_numbers, use_symbols)
            print(f"\nGenerated Password: {password}")
            
            # Ask if user wants another password
            again = input("\nGenerate another password? (yes/no): ")
            if again.lower() != 'yes':
                print("\nThank you for using the Password Generator!")
                break
                
        except ValueError:
            print("\nPlease enter a valid number for password length!")
        except Exception as e:
            print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()