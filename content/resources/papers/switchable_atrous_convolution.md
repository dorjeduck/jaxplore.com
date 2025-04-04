+++
title = "DetectoRS: Detecting Objects with Recursive Feature Pyramid and Switchable Atrous Convolution"
date = "2020-06-03"
weight = 20200603

template="resources/paper.html"

[extra]
web = "https://arxiv.org/abs/2006.02334v2"

author = "JSiyuan Qiao, Liang-Chieh Chen, Alan Yuille"

abstract = "Many modern object detectors demonstrate outstanding performances by using the mechanism of looking and thinking twice. In this paper, we explore this mechanism in the backbone design for object detection. At the macro level, we propose Recursive Feature Pyramid, which incorporates extra feedback connections from Feature Pyramid Networks into the bottom-up backbone layers. At the micro level, we propose Switchable Atrous Convolution, which convolves the features with different atrous rates and gathers the results using switch functions. Combining them results in DetectoRS, which significantly improves the performances of object detection. On COCO test-dev, DetectoRS achieves state-of-the-art 55.7% box AP for object detection, 48.5% mask AP for instance segmentation, and 50.0% PQ for panoptic segmentation. The code is made publicly available."
+++