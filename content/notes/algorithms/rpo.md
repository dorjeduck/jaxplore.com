+++
title = "Robust Policy Optimization (RPO)"
template = "notes/algorithm.html"
description = "RPO leverages a method of perturbing the distribution representing actions. The goal is to encourage high-entropy actions and provide a better representation of the action space. The method consists of a simple modification on top of the objective of the PPO algorithm. In the RPO algorithm, the mean of the action distribution is perturbed using a random number drawn from a Uniform distribution."

[extra]
links = ["https://arxiv.org/abs/2212.07536","https://docs.cleanrl.dev/rl-algorithms/rpo/"]
+++
