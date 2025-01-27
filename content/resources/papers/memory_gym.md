+++
title = "Memory Gym: Towards Endless Tasks to Benchmark Memory Capabilities of Agents"
date = "2023-09-29"
weight = 20230929

template="resources/paper.html"

[extra]
web = "https://arxiv.org/abs/2309.17207"

author = "Marco Pleines, Matthias Pallasch, Frank Zimmer, Mike Preuss"

abstract = "Memory Gym presents a suite of 2D partially observable environments, namely Mortar Mayhem, Mystery Path, and Searing Spotlights, designed to benchmark memory capabilities in decision-making agents. These environments, originally with finite tasks, are expanded into innovative, endless formats, mirroring the escalating challenges of cumulative memory games such as 'I packed my bag'. This progression in task design shifts the focus from merely assessing sample efficiency to also probing the levels of memory effectiveness in dynamic, prolonged scenarios. To address the gap in available memory-based Deep Reinforcement Learning baselines, we introduce an implementation within the open-source CleanRL library that integrates Transformer-XL (TrXL) with Proximal Policy Optimization. This approach utilizes TrXL as a form of episodic memory, employing a sliding window technique. Our comparative study between the Gated Recurrent Unit (GRU) and TrXL reveals varied performances across our finite and endless tasks. TrXL, on the finite environments, demonstrates superior effectiveness over GRU, but only when utilizing an auxiliary loss to reconstruct observations. Notably, GRU makes a remarkable resurgence in all endless tasks, consistently outperforming TrXL by significant margins."
+++