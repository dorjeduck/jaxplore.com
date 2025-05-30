+++
title = "Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement   Learning with a Stochastic Actor"
date = "2018-01-04"
weight = 20180104

template="resources/paper.html"

[extra]
web = "https://arxiv.org/abs/1801.01290"

author = "Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel, Sergey Levine"

abstract = """Model-free deep reinforcement learning (RL) algorithms have been demonstrated on a range of challenging decision making and control tasks. However, these methods typically suffer from two major challenges: very high sample complexity and brittle convergence properties, which necessitate meticulous hyperparameter tuning. Both of these challenges severely limit the applicability of such methods to complex, real-world domains. In this paper, we propose soft actor-critic, an off-policy actor-critic deep RL algorithm based on the maximum entropy reinforcement learning framework. In this framework, the actor aims to maximize expected reward while also maximizing entropy. That is, to succeed at the task while acting as randomly as possible. Prior deep RL methods based on this framework have been formulated as Q-learning methods. By combining off-policy updates with a stable stochastic actor-critic formulation, our method achieves state-of-the-art performance on a range of continuous control benchmark tasks, outperforming prior on-policy and off-policy methods. Furthermore, we demonstrate that, in contrast to other off-policy algorithms, our approach is very stable, achieving very similar performance across different random seeds."""
+++
