import numpy as np
import random
import math
import pdb
import sys
import pickle



class Neuron:

		def __init__(self, inputV):
			self.outfield = None
			self.weights = []
			self.new = 1
			self.inputV = inputV
			self.bias = None
			self.sqrerror = None
			self.error = None
			self.layertype = None





		def Neuronfunc(self, layertype, last_layer, inputArr):
			
			'''
			Function: Neuronfunc
			Summary: Node activation and setup
			Examples: InsertHere
			Attributes: 
				@param (self): class values
				@param (layertype):type of layer "flatten", "star", "dense"
				@param (last_layer):if last layer than 1
			Returns: 1 or 0 or y of activation function
			'''
			self.layertype = layertype
			if self.new == 1:

				if layertype == "flatten":  # flat conected layer with only 1 input for neuron				

					self.weights = random.random()
					self.bias = random.random()


				elif layertype == "star": # each neuron is connected with 4 neurons in each axe (kind of star) 

					size = len(self.inputV)
					self.weights = np.zeros((size), dtype = float)
					for i in range(size):
						self.weights[i] = random.random()
					self.bias = random.random()

				elif layertype == "dense": 					# dense connected naurons, each is connected 
															# with all neurons from privious layer

					x, y = np.shape(self.inputV)						 # getting shape of input array
					self.weights = np.zeros((x, y))
					self.bias = random.random()
					for xi in range (x):
						for yi in range(y):
							self.weights[xi][yi] = random.random()
			self.new = 0												 # could be potential error
			multarray = inputArr * self.weights
			neuronoutput = np.sum(multarray) + self.bias
			if last_layer == 1:
				return Neuron.activation_function(neuronoutput, "get_actfunc_output")
			else:
				return Neuron.activation_function(neuronoutput, 0)





		def Optimization(self, step, reword, output, layer, layernomber):

			'''
			Function: Optimization
			Summary: NN optimizer
			Examples: InsertHere
			Attributes: 
				@param (self):object
				@param (step):x and y of taken action
				@param (reword):ganed reword
				@param (output):output of NN
				@param (layer):NN (array of layers)
			Returns: None
			'''


			xn, yn = step
			#print("here ",xn, yn)
			self.error = output - reword
			self.sqrerror = (output - reword) ** 2
			#print("otput: ", output)
			##print("reword: ", reword)
			print("error: ", self.error)
			print("main sqere error: ", self.sqrerror)

			if self.sqrerror > 0.2:

				if self.layertype == "dense":
					#print("dense optimization")
					x, y = np.shape(self.inputV)
					if self.error > 0:
						self.weights -= 0.001
						self.weights -=0.001
						#print("weights decreasing")
					else:
						self.weights += 0.001
						self.bias += 0.001
						#print("weights encreasing")
					if layernomber > -1:
						for xi in range(x):
							for yi in range(y):
								layer[layernomber-1][xi][yi].Optimization([xi, yi], reword, output, layer, layernomber-1)

				elif self.layertype == "flatten":
					#print("flatten optimization")
					if self.error > 0:
						self.weights -= 0.001
						self.weights -= 0.001
						#print("weights decreasing")
					else:
						self.weights += 0.001
						self.bias += 0.001
						#print("weights encreasing")
					if layernomber > -1:
						layer[layernomber-1][xn][yn].Optimization([xn, yn], reword, output, layer, layernomber-1)
					
				elif self.layertype == "star":
					#print("star optimization")
					if self.error > 0:
						self.weights -= 0.001
						self.bias -= 0.001
						#print("weights decreasing")
					else:
						self.weights += 0.001
						self.bias += 0.001
						#print("weights encreasing")
					if layernomber > -1:
						v = [-1, 0, 1]
						for xi in v: 							# x vector left/right
							for yi in v: 							# y vector up/down
								if xi == 0 and yi ==0:
									layer[layernomber-1][xn][yn].Optimization([xn, yn], reword, output, layer, layernomber-1)
									continue
								for i in range(1, 5): # lenght of move
									if xn+i*xi>=0 and yn+i*yi>=0 and xn+i*xi < 19 and yn+i*yi < 19: 						# should make addaptated
										layer[layernomber-1][xn+i*xi][yn+i*yi].Optimization([xn+i*xi, yn+i*yi], reword, output, layer, layernomber-1)



		def activation_function(neuronoutput, get_actfunc_output):

			'''
			Function: activation_function
			Summary: Neuron activation function
			Examples: InsertHere
			Attributes: 
				@param (neuronoutput): output of neuron
				@param (get_actfunc_output): for the last layer when chance of move is requaired
			Returns: 1 or 0
			'''
			
			if get_actfunc_output == "get_actfunc_output":
				return 1 / (1 + (math.e ** -neuronoutput))
			elif 1 / (1 + (math.e ** -neuronoutput)) > 0.6:
				return 1 
			else:
				return 0





