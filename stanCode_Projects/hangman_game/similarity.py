"""
File: similarity.py
Name: Claire Yang
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    This program is to compare a short DNA sequence with sub sequences of a long DNA sequence
    """
    long_sequence = input('Please give me a DNA sequence to search: ')
    short_sequence = input('What DNA sequence would you like to match? ')
    print('The best match is '+str(match(long_sequence, short_sequence)))


def match(long_sequence, short_sequence):
    """
    This function is to find the best match of the short sequence from the long sequence
    :param long_sequence: str, the sequence to find a sub sequence which match with the short sequence
    :param short_sequence: str, the sequence to be matched
    :return: str, the best match sequence
    """
    long = long_sequence.upper()
    short = short_sequence.upper()
    ans = ''
    highest_score = 0
    # score is to identify if the sequence is the best match
    for i in range(len(short)):
        # to repeat matching from match sequence length is len(short) to 1
        score = highest_score
        for j in range(i + 1):
            # to repeat matching different combination of sequence under the same length
            highest_score = score
            short_to_match = short[j:len(short) + j - i]
            # the sub sequence to be matched from short_sequence
            if long.find(short_to_match) != -1:
                index = long.find(short_to_match)
                if index >= j:
                    # to check if the start of the match sequence (from long_sequence) exists
                    if index - j + len(short) <= len(long):
                        # to check if the end of the match sequence (from long_sequence) exists
                        match_sequence_from_long = long[index - j:index - j + len(short)]
                        # the match sequence from long_sequence
                        score_of_this_match = 0
                        for k in range(len(short)):
                            # to count the number of matched word
                            if match_sequence_from_long[k] == short[k]:
                                score_of_this_match += 1
                        if score_of_this_match > highest_score:
                            # if score_of_this_match is higher than highest_score:
                            # this match will become the best match
                            ans = match_sequence_from_long
                            highest_score = score_of_this_match
                            score = highest_score
                        else:
                            ans = ans
                    else:
                        ans = ans
                else:
                    ans = ans
            else:
                ans = ans
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
