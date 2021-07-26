#To use:
#First create a nn class object
#Then use the init_nn function (x.init_nn()) and pass the amount of input nodes as first parameter
#shape of the hidden layers ( a 1 dimensional list) as second
#for example, [2, 2, 3] would mean that there are 3 hidden layers and the first one
#has 2 nodes, second one has 2 nodes, and third one has 3 nodes
#The last parameter is the number of outputs of the net.
#Then, call the init_net function (x.init_net()) which has no parameters
#Next, call the train_net function to train the net.
#It has two parameters, the x values, and the y values, both are 3d lists:
#x.train_net([[[3]], [[4]], [[5]], [[[4]], [[5]], [[6]]])
#You also have to pass it the epoch rate which should generally be 10,000
#Also, pass it the learning rate which should be 0.03 generally
#Also, pass a boolean value stating whether or not you want to write a tensorboard file.
#say False.
#Then call get_value, which has one parameter, an input data in the form of a 2d list.
#[[1]]
#It will run this through the net and return an output.

import tensorflow as tf

class nn:

	def init_nn(self, inputs, hshape, outputs):
		self.layerdict = {}
		self.innum = inputs
		self.hshape = hshape
		self.outnum = outputs

	def init_net(self):
		self.layerdict['outputs'] = {'Weights':tf.Variable(tf.random_uniform(
			[self.hshape[len(self.hshape) - 1], self.outnum], minval = -1, maxval = 1))}
		self.layerdict['outputs']['Biases'] = tf.Variable(tf.random_uniform(
			[1, self.outnum], minval = -1, maxval = 1))

		for num, i in enumerate(self.hshape):
			if num == 0:
				self.layerdict[num] = {'Weights':tf.Variable(tf.random_uniform(
					[self.innum, i], minval = -1, maxval = 1))}
				self.layerdict[num]['Biases'] = tf.Variable(tf.random_uniform(
					[1, i], minval = -1, maxval = 1))
			else:
				self.layerdict[num] = {'Weights':tf.Variable(tf.random_uniform(
					[self.hshape[num - 1], i], minval = -1, maxval = 1))}
				self.layerdict[num]['Biases'] = tf.Variable(tf.random_uniform(
					[1, i], minval = -1, maxval = 1))
		print(self.layerdict)

	def run_net(self, x):	
		self.layerdict['inputs'] = x

		for num, i in enumerate(self.hshape):
			if num == 0:
				print('tensor1 ', self.layerdict['inputs'], 'tensor2 ',
					self.layerdict[num]['Weights'])
				self.layerdict[num]['Value'] = tf.add(tf.matmul(self.layerdict['inputs'],
					self.layerdict[num]['Weights']), self.layerdict[num]['Biases'])
			else:
				self.layerdict[num]['Value'] = tf.add(tf.matmul(self.layerdict[num - 1]['Value'],
					self.layerdict[num]['Weights']), self.layerdict[num]['Biases'])
			self.layerdict[num]['Value'] = tf.nn.relu(self.layerdict[num]['Value'])

		self.layerdict['outputs']['Value'] = tf.add(tf.matmul(
			self.layerdict[len(self.hshape) - 1]['Value'], self.layerdict['outputs']['Weights']),
			self.layerdict['outputs']['Biases'])

		return self.layerdict['outputs']['Value']

	def print_value(self, xd):
		output = self.sess.run(self.prediction, {self.x:xd})
		print(output)

	def correct_value(self, x):
		for num, i in enumerate(x[0]):
			if i > 1:
				x[0][num] = 1

		return x

	def get_value(self, xd):
		output = self.sess.run(self.prediction, {self.x:xd})
		return output

	def train_net(self, xd, yd, epoch_r, lr, write):
		self.x = tf.placeholder("float", [1, self.innum])
		self.y = tf.placeholder("float", [1, self.outnum])
		
		self.prediction = self.run_net(self.x)

		squared_deltas = tf.square(self.prediction - self.y)
		loss = tf.reduce_sum(squared_deltas)/(len(xd) * 2)

		if write == True:
			with tf.Session() as sess:
				writer = tf.summary.FileWriter('C:\\Users\\shloks\\summary' + '/train', sess.graph)

		optimizer = tf.train.GradientDescentOptimizer(learning_rate=lr).minimize(loss)

		gm_epochs = int(epoch_r/len(xd))
		init = tf.global_variables_initializer()
		self.sess = tf.Session()

		self.sess.run(init)
		for epoch in range(gm_epochs):
			epoch_loss = 0
			for num, i in enumerate(xd):
				xv = i
				yv = yd[num]
				_, c = self.sess.run([optimizer, loss], feed_dict = {self.x:xv, self.y:yv})
				epoch_loss += c

			print('Epoch ', epoch, ' completed out of ', gm_epochs, ' loss: ', epoch_loss)
