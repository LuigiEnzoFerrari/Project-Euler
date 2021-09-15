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
