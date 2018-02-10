#Cracking the Coding Interview: Chapter 1 - Arrays and Strings
#(1.1) 	Is Unique: Implement an algorithm to determine if a string unique characters. What if you cannot use additional data structures?

def is_unique(string):
	unique_chars = []

	for char in string:
		if char in unique_chars:
			return False
		else:
			unique_chars.append(char)

	return True

if __name__ == '__main__':
	import sys

	if len(sys.argv) == 1:
		print is_unique(raw_input("Enter a string: "))
	else:
		print is_unique(sys.argv[1])