+++
title="Model of the Environment "
template = "resources/glossary_item.html"

[extra]
links = ["https://spinningup.openai.com/en/latest/spinningup/rl_intro2.html#model-free-vs-model-based-rl"]
+++

A model of the environment is a function which predicts <a href="#state">state</a> transitions and rewards. One of the most important branching points in an RL algorithm is the question of whether the agent has access to (or learns) a model of the environment.  Algorithms which use a model are called model-based methods, and those that don’t are called model-free. 

* **Pros of Model-Based Methods**:
    * Enables agents to simulate potential outcomes before acting
    * Allows strategic thinking and systematic option evaluation
    * Improves decision-making efficiency
    * Can substantially enhance sample efficiency
* **Cons of Model-Based Methods**:
    * Ground-truth environmental models are rarely available
    * Requires learning models purely from experience
    * High risk of model bias leading to suboptimal real-world performance
    * Model-learning is inherently challenging
    * Significant time and computational investment may not yield results

