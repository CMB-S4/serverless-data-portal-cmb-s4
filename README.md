#  Serverless Data Portal prototype for CMB-S4

[![pages-build-deployment](https://github.com/CMB-S4/serverless-data-portal-cmb-s4/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/CMB-S4/serverless-data-portal-cmb-s4/actions/workflows/pages/pages-build-deployment)

Proof-of-concept for a data portal using static pages.

## NERSC Globus endpoint

The datasets shared by the data portal are in the NERSC Community file system at:

    /global/cfs/projectdirs/cmbs4/gsharing/

through a read-only [Globus Connection named "CMB-S4 Data Portal at NERSC"](https://app.globus.org/file-manager/collections/c9dc477a-3db5-4946-874d-a5dc7efcabcf/)

## How to prepare a release

### Put data under `gsharing/datareleases`

Create hard links to the `gsharing/datareleases/` folder, for example:

    cp -al /global/cfs/cdirs/cmbs4/dc/dc0 /global/cfs/cdirs/cmbs4/gsharing/datareleases/

it is the owner of the files that needs to create the hard-links.

Alternatively move the data under `gsharing` and then put a symlink at the original location that points to the new location of the folder.
The advantage of symlinks is that if we add a new file in a folder, that file is immediately available through Globus (it needs to be explicitely linked from the portal to make it available in the HTML interface). With hard links instead we need to create a new hard link for that file in the `gsharing` folder.

### Create manifests

`manifest.json` files need to be created inside each dataset (i.e. folder which contains data, instead of only containing other folders)
The file contains hash, size and url.

The URL for NERSC should be:

    https://g-9fdb0b.6b7bd8.0ec8.data.globus.org/datareleases/xxx

there `xxx` is the name of the release.

`makemanifest.py` is the Python script that executed at the root of a data release transverse the hierarchy of folders and creates a `manifest.json` file in each folder directly containing data.
