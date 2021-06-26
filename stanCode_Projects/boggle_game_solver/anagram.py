"""
File: anagram.py
Name: Claire Yang
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


# Global Variable
dictionary = []


def main():
    """
    This program recursively finds all the anagram(s) for the word input by user
    and terminates when the input string matches the EXIT constant
    """
    intro()
    read_dictionary()
    while True:
        s = input('Find anagrams for: ')
        if s == EXIT:
            break
        else:
            find_anagrams(s)


def intro():
    """This function wraps 1 print as intro()"""
    print('Welcome to stanCode \"Anagram Generator\" (or ' + str(EXIT) + ' to quit)')


def read_dictionary():
    """
    This function is to read FILE 'dictionary.txt' and return a list of words as dictionary
    :return: lst, a list of words in FILE
    """
    global dictionary
    with open(FILE, 'r') as f:
        for line in f:
            dictionary.append(line.strip())
        return dictionary


def find_anagrams(s):
    """
    This function is to find all the anagram(s) for s
    :param s: str, the word input by user
    :return: all the anagram(s) for s
    """
    global dictionary
    ans_lst = []     # to list the anagrams
    s_dict = turn_s_to_d(s)  # a dict to count the occurrence of the alphabet(s) in s
    print('Searching...')     # print the first 'Searching...' in console before the recursion starts
    helper_find_anagrams(s, s_dict, '', dictionary, ans_lst)     # helper function to add more variables
    print(str(len(ans_lst))+' anagrams: '+str(ans_lst))


def helper_find_anagrams(word, word_dict, current_s, dictionary_lst, answer):
    """
    This is the helper function of find_anagrams(s)
    :param word: str, the word input by user
    :param word_dict: dict, to count the occurrence of the alphabet(s) in word
    :param current_s: str, current string
    :param dictionary_lst: lst, a dictionary from global variable
    :param answer: lst, a list of anagrams(s) that were found
    :return: the anagram(s) for word
    """
    if len(current_s) == len(word):
        if current_s not in answer:
            if current_s in dictionary_lst:
                answer.append(current_s)
                print('Found: ' + current_s)
                print('Searching...')
    else:
        for i in range(len(word)):
            ch = word[i]
            # check if ch is already chosen
            if word_dict[ch] != 0:
                # Choose
                current_s += ch
                word_dict[ch] -= 1

                # Explore
                if len(word) > 5:
                    if has_prefix(current_s):
                        helper_find_anagrams(word, word_dict, current_s, dictionary_lst, answer)
                else:
                    helper_find_anagrams(word, word_dict, current_s, dictionary_lst, answer)

                # Un-choose
                current_s = current_s[:len(current_s) - 1]
                word_dict[ch] += 1


def turn_s_to_d(s):
    """This function is to create a dict to count the occurrence of the alphabet(s) in s"""
    d = {}
    for ch in s:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
    return d


def has_prefix(sub_s):
    """
    This function is the check if the word starts with sub_s exists in dictionary
    :param sub_s: str, the word to check
    :return: bool
    """
    global dictionary
    for i in range(len(dictionary)):
        if dictionary[i].startswith(sub_s):
            return True


if __name__ == '__main__':
    main()
