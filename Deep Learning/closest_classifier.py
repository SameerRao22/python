from math import sqrt

class closest:
	def get_distance(self, x, y):
		list1 = []
		answ = 0
		for num, i in enumerate(x):
			list1.append(i - y[num])

		for i in list1:
			answ = answ + i**2

		return sqrt(answ)

	def fit(self, trainingx, trainingy):
		self.trainingx = list(trainingx)
		self.trainingy = list(trainingy)
		return self

	def predict(self, targetx):
		bestfit = 100000
		bestnum = 0
		targety = []

		for onum, item in enumerate(targetx):
			for num, f in enumerate(self.trainingx):
				if abs(self.get_distance(f, targetx[onum])) < bestfit:
					bestfit = abs(self.get_distance(f, targetx[onum]))
					bestnum = num
			targety.append(self.trainingy[bestnum])
			bestfit = 1000000
			bestnum = 0

		return targety