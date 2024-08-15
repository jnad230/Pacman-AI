import logging

import util
from problems.q1b_problem import q1b_problem

def q1b_solver(problem: q1b_problem):
    "*** YOUR CODE HERE ***"
    
    return aStar(problem)


def aStar(problem:  q1b_problem):
    start = problem.getStartState()

    expanded_nodes = 0

    g_score = {}
    g_score[start] = 0
    f_score = {}
    f_score[start] = minimum_heuristic(start)

    # actions = []

    open_queue = util.PriorityQueue()
    # Stores each queue item with its start position and its actions list
    open_queue.push((start, []), f_score[start])


    while not open_queue.isEmpty():
        current_state, actions  = open_queue.pop()

        expanded_nodes += 1  # Increment counter each time a node is expanded

        if problem.isGoalState(current_state):       #ate all food
            return actions

        successors = problem.getSuccessors(current_state)
        # print(successors)
        for successor_state, action, cost in successors:

            temp_g_score = g_score[current_state] + cost
            temp_f_score = temp_g_score + minimum_heuristic(successor_state)

            if (successor_state not in g_score) or (temp_f_score < f_score[successor_state]):
                g_score[successor_state] = temp_g_score
                f_score[successor_state] = temp_f_score
                new_actions = actions + [action]
                open_queue.push((successor_state, new_actions), f_score[successor_state])
      
                

    return None

def minimum_heuristic(state):

    distances = [util.manhattanDistance(state[0], food) for food in state[1]]
    return min(distances) + sum(distances) if distances else 0






