+++
title = "Proximal Policy Optimization (PPO)"
template = "resources/algorithm.html"
description = "Proximal Policy Optimization, or PPO, is a policy gradient method for reinforcement learning. The motivation was to have an algorithm with the data efficiency and reliable performance of TRPO, while using only first-order optimization."
[extra]
links = ["https://paperswithcode.com/method/ppo"]
+++
* Policy gradient method that improves upon traditional policy iteration by introducing a surrogate objective function with a trust region constraint, which limits the size of policy updates to prevent excessive deviation from the previous policy.
* Uses a clipping mechanism to bound the ratio of new policy probabilities to old policy probabilities, ensuring stable learning by preventing large, potentially destructive policy updates while allowing gradual improvement.
* Balances exploration and exploitation by maintaining a proximity to the previous policy while still allowing meaningful updates, making it more sample-efficient and stable compared to traditional policy gradient methods like TRPO.
