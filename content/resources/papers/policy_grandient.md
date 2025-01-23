+++
title = "Policy Gradient Methods for RL"
date = "2000-06-01"
weight = 20000601
description = "Function approximation is essential to reinforcement learning, but the standard approach of approximating a value function and deter(cid:173) mining a policy from it has so far proven theoretically intractable. In this paper we explore an alternative approach in which the policy is explicitly represented by its own function approximator, indepen(cid:173) dent of the value function, and is updated according to the gradient of expected reward with respect to the policy parameters. Williams's REINFORCE method and actor-critic methods are examples of this approach. Our main new result is to show that the gradient can be written in a form suitable for estimation from experience aided by an approximate action-value or advantage function. Using this result, we prove for the first time that a version of policy iteration with arbitrary differentiable function approximation is convergent to a locally optimal policy."
template="resources/paper.html"

[extra]
web = "https://papers.nips.cc/paper_files/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html"
author = "Richard S. Sutton"
+++