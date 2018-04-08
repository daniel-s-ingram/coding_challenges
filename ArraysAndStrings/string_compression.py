#Cracking the Coding Interview: Chapter 1 - Arrays and Strings
#(1.6) 	String Compression: Implement a method to perform basic string compression using the counts of repeated characters.

def compress(original):
	n = len(original)
	i = 0
	count = 1

	compressed = []

	while i < n-1:
		i += 1

		if original[i] == original[i-1]:
			count += 1
		else:
			compressed.append(original[i-1] + str(count))
			count = 1

	compressed.append(original[i] + str(count))
	compressed = ''.join(compressed)	

	print compressed, len(compressed), n
	if len(compressed) >= n:
		return original
	else:
		return compressed

if __name__ == '__main__':
	import sys

	if len(sys.argv) == 1:
		original = 'aaaabbwwwtrtrrrrrrrrrrrrrlllllllAAAAA'
	else:
		original = sys.argv[1]

	compressed = compress(original)
	
	print original
	print compressed
	if original == compressed:
		print 'Could not compress string: compressed string longer than original.'
	else:
		print 'Compression Ratio:', str(100*len(compressed)/len(original)) + '%'