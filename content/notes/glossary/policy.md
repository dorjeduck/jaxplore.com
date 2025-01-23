+++
title = "Policy"
template = "resources/glossary_item.html"

[extra]
links = ["https://spinningup.openai.com/en/latest/spinningup/rl_intro.html#policies"]

+++

A rule used by an agent to decide what actions to take. 
* **deterministic policy**: a policy that always chooses the same action for a given state, with no randomness: 
  
$$
a_t = \mu(s_t)
$$

* **stochastic policy**: a policy that chooses actions probabilistically, introducing randomness: (e.g.  **categorical policies** for discrete action spaces and **diagonal Gaussian policies** for continuous action spaces)

$$
a_t \sim \pi( \cdot \mid s_t)
$$

* **parameterized policy**: policies whose outputs are computable functions that depend on a set of parameters (often denoted by $\theta$ or $\phi$)
                        
$$
a_t = \mu_\theta (s_t)
$$
$$
a_t \sim \pi_\theta ( \cdot \mid s_t)
$$
                        