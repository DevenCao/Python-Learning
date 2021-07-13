'''
Write a program (using functions!) that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.
'''

def get_string():
    return input("Enter some words: ")

def words_reverse(words = "", spliter = None, jointer = None):
    spliter = spliter or " "
    wordlist = words.split(spliter)
    wordlist.reverse()
    return jointer.join(wordlist)

def main():
    a = get_string()
    split = input("Enter spliter: ") or " "
    joint = input("Enter jointer: ") or " "
    input("press Enter to reverse words...")
    print(words_reverse(a,  split, joint))

main()
