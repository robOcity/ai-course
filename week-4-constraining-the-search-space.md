# Week 4 - Constraining the Search Space

1. Motivation: pplying constraints to reduce the size of the search space resulting in dramatic improvements in search algorithm performance.

1. **Learning objectives**

    1. Explain what a _constraint satisfaction problem_ (CSP) is.

    1. Disucss a real world problem that can be described as a CSP.

    1. Illustrate how backtracking can be used to solve a CSP.

    1. Contrast differenct approaches used to solve CSPs such as backtracking and local search.

    1. Show how the 8-queens problem can be solved using backtracking.

    1. Relate the complexity of solving a CSP with the graph of its constraints.

1. **Readings**
    1. Read Chapter 6 - Constraint Satisfaction Problems (sections)

1. From the experts

    1. [Constraints: Interpreting Line Drawings](https://youtu.be/l-tzjenXrvI)

    1. [Constraints: Search, Domain Reduction](https://youtu.be/d1KyYyLmGpA)

    1. [Constraints: Visual Object Recognition](https://youtu.be/gvmfbePC2pc)

    1. Cite: Patrick Winston. 6.034 Artificial Intelligence. Fall 2010. Massachusetts Institute of Technology: MIT OpenCourseWare, [https://ocw.mit.edu](https://ocw.mit.edu). License: Creative Commons BY-NC-SA.

1. **Discussion**

    1. **Discuss:**  Programming assignment. Post questions about the assignment here and offer assistance to others.  _Include the name of the koan and test that you are looking for help on  in your title._

    1. **Discuss:** Consider the following logic puzzle: In five houses, each with a different color, live five persons of different nationalities, each of whom prefers a different brand of candy, a different drink, and a different pet. Given the following facts, the questions to answer are “Where does the zebra live, and in which house do they drink water?”  _Come up with an answer as a team,post your answer and come to class ready to summarize your approach and what you found with the class.  This is about working as a team and making a presentation, not so much about getting the right answer._


        - The Englishman lives in the red house.

        - The Spaniard owns the dog.

        - The Norwegian lives in the first house on the left.

        - The green house is immediately to the right of the ivory house.

        - The man who eats Hershey bars lives in the house next to the man with the fox.

        - Kit Kats are eaten in the yellow house.

        - The Norwegian lives next to the blue house.

        - The Smarties eater owns snails.

        - The Snickers eater drinks orange juice.

        - The Ukrainian drinks tea.

        - The Japanese eats Milky Ways.

        - Kit Kats are eaten in a house next to the house where the horse is kept.

        - Coffee is drunk in the green house.

        - Milk is drunk in the middle house.

        - Discuss different representations of this problem as a CSP. Why would one prefer one representation over another?  