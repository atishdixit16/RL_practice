import numpy as np
from agentEnv import Environment, Agent

if __name__ == '__main__':
    env = Environment()
    gamma = 0.9
    epsilon = 0.1
    alpha = 0.8
    for episodes in range(100):
        statesSet = [[0,4]]
        agent = Agent([0,4])
        print(episodes)
        while True:
            currentState = list(agent.state)
            nextAction = env.policy(agent.state, gamma, epsilon )
            reward = agent.take_action(env, nextAction)
            bestAction = env.greedy_action(agent.state)
            env.q_table[currentState[0], currentState[1], env.actionSet.index(nextAction) ] += alpha * (reward + gamma*env.q_table [ agent.state[0], agent.state[1], env.actionSet.index(bestAction) ] - env.q_table [ currentState[0], currentState[1], env.actionSet.index(nextAction) ])
            statesSet.append(list(agent.state))
            if agent.state == env.terminal_state or env.cliff_state.count(agent.state):
                break
        print(statesSet)
        env.show(statesSet)