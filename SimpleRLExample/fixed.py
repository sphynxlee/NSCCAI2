import numpy as np

# each row and column of R represents a state (the room the agent is currently in)
# positive values represent potential actions
R = np.matrix([ [-1,-1,-1,-1, 0,-1  ],
		        [-1,-1,-1, 0,-1, 100],
		        [-1,-1,-1, 0,-1,-1  ],
		        [-1, 0, 0,-1, 0,-1  ],
		        [-1, 0, 0,-1,-1, 100],
		        [-1, 0,-1,-1, 0, 100] ])

Q = np.matrix(np.zeros([6,6]))

gamma = 0.8
initial_state = 1

# Returns all available actions from the specified state
def available_actions(state):
    current_state_row = R[state,]
    av_actions = np.where(current_state_row >= 0)[1]
    return av_actions

# Get available actions in the current state
available_act = available_actions(initial_state) 

# This function chooses at random which action to be performed within the range 
# of all the available actions.
def sample_next_action(available_actions_range):
    next_action = int(np.random.choice(available_act,1))
    return next_action

# Grab next action to take
action = sample_next_action(available_act)

# This function updates the Q matrix according to the path selected and the Q 
# learning algorithm
def update(current_state, action, gamma):
    
    max_index = np.where(Q[action,] == np.max(Q[action,]))[1]

    if max_index.shape[0] > 1:
        max_index = int(np.random.choice(max_index, size = 1))
    else:
        max_index = int(max_index)
    max_value = Q[action, max_index]
    
    # Q learning formula
    Q[current_state, action] = R[current_state, action] + gamma * max_value

# Update Q matrix
update(initial_state,action,gamma)

#-------------------------------------------------------------------------------
# Training

#---------------------------------------------------------------
# TRAINING
# Train over 10 000 iterations. (Re-iterate the process above).
#----------------------------------------------------------------
for i in range(10000):
    current_state = np.random.randint(0, int(Q.shape[0]))
    available_act = available_actions(current_state)
    action = sample_next_action(available_act)
    update(current_state,action,gamma)
    
# Normalize the "trained" Q matrix => just to make it easier to compare actions with each other
print("Trained Q matrix:")
print(Q/np.max(Q)*100)

#-----------------------------------------------------------------
# TESTING
# Goal state = 5
# Example: Best sequence path starting from 2 -> 2, 3, 1, 5
#------------------------------------------------------------------

current_state = int(input("What room would you like to start in? [0,1,2,3,4 or 5]?"))
steps = [current_state]

while current_state != 5: # continue until you get outside

    next_step_index = np.where(Q[current_state,] == np.max(Q[current_state,]))[1]
    
    if next_step_index.shape[0] > 1: # if there was a tie for maximum, randomly choose next step
        next_step_index = int(np.random.choice(next_step_index, size = 1))
    else:
        next_step_index = int(next_step_index)
    
    steps.append(next_step_index)
    current_state = next_step_index


print("Path:",steps)
