+++
title = "Phasic Policy Gradient (PPG)"
template = "notes/algorithm.html"
description = "PPG is a DRL algorithm that separates policy and value function training by introducing an auxiliary phase. The training proceeds by running PPO during the policy phase, saving all the experience in a replay buffer. Then the replay buffer is used to train the value function. This makes the algorithm considerably slower than PPO, but improves sample efficiency on Procgen benchmark."
[extra]
links = ["https://arxiv.org/abs/2009.04416","https://docs.cleanrl.dev/rl-algorithms/ppg/"]
+++
