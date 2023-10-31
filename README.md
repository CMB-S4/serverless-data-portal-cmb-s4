#  Serverless Data Portal prototype for CMB-S4

[![pages-build-deployment](https://github.com/CMB-S4/serverless-data-portal-cmb-s4/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/CMB-S4/serverless-data-portal-cmb-s4/actions/workflows/pages/pages-build-deployment)

Proof-of-concept for a data portal using static pages.

## NERSC Globus endpoint

The datasets shared by the data portal are in the NERSC Community file system at:

    /global/cfs/projectdirs/cmbs4/gsharing/

through a read-only [Globus Connection named "CMB-S4 Data Portal at NERSC"](https://app.globus.org/file-manager/collections/c9dc477a-3db5-4946-874d-a5dc7efcabcf/)

## How to prepare a release

Create hard links to the `gsharing/datareleases/` folder, for example:

    cp -al /global/cfs/cdirs/cmbs4/dc/dc0 /global/cfs/cdirs/cmbs4/gsharing/datareleases/

it is the owner of the files that needs to create the hard-links.
