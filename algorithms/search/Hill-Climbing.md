# HILL-CLIMBING

## AIMA3e
__function__ HILL-CLIMBING(_problem_) __returns__ a state that is a local maximum  
&emsp;_current_ &larr; MAKE\-NODE(_problem_.INITIAL\-STATE)  
&emsp;__loop do__  
&emsp;&emsp;&emsp;_neighbor_ &larr; a highest\-valued successor of _current_  
&emsp;&emsp;&emsp;__if__ _neighbor_.VALUE &le; _current_.VALUE __then return__ _current_.STATE  
&emsp;&emsp;&emsp;_current_ &larr; _neighbor_

---
__Figure ??__ The hill\-climbing search algorithm, which is the most basic local search technique. At each step the current node is replaced by the best neighbor; in this version, that means the neighbor with the highest VALUE, but if a heuristic cost estimate _h_ is used, we would find the neighbor with the lowest _h_.
