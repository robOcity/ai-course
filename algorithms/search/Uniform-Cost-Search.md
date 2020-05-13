# UNIFORM-COST-SEARCH

## AIMA3e
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
__Figure__ ?? Uniform\-cost search on a graph. The algorithm is identical to the general graph search algorithm in Figure ??, except for the use of a priority queue and the addition of an extra check in case a shorter path to a frontier state is discovered. The data structure for _frontier_ needs to support efficient membership testing, so it should combine the capabilities of a priority queue and a hash table.
