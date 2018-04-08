from __future__ import print_function
#Cracking the Coding Interview: Chapter 5 - Recursion and Dynamic Programming
#(5.1) 	Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps 
#		at a time. Implement a method to count how many possible ways the child can run up the stairs.

try:
	xrange		#Python 2
except NameError:
	xrange = range	#Python 3

def triple_step(n):
	if n < 1 or type(n) is not int:
		return 0
	elif n == 1:
		return 1
	elif n == 2:
		return 2
	elif n == 3:
		return 4
	else:
		lookup = [0 for i in xrange(n)]
		
		lookup[0] = 1
		lookup[1] = 2
		lookup[2] = 4

		for i in xrange(3, n):
			lookup[i] = lookup[i-1] + lookup[i-2] + lookup[i-3]

		return lookup[n-1]

if __name__ == '__main__':
	import sys

	if len(sys.argv) == 1:
		print(triple_step(5))
	else:
		try:
			n = int(sys.argv[1])
			print(triple_step(n))
		except ValueError:
			print('Please enter a positive integer.')