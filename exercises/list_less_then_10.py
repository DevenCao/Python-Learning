'''
Take a list, say for example this one:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:
1.Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
2.Write this in one line of Python.
2.Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#iterate list a and print out elements les than 5
for ele in a:
  if ele < 5:
    print(ele)

#iterate list a then add elements less than 5 to a new list b
b = []
for ele in a:
  if ele < 5:
    b.append(ele)
print(b)

#extra-2
print(list(filter(lambda x:(x<5), a)))

#extra-3
number = int(input("Enter a number: "))
print(list(filter(lambda x:(x < number), a)))