def Neural_net(shape, inputdata, layers):

	'''

	Function: Neural_net

	Summary: building a Neural Net

	Examples: InsertHere

	Attributes: 

		@param (shape):shape of input

		@param (inputdata):input data

	Returns: output of neural net(output), array of layers(layer)

	'''
	
	layer = [None, None, None] 										 # bad solution just for test
	layer[0], output = Layer_act(shape, inputdata, "flatten", 0, 0, layers)
	layer[1], output = Layer_act(shape, output, "star", 0, 1, layers)
	layer[2], output = Layer_act(shape, output, "flatten", 1, 2, layers)
	return output, layer 




def Layer_act(shape, inputdata, layertype, is_output_layer, layersrank, layers):

	'''
	Function: Layer_act
	Summary: input processing
	Examples: InsertHere
	Attributes: 
		@param (shape):shape of input
		@param (inputdata):input data
		@param (layertype): type of layer
		@param (is_output_layer): if last layer than 1 else 0
	Returns: InsertHere
	'''

	
	x, y = shape
	output = dataNP(x, y)
	if layers == None:									# bcs numpy doesnt accept classes
		layerneurons = dataNN(shape[0], shape[1])

	if layertype == "dense":

		for xi in range (x):
			for yi in range (y):
				if layers == None:
					layerneurons[xi][yi] = Neuron(inputdata)
					output[xi][yi] = layerneurons[xi][yi].Neuronfunc(layertype, is_output_layer, inputdata)
				else:
					output[xi][yi] = layers[layersrank][xi][yi].Neuronfunc(layertype, is_output_layer, inputdata)

	elif layertype == "flatten":

		for xi in range (x):
			for yi in range (y):
				if layers == None:
					layerneurons[xi][yi] = Neuron(inputdata[xi][yi])
					output[xi][yi] = layerneurons[xi][yi].Neuronfunc(layertype, is_output_layer, inputdata[xi][yi])
					#print("output: ", output)
				else:
					output[xi][yi] = layers[layersrank][xi][yi].Neuronfunc(layertype, is_output_layer, inputdata[xi][yi])

	elif layertype == "star": 											# experimental neurall structure

		neuron_input = []
		test = np.zeros((19,19))
		v = [1 ,0, -1]
		for xa in range(x):  					# x of neuron
			for ya in range (y): 					# y of neuron
				for xi in v: 							# x vector left/right
					for yi in v: 							# y vector up/down
						if xi == 0 and yi ==0:
							neuron_input.append(inputdata[xa][ya])
							continue
						for i in range(1, 5): # lenght of move
							if xa+i*xi>=0 and ya+i*yi>=0 and xa+i*xi < x and ya+i*yi < y: 
								neuron_input.append(inputdata[xa+i*xi][ya+i*yi])
							else:
								pass
				if layers == None:
					layerneurons[xa][ya] = Neuron(neuron_input)
					output[xa][ya] = layerneurons[xa][ya].Neuronfunc(layertype, is_output_layer, neuron_input)
				else:
					output[xa][ya] = layers[layersrank][xa][ya].Neuronfunc(layertype, is_output_layer, neuron_input)				

				
	if layers:
		return layers[layersrank], output	
	else:
		return layerneurons, output


