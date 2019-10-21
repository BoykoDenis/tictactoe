from tictactoe_env import TicTacToeEnv as MEnv #main env
#import tictactoe_env
#import random
#import tkinter as tk
#import pdb
#import numpy as np
import bot
import pickle

env = MEnv(19, 650, 650)
ateration = 0
reword = 0
epochs = 10
layers = None
done = False
Gametype = "EvE"#, "PvP", "EvP"#
try:
	with open('weights.pickle', 'rb') as weights:
		layers = pickle.load(weights)
		print(len(layers))
except:
	pass

env.render()
root = env.reset()

if Gametype == "EvE":
	for epoch in range(0, epochs):
		env.render()
		root = env.reset()
		#print("after reset")
		arrayCount = 0
		ateration += 1



		for ev in range(0, 361):
			if epoch == epochs -1:
				is_last_epoch = 1
			else:
				is_last_epoch = 0
			action, layers = bot.runningNN([19, 19], env.field, reword, layers) # add a parameter: Q value (for learning) + learning rate

			arrayCount +=1

			observation, reword, done, info = env.step(action, Gametype)

			if done is True:
				#print("True, reset")
				break
			root.update()

elif Gametype == "PvE":
	env.render()
	for i in range(0, 361):
		#print(env.Move)
		if env.Move == 1:
			while env.Move == 1:
				root.update()
		elif env.Move == -1:
			action, layers = bot.runningNN([19, 19], env.field, reword, layers) # add a parameter: Q value (for learning) + learning rate
			observation, reword, done, info = env.step(action, Gametype)
			root.update()
			#print(env.Move)
			#if done == True:
			#	break

#print(layers)
with open('weights.pickle', 'wb') as weights:
	pickle.dump(layers, weights)



