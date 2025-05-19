+++
title = "An Equivalence between Loss Functions and Non-Uniform Sampling in   Experience Replay"
date = "2020-07-12"
weight = 20200712

template="resources/paper.html"

[extra]
web = "https://arxiv.org/abs/2007.06049"

author = "Scott Fujimoto, David Meger, Doina Precup"

abstract = """Prioritized Experience Replay (PER) is a deep reinforcement learning technique in which agents learn from transitions sampled with non-uniform probability proportionate to their temporal-difference error. We show that any loss function evaluated with non-uniformly sampled data can be transformed into another uniformly sampled loss function with the same expected gradient. Surprisingly, we find in some environments PER can be replaced entirely by this new loss function without impact to empirical performance. Furthermore, this relationship suggests a new branch of improvements to PER by correcting its uniformly sampled loss function equivalent. We demonstrate the effectiveness of our proposed modifications to PER and the equivalent loss function in several MuJoCo and Atari environments."""
+++
