import numpy as np
from cliff_agentEnv import Environment, Agent

if __name__ == '__main__':
    env = Environment()
    epsilon = 0.3
    alpha = 0.8

    env.show_q()

    for episodes in range(5000):
        agent = Agent([0,4], 'd')
        
        # data record/survailence
        statesSet = [[0,4]]
        actionsSet = ['d']
        print('Episode No.:', episodes+1)
        reward = 0
        while True:
            reward += agent.step(env, agent.action[0])  # updates agent's state
            env.eps_policy(agent, epsilon ) # or env.eps_policy(agent, 1/(1+2*episodes) ) #updates agent's action

            # data record/survailence
            statesSet.append(list(agent.state))
            actionsSet.append(agent.action)

            if env.done(agent):
                break
            
        # data record/survailence
        print(statesSet)
        env.show(statesSet)

        # Q table update
        
        # take unique valuses of states and actions
        # a = np.unique(statesSet, axis=0, return_index=True) 
        # statesSet = a[0]
        # indices = a[1]
        # aset = np.array(actionsSet)
        # actionsSet = aset[ np.array (list ( indices ) ) ]

        for i in range(len(statesSet)):
            env.q_table[statesSet[i][0], statesSet[i][1], env.actionSet.index(actionsSet[i])] += alpha * (reward 
            - env.q_table[statesSet[i][0], statesSet[i][1], env.actionSet.index(actionsSet[i])])

# env.q_table

env.show_q()