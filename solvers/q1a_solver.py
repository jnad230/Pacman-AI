import logging

import util
from problems.q1a_problem import q1a_problem


def q1a_solver(problem: q1a_problem):
    "*** YOUR CODE HERE ***"
    return aStar(problem)


def aStar(problem:  q1a_problem):
    start_pos = problem.getStartState()["pacman_position"]
    food_locations = problem.getStartState()["food_locations"]

    goal_pos = food_locations[0]

    expanded_nodes = 0

    g_score = {}
    g_score[start_pos] = 0
    f_score = {}
    f_score[start_pos] = util.manhattanDistance(start_pos, goal_pos)

    actions = []

    open_queue = util.PriorityQueue()
    # Stores each queue item with its start position and its actions list
    open_queue.push((start_pos, actions), f_score[start_pos])

    came_from = {}

    while not open_queue.isEmpty():
        current_pos, actions = open_queue.pop()

        expanded_nodes += 1  # Increment counter each time a node is expanded

        if problem.isGoalState(current_pos):
            print("Total expanded nodes:", expanded_nodes)
            return actions

        for successor_pos, action, cost in problem.getSuccessors(current_pos):

            temp_g_score = g_score[current_pos] + cost
            temp_f_score = temp_g_score + util.manhattanDistance(successor_pos, goal_pos)

            if (successor_pos not in g_score) or (temp_f_score < f_score[successor_pos]):
                g_score[successor_pos] = temp_g_score
                f_score[successor_pos] = temp_f_score
                new_actions = actions + [action]
                open_queue.push((successor_pos, new_actions),
                                f_score[successor_pos])
                came_from[successor_pos] = current_pos

    print("Total expanded nodes:", expanded_nodes)
    return None
