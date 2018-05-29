# Week 7 - Machine Learning - Learning with Decision Trees - Solution

**Solution:**

1. Learning tennis is much simpler than learning to speak. The requisite skills can be divided into movement, playing strokes, and strategy. The environment consists of the court, ball, opponent, and one’s own body. The relevant sensors are the visual system and proprioception (the sense of forces on and position of one’s own body parts). The effectors are the muscles involved in moving to the ball and hitting the stroke. The  learning process involves both supervised learning and reinforcement learning. Supervised learning occurs in acquiring the predictive transition models, e.g., where the opponent will hit the ball, where the ball will land, and what trajectory the ball will have after one’s own stroke (e.g., if I hit a half-volley this way, it goes into the net, but if I hit it that way, it clears the net). Reinforcement learning occurs when points are won and lost—this is particularly important for strategic aspects of play such as shot placement and positioning (e.g., in 60% of the points where I hit a lob in response to a cross-court shot, I end up losing the point). In the early stages, reinforcement also occurs when a shot succeeds in clearing the net and landing in the opponent’s court. Achieving this small success is itself a sequential process involving many motor control commands, and there is no teacher available to tell the learner’s motor cortex which motor control commands to issue.

1. Note that to compute each split, we need to compute Remainder(Ai) for each attribute Ai, and select the attribute the provides the minimal remaining information, since the existing information prior to the split is the same for all attributes we may choose to split on. Computations for first split: remainders for A1, A2, and A3 are

    (4/5)(−2/4 log(2/4) − 2/4 log(2/4)) + (1/5)(−0 − 1/1 log(1/1)) = 0.800
    (3/5)(−2/3 log(2/3) − 1/3 log(1/3)) + (2/5)(−0 − 2/2 log(2/2)) ≈ 0.551
    (2/5)(−1/2 log(1/2) − 1/2 log(1/2)) + (3/5)(−1/3 log(1/3) − 2/3 log(2/3)) ≈ 0.951

Choose A2 for first split since it minimizes the remaining information needed to classify all examples. Note that all examples with A2 = 0, are correctly classified as B = 0. So we only need to consider the three remaining examples (x3,x4,x5) for which A2 = 1. After splitting on A2, we compute the remaining information for the other two attributes on the three remaining examples (x3,x4,x5) that have A2 = 1. The remainders for A1 and A3 are

    (2/3)(−2/2 log(2/2) − 0) + (1/3)(−0 − 1/1 log(1/1)) = 0
    (1/3)(−1/1 log(1/1) − 0) + (2/3)(−1/2 log(1/2) − 1/2 log(1/2)) ≈ 0.667.

So, we select attribute A1 to split on, which correctly classifies all remaining example.