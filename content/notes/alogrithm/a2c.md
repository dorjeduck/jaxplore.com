+++
title = "Advantage Actor-Critic (A2C)"
template = "resources/algorithm.html"
description = "A2C, or Advantage Actor Critic, is a synchronous version of the A3C policy gradient method. As an alternative to the asynchronous implementation of A3C, A2C is a synchronous, deterministic implementation that waits for each actor to finish its segment of experience before updating, averaging over all of the actors."

[extra]
links = ["https://paperswithcode.com/method/a2c"]
+++

* Synchronous reinforcement learning algorithm that uses multiple workers training simultaneously on the same environment, updating network parameters together to reduce variance and improve stability.
* Combines policy network (actor) and value network (critic) to estimate both optimal actions and state values, using an advantage function that compares action returns to average state returns.
* Helps reduce bias in policy gradient methods by providing a more accurate estimate of an action's relative value compared to other possible actions.