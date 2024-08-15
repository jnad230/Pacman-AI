import logging
import time
from typing import Tuple

import util
from game import Actions, Agent, Directions
from logs.search_logger import log_function
from pacman import GameState


class q1a_problem:
    """
    A search problem defines the state space, start state, goal test, successor
    function and cost function.  This search problem can be used to find paths
    to a particular point on the pacman board.

    The state space consists of (x,y) positions in a pacman game.

    Note: this search problem is fully specified; you should NOT change it.
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

        search_state = {
            "pacman_position": pacman_position,
            "food_locations": food_locations
        }

        return search_state

    @log_function
    def isGoalState(self, state):
        "*** YOUR CODE HERE ***"
        goal_state = self.getStartState()
        # If all food dots have been eaten, pacman wins
        goal_position = goal_state["food_locations"][0]
        return goal_position == state

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
                   Directions.WEST:  (-1, 0),
                   Directions.STOP:  (0, 0)}

        _directionsAsList = _directions.items()


        x, y = state
        x_int, y_int = int(x+0.5), int(y+0.5)

        successors = []
        
        # Getting the possible actions given the position of pacman
        for dir, vec in _directionsAsList:
            dx, dy = vec
            next_x = x_int + dx
            next_y = y_int + dy
            if not self.startingGameState.hasWall(next_x, next_y): successors.append(((next_x, next_y), dir, 1))

        return successors


