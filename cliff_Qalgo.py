import numpy as np
from agentEnv import Environment, Agent

if __name__ == '__main__':
    env = Environment()
    gamma = 0.9
    epsilon = 0.1
    alpha = 0.8

    r_Q = []

    for episodes in range(100):
        agent = Agent([0,4], 'd')
        
        # data record/survailence
        statesSet = [[0,4]]
        r_Q_e = []
        print('Episode No.:', episodes+1)

        while True:
            currentState, currentAction = list(agent.state), list(agent.action)
            reward = agent.step(env, currentAction[0])  # updates agent's state
            env.greedy_policy(agent) # or env.policy(agent.state, 1/(1+2*episodes) ) #updates agent's action

            # Q table update
            env.q_table[currentState[0], currentState[1], env.actionSet.index(currentAction[0]) ] += alpha * (reward + gamma*env.q_table [ agent.state[0], agent.state[1], env.actionSet.index(agent.action) ] - env.q_table [ currentState[0], currentState[1], env.actionSet.index(currentAction[0]) ])

            # data record/survailence
            r_Q_e.append(reward)
            statesSet.append(list(agent.state))

            if env.done(agent):
                break
            
        # data record/survailence
        r_Q.append(np.sum(r_Q_e))
        print(statesSet)
        env.show(statesSet)