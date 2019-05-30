from tkinter import *
from control import *
from dispset import *
#def grid(display_width, display_hight, nomberOfboxes, cell_size, field):
root = Tk()	
DisplaySetup()
CreateField(can, field, nomberOfboxes, cell_size)
mainloop()
