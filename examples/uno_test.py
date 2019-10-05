import rlcard
from rlcard.agents.random_agent import RandomAgent

env = rlcard.make('uno')

env.set_mode(single_agent_mode=True)
#env.set_mode(human_mode=True)

state = env.reset()

agent = RandomAgent(env.action_num)

counter = 0
total = .0

while True:
#    action = int(input('>> Choose your action: '))
    action = agent.step(state)
    state, reward, done = env.step(action)
    if done:
        counter += 1
        total += reward
    if counter == 1000:
        break

print(total / counter)
