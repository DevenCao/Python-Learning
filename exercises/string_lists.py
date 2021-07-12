'''
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
'''

s = input("Enter a string: ")
print("This string is a palindrome") if s == s[::-1] else print("This string is not a palindrome")
