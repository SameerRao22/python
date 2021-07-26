from ad import *

def loss_function(parameters, ts, model):
	sum1 = 0
	for i in ts:
		sum1 = sum1 + (model(i[0:-1], parameters) - i[-1])**2

	return sum1/(2.0 * len(ts))

def gd_optim(parameters, lr, func, *args):
	temp = []
	dparam = []
	cparam = []

	for i in parameters:
		dparam.append(adnumber(i))

	for i in dparam:
		y = func(dparam, *args)
		dterm = y.d(i)
		temp.append(lr * dterm)

	for num, i in enumerate(temp):
		cparam.append(parameters[num] - temp[num])

	return cparam