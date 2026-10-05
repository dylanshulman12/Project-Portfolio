---
title: Dactyl Manuform
status: in-progress
year: 2026
role: Maker
tags:
- Hardware
- Soldering
- Electronics
publish: true
featured: false
portfolio-order: 2.0
---

<div class="project-meta">
<div class="project-meta-row"><div class="project-meta-label">Status</div><div class="project-meta-value">in-progress</div></div>
<div class="project-meta-row"><div class="project-meta-label">Year</div><div class="project-meta-value">2026</div></div>
<div class="project-meta-row"><div class="project-meta-label">Role</div><div class="project-meta-value">Maker</div></div>
<div class="project-meta-row"><div class="project-meta-label">Tags</div><div class="project-tags"><span class="project-tag">Hardware</span><span class="project-tag">Soldering</span><span class="project-tag">Electronics</span></div></div>
</div>

# Dactyl Manuform Keyboard



> All of these years of being a software developer have led to some wrist damage. With wrist damage in mind, and my future careeer being in building physical things, I have decided to do some electronics projects. The Dactyl Manuform is a popular split, ergonomic keyboard developed by the open source community.  

## Overview

The idea of the Dactyl Manuform is to build a split keyboard that forms to the hand. This reduces wrist soreness and the risk of getting carpal tunnel, hopefully providing a better and more comfortable typing experience. 

I decided to use this as the starting point for my electronics journey as building a keyboard is a relatively easy beginner electronics project. However, while it may be "easy", it is super useful. So useful, that, once built, it will be replacing my current keyboard. 

![[media/dactylexample.jpg]]
## Design

## Specifications and Parts

- **Key PCBs:** Amoeba King single-switch PCBs, one per key, wired together by hand into a matrix
- **Sockets:** Kailh hotswap sockets, allowing hotswappable switches (easy to replace or change keyboard switches)
- **Diodes:** one per key, 1N4148W Mark T4 SMD Fast Switching Diode 150mA 75V,SOD-123
- **Microcontroller:** nice!nano v2 × 2, one per half since it's a split board
- **Firmware:** ZMK on nice_nano_v2
- **Battery**: Lithium Battery 750mAh × 2

## Build

First I wired up all the individual PCBs together. 

![[media/669f43ab-7fb7-4d57-9317-eabecc10e0aa.jpg|500]]*An individual PCB wired*


![[media/38549e59-aac3-493a-886b-fb413aad9fc0.jpg|500]]
*A photo of the each switch wired together in a matrix, with small Diode SMDs, Hotswap switches, and switches placed through the other side so the pins touch*

After you wire up each pcb into a matrix you have to find and connect those wires to the correct sockets on the microcontroller, the ports you wire depend directly on what you selected in the firmware.
![[media/35b4cb95-436a-4858-9f64-2f9b43078cb7.jpg|500]]


## What I Learned

When I first ordered my components I bought BOJACK 1N4148 Diodes which are not for surface mounting. 
They look like this: 
![[media/diodes.jpg|400]]
After I recieved them I realized I needed to change to surface mount diodes, which I never used before so that I could keep the pcb space small and fit within the case I had 3D printed. 

### 3x3 Matrix

Because I am so new to electronics I decided to first try wiring a 3x3 matrix together and see if I could get each switch to work. However, I am currently stuck and with school time constraints I got each switch to work individually but when wired together only about 3 of the switches work and will produce a key input on the keyboard. Therefore this project has been suspended until I decide to come back and work on it. 

### Next steps

I plan to desolder and use longer wiring to make testing easy and not have a tangled mess when I retest everyting. Once I get a 3x3 working, that will confirm that I understand the matrix wiring concept and can move onto placing each pcb into the normal full Dactyl Mauform matrix. 





## Other Images

![[media/1618dad2-95c4-4383-8af5-8c0ec8cdaae9.jpg|500]]
*A pcb in the 3d printed keyboard case for a fit test*
