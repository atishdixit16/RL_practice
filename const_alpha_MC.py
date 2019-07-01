import numpy as np
from cliff_agentEnv import Environment, Agent

if __name__ == '__main__':
    env = Environment()
    epsilon = 0.3
    alpha = 0.8

    for episodes in range(1200):
        agent = Agent([0,4], 'd')
        
        # data record/survailence
        statesSet = [[0,4]]
        actionsSet = ['d']
        print('Episode No.:', episodes+1)
        reward = 0
        while True:
            reward += agent.step(env, agent.action[0])  # updates agent's state
            env.eps_policy(agent, epsilon ) # or env.policy(agent.state, 1/(1+2*episodes) ) #updates agent's action

            # data record/survailence
            statesSet.append(list(agent.state))
            actionsSet.append(agent.action)

            if env.done(agent):
                break
            
        # Q table update
        
        # add unique function to the arrays

        for i in range(len(statesSet)):
            env.q_table[statesSet[i][0], statesSet[i][1], env.actionSet.index(actionsSet[i])] += alpha * (reward 
            - env.q_table[statesSet[i][0], statesSet[i][1], env.actionSet.index(actionsSet[i])])

        # data record/survailence
        print(statesSet)
        env.show(statesSet)