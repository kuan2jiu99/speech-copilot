# Speech-Copilot: Leveraging Large Language Models for Speech Processing via Task Decomposition, Modularization, and Program Generation

<p align="center">
  <a href="https://2024.ieeeslt.org/">[SLT2024]</a> <a href="https://arxiv.org/abs/2407.09886">[arXiv]</a> <a href="https://sites.google.com/view/slt2024-demo-page">[Demo]</a>
</p>

The official Github page of the paper "Speech-Copilot: Leveraging Large Language Models for Speech Processing via Task Decomposition, Modularization, and Program Generation". 
- Authors: Chun-Yi Kuan<sup>🐤</sup>, Chih-Kai Yang<sup>🐤</sup>, Wei-Ping Huang<sup>🐦 </sup>, Ke-Han Lu<sup>🐦 </sup>, Hung-yi Lee
- 🐤 🐦: Equal Contribution 
- Affiliation: National Taiwan University
- Accepted to SLT2024
- arXiv Link: https://arxiv.org/abs/2407.09886
- Refer to our demo [website](https://sites.google.com/view/slt2024-demo-page) for more examples. 👍

## Overview
![overview](https://github.com/user-attachments/assets/337c0995-b314-4635-a2aa-d816240d04a6)

## Abstract
In this work, we introduce Speech-Copilot, a modular framework for instruction-oriented speech-processing tasks that minimizes human effort in toolset construction. 
Unlike end-to-end methods using large audio-language models, Speech-Copilot builds speech processing-specific toolsets by analyzing pre-collected task instructions and breaking tasks into manageable sub-tasks. 
It features a flexible agent based on large language models that performs tasks through program generation. 
Our approach achieves state-of-the-art performance on the Dynamic-SUPERB benchmark, demonstrating its effectiveness across diverse speech-processing tasks. 
Key contributions include: 1) developing an innovative framework for speech processing-specific toolset construction, 2) establishing a high-performing agent based on large language models, and 3) offering a new perspective on addressing challenging instruction-oriented speech-processing tasks. 
Without additional training processes required by end-to-end approaches, our method provides a flexible and extendable solution for a wide range of speech-processing applications.

## Evaluation Results 🏆
<img width="1078" alt="result" src="https://github.com/user-attachments/assets/029a1399-5318-4f7f-8873-d5aa172034dc">

## Code
Coming Soon.

## Baseline Models
- Qwen-Audio-Chat
    - Qwen-audio: Advancing universal audio understanding via unified large-scale audio-language models [[arXiv](https://arxiv.org/abs/2311.07919)]

- SALMONN
    - SALMONN: Towards Generic Hearing Abilities for Large Language Models [[arXiv](https://arxiv.org/abs/2310.13289)]

- LTU-AS
    - Joint Audio and Speech Understanding [[arXiv](https://arxiv.org/abs/2309.14405)]

- WavLLM
    - WavLLM: Towards Robust and Adaptive Speech Large Language Model [[arXiv](https://arxiv.org/abs/2404.00656)]

- Cascade (ASR + Audio Captioning Model + LLM)
    - ASR: Robust Speech Recognition via Large-Scale Weak Supervision [[arXiv](https://arxiv.org/abs/2212.04356)]
    - Audio Captioning Model: Qwen-audio: Advancing universal audio understanding via unified large-scale audio-language models [[arXiv](https://arxiv.org/abs/2311.07919)]
    - LLM: gpt-3.5-turbo
