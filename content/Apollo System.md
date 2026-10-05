---
title: Apollo System
status: in-progress
year: 2026
role: Designer / Developer
tags:
- Python
- Hardware
- React
- Networking
- FASTAPI
publish: true
featured: false
portfolio-order: 3.0
---

<div class="project-meta">
<div class="project-meta-row"><div class="project-meta-label">Status</div><div class="project-meta-value">in-progress</div></div>
<div class="project-meta-row"><div class="project-meta-label">Year</div><div class="project-meta-value">2026</div></div>
<div class="project-meta-row"><div class="project-meta-label">Role</div><div class="project-meta-value">Designer / Developer</div></div>
<div class="project-meta-row"><div class="project-meta-label">Tags</div><div class="project-tags"><span class="project-tag">Python</span><span class="project-tag">Hardware</span><span class="project-tag">React</span><span class="project-tag">Networking</span><span class="project-tag">FASTAPI</span></div></div>
</div>

# Apollo Ambient Assistant 


## Overview

> Since I was a kid I had always admired the SciFI genre due to the seemingly simplistic but behind-the-scenes incredibly powerful computer systems and other fantastical technology. Now that I am older and have chosen to become an engineer I have started a few projects to bring me closer to a future that shares this vision. Named after one of the AIs featured in one of the best space VR games of the last few years, Lone Echo, the Apollo System or program is one of the few projects that must integrate an ecosystem across all of my techology. This includes local AI compute, secure networking and domain facing services, file sync services, large RAG memory databases and control of smart home and other personal devices. 

[view Github:](https://github.com/dylanshulman12/apollo_AI_Assistant)


## Design

This project is currently a work in progress, with all files being hosted on the github linked above. I have currently implemented the following:
- A very simple docker sandbox
- Simple tool calling
- Function Scaffolding for functions not yet fully integrated or even hosted
- AI streaming

A main goal of this project is to make the code as organized as possible, this means almost every function must belong to a class, and must be reusable and readable without excessive comments. 

## Example Runtime:


```text
Loading models
Models Loaded
Total time: 4.000272 seconds
user: Example message
AI: ANSWER
AI: ANSWER <------- Streamed answer
AI: ANSWER
AI: ANSWER
AI: ANSWER
```


*Note: Code is currently being edited and is a long term project that depends on several other pieces of an ecosystem to be built before it becomes useful such as a personal drive, a functioning compute server. Therefore, the example runtime is an emulation of loading a model into vram as currently strong ai reasoning models are limited to higher end hardware currently in the compute server, see other [project](#home-server-build)*
