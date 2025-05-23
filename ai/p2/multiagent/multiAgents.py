# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState: GameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState: GameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"        
        #Minimize Food Distance
        foodLists = newFood.asList()
        foodDistances = []
        for foodList in foodLists:
            foodDistances.append(util.manhattanDistance(newPos,foodList))
        minFoodDistance = min(foodDistances) if foodDistances else 0

        
        # Heurisitic
        for i in range(0,len(newGhostStates)):
            distance = util.manhattanDistance(newPos,newGhostStates[i].getPosition())
            if(distance <= 2 and newScaredTimes[i] == 0):
                return -float('inf')

        score = successorGameState.getScore()
        score += (10/minFoodDistance) if minFoodDistance != 0 else 10
        return score




def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

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

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        score = -float('inf')
        move = None
        for action in gameState.getLegalActions():
            tmp = self.miniMax(gameState.generateSuccessor(0,action),0,1)
            if(score < tmp):
                move = action
                score = tmp
        return move        

    def miniMax(self,state,depth,agentIndex):
        if(depth == self.depth or state.isWin() or state.isLose()):
            return self.evaluationFunction(state)


        actions = state.getLegalActions(agentIndex)
        if(actions is None):
            return self.evaluationFunction(state)

        nextAgent = (agentIndex + 1) % state.getNumAgents()
        nextDepth = depth+1 if nextAgent == 0 else depth
        scores = []
        for action in actions:
            scores.append(self.miniMax(state.generateSuccessor(agentIndex,action),nextDepth,nextAgent))
        
        if(agentIndex == 0):
            return max(scores)
        else:
            return min(scores) 
        

        

        
    
        

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        eval = -float('inf')
        move = None
        for action in gameState.getLegalActions():
            tmp = self.alphaPeta(eval,float('inf'),gameState.generateSuccessor(0,action),0,1)
            if(tmp > eval):
                eval = tmp
                move = action

        return move

    def alphaPeta(self,alpha: float, peta: float,state :GameState,depth: int,agentIndex :int):
        # import pdb; pdb.set_trace()
        if(depth == self.depth or state.isLose() or state.isWin()):
            return self.evaluationFunction(state)
        
        actions = state.getLegalActions(agentIndex)
        if(actions is None):
            return self.evaluationFunction(state)
        
        newAgentIndex = (agentIndex + 1) % state.getNumAgents()
        newDepth = depth + 1 if newAgentIndex == 0 else depth     

        eval = -float('inf') if agentIndex == 0 else float('inf')
        for action in actions:
            if(agentIndex == 0):
                eval = max(eval,self.alphaPeta(alpha,peta,state.generateSuccessor(agentIndex,action),newDepth,newAgentIndex))
                alpha = max(eval,alpha)
            else:
                eval = min(eval,self.alphaPeta(alpha,peta,state.generateSuccessor(agentIndex,action),newDepth,newAgentIndex))
                peta = min(eval,peta)
            if((agentIndex == 0 and alpha > peta) or (agentIndex != 0 and peta < alpha)):
                return eval
        return eval    
        


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        eval = -float('inf')
        move = None
        for action in gameState.getLegalActions(0):
            tmp = self.expectimax(gameState.generateSuccessor(0,action),0,1)
            if(tmp > eval):
                eval = tmp
                move = action
        return move
            

        
    def expectimax(self, state: GameState, depth: int, agentIndex: int):
        if(depth == self.depth or state.isLose() or state.isWin()):
            return self.evaluationFunction(state)
        
        newAgentIndex = (agentIndex + 1) % state.getNumAgents()
        newDepth = depth + 1 if newAgentIndex == 0 else depth
        evals = []
        for action in state.getLegalActions(agentIndex):
            evals.append(self.expectimax(state.generateSuccessor(agentIndex,action),newDepth,newAgentIndex))
        
        if(agentIndex == 0):
            return max(evals)
        else:
            return sum(evals) / len(evals)


def betterEvaluationFunction(currentGameState: GameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    foodPositions = currentGameState.getFood().asList()
    ghostPositions = currentGameState.getGhostPositions()
    pacmanPosition = currentGameState.getPacmanPosition()
    ghostStates = currentGameState.getGhostStates()
    # Calculate nearest food
    minFoodDistance = getMinDistance(foodPositions,pacmanPosition)
    # Calculate nearest Ghost and penalty
    scaredReward = 0
    ghostPenalty = 0
    for ghost in ghostStates:
        dist = util.manhattanDistance(pacmanPosition,ghost.getPosition()) 
        if(ghost.scaredTimer > 0):
            scaredReward += 400 / (dist + 1)
        else:
            if(dist < 2):
                ghostPenalty = 400
            elif(dist < 4):
                ghostPenalty = 200
    #heruistic
    eval = (
            currentGameState.getScore() 
            + 10/minFoodDistance
            - ghostPenalty
            + scaredReward
        ) 
    return eval

def getMinDistance(objectsPosition : [],pacmanPosition: ()):
    minDistance = float('inf')
    for objectPosition in objectsPosition:
        distance = util.manhattanDistance(objectPosition,pacmanPosition)
        minDistance = distance if distance < minDistance else minDistance
    return minDistance

# Abbreviation
better = betterEvaluationFunction
