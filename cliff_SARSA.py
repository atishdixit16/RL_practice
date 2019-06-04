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
        currentAction = env.policy(agent.state, gamma, epsilon )
        print(episodes)
        while True:
            currentState = list(agent.state)
            reward = agent.take_action(env, currentAction)
            NextAction = env.policy(agent.state, gamma, epsilon )
            env.q_table[currentState[0], currentState[1], env.actionSet.index(currentAction) ] += alpha * (reward + gamma*env.q_table [ agent.state[0], agent.state[1], env.actionSet.index(NextAction) ] - env.q_table [ currentState[0], currentState[1], env.actionSet.index(currentAction) ])
            statesSet.append(list(agent.state))
            currentAction = NextAction
            if agent.state == env.terminal_state or env.cliff_state.count(agent.state):
                break
        print(statesSet)
        env.show(statesSet)