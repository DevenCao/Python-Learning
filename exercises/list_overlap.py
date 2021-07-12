'''
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extras:

1.Randomly generate two lists to test this
2.Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
'''

from random import  sample

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(list({item for item in a if item in b}))

#extra-1
a = sample(range(100), 20)
b = sample(range(100), 20)
print(a, '\n', b)
print(list(set(a).intersection(set(b))))

#extra-2
print(list(set(sample(range(100), 20)).intersection(set(sample(range(100), 20)))))

