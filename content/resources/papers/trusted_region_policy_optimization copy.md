+++
title = "Trust Region Policy Optimization"
date = "2015-02-19"
weight = 20150219

template="resources/paper.html"

[extra]
web = "https://arxiv.org/abs/1502.05477"

author = "John Schulman, Sergey Levine, Philipp Moritz, Michael I. Jordan, Pieter Abbeel"

abstract = "We describe an iterative procedure for optimizing policies, with guaranteed monotonic improvement. By making several approximations to the theoretically-justified procedure, we develop a practical algorithm, called Trust Region Policy Optimization (TRPO). This algorithm is similar to natural policy gradient methods and is effective for optimizing large nonlinear policies such as neural networks. Our experiments demonstrate its robust performance on a wide variety of tasks: learning simulated robotic swimming, hopping, and walking gaits; and playing Atari games using images of the screen as input. Despite its approximations that deviate from the theory, TRPO tends to give monotonic improvement, with little tuning of hyperparameters."
+++