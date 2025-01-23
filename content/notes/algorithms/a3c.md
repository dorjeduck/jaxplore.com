+++
title = "Asynchronous Advantage Actor-Critic (A3C)"
template = "resources/algorithm.html"
description = "A3C, Asynchronous Advantage Actor Critic, is a policy gradient algorithm in reinforcement learning that maintains a policy and an estimate of the value function . It operates in the forward view and uses a mix of $n$-step returns to update both the policy and the value-function." 
[extra]
links = ["https://paperswithcode.com/method/a3c"]
+++

* Parallel learning algorithm where multiple independent worker agents explore different environment variations concurrently, each with slightly different network parameters.
* Workers update a global network asynchronously, allowing for more diverse exploration and faster learning across different environment instances.
* Enables more efficient and robust learning by leveraging parallel computation and reducing the correlation between training samples through independent worker experiences.