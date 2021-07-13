'''
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.). 
You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity 
to practice using functions, described below.
'''
def is_whole_number(number):
    return number == int(number) and number >= 0

def get_divisors(number):
    return [e for e in range(2, number) if number % e == 0]

def get_whole_number():
    number = input("Enter a whole number: ")
    while not number.isdigit() or not is_whole_number(float(number)):
        number = input("Enter a whole number: ")
    return int(number)

def is_prime(number):
    return not get_divisors(number) and is_whole_number(number) and number > 1

num = get_whole_number()

if is_prime(num):
    print("%d is a prime" % num)
else:
    print("%d is not a prime" % num)
