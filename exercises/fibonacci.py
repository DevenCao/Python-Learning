'''
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence
is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''

#callback function
def fibonacci_generator(count = 0, first = 1, second = 1):
    fibonacci_list = [first]
    if count <= 1:
        return fibonacci_list
    fibonacci_list += fibonacci_generator(count-1, second, first + second)
    return fibonacci_list

print(fibonacci_generator(10))

