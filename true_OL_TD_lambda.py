import numpy as np
from cliff_agentEnv import Environment, Agent

if __name__ == '__main__':
    env = Environment()
    gamma = 0.9
    epsilon = 0.1
    alpha = 0.8
    lamda = 0.6

    Q_old = 0

    for episodes in range(200):
        agent = Agent([0,4], 'd')
        
        # data record/survailence
        statesSet = [[0,4]]
        print('Episode No.:', episodes+1)

        while True:
            currentState, currentAction = list(agent.state), list(agent.action)
            reward = agent.step(env, currentAction[0])  # updates agent's state
            env.eps_policy(agent, epsilon ) # or env.policy(agent.state, 1/(1+2*episodes) ) #updates agent's action
            
            delta = env.q_table[currentState[0], currentState[1], env.actionSet.index(currentAction[0]) ] - Q_old
            Q_old = env.q_table [ agent.state[0], agent.state[1], env.actionSet.index(agent.action) ]
            daba  = reward + gamma*env.q_table [ agent.state[0], agent.state[1], env.actionSet.index(agent.action) ] \
                - env.q_table[currentState[0], currentState[1], env.actionSet.index(currentAction[0]) ]

            env.e_table[currentState[0], currentState[1], env.actionSet.index(currentAction[0]) ] = \
                (1-alpha) * env.e_table[currentState[0], currentState[1], env.actionSet.index(currentAction[0]) ] + 1

            env.q_table += alpha*(daba+delta)*env.e_table
            env.e_table = gamma * lamda * env.e_table


            # Q table update
            env.q_table[currentState[0], currentState[1], env.actionSet.index(currentAction[0]) ] -= alpha * delta

            # data record/survailence
            statesSet.append(list(agent.state))

            if env.done(agent):
                break
            
        # data record/survailence
        print(statesSet)
        env.show(statesSet)

env.show_q()