from types import resolve_bases
from const import isprime
from math import sqrt

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

	@staticmethod
	def Smallest_multiple(init=1, end=20):
		n = end
		while True:
			count = 0
			for i in range(init, (end + 1)):
				if ((n % i) == 0):
					count += 1
			if (count == 20):
				return (n)
			n += end

	@staticmethod
	def Sum_square_difference(x=100, y=100):
		sum1 = 0
		sum2 = 0
		for i in range(1, (x + 1)):
			sum1 += i**2
		for j in range(1, (y + 1)):
			sum2 += j
		return (sum2**2 - sum1)

	@staticmethod
	def P_10001st_prime(nth=10001):
		i = 1
		n = 3
		while True:
			if (isprime(n)):
				i += 1
			if (i == nth):
				return (n)
			n += 2

	@staticmethod
	def Largest_product_in_a_series(n:str):
		n = ''.join(n.split())
		start = 0
		end = 13
		n_len = len(n) - 12
		products = 1
		product = 1
		while (start < n_len):
			s = n[start:end]
			for x in s:
				products *= int(x)
			if (products > product):
				product = products
			products = 1
			start += 1
			end += 1
		return (product)

	@staticmethod
	def Special_Pythagorean_triplet(n_max:int):

		a =  1
		b =  2
		c = 0
		while True:
			c = sqrt(a**2 + b**2)
			thesum = a + b + c
			if thesum == n_max:
				break
			if thesum > n_max or c <= b:
				a += 1
				b = a
			b += 1
		return int(a * b * c)