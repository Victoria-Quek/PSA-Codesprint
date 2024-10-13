import gymnasium as gym

# Create the CartPole-v1 environment
env = gym.make("CartPole-v1")

observation, info = env.reset()

for i in range(10):  # Run for 1000 steps
    env.render()  # Render the environment (you can skip this for speed)
    action = env.action_space.sample()  # Take a random action
    print("Action", i, ":", action)
    observation, reward, done, info, _ = env.step(action)  # Perform the action
    print("_", _)
    print("Observation", i, ":", observation)
    print("Reward", i, ":", reward)
    print("Done", i, ":", done)
    print("Info", i, ":", info)
    
    if done:  # If the episode is done, reset the environment
        observation, info = env.reset()

env.close()
