"""
File: complement.py
Name: Claire Yang
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    This program is to output the complement of the DNA sequence user inputs
    """
    dna = input('Please give me a DNA strand and I\'ll find the complement: ')
    print('The complement of '+str(dna)+' is '+str(build_complement(dna)))


def build_complement(dna):
    """
    This function is to build the complement of the DNA sequence user inputs
    :param dna: str, the DNA sequence user inputs
    :return: str, the complement of the DNA sequence param
    """
    dna = dna.upper()
    ans = ''
    for base in dna:
        if base == 'A':
            ans += 'T'
        elif base == 'T':
            ans += 'A'
        elif base == 'C':
            ans += 'G'
        elif base == 'G':
            ans += 'C'
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
