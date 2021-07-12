'''
Ask the user for a number. Depending on whether the number is even or odd, 
print out an appropriate message to the user. Hint: how does an even / odd 
number react differently when divided by 2?

Extras:

1.If the number is a multiple of 4, print out a different message.
2.Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''

number = int(input("Please enter a number: "))

if number % 4 == 0:
		print(str(number) + " is multiple of 4")
elif number % 2 == 0:
		print(str(number) + " is even")
else:
	print(str(number) + " is odd")
