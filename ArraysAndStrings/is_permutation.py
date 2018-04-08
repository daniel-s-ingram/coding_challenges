#Cracking the Coding Interview: Chapter 1 - Arrays and Strings
#(1.2) 	Check Permutation: Given two strings, wrie a method to decide if one is a permutation of the other.

def is_permutation(str1, str2):
	str1 = list(str1)
	str2 = list(str2)

	str1.sort()
	str2.sort()
	
	return True if str1 == str2 else False

if __name__ == '__main__':
	import sys

	if len(sys.argv) == 1:
		print is_permutation('anagram', 'nagaram')
	else:
		print is_permutation(sys.argv[1], sys.argv[2])