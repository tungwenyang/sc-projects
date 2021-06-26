"""
File: boggle.py
Name: Claire Yang
----------------------------------------
This program recursively find all
the words from the letters user input
like game Boggle
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


# Global Variable
dictionary = []


def main():
	"""
	This program recursively find all the words from the letters user input like game Boggle
	"""
	# user input
	d = {}
	for i in range(4):
		letters = input(str(i + 1) + ' row of letters: ').lower()
		if check_format(letters) is False:
			print('Illegal input')
			return
		for j in range(0, 7, 2):
			d[str(i + 1) + '-' + str(j // 2 + 1)] = letters[j]
	# search
	boggle(d)


def boggle(input_dict):
	"""
	This function is to recursively find all the words from input_dict like game Boggle
	:param input_dict: dict, to identify each letter with its item number
	:return: print total count of words in the console
	"""
	global dictionary
	read_dictionary()
	ans = []
	for i in range(4):
		for j in range(4):
			ch = input_dict[str(i + 1) + '-' + str(j + 1)]
			input_dict[str(i + 1) + '-' + str(j + 1)] = ''
			helper_boggle(input_dict, ch, i + 1, j + 1, dictionary, ans)
			input_dict[str(i + 1) + '-' + str(j + 1)] = ch
	print('There are ' + str(len(ans)) + ' words in total.')


def helper_boggle(input_dict, current_s, row, line, dictionary_lst, answer):
	"""
	This is the helper function of boggle(input_dict)
	:param input_dict: dict, to identify each letter with its item number
	:param current_s: str, current string
	:param row: int, the row of the last letter in current_s
	:param line: int, the line of the last letter in current_s
	:param dictionary_lst: lst, a dictionary from global variable
	:param answer: lst, a list of words that were found
	"""
	if len(current_s) >= 4:
		if current_s not in answer:
			if current_s in dictionary_lst:
				answer.append(current_s)
				print('Found \"' + current_s + '\"')
	boggle_find_neighbor(input_dict, current_s, row, line, dictionary_lst, answer)


def boggle_find_neighbor(input_dict, current_s, row, line, dictionary_lst, answer):
	"""
	This function is to check the neighbor letters of the last letter in current_s
	:param input_dict: dict, to identify each letter with its item number
	:param current_s: str, current string
	:param row: int, the row of the last letter in current_s
	:param line: int, the line of the last letter in current_s
	:param dictionary_lst: lst, a dictionary from global variable
	:param answer: lst, a list of words that were found
	"""
	for i in range(-1, 2, 1):
		for j in range(-1, 2, 1):
			if 0 < row + i <= 4:
				if 0 < line + j <= 4:
					ch = input_dict[str(row + i) + '-' + str(line + j)]
					if ch != '':
						# Choose
						current_s += ch
						input_dict[str(row + i) + '-' + str(line + j)] = ''

						# Explore
						if has_prefix(current_s):
							helper_boggle(input_dict, current_s, row + i, line + j, dictionary_lst, answer)

						# Un-choose
						current_s = current_s[:len(current_s) - 1]
						input_dict[str(row + i) + '-' + str(line + j)] = ch


def check_format(letters):
	"""This function is to check if user input is in correct format"""
	if len(letters) != 7:
		return False
	else:
		for i in range(0, 7, 2):
			if not letters[i].isalpha():
				return False
		for i in range(1, 6, 2):
			if not letters[i] == ' ':
				return False


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dictionary
	with open(FILE, 'r') as f:
		for line in f:
			dictionary.append(line.strip())
		return dictionary


def has_prefix(sub_s):
	"""
	:param sub_s: str, a substring that is constructed by neighboring letters on a 4x4 square grid
	:return: bool, if there is any words with prefix stored in sub_s
	"""
	global dictionary
	for i in range(len(dictionary)):
		if dictionary[i].startswith(sub_s):
			return True


if __name__ == '__main__':
	main()
