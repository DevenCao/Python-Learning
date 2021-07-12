'''
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they
will turn 100 years old.
'''

#Input name & age
name = input("Please enter your name: ")
print("Your name is " + name)
age = input("Please enter your age: ")
print("Your age is " + age)
age = int(age)

#calculate the year age will become 100

year = 100 - age + 2021

print("You will turn 100 at " + str(year))

