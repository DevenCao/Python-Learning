'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 
13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

number = int(input("Enter a number: "))
x = range(1, number+1)
divisors = [e for e in x if number % e == 0]
print(str(number) + "'s divisors are " + str(divisors))
