#Cracking the Coding Interview: Chapter 1 - Arrays and Strings
#(1.3) 	URLify: Write a method to replace all spaces in a string with '%20'.

def URLify(string):
	string = list(string)
	i = 0

	while i < len(string):
		if string[i] == ' ':
			string = string[:i] + list('%20') + string[i+1:]

		i +=1

	return ''.join(string)

if __name__ == '__main__':
	import sys

	if len(sys.argv) == 1:
		print URLify('Hello World!')
	else:
		print URLify(sys.argv[1])