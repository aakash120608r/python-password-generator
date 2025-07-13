import random
import string

def password_gen(n):
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    punct = random.choice(string.punctuation)

    password_list = [lower, upper, digit, punct]
    
    for i in range(n-4):
        password_list.append(random.choice(string.ascii_letters + string.digits + string.punctuation))
        
    random.shuffle(password_list)
    password=''.join(password_list)

    return password

print("=== Password Generator ===")
while True:
    n=int(input('Entert the length of the password: '))
    if n < 4:
        print("Password length must be at least 4")
        continue

    print()

    print('Your password is: ',password_gen(n))
    
    print()

    print('Not satisfied with your password, Generate again then!')
    a=input('Do you want to generate again (y/n): ')
    if a=='y'or a=='yes' or a=='Yes':
        continue
    elif a=='n' or a=='no' or a=='No':
        print('Thank You')
        break
    else:
        print('Invalid Input')
        continue
