
def buttonf(butfield, k, w, h):
	global Move
	print()
	if Move == 1:
		butfield[k].configure(text = "x")
		butfield[k].configure(state = "disabled")
		butfield[k].configure(bg = "green", fg = "red")
		field[w, h] = Move
		print(field)
		Move = -1
	elif Move == -1:
		butfield[k].configure(text = "o")
		butfield[k].configure(state = "disabled")
		butfield[k].configure(bg = "blue", fg = "red")
		field[w, h] = Move
		print(field)
		Move = 1
	print(Move)