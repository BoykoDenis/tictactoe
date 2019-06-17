from tkinter import *
from XO import CreateField
from dispset import *
from data import *
display_width = 650
display_hight = 650
nomberOfboxes = 19
cell_size = int(display_hight/nomberOfboxes)
GM=1
root = Tk()
DisplaySetup(display_width, display_hight, root)
can = Canvas(root, width=display_width, height=display_hight)
can.pack() 
can = CreateField(can, nomberOfboxes, cell_size)

mainloop()


#GameStart(display_width, display_hight, nomberOfboxes, cell_size, GM)