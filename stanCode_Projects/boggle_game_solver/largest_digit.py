"""
File: largest_digit.py
Name: Claire Yang
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	"""This program recursively prints the largest digit in 5 different integers"""
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	This function is to print the largest digit in n
	:param n: int, given in main function
	:return: the largest digit in n
	"""
	return helper_find_largest_digit(n, 0)   # 0 is to record the largest digit


def helper_find_largest_digit(n, largest):
	"""
	This function is the helper function of find_largest_digit(n)
	:param n: int, given in main function
	:param largest: int, the latest largest digit in n
	:return: the largest digit in n
	"""
	# check whether n is positive or negative
	if n < 0:
		n = - n

	# check if the last digit in n is the largest digit
	last = n % 10
	if last > largest:
		largest = last

	# check if n is single digit; if not (=else), remove last digit and do recursion
	if n // 10 == 0:
		return largest
	else:
		return helper_find_largest_digit(n // 10, largest)


if __name__ == '__main__':
	main()
