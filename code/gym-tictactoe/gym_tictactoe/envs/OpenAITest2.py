import gym
env = gym.make('CartPole-v0')
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print("envac: ", env.action_space)
        print("envob: ", env.observation_space)
        print("env rendered")
        print("observations are: ", observation)
        action = env.action_space.sample()
        print("action is: ", action)
        observation, reward, done, info = env.step(action)
        print("steps: ", observation, reward, done, info)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()