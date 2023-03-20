---
title: "CMB-S4 Data Repository"
author: "CMB-S4 Collaboration"
description: "Proof-of-concept data repository for the CMB-S4 Collaboration"
date_created: "2023-01-22"
---

# CMB-S4 Data Portal

The CMB-S4 Data Portal hosts the CMB-S4 data products and other datasets of interest for the Cosmic Microwave Background community.

The data hosting/transfer capability and permissions are provided by [Globus](https://globus.org), the Portal website is a discovery, navigation and documentation tool.

For technical details about the portal, see the [About page](about.md).

## Data Releases

- [Data Challenge 0 (DC0)](dc0.html) - Data download is currently restricted to CMB-S4 Collaboration members
- [Planck TOAST NPIPE 6v20](npipe6v20.html) - Public

## Data Access 

Browsing the metadata on the website is always public for any dataset.
Data access can be restricted dataset by dataset to CMB-S4 Collaboration members or to members of the CMB-S4 Data Management group.

If you are a member of the CMB-S4 Collaboration, you should have received an invite on your registered email address to join the [CMB-S4 Collaboration Globus group](https://app.globus.org/groups/49966b08-15a6-11ec-ac5b-5fee5047b788/) if you get permission denied, please [open an issue in the repository](https://github.com/CMB-S4/serverless-data-portal-cmb-s4/issues/new).

## How to download data

Data can be downloaded locally just by clicking on a link on the website, the browser will first be redirected to Globus for authentication and then the file will be downloaded locally without the need of having any Globus services running locally.

For downloading a large amount of data to a local or a remote machine machine, it is recommended to install [Globus Connect Personal](https://www.globus.org/globus-connect-personal), this also allows to download a complete hierarchy of folders with just 1 click.

In order to access the data via the Globus Web App, click on any of the links "Click here to view the files in the Globus web app".

For downloading data to a Supercomputer, checkout the documentation on how to access the Globus endpoint which is most probably already available, then use that as the destination endpoint in the [Globus web interface](https://app.globus.org/).
