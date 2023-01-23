---
title: "CMB-S4 Data Repository POC"
author: "CMB-S4 Collaboration"
description: "Proof-of-concept data repository for the CMB-S4 Collaboration"
date_created: "2023-01-22"
---

[Browse the repository](#releases)

# CMB-S4 Data Repository POC

This is a proof-of-concept of how to host dataset files in Globus collections while
providing a publicly available site for data discovery. The site is
hosted using [GitHub Pages](https://pages.github.com), a free service
that can deploy sites written in Markdown. Because the Globus
collection hosting the datasets provides HTTPS access, files from the
collection can be downloaded via browser or copied using Globus Transfer.

## Data Organization

This site represents the catalog, with metadata about the catalog
itself and the datasets in the repository. Data is grouped hierarchically:
- Releases
- Datasets
- Files

## Datasets

Datasets are contained within a folder with one or more files and may
have subfolders. These datasets are grouped by releases.

[Jekyll SEO Tag](https://jekyll.github.io/jekyll-seo-tag/) provides
Schema.org JSON-LD 

```
---
title: "(Mock) BOUNDEDNESS285G"
author: "Rick Wagner"
description: "A few random images as a dataset"
date_created: "2022-08-30T03:17:24.767050"
seo:
  type: Dataset
---
```

- Manifest
- download links
- other metadata

## Data Access

The catalog is completely public while the datasets are grouped into three levels of access:

- [Public](#public-access)
- [CMB-S4 Users (POC)](#cmb-s4-users-poc): Registration required
- [CMB-S4 Collaborators (POC)](#cmb-s4-collaborators-poc):  Moderated access, approval required

Data access is controlled by the per-folder permissions on the [CMB S4
Data Portal POC Globus
Collection](https://app.globus.org/file-manager/collections/38f01147-f09e-483d-a552-3866669a846d/sharing). ([Globus
documentation on how to manage permissions.](https://docs.globus.org/how-to/share-files/))

**Note:** Globus Groups can also be used to define groups of data
stewards and administrators.

### Public Access

Public is completely public, including anonymous access via HTTPS. 

### CMB-S4 Users (POC)

**Note:** This Group is currently set to approval required.

Any logged in Globus user may join the [CMB-S4 Users (POC)](https://app.globus.org/groups/f6c4ab39-9aa9-11ed-bd74-ff3b77a8cdd3/about)
Globus Group, provided they accept the terms & conditions. This does
not require  any actions by repository personnel. This is the “just sign
up” model where joining the Group provides a list of registered users
to the Group adminstrators.

### CMB-S4 Collaborators (POC)

Users may request to join the the [CMB-S4 Collaborators
(POC)](https://app.globus.org/groups/e3a53329-9aaa-11ed-b37d-b7fded1d3618/about)
Globus Group. Membership in the Group must be approved by an
adminstrator. This is the “request access” model.

To support datasets with different access requirements, datasets could
be gather into folders with access tied to various Globus Groups. This
also allows different projects to curate access to their
datasets, where PIs or their delegates can be assigned as Group
managers. Then they receive and decide on access requests.

## Releases

- [TOAST NPIPE 6v20](releases/npipe6v20/)

## Prior Art

An inspiration for this concept is the [X-ray Tomography Data
Bank](https://tomobank.readthedocs.io/). TomoBank uses a Globus
collection at Argonne to store files and publishes descriptions of its
datasets on [ReadTheDocs](https://readthedocs.org). Because the
dataset metadata is on Github in the [TomoBank
repo](https://github.com/tomography/tomobank), users can submit new
datasets through pull requests.
