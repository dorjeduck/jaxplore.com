+++
title = "Prioritized Experience Replay"
date = "2015-11-18"
weight = 20151118

template="resources/paper.html"

[extra]
web = "https://arxiv.org/abs/1511.05952"

author = "Tom Schaul, John Quan, Ioannis Antonoglou, David Silver"

abstract = "Experience replay lets online reinforcement learning agents remember and reuse experiences from the past. In prior work, experience transitions were uniformly sampled from a replay memory. However, this approach simply replays transitions at the same frequency that they were originally experienced, regardless of their significance. In this paper we develop a framework for prioritizing experience, so as to replay important transitions more frequently, and therefore learn more efficiently. We use prioritized experience replay in Deep Q-Networks (DQN), a reinforcement learning algorithm that achieved human-level performance across many Atari games. DQN with prioritized experience replay achieves a new state-of-the-art, outperforming DQN with uniform replay on 41 out of 49 games."
+++