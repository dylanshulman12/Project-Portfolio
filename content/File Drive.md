---
title: File Drive
status: in-progress
year: 2026
role: Designer / Developer
tags:
- Python
- FASTAPI
- React
- Typescript
publish: true
featured: false
portfolio-order: 1.0
---

<div class="project-meta">
<div class="project-meta-row"><div class="project-meta-label">Status</div><div class="project-meta-value">in-progress</div></div>
<div class="project-meta-row"><div class="project-meta-label">Year</div><div class="project-meta-value">2026</div></div>
<div class="project-meta-row"><div class="project-meta-label">Role</div><div class="project-meta-value">Designer / Developer</div></div>
<div class="project-meta-row"><div class="project-meta-label">Tags</div><div class="project-tags"><span class="project-tag">Python</span><span class="project-tag">FASTAPI</span><span class="project-tag">React</span><span class="project-tag">Typescript</span></div></div>
</div>

## Overview

> As a big fan of open source projects, I have tried many different file drives and services. But while they are feature rich, simply downloading and using a pre-made File hosting service and running it on my own hardware never gave me the feeling of discovery and control that I get by studying and building the service from scratch. So that is what I did with this project. 

[View source on Github](https://github.com/dylanshulman12/FileDrive)
## Design and Capabilities

Currently this project is capable of uploading/downloading files, and resumable chunked file uploads, and a db so a user can traverse through folders, async independent file uploads, pre-hashing files for integrity verification
![[media/image-6.png| 550]]*A screenshot from the current iteration of the file drive*

## Not Yet Implemented

- Folder and File Move logic (not yet pushed to github)
- Zip a folder before downloading
- Multi CPU-core file hasing
- Async within 1 file upload (uploading several parts of a file at once
- Permissions
- Login screen
- Left nav bar is purely aesthetic apart from the 'upload files' button, and does not have any functionality 

### Other known issues: 
- UI is not pleasing to look at
- Not yet dockerized
- Does not currently support folder uploads, just several files. However, code is present inside codebase
