+++
title = "Image Augmentation Is All You Need: Regularizing Deep Reinforcement   Learning from Pixels"
date = "2020-04-28"
weight = 20200428

template="resources/paper.html"

[extra]
web = "https://arxiv.org/abs/2004.13649"

author = "Ilya Kostrikov, Denis Yarats, Rob Fergus"

abstract = """We propose a simple data augmentation technique that can be applied to standard model-free reinforcement learning algorithms, enabling robust learning directly from pixels without the need for auxiliary losses or pre-training. The approach leverages input perturbations commonly used in computer vision tasks to regularize the value function. Existing model-free approaches, such as Soft Actor-Critic (SAC), are not able to train deep networks effectively from image pixels. However, the addition of our augmentation method dramatically improves SAC's performance, enabling it to reach state-of-the-art performance on the DeepMind control suite, surpassing model-based (Dreamer, PlaNet, and SLAC) methods and recently proposed contrastive learning (CURL). Our approach can be combined with any model-free reinforcement learning algorithm, requiring only minor modifications. An implementation can be found at https://sites.google.com/view/data-regularized-q."""
+++
