# Week 2 - Searching for Solutions

1. Motivation: Introducing search algorithms and how to improve their efficiency by minimizing a cost function.  Solving a problem involves moving from an initial state to the goal.  The domain of a problem, say the board game checkers, controls the number of possible states, and the actions that can be taken.  Imagine playing checkers without knowing any of the rules -- this is uninformed search -- and yes, winnig would take a long time.  Informed search -- where we know the rule and can evaluate the cost of each -- is a much more efficient way of finding the goal.  This week we will examine both types of algorithms, understand thier costs, and learn how to measure their performance.  

1. Learning objectives

    1. Contrast informed and uninformed search algorithms in terms of completness, optimality, time complexity and space complexity.

    1. Illustrate how a path through the state space from the initial state to the goal state is a product of actions taken to transistion from one state to the next.
    
    1. Explain and demonstrate breadth-first search, depth-first search, greedy best-first search and A* search algorithms.   

    1. Develop a working code that implement two different search algorithms.  

1. Readings
    1.  Read Chapter 3 - Solving Problems by Searching (all - except for 3.5.3, 3.6.2-4)

    1.  Text: Stuart Russel and Peter Norvig. _Artificial Intelligence: A Modern Approach_ (3rd ed). Prentice-Hall. 2010.

1. From the experts

    1. Video - [Reasoning: Goal Trees and Problem Solving](https://youtu.be/PNKj529yY5c)

    1. Video - [Search: Depth-First, Hill Climbing, Beam](https://youtu.be/j1H3jAAGlEA)

    1. Video - [Search: Optimal, Branch and Bound, A*](https://youtu.be/gGQ-vAmdAOI)

    1. Cite: Patrick Winston. 6.034 Artificial Intelligence. Fall 2010. Massachusetts Institute of Technology: MIT OpenCourseWare, https://ocw.mit.edu. License: Creative Commons BY-NC-SA.

1. Discussion

    1. Topic - Programming assignment. Post questions about the assignment here and offer assistance to others.  _Include the name of the koan and test that you are looking for help on  in your title._ 

    1. Topic - What is the difference between a world state, a state description, and a search node?  Why is the distinction useful?  _Post your response by Wednesday and find two others who approached the problem differently, acknowledge the differences and seek common ground._

1. Programming Assignment. 

    1. **Configure:**  Use the Python 3 development environment you built last week to complete this assignment. 

    1. **Complete:** From the Python Koans repository, complete the following Koans in the **python3 folder**.  If you need help or have questions, please post to week's programming assignment discussion topic.   

        1. about_true_and_false.py
        
        1. about_dictionaries.py
        
        1. about_classes.py

        1. about_methods.py

        1. about_inheritance.py

    1. Helpful Resources

        1. [PyToLearn](http://pytolearn.csd.auth.gr/index.html) -- Introductory Python tutorial focused on data science and statistics

        1. [Scipy Lecture Notes](http://www.scipy-lectures.org/) -- An in-depth Python tutorial covering the basics and data science related packages

        1. [Problem Solving with Algorithms and Data Structures using Python](https://interactivepython.org/runestone/static/pythonds/index.html#) -- Algorithms are recipes for solving problems 

        1. [Python Challenge](http://www.pythonchallenge.com/) -- A gamified Python Tutorial

        1. [iPython Tutorial](https://www.learnpython.org/) -- iPython based introductory tutorial

        1. [Solr](https://www.sololearn.com/Course/Python/) -- A beginning to intermediate Python tutorial available online and with mobile app

        1. [Repl.it](https://repl.it/) -- An online development environment for Python and other languages
    
    1. **Submit:** 
        1. Run all koans using the `run.sh` script for macOS or Linux systems, or `run.bat` script for Windows systems.  
        
        1. Take a screen shot of your results and submit it to dropbox by midnight Sunday.  
        1. Directions for how to take a screenshot can be found here for [macOS](https://www.wikihow.com/Take-a-Screenshot-on-a-Mac), [Linux](https://www.wikihow.com/Take-a-Screenshot-in-Linux) and [Windows](https://www.wikihow.com/Take-a-Screenshot-in-Microsoft-Windows).  
