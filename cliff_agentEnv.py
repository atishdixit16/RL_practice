import numpy as np

class Agent:
    def __init__(self, state, action):
        self.state = state
        self.action = action

    def step(self, env, a):
        if a == 'l':
            self.state[0] = np.max( [ self.state[0]-1 , 0] )
        elif a=='r':
            self.state[0] = np.min( [ self.state[0]+1 , env.length-1] )
        elif a=='u':
            self.state[1] = np.min( [ self.state[1]+1 , env.height-1] )
        elif a=='d':
            self.state[1] = np.max( [ self.state[1]-1 , 0] )
        else:
            return 0
        
        if self.state == env.terminal_state:
            reward = 0
        elif env.cliff_state.count(self.state):
            reward = -100
        else:
            reward = -1

        return reward


class Environment:
    def __init__(self):
        self.length = 10
        self.height = 5
        self.start_state = [0, 4]
        self.terminal_state = [9, 4]
        self.cliff_state = [ [1, 4], [2, 4] , [3, 4] , [4, 4] , [5, 4] , [6, 4] , [7, 4] , [8, 4] ]
        self.q_table = np.ones([self.length, self.height, 4])
        self.e_table = np.ones([self.length, self.height, 4])
        self.actionSet = ['l', 'r', 'u', 'd']

    def eps_policy(self, agent, epsilon ):
        e = np.random.rand()
        if e < epsilon:
            a = self.actionSet[np.random.randint(4)]
        else:
            a = self.actionSet[np.argmax(self.q_table[agent.state[0], agent.state[1]])]
        agent.action = a

    def greedy_policy(self, agent):
        agent.action = self.actionSet[np.argmax(self.q_table[agent.state[0], agent.state[1]])]
    
    def show(self, statesSet):
        for j in range(self.height):
            for i in range(self.length):
                if self.cliff_state.count([i,j]):
                    print('X', end="")
                elif [i,j] == self.start_state:
                    print('S', end="")
                elif [i,j] == self.terminal_state:
                    print('T', end="")
                elif statesSet.count([i,j]):
                    print('*', end="")
                else:
                    print('.', end="")
            
            print('\n')

    def done(self, agent):
        return agent.state == self.terminal_state or self.cliff_state.count(agent.state)