"""
def layer(input_array, nomber_of_neurons, shape, output):
	x, y = shape
	Neurons = dataNN(x, y) 											# creating array
	output = [[0] * x for i in range(y)]							 # creating array for layers output value
	for x in range(x):
		for y in range (y):
			Neurons[x][y] = Neuron(input_array[x][y]) 					# fit neurons into the array(layer)
	return Neurons, output
"""	


def dataNN(x, y):

	'''
	Function: dataNN
	Summary: Make an python array with goten shape; can handle anythong; good for handling classes
	Examples: InsertHere
	Attributes: 
		@param (x): x shape
		@param (y): y shape
	Returns: python array
	'''

	field = [[0] * x for i in range(y)]									 # making simple python 2D array
	return field

def dataNP(x, y):

	'''
	Function: dataNP
	Summary: Make a numpy array of zerose with goten shape; cant handle classes; cant handle anything but ints and floats
	Examples: InsertHere
	Attributes: 
		@param (x): x shape
		@param (y): y shape
	Returns: numpy array
	'''

	field = np.zeros((x, y), dtype = "float64") 							# making numpy array of zeros
	return field




def OptimizationAct(x, y, reword, output, layer):
	'''

	Function: OptimizationAct

	Summary: Activation of class object activation function

	Examples: InsertHere

	Attributes: 

		@param (x):x of best output

		@param (y):y of best output

		@param (reword):reword for best choosen action

		@param (output):expectation of neural net about reword(output of neural net)

		@param (layer):array of layers

	Returns: None

	'''
 
	layer[len(layer)-1][x][y].Optimization([x, y], reword, output, layer, len(layer)-1)




def runningNN(shape, field, reword, layers):

	'''

	Function: runningNN

	Summary: Activatin Neural Net

	Examples: InsertHere

	Attributes: 

		@param (shape):shape of input 

		@param (field):input

		@param (reword):reword for taken action

		@param (is_last_epoch): flag for saving weights

	Returns: cordinates of best action

	'''
	#if can load:

	#else:
	

	x, y = shape
	#print(field)
	output, layer = Neural_net([x,y], field, layers)					# nn activation
	#print(output)
	res = np.amax(output)											 # getting the biggest value from nn output
	#print("res: ",res)
	result = np.where(output == np.amax(output)) 						# getting cords of maximall value from nn
	#print("result: ", result)
	action = list(zip(result[0], result[1]))										 # pack it in 2D array
	#print("1: ",action)
	xstep, ystep = action[0][0], action[0][1]
	#print("2: ", xstep, ystep)
	action = testforlegality(field, output, xstep, ystep)
	xstep, ystep = action
	#print(reword)						  # testing for illigal move
	OptimizationAct(xstep, ystep, reword, res, layer)
	#print("6: ", xstep, ystep)
	return action, layer










def testforlegality(field, output, x, y):  									 # testing for illigal move

	'''

	Function: testforlegality

	Summary: check if choosen action is legal

	Examples: InsertHere

	Attributes: 

		@param (field):input

		@param (output):output of Neural net

		@param (x): x cord of taken action

		@param (y): y cord of taken action

	Returns: cords of legal action with heighest value

	'''

	out = x, y
	#print("3: ", l)
	while field[x][y] != 0:													# checking info array for free position 
		output[x][y] = -1
		result = np.where(output == np.amax(output))
		#print("result:", result)
		l = list(zip(result[0], result[1]))
		#print("4: ", l)
		out = l[0][0], l[0][1]
		#print("5: ", l)
		x, y = out
	return out
