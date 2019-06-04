import numpy as np
from agentEnv import Environment, Agent

if __name__ == '__main__':
    env = Environment()
    gamma = 0.9
    epsilon = 0.1
    alpha = 0.8

    r_Q = []

    for episodes in range(100):
        statesSet = [[0,4]]
        agent = Agent([0,4])
        r_Q_e = []
        print(episodes)
        while True:
            currentState = list(agent.state)
            currentAction = env.policy(agent.state, gamma, epsilon )
            reward = agent.take_action(env, currentAction)
            r_Q_e.append(reward)
            bestAction = env.greedy_action(agent.state)
            env.q_table[currentState[0], currentState[1], env.actionSet.index(currentAction) ] += alpha * (reward + gamma*env.q_table [ agent.state[0], agent.state[1], env.actionSet.index(bestAction) ] - env.q_table [ currentState[0], currentState[1], env.actionSet.index(currentAction) ])
            statesSet.append(list(agent.state))
            if agent.state == env.terminal_state or env.cliff_state.count(agent.state):
                break
        r_Q.append(np.mean(r_Q_e))
        print(statesSet)
        env.show(statesSet)