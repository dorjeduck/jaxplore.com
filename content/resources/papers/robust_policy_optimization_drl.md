+++
title = "Robust Policy Optimization in Deep Reinforcement Learning"
date = "2022-12-14"
weight = 20221214

template="resources/paper.html"

[extra]
web = "https://arxiv.org/abs/2212.07536"

author = "Md Masudur Rahman, Yexiang Xue"

abstract = "The policy gradient method enjoys the simplicity of the objective where the agent optimizes the cumulative reward directly. Moreover, in the continuous action domain, parameterized distribution of action distribution allows easy control of exploration, resulting from the variance of the representing distribution. Entropy can play an essential role in policy optimization by selecting the stochastic policy, which eventually helps better explore the environment in reinforcement learning (RL). However, the stochasticity often reduces as the training progresses; thus, the policy becomes less exploratory. Additionally, certain parametric distributions might only work for some environments and require extensive hyperparameter tuning. This paper aims to mitigate these issues. In particular, we propose an algorithm called Robust Policy Optimization (RPO), which leverages a perturbed distribution. We hypothesize that our method encourages high-entropy actions and provides a way to represent the action space better. We further provide empirical evidence to verify our hypothesis. We evaluated our methods on various continuous control tasks from DeepMind Control, OpenAI Gym, Pybullet, and IsaacGym. We observed that in many settings, RPO increases the policy entropy early in training and then maintains a certain level of entropy throughout the training period. Eventually, our agent RPO shows consistently improved performance compared to PPO and other techniques: entropy regularization, different distributions, and data augmentation. Furthermore, in several settings, our method stays robust in performance, while other baseline mechanisms fail to improve and even worsen the performance."
+++