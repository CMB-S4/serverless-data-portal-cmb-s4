---
title: "CMB-S4 Data Challenge 0"
author: "CMB-S4 Collaboration"
description: "CMB-S4 Data Challenge 0 (DC0)"
date_created: "2023-03-16"
---

# Data Release: Data Challenge 0 (DC0)

## Description

Data Challenge 0. 

TODO: Awesome description goes here.

## Data Access

Data access is restricted to members of the CMB-S4 Collaboration via a Globus Group. You may request to [join the CMB-S4 Collaborators Globus Group](https://app.globus.org/groups/e3a53329-9aaa-11ed-b37d-b7fded1d3618/join) and your request will be reviewed.

Data can be download over HTTPS or using [Globus Connect](https://www.globus.org/globus-connect).

## Data Products & Organization

TODO: Pull relevant information from the Data Schema reference document.

Describe both file organization and the contents of the files. This will be reusable text later and could be split out to separate pages.

## Datasets & Files

Files are grouped into datasets by telescope, time split, and frequency band. Each dataset is contained within a single folder and may contain subfolders. The top-level dataset folder contains a JSON file (`manifest.json`) using the BDBag [remote file manifest
format](https://github.com/fair-research/bdbag/blob/master/doc/config.md#remote-file-manifest) with the checksum, size, and HTTPS URL of each file.

The dataset pages provide a link to the dataset's folder in the Globus web app and links to the the invidual files for immediate download.


| Link | Telescope | Split | Frequency Band (GHz) | Number of Files | Total Size |
| ---- | ------- | ----- | ---------------------- | --------------- | ---------- |
| [Link](dc0-chlat-split01-025.html) | Chilean Large Aperture Telescope (CHLAT) | `01` | `025` | `2` | 3.8 GiB |
