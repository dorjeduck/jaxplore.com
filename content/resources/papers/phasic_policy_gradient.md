+++
title = "Phasic Policy Gradient"
date = "2020-09-09"
weight = 20200909

template="resources/paper.html"

[extra]
web = "https://arxiv.org/abs/2009.04416"

author = "Karl Cobbe, Jacob Hilton, Oleg Klimov, John Schulman"

abstract = "We introduce Phasic Policy Gradient (PPG), a reinforcement learning framework which modifies traditional on-policy actor-critic methods by separating policy and value function training into distinct phases. In prior methods, one must choose between using a shared network or separate networks to represent the policy and value function. Using separate networks avoids interference between objectives, while using a shared network allows useful features to be shared. PPG is able to achieve the best of both worlds by splitting optimization into two phases, one that advances training and one that distills features. PPG also enables the value function to be more aggressively optimized with a higher level of sample reuse. Compared to PPO, we find that PPG significantly improves sample efficiency on the challenging Procgen Benchmark."
+++