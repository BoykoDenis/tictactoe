from data import dataNP, dataNN, data1D
from tkinter import *
from numpy import *
from array import *
from game import *
nomberOfboxes = 19
Move = 1
field = dataNP(nomberOfboxes)
butfield = dataNN(nomberOfboxes)







def CreateField(can, nomberOfboxes, cell_size):
	global butfield
	k = 0
	for w in range(0, nomberOfboxes):
		can.columnconfigure(w, minsize = cell_size)
		can.rowconfigure(w, minsize = cell_size)
		for h in range(0, nomberOfboxes):
			print("creating a button field...")
			print(can)
			butfield[w][h] = Button(can, bd = 5, relief = GROOVE, text = " ", fg ='red', command=lambda w = w, h = h: buttonf(butfield, w, h), width=2, height=1)
			butfield[w][h].grid(row = w, column = h)
			bfield = field
	return can, butfield, bfield













def buttonf(butfield, w, h):
	global Move
	global field
	if Move == 1:
		butfield[w][h].configure(text = "x", state = "disabled", bg = "green", fg = "red")
		field[w, h] = Move
		print(field)
		Move = -1
	elif Move == -1:
		butfield[w][h].configure(text = "o", state = "disabled", bg = "blue", fg = "red")
		field[w, h] = Move
		print(field)
		Move = 1
	win = WinCheck(field, butfield, Move*-1, w, h)
	if win != None:
		print("hura player {} won!!!".format(Move))
#, width=cell_size, height=cell_size