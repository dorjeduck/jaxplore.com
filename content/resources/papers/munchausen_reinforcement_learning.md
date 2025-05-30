+++
title = "Munchausen Reinforcement Learning"
date = "2020-07-28"
weight = 20200728

template="resources/paper.html"

[extra]
web = "https://arxiv.org/abs/2007.14430"

author = "Nino Vieillard, Olivier Pietquin, Matthieu Geist"

abstract = """Bootstrapping is a core mechanism in Reinforcement Learning (RL). Most algorithms, based on temporal differences, replace the true value of a transiting state by their current estimate of this value. Yet, another estimate could be leveraged to bootstrap RL: the current policy. Our core contribution stands in a very simple idea: adding the scaled log-policy to the immediate reward. We show that slightly modifying Deep Q-Network (DQN) in that way provides an agent that is competitive with distributional methods on Atari games, without making use of distributional RL, n-step returns or prioritized replay. To demonstrate the versatility of this idea, we also use it together with an Implicit Quantile Network (IQN). The resulting agent outperforms Rainbow on Atari, installing a new State of the Art with very little modifications to the original algorithm. To add to this empirical study, we provide strong theoretical insights on what happens under the hood -- implicit Kullback-Leibler regularization and increase of the action-gap."""
+++
