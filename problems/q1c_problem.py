import logging
import time
from typing import Tuple

import util
from game import Actions, Agent, Directions
from logs.search_logger import log_function
from pacman import GameState


class q1c_problem:
    """
    A search problem associated with finding a path that collects all of the
    food (dots) in a Pacman game.
    Some useful data has been included here for you
    """
    def __str__(self):
        return str(self.__class__.__module__)

    def __init__(self, gameState: GameState):
        """
        Stores the start and goal.

        gameState: A GameState object (pacman.py)
        costFn: A function from a search state (tuple) to a non-negative number
        goal: A position in the gameState
        """
        self.startingGameState: GameState = gameState

    @log_function
    def getStartState(self):
        "*** YOUR CODE HERE ***"
        # Get pac man's initial position
        pacman_position = self.startingGameState.getPacmanPosition()

        # Get food positions in a grid and remaining food count
        food_locations = self.startingGameState.getFood().asList()

        return (pacman_position, frozenset(food_locations))

    @log_function
    def isGoalState(self, state):
        "*** YOUR CODE HERE ***"
        return len(state[1]) == 0

    @log_function
    def getSuccessors(self, state):
        """
        Returns successor states, the actions they require, and a cost of 1.

         As noted in search.py:
             For a given state, this should return a list of triples,
         (successor, action, stepCost), where 'successor' is a
         successor to the current state, 'action' is the action
         required to get there, and 'stepCost' is the incremental
         cost of expanding to that successor
        """
        "*** YOUR CODE HERE ***"
        successors = []

        _directions = {Directions.NORTH: (0, 1),
                   Directions.SOUTH: (0, -1),
                   Directions.EAST:  (1, 0),
                   Directions.WEST:  (-1, 0)}

        _directionsAsList = _directions.items()

        x, y = state[0]
        food_locations = state[1]
        x_int, y_int = int(x+0.5), int(y+0.5)
        successors = []
        
        # Getting the possible actions given the position of pacman
        for dir, vec in _directionsAsList:
            dx, dy = vec
            next_x = x_int + dx
            next_y = y_int + dy
            
            if not self.startingGameState.hasWall(next_x, next_y):
                new_remaining_goals = food_locations - frozenset([(next_x, next_y)])

                successors.append((((next_x, next_y), new_remaining_goals), dir, 1))

        return successors

