from tictactoe_env import TicTacToeEnv as MEnv #main env
import random
import tkinter as tk
import sys

env = MEnv(19, 650, 650)
root = env.render()
for epoch in range (0, 2):
	env.reset()
	for ev in range (0, 361):
		#print("epoch: ", epoch)
		#print("evo-step: ", ev)
		action = random.choice(random.choice(env.action_space))
		if action == None:
			while action is None:
				action = random.choice(random.choice(env.action_space))
				#print("action is: ", action)
		a, b = action		
		env.action_space[a][b] = None
		observation, reword, done, info = env.step(action)
		#print("step output: ", observation, done, reword, info)
		if done == True:
			pass
			#print("done")
		root.update()