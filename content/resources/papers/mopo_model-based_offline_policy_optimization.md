+++
title = "MOPO: Model-based Offline Policy Optimization"
date = "2020-05-27"
weight = 20200527

template="resources/paper.html"

[extra]
web = "https://arxiv.org/abs/2005.13239"

author = "Tianhe Yu, Garrett Thomas, Lantao Yu, Stefano Ermon, James Zou, Sergey Levine, Chelsea Finn, Tengyu Ma"

abstract = """Offline reinforcement learning (RL) refers to the problem of learning policies entirely from a large batch of previously collected data. This problem setting offers the promise of utilizing such datasets to acquire policies without any costly or dangerous active exploration. However, it is also challenging, due to the distributional shift between the offline training data and those states visited by the learned policy. Despite significant recent progress, the most successful prior methods are model-free and constrain the policy to the support of data, precluding generalization to unseen states. In this paper, we first observe that an existing model-based RL algorithm already produces significant gains in the offline setting compared to model-free approaches. However, standard model-based RL methods, designed for the online setting, do not provide an explicit mechanism to avoid the offline setting's distributional shift issue. Instead, we propose to modify the existing model-based RL methods by applying them with rewards artificially penalized by the uncertainty of the dynamics. We theoretically show that the algorithm maximizes a lower bound of the policy's return under the true MDP. We also characterize the trade-off between the gain and risk of leaving the support of the batch data. Our algorithm, Model-based Offline Policy Optimization (MOPO), outperforms standard model-based RL algorithms and prior state-of-the-art model-free offline RL algorithms on existing offline RL benchmarks and two challenging continuous control tasks that require generalizing from data collected for a different task. The code is available at https://github.com/tianheyu927/mopo."""
+++
