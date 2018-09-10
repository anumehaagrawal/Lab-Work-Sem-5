from random import seed
from random import random
from math import exp
import pandas as pd
import numpy as np
# Initialize a network
def initialize_network(n_inputs, n_hidden, n_outputs):
	network = list()
	hidden_layer = [{'weights':[random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
	network.append(hidden_layer)
	output_layer = [{'weights':[random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
	network.append(output_layer)
	return network

def calculate_z(weights,inputs):
	z=0

	for i in range(len(weights)-1):
		z=z+weights[i]*inputs[i]
	z=z+weights[-1]
	return z

def activation(z):
	act = 1.0/(1.0 +exp(-1*z))
	return act

def forward_prop(network,row):
	inputs = row
	for layer in network:
		new_inputs=[]
		for neuron in layer:
			z= calculate_z(neuron['weights'],inputs)
			neuron['output']=activation(z)
			new_inputs.append(neuron['output'])
		inputs=new_inputs
	return inputs

def sigmoid_derivative(output):
	return output*(1-output)

def backward_propagate_error(network, expected):
	for i in reversed(range(len(network))):
		layer = network[i]
		errors = list()
		if i != len(network)-1:
			for j in range(len(layer)):
				error = 0.0
				for neuron in network[i + 1]:
					error += (neuron['weights'][j] * neuron['delta'])
				errors.append(error)
		else:
			for j in range(len(layer)):
				neuron = layer[j]
				errors.append(expected[j] - neuron['output'])
		for j in range(len(layer)):
			neuron = layer[j]
			neuron['delta'] = errors[j] * sigmoid_derivative(neuron['output'])
	
def update_weights(network, row, alpha):
	for i in range(len(network)):
		inputs = row[:-1]
		if i != 0:
			inputs = [neuron['output'] for neuron in network[i - 1]]
		for neuron in network[i]:
			for j in range(len(inputs)):
				neuron['weights'][j] += alpha * neuron['delta'] * inputs[j]
			neuron['weights'][-1] += alpha * neuron['delta']

def train_network(network, train, alpha, n_epoch, n_outputs):
	for epoch in range(n_epoch):
		sum_error = 0
		for row in train:
			outputs = forward_prop(network, row)
			expected = [0 for i in range(n_outputs)]
			
			sum_error += sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
			backward_propagate_error(network, expected)
			update_weights(network, row, l_rate)

def predict(network, row):
	outputs = forward_prop(network, row)
	return outputs.index(max(outputs))
	
		


df = pd.read_csv('Iris.csv')
df=df.values.tolist()
n_inputs = 5
n_outputs =3
l_rate=0.5
network = initialize_network(n_inputs, 1, n_outputs)
train_network(network, df, l_rate, 1000, n_outputs)
for layer in network:
	print(layer)
count =0
accuracy=0
Matrix = [[0 for x in range(3)] for y in range(3)] 
for row in df:
	prediction = predict(network, row)
	Matrix[int(prediction)][int(row[-1])]=Matrix[int(prediction)][int(row[-1])]+1
	print('Expected=%d, Got=%d' % (row[-1], prediction))
	count=count+1
	if(row[-1]==prediction):
		accuracy=accuracy+1
print(accuracy/count)

precision_A=0
sum_A=1
rec_A=1
for i in range(3):
	sum_A=sum_A+Matrix[0][i]
	rec_A=rec_A+Matrix[i][0]

precision_A=Matrix[0][0]/sum_A
recal_A = Matrix[0][0]/rec_A

precision_b=0
sum_b=1
rec_b=1
for i in range(3):
	sum_b=sum_b+Matrix[1][i]
	rec_b=rec_b+Matrix[i][1]

precision_b=Matrix[1][1]/sum_b
recal_b = Matrix[1][1]/rec_b

precision_c=0
sum_c=1
rec_c=1
for i in range(3):
	sum_c=sum_c+Matrix[2][i]
	rec_c=rec_c+Matrix[i][2]

precision_c=Matrix[2][2]/sum_c
recal_c = Matrix[2][2]/rec_c

print((precision_A+precision_c+precision_b)/3)
print((recal_c+recal_A+recal_b)/3)