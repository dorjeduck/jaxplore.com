+++
title = "Learning Discrete World Models for Heuristic Search"
date = "2024-08-09"
weight = 20240809


template="resources/paper.html"

[extra]
web = "https://rlj.cs.umass.edu/2024/papers/Paper225.html"

authors = "Forest Agostinelli, Misagh Soltani"

abstract = "For many sequential decision making problems, planning is often necessary to find solutions. However, for domains such as those encountered in robotics, the transition function, also known as the world model, is often unknown. While model-based reinforcement learning methods learn world models that can then be used for planning, such approaches are limited by errors that accumulate when the model is applied across many timesteps as well as the inability to re-identify states during planning. To solve these problems, we introduce DeepCubeAI, an algorithm that learns a world model that represents states in a discrete latent space, uses reinforcement learning to learn a heuristic function that generalizes over start and goal states using this learned model, and combines the learned model and learned heuristic function with heuristic search to solve problems. Since the latent space is discrete, we can prevent the accumulation of small errors by rounding and we can re-identify states by simply comparing two binary vectors. In our experiments on a pixel representation of the Rubik's cube, Sokoban, IceSlider, and DigitJump, we find that DeepCubeAI is able to apply the model for thousands of steps without accumulating any error. Furthermore, DeepCubeAI solves over 99% of test instances in all domains, generalizes across goal states, and significantly outperforms a greedy policy that does not plan with the learned world model."
+++