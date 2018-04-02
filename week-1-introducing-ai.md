# Week 1 - Introducing Artificial Intelligence

1. Motivation:  Introducing the field of artificial intelligence (AI), its history and foundations.  Our text focuses on rational agents that sense and act in their environment to achieve goals, and shows how artificially intelligent systems are constructed.

1. Learning objectives

    1. Describe how thinking, acting and behaving provide a framework for understanding differing approaches to AI.

    1. Discuss the elements of a task environment and how they relate to the state space that the agent must navigate.

    1. Explain how a rational agent achieves a goal in an environment.

    1. Contrast simple reflex agents, model-based reflex agents, goal-based agents and utility-based agents.

1. Readings
    1.  Read Chapter 1 - Introduction (sections 1.1, 1.2 (skim), 1.3 (skim))

    1.  Read Chapter 2 - Intelligent Agents (all sections)

    1.  Text: Stuart Russel and Peter Norvig. _Artificial Intelligence: A Modern Approach_ (3rd ed). Prentice-Hall. 2010.

1. From the experts

    1.  The British mathematician Alan Turing work was foundational in the field of artificial intelligence and theoretical computer science.  His original work is available online and is surprisinglyt readable.

        1.  By posing the deceptively simple question "Can machines think?", Alan Turing initiated what would become field of artificial intelligence with the publication of his "Computing Machinery and Intelligence" paper ([original](http://www.turingarchive.org/browse.php/B/9) and [pdf](https://www.csee.umbc.edu/courses/471/papers/turing.pdf)) in 1950.  In this paper he proposes a simple game where the contestant tries to determine which one of two hidden conttestents is a computer.  All communication is limited to text.  Calling this the "imitation game", asks what would happen when a machine is questioned, and whether it should be considered intelligent if it able to fool the human.  The Turing test conditions artificial intelligence on acting humanly.  Cite: [On Turing’s “Computing Machinery and Intelligence”](https://graehamdouglas.com/2013/12/27/on-turings-computing-machinery-and-intelligence/).

        1.  Turing machines -- a hypothetical machine that is capable of simulating *any* computer algorithm -- are a central topic in theoretical computer science.  Turing used this abstraction to prove that an algorithm cannot determine if another algorithm will find a result and stop, or not. Known as the halting problem, Turing showed that this problem is undecidable in his 1936 [paper](http://www.turingarchive.org/browse.php/B/12). Cite: Copeland, J. (2000, July). What is a Turing Machine? Retrieved March 22, 2018, from [What is a Turing Machine](http://www.alanturing.net/turing_archive/pages/reference%20articles/what%20is%20a%20turing%20machine.html).

1. Discussion

    1. Topic - Programming assignment. Post questions about the assignment here and offer assistance to others.  .  
    
    1. Topic - Agents. Do you think the following assertions are true or false.  Support you conclusions with a example or counter example where appropriate.  _Please pick four of the following, keep your answers to a sentence or two, and post your response by Wednesday._

        1.  An agent that senses only partial information about the state cannot be perfectly rations.

        1.  There exists task environments in which every agent is rational.

        1.  The input to an agent program is the same as the input to the agent function.

        1.  Every agent function is implementable by some combination of code and machine.

        1.  Suppose an agent selects it actions at random from a set of possible actions.  There exists a deterministic task environment in which this agent is rational.

        1.  It is perfectly possible for an agent to be perfectly rational in two different task environments.

        1.  Every agent is rational in an unobservable environment.

        1.  A perfectly rational poker-playing agent never loses.

    1. Topic - Autonomous vehicle safety: On a warm Sunday night in Tempe Arizona, Elaine Herzberg was walking her bike across a street. Maybe she thought that the car approaching car would slow, or change lanes. The driver behind the wheel was alert but was simply there to keep an eye on the artificial intelligence (AI) that in control of the car. An array of sensors fed streams of data to the AI as it drove cautiously through the night at 5 MPH below the posted speed limit. Tragically, none of the participants involved in this accident were able to prevent it.  Moments later -- having been hit by a vehicle moving at 40 MPH -- Elaine Herzberg lay dying on the side of the road.  Please read [How a Self-Driving Uber
Killed a Pedestrian in Arizona](https://www.nytimes.com/interactive/2018/03/20/us/self-driving-uber-pedestrian-killed.html).  Then respond to the following prompt by midnight Wednesday and by midnight Sunday please share your respectful thoughts on three other student's responses.  _Which of the participants is responsible for this tragic accident?  How can an AI be held accountable?_


1. Programming Assignment. 

    1. **Configure:** We will be using Python 3 for all of our assignments in this class.  Prepare your development environment by installing Python and and a code editor.  

        1. Install the latest version of _Anaconda Python 3_ for your operating system from [Anaconda](https://www.anaconda.com/) > Products > Download.  If you are familiar with Python and are comfortable using pipenv and pip, then you can use your existing Python installation or get the latest from [Official Python Site](https://www.python.org/) > Downloads.  

        1. Install a coding editor such as [Visual Studio Code](https://code.visualstudio.com/) or [Atom](https://atom.io/).  Both are free and are well docuemented.  
    
        1. Clone or download the [Python Koans](https://github.com/gregmalcolm/python_koans) from [GitHub](https://github.com/).
        
            1. [Installing the Python Koans - Get started using PythonKoans on a Mac: part 1](https://youtu.be/e2WXgXEjbHY)

            1. [How to completing the Koans - Get started using PythonKoans on a Mac: part 2](https://youtu.be/2r3MLH15kQc)

    1. **Complete:** From the Python Koans repository, complete the **python3 folder**, complete the following koans and post any questions on this week's programming assignment discussion topic.   

        1. about_asserts.py
         
        1. about_strings.py

        1. about_lists.py

        1. about_control_statements.py

        1. about_statements.py 

    1. Helpful resources

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
