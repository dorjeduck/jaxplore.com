+++
title = "Deep Reinforcement Learning with Double Q-Learning"
date = "2015-09-22"
weight = 20150922

description = "The popular Q-learning algorithm is known to overestimate action values under certain conditions. It was not previously known whether, in practice, such overestimations are common, whether they harm performance, and whether they can generally be prevented. In this paper, we answer all these questions affirmatively. In particular, we first show that the recent DQN algorithm, which combines Q-learning with a deep neural network, suffers from substantial overestimations in some games in the Atari 2600 domain. We then show that the idea behind the Double Q-learning algorithm, which was introduced in a tabular setting, can be generalized to work with large-scale function approximation. We propose a specific adaptation to the DQN algorithm and show that the resulting algorithm not only reduces the observed overestimations, as hypothesized, but that this also leads to much better performance on several games."
template="resources/paper.html"

[extra]
web = "https://arxiv.org/abs/1509.06461"
authors = "Hasselt, Hado van; Guez, Arthur; Silver, David"
+++