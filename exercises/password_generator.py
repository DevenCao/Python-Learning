'''
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters,
uppercase letters, numbers, and symbols. The passwords should be random,
generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
'''


import random, string

def password_generator(size = None):
    size = size or random.randint(15, 30)
    chars = string.ascii_letters + string.digits + string. punctuation
    return "".join([random.choice(chars) for i in range(size)])

def main():
    run = True
    while run:
        size = input("Enter new password length('q' to quit): ")
        if not size.isdigit() and size != 'q':
            print("Invalid enter, pls try again")
            continue
        elif size == 'q':
            break
        else:
            print(password_generator(int(size)))

if __name__ == '__main__':
    main()

