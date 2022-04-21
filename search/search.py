# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import re
from tabnanny import check
from tokenize import ContStr
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
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
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

#Question 1:
def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    nodeStack = util.Stack()
    nodeStack.push((problem.getStartState(),[]))
    visitedNodes = set()

    while not nodeStack.isEmpty():
        currentNodeState, action = nodeStack.pop()

        if (currentNodeState not in visitedNodes):
            visitedNodes.add(currentNodeState)

            if (problem.isGoalState(currentNodeState)):
                return action
            
            else:
                for nextNode in problem.getSuccessors(currentNodeState):
                    nodeStack.push((nextNode[0], action + [nextNode[1]]))
    return action

    util.raiseNotDefined()

# Question 2:
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"



    nodeQueue = util.Queue()
    nodeQueue.push((problem.getStartState(), []))
    visitedNodes = set()

    while not nodeQueue.isEmpty():
        currentNodeState, action = nodeQueue.pop()

        if (currentNodeState not in visitedNodes):
            visitedNodes.add(currentNodeState)

            if (problem.isGoalState(currentNodeState)):
                return action
            
            else:
                for nextNode in problem.getSuccessors(currentNodeState):
                    nodeQueue.push((nextNode[0], action + [nextNode[1]]))
 
    util.raiseNotDefined()

# Question 3:
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    nodePriorityQueue = util.PriorityQueue()
    nodePriorityQueue.push((problem.getStartState(), [], 0), 0)
    visitedNodes = {}

    while not nodePriorityQueue.isEmpty():
        currentNodeState, action, cost = nodePriorityQueue.pop()

        if ((currentNodeState not in visitedNodes) or (cost < visitedNodes[currentNodeState])):
            visitedNodes[currentNodeState] = cost

            if (problem.isGoalState(currentNodeState)):
                return action

            else:
                for nextNode in problem.getSuccessors(currentNodeState):
                    nodePriorityQueue.update(
                        (nextNode[0], action + [nextNode[1]], cost + nextNode[2]), cost + nextNode[2])
    return action

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

#Question 4: 
def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    nodePriorityQueue = util.PriorityQueue()
    nodePriorityQueue.push((problem.getStartState(), [], 0), 0)
    visitedNodes = set()

    while not nodePriorityQueue.isEmpty():
        currentNodeState, action, cost = nodePriorityQueue.pop()
        visitedNodes.add((currentNodeState, cost))

        if (problem.isGoalState(currentNodeState)):
            return action
        else:
            for nextNode in problem.getSuccessors(currentNodeState):
                _action = action + [nextNode[1]]
                _cost = problem.getCostOfActions(_action)
                _node = (nextNode[0], _action, _cost)

                check = False
                for visited in visitedNodes:
                    if(nextNode[0] == visited[0] and _cost >= visited[1]):
                        check = True
                
                if (not check):
                    nodePriorityQueue.push(_node, _cost + heuristic(nextNode[0], problem))
                    visitedNodes.add((nextNode[0], _cost))
        
    return action
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
