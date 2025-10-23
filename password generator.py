import random
import string
import time

def password_gen(n, include_symbols=True, easy_to_read=False):
    # Define character sets
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
    
    # Shuffle to randomize positions
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    return password

def get_strength(n, include_symbols):
    """Return password strength based on length and complexity"""
    score = n
    if include_symbols:
        score += 2
    
    if score < 8:
        return "Weak 🔴", "Not recommended"
    elif score < 12:
        return "Medium 🟡", "Okay for basic accounts"
    elif score < 16:
        return "Strong 🟢", "Good for most accounts"
    else:
        return "Very Strong 💪", "Excellent for banking/email"

def calculate_combinations(n, include_symbols):
    """Calculate possible combinations"""
    charset_size = 26 + 26 + 10  # lower + upper + digits
    if include_symbols:
        charset_size += 32  # punctuation
    
    combinations = charset_size ** n
    return combinations

def save_passwords(passwords):
    """Save passwords to a file"""
    filename = f"passwords_{int(time.time())}.txt"
    with open(filename, 'w') as f:
        f.write("=== Generated Passwords ===\n")
        f.write(f"Generated on: {time.ctime()}\n\n")
        for i, pwd in enumerate(passwords, 1):
            f.write(f"{i}. {pwd}\n")
    print(f"✅ Passwords saved to {filename}")

print("=== Password Generator ===")
while True:
    n=int(input('Enter the length of the password: '))
    
    easy=input('Do you want easy to read password (y/n): ')
    if easy == 'y' or easy == 'yes' or easy == 'Yes':
        easy_to_read = True
    elif easy == 'n' or easy == 'no' or easy == 'No':
        easy_to_read = False
    else:
        print('Invalid Input')
        continue

    include=input('Do you want to include symbols (y/n): ')
    if include=='y' or include=='yes' or include=='Yes':
        include_symbols = True
    elif include=='n' or include=='no' or include=='No':
        include_symbols = False
    else:
        print('Invalid Input')
        continue

    print('Your password is: ',password_gen(n, include_symbols = include_symbols, easy_to_read = easy_to_read))
    
    print(str(get_strength(n, include_symbols)))
    print()

    print('Not satisfied with your password, Generate again then!')
    a = input('Do you want to generate again (y/n): ')
    if a == 'y'or a == 'yes' or a == 'Yes':
        print()
        continue
    elif a == 'n' or a == 'no' or a == 'No':
        print('Thank You')
        break
    else:
        print('Invalid Input')
        continue
