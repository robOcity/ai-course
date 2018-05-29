# Week 6 - Probabilistic Reasoning - Bayesian Networks

**Solve:**

1. We have a bag of three biased coins a, b, and c with probabilities of coming up heads of 20%, 60%, and 80%, respectively. One coin is drawn randomly from the bag (with equal likelihood of drawing each of the three coins), and then the coin is flipped three times to generate the outcomes X1, X2, and X3.

    1. Draw the Bayesian network corresponding to this setup and define the necessary CPTs.

    1. Calculate which coin was most likely to have been drawn from the bag if the observed flips come out heads twice and tails once.

1. Two astronomers in different parts of the world make measurements M1 and M2 of the number of stars N in some small region of the sky, using their telescopes. Normally, there is a small possibility e of error by up to one star in each direction. Each telescope can also (with a much smaller probability f) be badly out of focus (events F1 and F2), in which case the scientist will under-count by three or more stars (or if N is less than 3, fail to detect any stars at all). Consider the three networks shown in Figure 14.22.

    1. Which of these Bayesian networks are correct (but not necessarily efficient) representations of the preceding information?

    1. Which is the best network? Explain.

    1. Write out a conditional distribution for P(M1 | N), for the case where N ∈ {1, 2, 3} and M1 ∈ {0, 1, 2, 3, 4}. Each entry in the conditional distribution should be expressed as a function of the parameters e and/or f.

    1. Suppose M1 = 1 and M2 = 3. What are the possible numbers of stars if you assume no prior constraint on the values of N?

    1. What is the most likely number of stars, given these observations? Explain how to compute this, or if it is not possible to compute explain what additional information is needed and how it would affect the result.

**Post:** Post your solution to the Assignments folder as a PDF file by Sunday at Midnight.