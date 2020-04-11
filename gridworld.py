#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
from operator import add


# In[4]:


# Windy Gridworld
class gridworld_agent:
    def __init__(self, m, n, wind, start, goal, action_mode):
        
        # m -> Rows, n -> Columns
        # wind -> Array of length n, wind in each column
        # action_mode = "king"/"std"
        
        self.rows = m
        self.cols = n
        self.wind_grid = np.zeros([m,n])
        self.wind = wind
        self.goal = goal
        self.curr_pos = start
        self.start = start
        self.reward = 100
        self.action_mode = action_mode
        for c in range(self.cols):
            self.wind_grid[:, c] = -1*wind[c]*np.ones(self.rows)
        
        self.std_action_size = 4
        self.std_actions = {0:[-1, 0], 1:[0, 1], 2:[1, 0], 3:[0, -1]}
        
        self.king_action_size = 8
        self.king_actions = {0:[-1, 0], 1:[-1, 1], 2:[0, 1], 3:[1, 1], 4:[1, 0], 5:[1, -1], 6:[0, -1], 7:[-1, -1]}
        
        if action_mode == "king":
            self.action_size = self.king_action_size
            self.actions = self.king_actions
        else:
            self.action_size = self.std_action_size
            self.actions = self.std_actions
        
    def get_reward(self):
        if self.curr_pos == self.goal:
            return self.reward, True
        else:
            return -1, False
        
    def step(self, action):
        new_p = list( map(add, self.curr_pos, self.actions[action]) )
        if new_p[0]<self.rows and new_p[0]>=0 and new_p[1]<self.cols and new_p[1]>=0:
            self.curr_pos = new_p
            
        w = self.wind[self.curr_pos[1]]
        new_p = [self.curr_pos[0]-w, self.curr_pos[1]]
        if new_p[0]<self.rows and new_p[0]>=0:
            self.curr_pos[0] = new_p[0]
        if new_p[1]<self.cols and new_p[1]>=0:
            self.curr_pos[1] = new_p[1]
        reward, done = self.get_reward()
        return self.curr_pos, reward, done
    
    def reset(self):
        self.curr_pos = self.start
        return self.curr_pos
    
    def printenv(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print('--', end='')
            print('-')
            for j in range(self.cols):
                print('|', end='')
                if [i,j] == self.curr_pos:
                    print('*', end='')
                elif [i,j] == self.goal:
                    print('g', end='')
                else:
                    print(' ', end='')
            print('|')
        for j in range(self.cols):
            print('--', end='')
        print('-')
        for j in range(self.cols):
            print(' {}'.format(self.wind[j]), end='')
        print()


# In[ ]:




