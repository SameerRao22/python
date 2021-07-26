from optim_lib import *
import matplotlib.pyplot as plt
itera = []
lossl = [] 

def model(x, parameters):
	return parameters[0] + (parameters[1] * x[0]) + (parameters[2] * x[1])

ts = []

for i in range(5):
	for f in range(5):
		ts.append([i, f, i + f])

param = [0, 0, 0]

for i in range(100):
	param = gd_optim(param, 0.17, loss_function, ts, model)
	loss = loss_function(param, ts, model)
	print ('loss is', loss)
	itera.append(i)
	lossl.append(loss)

plt.plot(itera, lossl)

plt.show()

print(param)
print (round(model([1, 1], param)))