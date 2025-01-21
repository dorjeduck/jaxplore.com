+++
title = "Reward and Return"

[extra]
links = ["https://spinningup.openai.com/en/latest/spinningup/rl_intro.html#reward-and-return"]
+++


The reward function $R$ depends on the current <a href="#state">state</a> of the world, the action just taken, and the next <a href="#state">state</a> of the world:

$$
r_t = R(s_t, a_t, s_{t+1})
$$

The return is the cumulative reward over a <a href="#trajetory">trajectory</a>, $R(\tau)$.

* **finite-horizon undiscounted return**: the sum of rewards obtained in a fixed window of steps:

$$
R(\tau) = \sum_{t=0}^T r_t
$$

* **infinite-horizon discounted return**: the sum of all rewards ever obtained by the agent, discounted by how far off in the future they’re obtained. For $\gamma \in (0,1)$:

$$
R(\tau) = \sum_{t=0}^{\infty} \gamma^t r_t 
$$