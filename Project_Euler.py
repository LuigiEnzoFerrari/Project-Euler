from const import isprime

class ProjectEuler:
	@staticmethod
	def Multiples_of_3_or_5():
		x = 0
		sum = 0
		while x < 1000:
			if ((x % 3) == 0 or (x % 5) == 0):
				sum += x
			x += 1
		return (sum)

	@staticmethod
	def Even_Fibonacci_numbers():
		x = 0
		n_1 = 1
		n_2 = 2
		sum = 2
		while x <= 4000000:
			if ((x % 2) == 0):
				sum += x
			x = (n_1 + n_2)
			n_1 = n_2
			n_2 = x
		return (sum)

	@staticmethod
	def Largest_prime_factor():
		max_n = 600851475143
		x = 2
		while (True):
			if ((max_n % x) == 0):
				factor = int(max_n / x)
				if (isprime(factor)):
					return (factor)
			x += 1
		return (-1)