# Datasets

## Files & Manifest

As a minimum, datasets are contained within a folder with one or more files and may
have subfolders. Along with the files making up the dataset, dataset folders contain a JSON file (`manifest.json`) using the BDBag [remote file manifest
format](https://github.com/fair-research/bdbag/blob/master/doc/config.md#remote-file-manifest). 

The files making up the datasets and their manifests are stored in a Globus Guest Collection (CMB S4 Data Portal POC, UUID `38f01147-f09e-483d-a552-3866669a846d`). The datasets are currently grouped under a `/datareleases/` folder, with a single `npipe6v20` data release.

The manifest is a simple list of:

- file paths relative to the dataset folder
- file size in bytes
- a URL for the file
- a checksum for the file

This manifest can be used to download data, verify file integrity, and to generate the table of files on the dataset's GitHub Markdown page.

As an example, there is a simple [`datasetA`](https://app.globus.org/file-manager?origin_id=38f01147-f09e-483d-a552-3866669a846d&origin_path=%2Fdatareleases%2Fnpipe6v20%2FdatasetA%2F) with two files in the [TOAST NIPE6v20](https://app.globus.org/file-manager?origin_id=38f01147-f09e-483d-a552-3866669a846d&origin_path=%2Fdatareleases%2Fnpipe6v20%2F) release: 

```
datasetA/
  manifest.json
  file1.dat
  folder/
    fileX.txt
```

### Checksums

Globus uses checksums to verify file integrity after a transfer or as part of a replication task. While checksum can be provided to the Globus Transfer API, it does not yet return them. For this POC I transferred the files to a local system and generated the checksums separately using a SHA512 hash. These checksums are in some of the folders with the name `manifest.txt`.

```
# On macOS 12
$ shasum -a 512 file1.dat 
27c930d7d3323700a82c47b5a2f783381e1a0cc0250f49c947e40aa4835eb440383590cf2f157c4ac441b8673cadaf58c332b66a887029f0e4a5b978027cbc93  file1.dat
```

### URLs

For the CMB-S4 Data Repository POC, the datasets are being stored in a Globus Guest Collection with a base URL of

```
https://g-456d30.0ed28.75bc.data.globus.org/
```

These URLs can only be used to download files, not for listing files. The base URL for the folder with the TOAST NPIPE 6v20 data release is:

```
https://g-456d30.0ed28.75bc.data.globus.org/datareleases/npipe6v20/
```

The example dataset is under this folder, so the URL to `file1.dat` is:

```
https://g-456d30.0ed28.75bc.data.globus.org/datareleases/npipe6v20/datasetA/file1.dat
```

Access to the file via HTTPS uses the permissions as doing a transfer. Users will be prompted to authenticate if they use the link in their browser. From the command line, tools like `wget` work easily on public files. Accessing restricted files is also doable, but requires retrieving an OAuth access token. This could be used to create download scripts for users who can't run Globus Connect. However, I would recommend writing a bit of documentation to help get users with Globus Connect and Transfer before promoting just HTTPS for large datasets. (Large is either a lot of bytes or a lot of files.)

The dataset folders can also be linked to in the Globus web app. The link for the [data release folder](https://app.globus.org/file-manager?origin_id=38f01147-f09e-483d-a552-3866669a846d&origin_path=%2Fdatareleases%2Fnpipe6v20%2F) containing all of the datasets is:

```
https://app.globus.org/file-manager?origin_id=38f01147-f09e-483d-a552-3866669a846d&origin_path=%2Fdatareleases%2Fnpipe6v20%2F
```

The web app links can be in included in the Markdown pages so that users can browse the files in individual datasets. Here's the link for `datasetA`:

```
https://app.globus.org/file-manager?origin_id=38f01147-f09e-483d-a552-3866669a846d&origin_path=%2Fdatareleases%2Fnpipe6v20%2FdatasetA%2F
```

### Manifests

The [`manifest.json`](https://g-456d30.0ed28.75bc.data.globus.org/datareleases/npipe6v20/datasetA/manifest.json) for `datasetA` is

```
[
    {
        "url":"https://g-456d30.0ed28.75bc.data.globus.org/datareleases/npipe6v20/datasetA/file1.dat",
        "length": 192514895,
        "filename": "file1.dat",
        "sha512": "27c930d7d3323700a82c47b5a2f783381e1a0cc0250f49c947e40aa4835eb440383590cf2f157c4ac441b8673cadaf58c332b66a887029f0e4a5b978027cbc93"
    },
    {
        "url":"https://g-456d30.0ed28.75bc.data.globus.org/datareleases/npipe6v20/datasetA/folder/fileX.txt",
        "length": 2891,
        "filename": "folder/fileX.txt",
        "sha512": "d9dd7f7851f50e53b5c7bb13fbcf2ab2396334ddadcd6c9c73386b12e037b384da07ac85bf02637b6d3cf0614d2dd771a549cef725df8f413338465803aac061"
    }
]
```

To create the manifests for the [`fullsky`](https://cmb-s4.github.io/serverless-data-portal-cmb-s4/releases/npipe6v20/fullsky.html) ([manifest](https://g-456d30.0ed28.75bc.data.globus.org/datareleases/npipe6v20/fullsky/manifest.json)) and [`lowres`](https://cmb-s4.github.io/serverless-data-portal-cmb-s4/releases/npipe6v20/lowres.html) ([manifest](https://g-456d30.0ed28.75bc.data.globus.org/datareleases/npipe6v20/fullsky/manifest.json)) datasets, I merged the checksums with the output of the [Globus CLI](https://docs.globus.org/cli/) `globus ls` command in the [`makemanifest.py`](makemanifest.py) script. 

```
globus ls -lr --format json 38f01147-f09e-483d-a552-3866669a846d:datareleases/npipe6v20/datasetA/ > file-list.json
```

Once I had the `manifest.json` for a dataset, I transferred it to the dataset's folder in the repository.


## Dataset Pages

Descriptions of the datasets are in Markdown files in GitHub:

- [`releases/npipe6v20/fullsky.md`](https://github.com/rpwagner/serverless-data-portal-cmb-s4/blob/main/releases/npipe6v20/fullsky.md)
- [`releases/npipe6v20/lowres.md`](https://github.com/rpwagner/serverless-data-portal-cmb-s4/blob/main/releases/npipe6v20/lowres.md)
- [`releases/npipe6v20/datasetA.md`](https://github.com/rpwagner/serverless-data-portal-cmb-s4/blob/main/releases/npipe6v20/datasetA.md)

There is also an index page ([`releases/npipe6v20/index.md`](https://github.com/rpwagner/serverless-data-portal-cmb-s4/blob/main/releases/npipe6v20/index.md)) for the data release listing the datasets.

The pages were mostly created by hand to get started--see the suggestion at the bottom of this page. The table of files at the bottom of the dataset pages were created using the [`makefiletable.py`](makefiletable.py) script. That script looks for a `manifest.json` file in the current working directory and creates a `file-table.md` snippet to add to the page.

### Page Structure

The pages consist of

- a YAML header
- name
- description & metadata
- access level or requirements
- link to manifest
- table of files

Right now, the descriptive text is minimal. See the comments below about metadata for how to add more attributes that can be reused as part of data publication. More project-specific metadata can also be added. There are JavaScript libraries that can build search pages based on this metadata and page content in various ways.

[Jekyll SEO Tag](https://jekyll.github.io/jekyll-seo-tag/) provides
Schema.org JSON-LD in the HTML headers. This is built from the YAML in
the Markdown file headers which labels the pages as describing datasets.

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

### Example Page for Dataset A

```
---
title: "TOAST NPIPE 6v20 Dataset A"
author: "CMB-S4 Collaboration"
description: "Example dataset"
date_created: "2023-01-24"
seo:
  type: Dataset
---

[Back to release](./#datasets)

# Dataset: Dataset A

## Description

Example dataset

## Data Access

Access to this dataset requires approval. Requst to join the Globus Group [CMB-S4 Collaborators (POC)](https://app.globus.org/groups/e3a53329-9aaa-11ed-b37d-b7fded1d3618/about) for access.

[Request Access](https://app.globus.org/groups/e3a53329-9aaa-11ed-b37d-b7fded1d3618/join)

This dataset is available via Globus Transfer or HTTPS. [Click here](https://app.globus.org/file-manager?origin_id=38f01147-f09e-483d-a552-3866669a846d&origin_path=%2Fdatareleases%2Fnpipe6v20%2FdatasetA%2F) to view the files in the Globus web app.

## Files

- Number of files: 2
- Total size: 183.6 MiB
- [JSON format file manifest](https://g-456d30.0ed28.75bc.data.globus.org/datareleases/npipe6v20/datasetA/manifest.json)

|                                                    File Name                                                     |   Size    |     Hash     |
| ---------------------------------------------------------------------------------------------------------------- | --------- | ------------ |
| [file1.dat](https://g-456d30.0ed28.75bc.data.globus.org/datareleases/npipe6v20/datasetA/file1.dat)               | 183.6 MiB | `..27c930d7` |
| [folder/fileX.txt](https://g-456d30.0ed28.75bc.data.globus.org/datareleases/npipe6v20/datasetA/folder/fileX.txt) | 2.8 KiB   | `..d9dd7f78` |
```


## Metadata

In addition to the manifest file, I would suggest creating a `metadata.json` file for each directory.

Base attributes 

- identifier (just a unique internal identifier for now, like `npipe6v20/datasetA`)
- title or name of the dataset
- creator or author
- publisher
- publication date or year
- version

Suggested attributes

- description
- subject or keywords
- rights or license (e.g., Creative Commons)

https://github.com/ESIPFed/science-on-schema.org/blob/master/guides/Dataset.md

https://support.datacite.org/docs/how-can-i-map-different-metadata-formats-to-the-datacite-xml

### Suggestion

- Draft a few dataset pages and JSON files by hand
- develop basic Python tools to generate the JSON manifest and metadata files
- add some methods or scripts to serialize the datasets to Markdown
