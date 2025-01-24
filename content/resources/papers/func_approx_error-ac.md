+++
title = "Addressing Function Approximation Error in Actor-Critic Methods"
date = "2018-02-26"
weight = 20180226

template="resources/paper.html"

[extra]
web = "https://arxiv.org/abs/1802.09477v3"

author = "Scott Fujimoto, Herke van Hoof, David Meger"

abstract = "In value-based reinforcement learning methods such as deep Q-learning, function approximation errors are known to lead to overestimated value estimates and suboptimal policies. We show that this problem persists in an actor-critic setting and propose novel mechanisms to minimize its effects on both the actor and the critic. Our algorithm builds on Double Q-learning, by taking the minimum value between a pair of critics to limit overestimation. We draw the connection between target networks and overestimation bias, and suggest delaying policy updates to reduce per-update error and further improve performance. We evaluate our method on the suite of OpenAI gym tasks, outperforming the state of the art in every environment tested."
+++