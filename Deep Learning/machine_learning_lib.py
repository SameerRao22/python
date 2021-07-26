from sklearn import tree
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
from closest_classifier import closest


class mlo:
	def __init__(self, mode, mapper, reverse):
		self.mode = mode
		self.mapper = mapper
		self.reverse = reverse
		if self.mode == 'dt':
			self.clf = tree.DecisionTreeClassifier()
		elif self.mode == 'linear':
			self.clf = linear_model.LinearRegression()
		elif self.mode == 'closest':
			self.clf = closest()

	def set_training_data(self, x1, y1, file):
		if file == None:
			self.x = list(x1)
			self.y = list(y1)

		else:
			if x1 == None:
				file = open(file, 'r')
				content = file.readlines()

				buffer1 = ""
				x = []
				y = []
				donelist = []

				content = [i.strip() for i in content]
				for num, i in enumerate(content[0].split()):
					x.append([])
					for f in i:
						if f == ',':
							x[num].append(float(buffer1))
							buffer1 = ""
						else:
							buffer1 = buffer1 + f
					x[num].append(float(buffer1))
					buffer1 = ""

				for i in content[1].split():
					y.append(i)
					if i not in donelist:
						donelist.append(i)
						self.set_mapper(i, len(donelist) - 1, len(donelist) - 1, i)


				file.close()
				self.x = x
				self.y = y
				self.content = content
			else:
				self.x.append([x1[0], x1[1]])
				self.content[0] = self.content[0] + " " + str(x1[0]) + "," + str(x1[1])
				
				self.y.append(y1)
				self.content[1] = self.content[1] + " " + y1

				if y1 not in self.mapper:
					self.set_mapper(y1, len(self.mapper), len(self.mapper), y1)

				file = open(file, 'w')
				for index in self.content:
					file.write(index + '\n')
				file.close()


		for num, i in enumerate(self.y):
			if i in self.mapper:
				self.y[num] = self.mapper[i]

		self.clf = self.clf.fit(self.x, self.y)

	def get_prediction(self, x):
		if self.mode == 'dt' or self.mode == 'closest':
			return self.reverse[self.clf.predict([x])[0]]

		return self.clf.predict([x])[0]

	def set_mapper(self, mapperk, mapperd, reversek, reverseda):
		self.mapper[mapperk] = mapperd
		self.reverse[reversek] = reverseda
