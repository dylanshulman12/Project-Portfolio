---
title: Home Server
status: in-progress
year: 2026
role: Designer
tags:
- Python
- CAD
- Hardware
- FreeCAD
publish: true
featured: false
portfolio-order: 0.0
---

<div class="project-meta">
<div class="project-meta-row"><div class="project-meta-label">Status</div><div class="project-meta-value">in-progress</div></div>
<div class="project-meta-row"><div class="project-meta-label">Year</div><div class="project-meta-value">2026</div></div>
<div class="project-meta-row"><div class="project-meta-label">Role</div><div class="project-meta-value">Designer</div></div>
<div class="project-meta-row"><div class="project-meta-label">Tags</div><div class="project-tags"><span class="project-tag">Python</span><span class="project-tag">CAD</span><span class="project-tag">Hardware</span><span class="project-tag">FreeCAD</span></div></div>
</div>

> For over 3 years I have been experimenting with small headless linux servers running on old laptops and mini computers meant for servers. However, with an increasing need for more power I am now currently building a more dedicated server rack. 

## Design

For power consumption reasons I went for a dual computer design. After repairing a gaming laptop with a dead motherboard, and gutting an older gaming pc. I was able to replace the desktop GPU, a NVIDIA GTX 1650 TI, with an EVGA RTX 3090 and add a newer more capable 860W power supply for the increase in energy consuption. 

This dual computer design allows for an always on, relatively lower power consumption by the laptop, while giving me the ability to use Wake on Lan or WOL to power on my more expensive 'compute server'. Both of these computers will only be accessible via Tailscale. For me, Tailscale was an excellent choice as it protects me from directly publishing services on the open internet, and instead allows me to use Tailscale's peer-to-peer mesh network, which uses the well known Wireguard protocol. This protects me from a whole range of cybersecurty attacks as long as I mitigate user error, and dont get anyone my passwords. 

### Specs

Laptop (always on)
**CPU:** Ryzen 7 5800H
**GPU:** RTX 3050 Laptop GPU
**RAM:** 8 GB

Desktop (compute server)
**CPU:** AMD Ryzen 7 5800X, 8 cores / 16 threads
**GPU:** EVGA GeForce RTX 3090 FTW3 Ultra, 24 GB GDDR6X
**RAM:** 32 GB DDR4
**Motherboard:** MSI B560-A PRO
**PSU:** MSI MAG A850GL PCIE5, 850 W (80+ Gold, ATX 3.x / PCIe 5.x)
**OS:** Fedora Linux, headless/server-oriented
**Storage:** several expandable SSDs/drives

### Design Considerations

Due to the fact that one has to pay for electricty, an always on power-hungry desktop is not such an attractive option. Below is a table with the average predicted power consumption for the two computers.

| Device         | Avg. Power Draw | Energy Used per Hour | Cost per Hour @ $0.2172/kWh |
| -------------- | --------------- | -------------------- | --------------------------- |
| Compute Server | ~418 W          | ~0.40 kWh            | ~$0.087/hr                  |
| Laptop         | ~50 W           | ~0.05 kWh            | ~$0.011/hr                  |
*The above table is a prediction on the amount of power consumption we can expect to see from the two computers. For the compute server's GPU, an Average of 350 Watts during gaming to 450 W on max usage is expected, while the CPU uses around 65W [^2]. With all the other components of the computer contributing less to the total power usage.*


Doing some dimensional analysis, with around 4 hours a day of compute use.Doing some dimensional analysis, with around 4 hours a day of compute use:

$$
4\ \frac{\text{hr}}{\text{day}}
\times
7\ \frac{\text{days}}{\text{week}}
\times
52\ \frac{\text{weeks}}{\text{year}}
=
1456\ \frac{\text{hr}}{\text{year}}
$$

$$
0.418\ \text{kW}
\times
1456\ \frac{\text{hr}}{\text{year}}
\times
0.2172\ \frac{\$}{\text{kWh}}
=
\boxed{132.18\ \frac{\$}{\text{year}}}
$$

As you can see this is super expensive but no where near as expensive as running the compute server as an always on server. In my opinion, this is a small price to pay for local, private compute, where I am in control of every piece of software on my personal server. This keeps my data private and gives me the opportunity to learn more math, coding and engineering related skills. 



## Build

### Early stages

![[media/serverfloor4.jpg|450]] ![[media/serverfloor3.jpg|450]] ![[media/serverfloor2.jpg|450]]
*Above images show different views of my workspace after initially putting together the compute portion of my server aswell as OS install*

### Current issues and Progress

Currently, my server is inside an open pc workbench, which was picked due to budget constraints. However, I am currently in the process of building a 2 part enclosure for this server. 

Part 1 is mostly detailed in the schematic below and shows dimensions for a case covering to be placed over the outside of the open pc workbench, but is yet to be digitized. Part 2 involves aluminum 2020 Extrusion T-Slots, which encase the full server rack, including the laptop. 
![[media/Part 1 Schematic.jpg|450]]*Schematics for part 1*

![[media/aluminum 2020 Extrusion T-Slots.png|450]] *aluminum 2020 Extrusion T-Slots*


# 3d Models

I will have to design several brackets and an ssd/drive bay enclosure for this project. I have only started on the drive bay. 

Modeling the drive bay on a commerical design, I have currently drawn up schematics with dimensions on paper. I have also already created a functional print-in-place model for the closing hinge for which i have used my 3d printer to print out and test. 

![[media/ssdbayref.png|500]]
![[media/ssdbayenclosure.jpg|500]]
![[media/hingewireframe.png|500]]
![[media/hinge.png|500]]
![[media/hingeschematics.jpg|500]]

Sources: 
1. NVIDIA, "GeForce RTX 3090 Specifications." https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3090-3090ti/
2. AMD, "AMD Ryzen 7 5700X Specifications." https://www.amd.com/en/products/processors/desktops/ryzen/5000-series/amd-ryzen-7-5700x.html
3. U.S. Energy Information Administration, "Average Price of Electricity to Ultimate Customers by End-Use Sector." https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_a
