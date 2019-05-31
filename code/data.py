import numpy as np
from array import *
def dataNP(nomberOfboxes):
	fieldline = np.array([0]*nomberOfboxes)
	field = np.array([fieldline]*nomberOfboxes)
	return field

def dataNN(nomberOfboxes):
	field = [[0] * nomberOfboxes for i in range(nomberOfboxes)]
	return field

def data1D(nomberOfboxes):
	nomberOfboxes = nomberOfboxes*nomberOfboxes
	field = [0]*nomberOfboxes
	return field
