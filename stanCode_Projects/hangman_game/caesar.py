"""
File: caesar.py
Name: Claire Yang
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program is to decipher the string user inputs
    The string will be encrypted by a cipher table produced by the user input number shifted ALPHABET
    """
    shift_steps = int(input('Secret number: '))
    cipher = input('What\'s the ciphered string?')
    new_alphabet = produce_new_alphabet(shift_steps)
    print('The deciphered string is: '+str(decipher(cipher, new_alphabet)))


def produce_new_alphabet(shift_steps):
    """
    This function is to produce a new alphabet table with the secret number user inputs
    :param shift_steps: int, the number user inputs to shift the ALPHABET
    :return: str, a shifted alphabet table
    """
    ans = ''
    for i in range(len(ALPHABET)):
        index = len(ALPHABET) - shift_steps + i
        if index < len(ALPHABET):
            ch = ALPHABET[index]
            ans += ch
        else:
            ch = ALPHABET[i - shift_steps]
            ans += ch
    return ans


def decipher(cipher, new_alphabet):
    """
    This function is to decipher the string user inputs
    :param cipher: str, the ciphered string user inputs
    :param new_alphabet: str, the shifted alphabet table
    :return: str, the deciphered string
    """
    cipher = cipher.upper()
    ans = ''
    for i in range(len(cipher)):
        s = cipher[i]
        if s.isalpha():
            index = new_alphabet.find(s)
            ch = ALPHABET[index]
            ans += ch
        else:
            ans += s
    return ans


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
