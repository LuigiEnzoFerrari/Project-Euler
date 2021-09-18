from types import resolve_bases
from const import isprime

class ProjectEuler:
	@staticmethod
	def Multiples_of_3_or_5(n=1000):
		x = 0
		sum = 0
		while x < n:
			if ((x % 3) == 0 or (x % 5) == 0):
				sum += x
			x += 1
		return (sum)

	@staticmethod
	def Even_Fibonacci_numbers(n=4000000):
		x = 0
		n_1 = 1
		n_2 = 2
		sum = 2
		while x <= n:
			if ((x % 2) == 0):
				sum += x
			x = (n_1 + n_2)
			n_1 = n_2
			n_2 = x
		return (sum)

	@staticmethod
	def Largest_prime_factor(n=600851475143):
		x = 2
		while (True):
			if ((n % x) == 0):
				factor = int(n / x)
				if (isprime(factor)):
					return (factor)
			x += 1
		return (-1)

	@staticmethod
	def Largest_palindrome_product(x=999, y=999):
		holder = x
		max_n = 0
		while y > 0:
			x = holder
			while x > 0:
				n_str = str(x * y)
				if (n_str == n_str[::-1]):
					if (max_n < int(n_str)):
						max_n = int(n_str)
				x -= 1
			y -= 1
		return (max_n)