
""" 
*WATER BALLOON
    Once a water balloon pops, is soaks the area around it. 
    The ground gets drier the further away you travel from the balloon.
    The effect of a water balloon popping can be modeled using a list. 
    Create a function that takes a list which takes the pre-pop state and returns the state after the balloon is popped. 
    The pre-pop state will contain at most a single balloon, whose size is represented by the only non-zero element.

*NOTE
    -Length of input list is always odd.
    -The input list will always be the exact length it takes for there to be exactly one border zero.
    -If the input list consists only of zeroes, return the same list.

*EXAMPLE
    pop([0, 0, 0, 0, 4, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4, 3, 2, 1, 0]
    pop([0, 0, 0, 3, 0, 0, 0]) ➞ [0, 1, 2, 3, 2, 1, 0]
    pop([0, 0, 2, 0, 0]) ➞ [0, 1, 2, 1, 0]

pop([0]) ➞ [0]
"""
# new_state = []



def pop(state):
    new_state = []
    len_state = 0
    pop_size = sum(state)

    for _ in range(pop_size):  #iterates upto pop_size - 1
        new_state.append(len_state)
        len_state+=1
    new_state.append(pop_size)
    len_state = pop_size -1

    for _ in range(pop_size):
        new_state.append(len_state)
        len_state-=1
    
    return new_state











