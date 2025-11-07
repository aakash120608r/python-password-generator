import random
import string
import time

def password_gen(n, include_symbols=True, easy_to_read=False):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    if easy_to_read:
        punctuation = "!@#$%&*"

        lowercase = lowercase.replace('l', '').replace('o', '')
        uppercase = uppercase.replace('I', '').replace('O', '')
        digits = digits.replace('0', '').replace('1', '')

    all_chars = lowercase + uppercase + digits

    min_length = 3

    password_list = []

    password_list.append(random.choice(lowercase))
    password_list.append(random.choice(uppercase))
    password_list.append(random.choice(digits))

    if include_symbols:
        password_list.append(random.choice(punctuation))
        all_chars += punctuation
        min_length = 4

    if n < min_length:
        return "Error: Length too short for the selected options."
    
    for i in range(n - min_length):
        password_list.append(random.choice(all_chars))
    
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    return password

def get_strength(n, include_symbols):
    score = n
    if include_symbols:
        score += 2
    
    if score < 8:
        return "Weak 🔴"
    elif score < 12:
        return "Medium 🟡"
    elif score < 16:
        return "Strong 🟢"
    else:
        return "Very Strong 💪"

def calculate_combinations(n, include_symbols):
    charset_size = 26 + 26 + 10  # lower + upper + digits
    if include_symbols:
        charset_size += 32  # punctuation
    
    combinations = charset_size ** n
    return combinations

def save_passwords(passwords):
    filename = f"passwords_{int(time.time())}.txt"
    with open(filename, 'w') as f:
        f.write("=== Generated Passwords ===\n")
        f.write(f"Generated on: {time.ctime()}\n\n")
        for i, pwd in enumerate(passwords, 1):
            f.write(f"{i}. {pwd}\n")
    print(f"✅ Passwords saved to {filename}")

def display_password_info(password, n, include_symbols):
    print('━' * 50)
    print(f'Your password is: {password}')
    print('━' * 50)
    print(f'Length: {n} characters')
    
    strength = get_strength(n, include_symbols)
    print(f'Strength: {strength}')
    
    combos = calculate_combinations(n, include_symbols)
    print(f'Possible combinations: {combos:,}')
    
    # Count character types
    has_lower = sum(1 for c in password if c.islower())
    has_upper = sum(1 for c in password if c.isupper())
    has_digit = sum(1 for c in password if c.isdigit())
    has_symbol = sum(1 for c in password if c in string.punctuation)
    
    print(f'Contains: {has_lower} lowercase, {has_upper} uppercase, {has_digit} digits, {has_symbol} symbols')
    print('━' * 50)

def check_password_strength():
    pwd = input("Enter the password to check: ")
    n = len(pwd)
    include_symbols = any(c in string.punctuation for c in pwd)
    
    display_password_info(pwd, n, include_symbols)

def main():
    print("Welcome to the Password Generator!")
    print("1. Generate a single password")
    print("2. Generate multiple passwords")
    print("3. Password strength checker")
    print("4. Exit")
    choice = input("Select an option (1-5): ")

    if choice == '1':    
        try:
            n = int(input("Enter password length: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        include_symbols = input("Include symbols? (y/n): ")
        easy_to_read = input("Make password easy to read? (y/n): ")
        
        password = password_gen(n, include_symbols, easy_to_read)
        
        if password.startswith("Error"):
            print(password)
            return
        
        display_password_info(password, n, include_symbols)
        
        save_option = input("Do you want to save the password? (y/n): ").lower()
        if save_option == 'y':
            save_passwords([password])

    elif choice == '2':
        try:
            count = int(input("How many passwords to generate? "))
            n = int(input("Enter password length: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            return

        include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        easy_to_read = input("Make passwords easy to read? (y/n): ").lower() == 'y'
        
        passwords = []
        for i in range(count):
            pwd = password_gen(n, include_symbols, easy_to_read)
            if pwd.startswith("Error"):
                print(pwd)
                return
            passwords.append(pwd)
            display_password_info(pwd, n, include_symbols)
        
        save_option = input("Do you want to save the passwords? (y/n): ").lower()
        if save_option == 'y':
            save_passwords(passwords)

    elif choice == '3':
        check_password_strength()

    elif choice == '4':
        print("Exiting the program. Goodbye!")
        return
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()