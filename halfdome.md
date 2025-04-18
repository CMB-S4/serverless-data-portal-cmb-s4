---
title: "Half Dome"
author: ""
description: ""
date_created: "2025-03-11"
---

[Back to catalog](./#data-releases)

# Data Release: Half Dome

## Description

The HalfDome simulations are correlated full sky N-body simulations with 6144^3 particles in 
a big box of side-length 3.75 Gpc/h for final resolution. Our data products include halo 
snapshots for 9 redshifts and continuous lightcone outputs (including both downsampled 
particle and halo, mass sheet and velocity sheet) between redshift z=0-4.

The HalfDome simulations are designed to accomplish three goals. First, the simulations are 
tailored to cross-correlations and joint analysis of stage IV surveys. Our choices of 
resolution, sky coverage, observables, and number of simulations are made to balance the 
different requirements of multiple large-scale structure and CMB surveys, within the current 
computational limitations. Second, to allow continuous future upgrades, the simulation 
pipleline is designed with distinct modules, making it possible to quickly and flexibly 
adopt future advancements in observations, numerical methods, and theories. Finally, we take
 an emperical route to incorporate realistic observations, instead of assuming first 
 principles in galaxy formation which remain largely uncertain at present. As a result, our 
 astrophysical parameters can be informative for the study of e.g. baryonic feedback, 
 stellar formation, and black hole accretion.

For more details see the [The HalfDome Multi-Survey Cosmological Simulations: N-body Simulations
 paper](https://arxiv.org/abs/2407.17462) and the [Official Halfdome simulations website](https://halfdomesims.github.io/).
 
## Data Access

The Half-Dome simulation results are publicly available. Individual
files may be downloaded using the links on the dataset pages with no need of logging in or using Globus. You can
also access the data through the Globus web interface: [![Download via Globus](images/globus-logo.png)](https://app.globus.org/file-manager?origin_id=38f01147-f09e-483d-a552-3866669a846d&origin_path=%2Fdatareleases%2Fpanexv1%2F)

## Datasets

Browse the datasets to view the list of files available and download them individually through your browser.

The data portal only hosts the Y maps, halos and lensing products, for Nbody raw outputs access via Globus.

|             Link              |  Dataset  | Number of Files | Total Size |
| ----------------------------- | --------- | --------------- | ---------- |
| [Link](halfdome-cmb.html)     | `Y maps`  | `11`            | 76.5 GiB   |
| [Link](halfdome-halos.html)   | `halos`   | `10`            | 154.9 GiB  |
| [Link](halfdome-lensing.html) | `lensing` | `49`            | 150.0 GiB  |
