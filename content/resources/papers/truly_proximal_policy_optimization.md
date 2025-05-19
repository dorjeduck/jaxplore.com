+++
title = "Truly Proximal Policy Optimization"
date = "2019-03-19"
weight = 20190319

template="resources/paper.html"

[extra]
web = "https://arxiv.org/abs/1903.07940"

author = "Yuhui Wang, Hao He, Chao Wen, Xiaoyang Tan"

abstract = """Proximal policy optimization (PPO) is one of the most successful deep reinforcement-learning methods, achieving state-of-the-art performance across a wide range of challenging tasks. However, its optimization behavior is still far from being fully understood. In this paper, we show that PPO could neither strictly restrict the likelihood ratio as it attempts to do nor enforce a well-defined trust region constraint, which means that it may still suffer from the risk of performance instability. To address this issue, we present an enhanced PPO method, named Truly PPO. Two critical improvements are made in our method: 1) it adopts a new clipping function to support a rollback behavior to restrict the difference between the new policy and the old one; 2) the triggering condition for clipping is replaced with a trust region-based one, such that optimizing the resulted surrogate objective function provides guaranteed monotonic improvement of the ultimate policy performance. It seems, by adhering more truly to making the algorithm proximal - confining the policy within the trust region, the new algorithm improves the original PPO on both sample efficiency and performance."""
+++
