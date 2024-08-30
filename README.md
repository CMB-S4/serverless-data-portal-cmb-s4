#  Serverless Data Portal prototype for CMB-S4

[![pages-build-deployment](https://github.com/CMB-S4/serverless-data-portal-cmb-s4/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/CMB-S4/serverless-data-portal-cmb-s4/actions/workflows/pages/pages-build-deployment)

Proof-of-concept for a data portal using static pages.

## NERSC Globus endpoints

The data portal supports having datasets stored on different Globus Endpoints, as long as they support HTTPS access (so that people can download data directly).
The easiest way is to host data at NERSC and activate a [Guest Collection](https://docs.nersc.gov/services/globus/#guest-collections).
At the moment we have them activated on the `cmb` and the `cmbs4` projects,
therefore any data under:

    /global/cfs/projectdirs/cmbs4/gsharing/
    /global/cfs/projectdirs/cmb/gsharing/

The collections on Globus:

* [Globus Connection named "CMB-S4 Data Portal at NERSC"](https://app.globus.org/file-manager/collections/c9dc477a-3db5-4946-874d-a5dc7efcabcf/)
* [CMB Collection](https://app.globus.org/file-manager/collections/53b2a147-ae9d-4bbf-9d18-3b46d133d4bb/overview)

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
This script is the only step in the process that **needs** to be executed where the data files are available, with writing access. So the easiest way at the moment is to login at NERSC with the `cmbs4` Collaboration account and execute the script.

### Create file metadata JSON files

The next step can be executed from any machine, no data access is necessary, we run a bash script that uses the `globus-cli` to gather information about all the files to be registered with the data portal, most notably the size.
As output we have 1 JSON file for each data file.
At the moment we have a simple bash script which builds all the filenames with nested loops and then calls `globus ls`.
Unfortunately we need to customize the script for each data release, see as an example [`get-dc0-file-lists.sh`](./get-dc0-file-lists.sh).

### Generate the pages

The last step is a Python script that loads information about the files from the JSON files and writes all the markdown files, one page for each dataset.
This script is highly customized for each dataset, see for example [`builddc0.py`](./builddc0.py).
We also need to create a homepage for the release, mostly with documentation about it, see for example [`dc0.md`](./dc0.md).
It also generates the sidebar, which we need to paste into `_data/sidebars/home_sidebar.yml` and the dataset table which we need to paste at the botttom of the homepage for the release.
