# search.py
# ---------

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        path, stepCost), where 'successor' is a successor to the current
        state, 'path' is the path required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfpaths(self, paths):
        """
         paths: A list of paths to take

        This method returns the total cost of a particular sequence of paths.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of paths that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    from game import Directions

    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    explored = set()
    frontier = util.Stack()
    frontier.push((problem.getStartState(),[]))
    while not frontier.isEmpty():
        state,path = frontier.pop()
        explored.add(state)
        if problem.isGoalState(state):
            return path
        

        frontierStates = []
        for t in frontier.list:
            frontierStates.append(t[0])

        for successor in problem.getSuccessors(state):
            if successor[0] not in explored and successor[0] not in frontierStates:
                frontier.push((successor[0],path + [successor[1]]))
        
    return []

                

    
def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    explored = set()
    frontier = util.Queue()
    frontier.push((problem.getStartState(),[]))
    while(not frontier.isEmpty()):
        state,path = frontier.pop()
        explored.add(state)
        if problem.isGoalState(state):
            return path

        frontierStates = []
        for t in frontier.list:
            frontierStates.append(t[0])

        for successor in problem.getSuccessors(state):
            if successor[0] not in explored and successor[0] not in frontierStates:
                frontier.push((successor[0],path+[successor[1]]))
    return []
        

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    explored = set()
    frontier = util.PriorityQueue()
    frontier.push((problem.getStartState(),[]),0)
    while(not frontier.isEmpty()):
        (state, path) = frontier.pop()
        explored.add(state)
        if(problem.isGoalState(state)):
            return path

        for successor in problem.getSuccessors(state):            
            if(successor[0] not in explored):
                frontierStates = []
                for t in frontier.heap:
                    frontierStates.append(t[2][0])
                newPath = path + [successor[1]]
                newCost = problem.getCostOfActions(newPath)
                if(successor[0] not in frontierStates):
                    frontier.push((successor[0],newPath),newCost)
                else:
                    for i in range(0,len(frontierStates)):
                        if(successor[0] == frontierStates[i]):  
                            if(newCost < frontier.heap[i][0]):
                                frontier.update(frontier.heap[i][2],newCost)
    return []
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    explored = set()
    frontier = util.PriorityQueue()
    frontier.push((problem.getStartState(),[]),0 + heuristic(problem.getStartState(),problem))
    while(not frontier.isEmpty()):
        (state, path) = frontier.pop()
        explored.add(state)
        if(problem.isGoalState(state)):
            return path

        for successor in problem.getSuccessors(state):            
            if(successor[0] not in explored):
                frontierStates = []
                for t in frontier.heap:
                    frontierStates.append(t[2][0])
                newPath = path + [successor[1]]
                newCost = problem.getCostOfActions(newPath) + heuristic(successor[0],problem)
                if(successor[0] not in frontierStates):
                    frontier.push((successor[0],newPath),newCost)
                else:
                    for i in range(0,len(frontierStates)):
                        if(successor[0] == frontierStates[i]):  
                            if(newCost < frontier.heap[i][0]):
                                frontier.update(frontier.heap[i][2],newCost)
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
