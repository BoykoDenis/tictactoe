from tkinter import *
def btnhandler(btn):
	print("this button is: {}".format(btn["text"]))
	print(type(btn))
	btn.config(text = "X")
	btn.config(state = "disabled")

root = Tk() 
frame = Canvas(root) 
frame.pack() 
redbutton = Button(frame, text = '   ', fg ='red', command=lambda: btnhandler(redbutton)) 
redbutton.pack( side = LEFT) 
greenbutton = Button(frame, text = 'Brown', fg='brown') 
greenbutton.pack( side = LEFT ) 
bluebutton = Button(frame, text ='Blue', fg ='blue') 
#bluebut	ton.pack( side = LEFT ) 
root.mainloop() 

