+++
title = "Double DQN"
template = "notes/algorithm.html"
description="A Double Deep Q-Network, or Double DQN utilises Double Q-learning to reduce overestimation by decomposing the max operation in the target into action selection and action evaluation. We evaluate the greedy policy according to the online network, but we use the target network to estimate its value."

[extra]
links = ["https://arxiv.org/abs/1509.06461v3","https://paperswithcode.com/method/double-dqn"]
+++
