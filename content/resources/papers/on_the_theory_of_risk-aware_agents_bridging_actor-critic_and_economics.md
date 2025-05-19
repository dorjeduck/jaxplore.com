+++
title = "On the Theory of Risk-Aware Agents: Bridging Actor-Critic and Economics"
date = "2023-10-30"
weight = 20231030

template="resources/paper.html"

[extra]
web = "https://arxiv.org/abs/2310.19527"

author = "Michal Nauman, Marek Cygan"

abstract = """Risk-aware Reinforcement Learning (RL) algorithms like SAC and TD3 were shown empirically to outperform their risk-neutral counterparts in a variety of continuous-action tasks. However, the theoretical basis for the pessimistic objectives these algorithms employ remains unestablished, raising questions about the specific class of policies they are implementing. In this work, we apply the expected utility hypothesis, a fundamental concept in economics, to illustrate that both risk-neutral and risk-aware RL goals can be interpreted through expected utility maximization using an exponential utility function. This approach reveals that risk-aware policies effectively maximize value certainty equivalent, aligning them with conventional decision theory principles. Furthermore, we propose Dual Actor-Critic (DAC). DAC is a risk-aware, model-free algorithm that features two distinct actor networks: a pessimistic actor for temporal-difference learning and an optimistic actor for exploration. Our evaluations of DAC across various locomotion and manipulation tasks demonstrate improvements in sample efficiency and final performance. Remarkably, DAC, while requiring significantly less computational resources, matches the performance of leading model-based methods in the complex dog and humanoid domains."""
+++
