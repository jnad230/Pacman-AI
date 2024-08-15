import logging
import random

import util
from game import Actions, Agent, Directions
from logs.search_logger import log_function
from pacman import GameState
from util import manhattanDistance


def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """

    return currentGameState.getScore()


class Q2A_Agent(Agent):

    def __init__(self, evalFn='scoreEvaluationFunction', depth='3'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

    @log_function
    def getAction(self, gameState: GameState):
        """
            Returns the minimax action from the current gameState using self.depth
            and self.evaluationFunction.

            Here are some method calls that might be useful when implementing minimax.

            gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

            gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

            gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        logger = logging.getLogger('root')
        logger.info('MinimaxAgent')
        "*** YOUR CODE HERE ***"

        _, action = self.minimaxAB(gameState, 0, 0, float("-inf"), float("inf"))
        if action is not None:
            return action
        else: 
            return Directions.STOP
   
    
    def minimaxAB(self, state, depth, agent_index, alpha, beta):
        if (depth == self.depth and agent_index == 0) or state.isWin() or state.isLose():
            return self.evaluationFunction(state), None

        if agent_index == 0:
            maxEval = float('-inf')
            evaluation = maxEval
            best_action = None
            for action in state.getLegalActions(agent_index):
                successor_state = state.generateSuccessor(agent_index, action)
                evaluation, _ = self.minimaxAB(successor_state, depth, agent_index + 1, alpha, beta)
                
                if evaluation > maxEval:
                    maxEval = evaluation
                    best_action = action

                if maxEval > beta:
                    return maxEval, None

                alpha = max(alpha, maxEval)

                # Prune
                if beta <= alpha:
                    break
            
            return maxEval, best_action
        
        else:
            minEval = float('inf')
            evaluation = minEval
            best_action = None 

             # if there are more ghosts, continue getting moves for min_Player i.e ghost else get move for pacman
            if agent_index == state.getNumAgents() - 1:
                next_agent = 0      # all ghosts have been visited, set counter back to pacman
            else:
                next_agent = agent_index + 1   # increment ghost counter

            for action in state.getLegalActions(agent_index):
                successor_state = state.generateSuccessor(agent_index, action)
                if next_agent != 0:
                    next_depth = depth   # Depth stays the same, min layer maintenance till all ghosts moves are evaluated
                    evaluation, _ = self.minimaxAB(successor_state, next_depth, next_agent, alpha, beta)
                else:  # agent is pacman
                    if depth == self.depth - 1:   # reached leaf node
                        evaluation = self.evaluationFunction(successor_state)
                    else:
                        next_depth = depth + 1  # Depth increases, all min_players have made their move change layer
                        evaluation, _ = self.minimaxAB(successor_state, next_depth, next_agent, alpha, beta)
                
                if evaluation < minEval:
                    minEval = evaluation
                    best_action = action
                
                if minEval < alpha:
                    return minEval, None

                beta = min(beta, minEval)
                
            return minEval, best_action
        
