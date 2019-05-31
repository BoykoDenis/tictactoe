
def WinCheck(field, butfield, Move, w, h):
	v = [-1, 1]
	count = 0
	for x in range (-1, 2):
		for y in range (-1, 2):
			count = 0
			stack = []
			stack.append(butfield[w][h])
			for i in v:
				if x == 0 and y == 0:
					continue
				try:
					wa = w
					ha = h
					while field[wa][ha] == field[wa+x*i][ha+y*i] and count < 4:
						wa, ha = wa + x*i, ha + y*i
						stack.append(butfield[wa][ha])
						count += 1
						if count >= 4:
							print("win")
							while True:
								stack.pop().config(bg = "red", fg = "blue")
							return Move
				except:
					continue

