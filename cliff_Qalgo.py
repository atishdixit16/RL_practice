import numpy as np

class Agent:
    def __init__(self, x, y):
        self.state = [x y]

    def take_action(self, env, a):
        if a == 'l':
            self.state[0] -= 1
        elif a=='r':
            self.state[0] += 1
        elif a=='u':
            self.state[1] += 1
        elif a=='d':
            self.state[1] -= 1
        else
            return 0
        
        if this.state == env.terminal_state
            reward = 0
        elif env.cliff_state.count(this.state)
            reward = -100
        else
            reward = -1

        return this.state, reward



class Environment:
    def __init__(self):
        self.length = 20
        self.height = 10
        self.start_state = [0 9]
        self.terminal_state = [9 9]
        self.cliff_state = [ [1 9], [2 9] , [3 9] , [4 9] , [5 9] , [6 9] , [7 9] , [8 9] ]
        self.q_table = np.empty([self.length, self.height, 4])
        self.actionSet = ['l', 'r', 'u', 'd']

    def policy(self, state, gamma, epsilon ):
        e = np.random.rand()
        if e < epsilon:
            a = self.actionSet[np.random.randint(4)]
        else:
            a = self.actionSet[np.argmax(this.q_table[state[0], state[1]])]
        return a

    def greedy_action(self, state):
        return self.actionSet[np.argmax(this.q_table[state[0], state[1]])]
    
    def show(self, statesSet):
        for j in self.height:
            for i in length:
                if statesSet.count([i,j]):
                    print('*')
                elif self.cliff_state.count([i,j]):
                    print('X')
                elif [i,j] == self.start_state:
                    print('S')
                elif [i,j] == self.terminal_state:
                    print('T')
                else
                    print('.')
            
            print('\n')


