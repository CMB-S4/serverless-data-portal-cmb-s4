---
title: "CMB-S4 Data Challenge 0"
author: "CMB-S4 Collaboration"
description: "CMB-S4 Data Challenge 0 (DC-0)"
date_created: "2023-03-16"
---

# Data Release: Data Challenge 0 (DC-0)

## Description

CMB-S4 Data Challenges involve the simulation, reduction, and analysis of a mock dataset corresponding to the current point design of the instruments and their observations and is used:

* to validate that the point design meets all of the project’s measurement and science requirements
* to verify that the project pipelines run sufficiently fast on that generation’s computational architecture(s), and scale sufficiently well to the CMB-S4 data volume.

DC-0 is the first execution of a Data Challenge run, it has been completed only for Large Aperture Telescopes located in Chile (`CHLAT`), the rest of the channels are still being worked on.

## Data Access

Data access is restricted to members of the CMB-S4 Collaboration via a Globus Group.

See the [homepage of the data portal](index.md) for details on how to access the data.


## Data Products & Organization

TODO: Pull relevant information from the Data Schema reference document.

- Describe both file organization and the contents of the files.
- This will be reusable text later and could be split out to separate pages.
- Include links to tools used by the collaboration.

## Datasets & Files

Files are grouped into datasets by telescope, time split, and frequency band. Each dataset is contained within a single folder and may contain subfolders. The top-level dataset folder contains a JSON file (`manifest.json`) using the BDBag [remote file manifest
format](https://github.com/fair-research/bdbag/blob/master/doc/config.md#remote-file-manifest) with the checksum, size, and HTTPS URL of each file.

The dataset pages provide a link to the dataset's folder in the Globus web app and links to the the invidual files for immediate download.


|                Link                | Telescope | Split | Frequency Band (GHz) | Number of Files | Total Size |
| ---------------------------------- | --------- | ----- | -------------------- | --------------- | ---------- |
| [Link](dc0-chlat-split01-025.html) | CHLAT     | `01`  | `025`                | `2`             | 3.8 GiB    |
| [Link](dc0-chlat-split01-040.html) | CHLAT     | `01`  | `040`                | `2`             | 3.8 GiB    |
| [Link](dc0-chlat-split01-090.html) | CHLAT     | `01`  | `090`                | `2`             | 3.8 GiB    |
| [Link](dc0-chlat-split01-150.html) | CHLAT     | `01`  | `150`                | `2`             | 3.8 GiB    |
| [Link](dc0-chlat-split01-230.html) | CHLAT     | `01`  | `230`                | `2`             | 3.8 GiB    |
| [Link](dc0-chlat-split01-280.html) | CHLAT     | `01`  | `280`                | `2`             | 3.8 GiB    |
| [Link](dc0-chlat-split02-025.html) | CHLAT     | `02`  | `025`                | `4`             | 7.5 GiB    |
| [Link](dc0-chlat-split02-040.html) | CHLAT     | `02`  | `040`                | `4`             | 7.5 GiB    |
| [Link](dc0-chlat-split02-090.html) | CHLAT     | `02`  | `090`                | `4`             | 7.5 GiB    |
| [Link](dc0-chlat-split02-150.html) | CHLAT     | `02`  | `150`                | `4`             | 7.5 GiB    |
| [Link](dc0-chlat-split02-230.html) | CHLAT     | `02`  | `230`                | `4`             | 7.5 GiB    |
| [Link](dc0-chlat-split02-280.html) | CHLAT     | `02`  | `280`                | `4`             | 7.5 GiB    |
| [Link](dc0-chlat-split04-025.html) | CHLAT     | `04`  | `025`                | `8`             | 15.0 GiB   |
| [Link](dc0-chlat-split04-040.html) | CHLAT     | `04`  | `040`                | `8`             | 15.0 GiB   |
| [Link](dc0-chlat-split04-090.html) | CHLAT     | `04`  | `090`                | `8`             | 15.0 GiB   |
| [Link](dc0-chlat-split04-150.html) | CHLAT     | `04`  | `150`                | `8`             | 15.0 GiB   |
| [Link](dc0-chlat-split04-230.html) | CHLAT     | `04`  | `230`                | `8`             | 15.0 GiB   |
| [Link](dc0-chlat-split04-280.html) | CHLAT     | `04`  | `280`                | `8`             | 15.0 GiB   |
| [Link](dc0-chlat-split08-025.html) | CHLAT     | `08`  | `025`                | `16`            | 30.0 GiB   |
| [Link](dc0-chlat-split08-040.html) | CHLAT     | `08`  | `040`                | `16`            | 30.0 GiB   |
| [Link](dc0-chlat-split08-090.html) | CHLAT     | `08`  | `090`                | `16`            | 30.0 GiB   |
| [Link](dc0-chlat-split08-150.html) | CHLAT     | `08`  | `150`                | `16`            | 30.0 GiB   |
| [Link](dc0-chlat-split08-230.html) | CHLAT     | `08`  | `230`                | `16`            | 30.0 GiB   |
| [Link](dc0-chlat-split08-280.html) | CHLAT     | `08`  | `280`                | `16`            | 30.0 GiB   |
| [Link](dc0-chlat-split16-025.html) | CHLAT     | `16`  | `025`                | `32`            | 60.0 GiB   |
| [Link](dc0-chlat-split16-040.html) | CHLAT     | `16`  | `040`                | `32`            | 60.0 GiB   |
| [Link](dc0-chlat-split16-090.html) | CHLAT     | `16`  | `090`                | `32`            | 60.0 GiB   |
| [Link](dc0-chlat-split16-150.html) | CHLAT     | `16`  | `150`                | `32`            | 60.0 GiB   |
| [Link](dc0-chlat-split16-230.html) | CHLAT     | `16`  | `230`                | `32`            | 60.0 GiB   |
| [Link](dc0-chlat-split16-280.html) | CHLAT     | `16`  | `280`                | `32`            | 60.0 GiB   |
| [Link](dc0-chlat-split32-025.html) | CHLAT     | `32`  | `025`                | `64`            | 120.0 GiB  |
| [Link](dc0-chlat-split32-040.html) | CHLAT     | `32`  | `040`                | `64`            | 120.0 GiB  |
| [Link](dc0-chlat-split32-090.html) | CHLAT     | `32`  | `090`                | `64`            | 120.0 GiB  |
| [Link](dc0-chlat-split32-150.html) | CHLAT     | `32`  | `150`                | `64`            | 120.0 GiB  |
| [Link](dc0-chlat-split32-230.html) | CHLAT     | `32`  | `230`                | `64`            | 120.0 GiB  |
| [Link](dc0-chlat-split32-280.html) | CHLAT     | `32`  | `280`                | `64`            | 120.0 GiB  |
