+++
title="Value Function"

[extra]
links = ["https://spinningup.openai.com/en/latest/spinningup/rl_intro.html#trajectories"]
+++

A value function predicts the expected <a href="#reward-and-return">return</a> from a <a href="#state">state</a> when following a specific <a href="#policy">policy</a>.

* **On-Policy Value Function $V^{\pi}(s)$**: Expected return when starting in state $s$ and following policy $\pi$:


$$
V^{\pi}(s) = \underset{\tau \sim \pi}{\Epsilon}\left[R(\tau) \mid s_0 = s\right]
$$

* **On-Policy Action-Value Function**: Expected return when starting in state $s$, taking action $a$, then following policy $\pi$:

$$
Q^{\pi}(s,a) = \underset{\tau \sim \pi}{\Epsilon}\left[R(\tau) \mid s_0 = s, a_0 = a\right]
$$

* **Optimal Value Function**: Expected return when starting in state s and following the optimal policy

$$
V^* (s) = \max_{\pi}\underset{\tau \sim \pi}{\Epsilon}\left[R(\tau) \mid s_0 = s\right]
$$

* **Optimal Action-Value Function**: Expected return when starting in state s, taking action a, then following the optimal policy

$$
Q^*(s,a) = \max_{\pi}\underset{\tau \sim \pi}{\Epsilon}\left[R(\tau) \mid s_0 = s, a_0 = a\right]
$$