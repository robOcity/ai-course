# Search Exercise

Use this tree and graph to answer the questions below.  _Solve the problems by hand, not in code._  Use the videos posted in the Lecture section of the course on [Worldclass](https://worldclass.regis.edu) for demonstrations of the techniques required and the algorithms below to clarify your thinking.

![Use this graph and tree to answer the questions below](images/informed-search-graphs.png)

---

## Questions

1. Search the tree and assume I is the goal.  Use alphabetic order of your data structures for uninformed searches and path cost for informed searches.  Use alphabetic order to break ties.  _In what order are the nodes expanded_?

    * Depth First Search:

    * Breadth First Search:

    * Uniform Cost Search:

2. Search the graph and assume E is the goal.  Use alphabetic order of your data structures for uninformed search and for informed search use path cost, heuristic estimate, or the combination as appropriate for the algorithm.  Use alphabetic order to break ties.  _What is the path to the goal and it's cost?_  

    * Depth First Search:

    * Hill Climbing:

    * A*:

3. Is the heuristic in the graph _admissible_?  If not, _why_?
<br></br>
<br></br>
<br></br>

4. Is the heuristic in the graph _consistent_?  If not, _why_?
<br></br>
<br></br>
<br></br>

---

## Uninformed Search Algorithms

### Depth First Search

__function__ DEPTH-FIRST-SEARCH(_problem_) __returns__ a solution, or failure  
&emsp;_node_ &larr; a node with STATE = _problem_.INITIAL\-STATE, PATH\-COST = 0    
&emsp;__if__ _problem_.GOAL\-TEST(_node_.STATE) __then return__ SOLUTION(_node_)  
&emsp;_frontier_ &larr; a LIFO queue with _node_ as the only element  
&emsp;_explored_ &larr; an empty set  
&emsp;__loop do__  
&emsp;&emsp;&emsp;__if__ EMPTY?(_frontier_) __then return__ failure  
&emsp;&emsp;&emsp;_node_ &larr; POP(_frontier_) /\* chooses the deepest node in _frontier_ \*/  
&emsp;&emsp;&emsp;add _node_.STATE to _explored_  
&emsp;&emsp;&emsp;__for each__ _action_ __in__ _problem_.ACTIONS(_node_.STATE) __do__  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;_child_ &larr; CHILD\-NODE(_problem_,_node_,_action_)  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;__if__ _child_.STATE is not in _explored_ or _frontier_ __then__  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;__if__ _problem_.GOAL\-TEST(_child_.STATE) __then return__ SOLUTION(_child_)  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;_frontier_ &larr; INSERT(_child_,_frontier_)

---

### Breadth First Search

__function__ BREADTH-FIRST-SEARCH(_problem_) __returns__ a solution, or failure  
&emsp;_node_ &larr; a node with STATE = _problem_.INITIAL\-STATE, PATH\-COST = 0    
&emsp;__if__ _problem_.GOAL\-TEST(_node_.STATE) __then return__ SOLUTION(_node_)  
&emsp;_frontier_ &larr; a FIFO queue with _node_ as the only element  
&emsp;_explored_ &larr; an empty set  
&emsp;__loop do__  
&emsp;&emsp;&emsp;__if__ EMPTY?(_frontier_) __then return__ failure  
&emsp;&emsp;&emsp;_node_ &larr; POP(_frontier_) /\* chooses the shallowest node in _frontier_ \*/  
&emsp;&emsp;&emsp;add _node_.STATE to _explored_  
&emsp;&emsp;&emsp;__for each__ _action_ __in__ _problem_.ACTIONS(_node_.STATE) __do__  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;_child_ &larr; CHILD\-NODE(_problem_,_node_,_action_)  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;__if__ _child_.STATE is not in _explored_ or _frontier_ __then__  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;__if__ _problem_.GOAL\-TEST(_child_.STATE) __then return__ SOLUTION(_child_)  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;_frontier_ &larr; INSERT(_child_,_frontier_)

---

## Informed Search

### Uniform Cost Search

__function__ UNIFORM-COST-SEARCH(_problem_) __returns__ a solution, or failure  
&emsp;_node_ &larr; a node with STATE = _problem_.INITIAL\-STATE, PATH\-COST = 0  
&emsp;_frontier_ &larr; a priority queue ordered by PATH\-COST, with _node_ as the only element  
&emsp;_explored_ &larr; an empty set  
&emsp;__loop do__  
&emsp;&emsp;&emsp;__if__ EMPTY?(_frontier_) __then return__ failure  
&emsp;&emsp;&emsp;_node_ &larr; POP(_frontier_) /\* chooses the lowest\-cost node in _frontier_ \*/  
&emsp;&emsp;&emsp;__if__ _problem_.GOAL\-TEST(_node_.STATE) __then return__ SOLUTION(_node_)  
&emsp;&emsp;&emsp;add _node_.STATE to _explored_  
&emsp;&emsp;&emsp;__for each__ _action_ __in__ _problem_.ACTIONS(_node_.STATE) __do__  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;_child_ &larr; CHILD\-NODE(_problem_,_node_,_action_)  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;__if__ _child_.STATE is not in _explored_ or _frontier_ __then__   
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;_frontier_ &larr; INSERT(_child_,_frontier_)  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;__else if__ _child_.STATE is in _frontier_ with higher PATH\-COST __then__  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;replace that _frontier_ node with _child_ 

---

### Hill Climbing Search (aka Greedy Search)

Apply the Uniform Cost Search algorithm and use the heuristic distance from each node to order the queue.  Heuristic values are not summed, they are point estimates of cost to the goal from _one_ place.  Smaller values are popped off first.  

---

### A* Search

Apply the Uniform Cost Search algorithm using heuristic distance estimate from each node, plus the accumulated path cost.  When a new lower cost path to a node is found, replace the previous higher cost estimate with the new lower value.

---