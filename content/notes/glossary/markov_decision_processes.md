+++
title = "Markov Decision Processes"

[extra]
links=["https://spinningup.openai.com/en/latest/spinningup/rl_intro.html#optional-formalism","https://www.geeksforgeeks.org/markov-decision-process/","https://en.wikipedia.org/wiki/Markov_decision_process"]
+++

An MDP is a 5-tuple, $\langle S, A, R, P, \rho_0 \rangle$, where

* $S$ is the set of all valid states,
* $A$ is the set of all valid actions,
* $R : S \times A \times S \to \mathbb{R}$ is the reward function, with $r_t = R(s_t, a_t, s_{t+1})$,
* $P : S \times A \to \mathcal{P}(S)$ is the transition probability function, with $P(s'|s,a)$ being the probability of transitioning into state $s'$ if you start in state $s$ and take action $a$,
* and $\rho_0$ is the starting state distribution.

The name Markov Decision Process refers to the fact that the system obeys the Markov property: transitions only depend on the most recent state and action, and no prior history.