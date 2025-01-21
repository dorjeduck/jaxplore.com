+++
title="Advantage Function"

[extra]
links=["https://spinningup.openai.com/en/latest/spinningup/rl_intro.html#advantage-functions"]
+++

The advantage function $A^{\pi}(s,a)$ corresponding to a <a href="#policy">policy</a>  $\pi$ describes how much better it is to take a specific action $a$ in <a href="#state">state</a> $s$, over randomly selecting an action according to $\pi(\cdot|s)$, assuming you act according to $\pi$ forever after. 

$$
A^{\pi}(s,a) = Q^{\pi}(s,a) - V^{\pi}(s).
$$