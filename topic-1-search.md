# Topic 1: Searching for Solutions

1. **Motivation:** Introducing search algorithms and how to improve their efficiency by minimizing a cost function.  Solving a problem involves moving from an initial state to the goal.  The domain of a problem, say the board game checkers, controls the number of possible states and the actions that can be taken.  Imagine playing checkers without knowing any of the rules -- this is uninformed search -- and yes, winning would take a long time.  Informed search -- where we know the rule and can evaluate the cost of each -- is a much more efficient way of finding the goal.  This week we will examine both types of algorithms, understand their costs, and learn how to measure their performance.

1. **Learning objectives**

    1. Construct a model of a search tree, explain the role of nodes and edges, and explain the difference between a graph and a tree.

    1. Contrast informed and uninformed search algorithms in terms of completeness, optimality, time complexity and space complexity.

    1. Illustrate how a path through the state space from the initial state to the goal state is a product of actions taken to transition from one state to the next.

    1. Explain and demonstrate breadth-first search, depth-first search, greedy best-first search and A* search algorithms.

1. **Readings**

    1. Read Chapter 3 - Solving Problems by Searching (all - except for 3.5.3, 3.6.2-4)

    1. Text: Stuart Russel and Peter Norvig. _Artificial Intelligence: A Modern Approach_ (3rd ed). Prentice-Hall. 2010.

1. **From the experts**

    1. Video - [Reasoning: Goal Trees and Problem Solving](https://youtu.be/PNKj529yY5c)

    1. Video - [Search: Depth-First, Hill Climbing, Beam](https://youtu.be/j1H3jAAGlEA)

    1. Video - [Search: Optimal, Branch and Bound, A*](https://youtu.be/gGQ-vAmdAOI)

    1. Cite: Patrick Winston. 6.034 Artificial Intelligence. Fall 2010. Massachusetts Institute of Technology: MIT OpenCourseWare, [MITOpenCourseWare](https://ocw.mit.edu). License: Creative Commons BY-NC-SA.

    1. Demonstration - [Interactive demonstration of search algorithms](https://qiao.github.io/PathFinding.js/visual/).

    1. Cite: Xu, X. (n.d.). PathFinding.js. Retrieved July 11, 2018, from [Demonstrations of Search Algorithms](https://qiao.github.io/PathFinding.js/visual/) - A comprehensive path-finding library for grid based games.

    1. Demonstration - [Visualgo.net - DFS and BFS](https://visualgo.net/en/dfsbfs)

    1. Cite: VisuAlgo - Graph Traversal (Depth/Breadth First Search). (n.d.). Retrieved July 11, 2018, from [Visualgo.net - DFS and BFS](https://visualgo.net/en/dfsbfs)

1. **Discussion**

    1. Discuss - Programming assignment. Post questions about the assignment here and please offer assistance to others.  _Include the name of the koan and test that you are looking for help on  in your title._

    1. Read [How a Self-Driving Uber Killed a Pedestrian in Arizona](https://www.nytimes.com/interactive/2018/03/20/us/self-driving-uber-pedestrian-killed.html).

    1. Discuss: Autonomous vehicle safety: On a warm Sunday night in Tempe Arizona, Elaine Herzberg was walking her bike across a street. Maybe she thought that the car approaching car would slow, or change lanes. The driver behind the wheel was alert but was simply there to keep an eye on the artificial intelligence (AI) that was in control of the car. An array of sensors fed streams of data to the AI as it drove cautiously through the night at 5 MPH below the posted speed limit. Tragically, none of the participants involved in this accident were able to prevent it.  Moments later -- having been hit by a vehicle moving at 40 MPH -- Elaine Herzberg lay dying on the side of the road.

    1. _Respond to the following prompts by midnight Wednesday and by midnight Sunday.  Please share your respectful thoughts with two other student's responses._

        1. Which of the participants is responsible for this tragic accident?

        2. How can an AI be held accountable?

1. **Quiz**

    1. What is the difference between a world state, a state description, and a search node?  Why is the distinction useful?