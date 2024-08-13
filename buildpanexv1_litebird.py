#!/usr/bin/env python

# Get a listings of the files in each dataset
# see get-panexv1-file-lists.sh

import json
from pytablewriter import MarkdownTableWriter

# NERSC CMB Globus Guest Collection
ENDPOINT = '53b2a147-ae9d-4bbf-9d18-3b46d133d4bb'
DOMAIN = 'g-0a470a.6b7bd8.0ec8'
FOLDER = 'panexp_v1_litebird'
RELEASE_NAME = 'panexv1-litebird'

dsets = 'combined_cmb_unlensed_dipole  combined_cmb_lensing_signal   combined_foregrounds_lowcomplexity combined_foregrounds_mediumcomplexity combined_foregrounds_highcomplexity ame_a1 ame_a2 cib_cib1 cmb_c3 cmb_c4 co_co1 co_co3 dipole dust_d10 dust_d12 dust_d9 freefree_f1 ksz_ksz1 radio_rg1 synchrotron_s4 synchrotron_s5 synchrotron_s7 tsz_tsz1'.split()

# from https://stackoverflow.com/questions/1094841/get-human-readable-version-of-file-size
def sizeof_fmt(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f} {unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f} Yi{suffix}"

def get_fileinfo(fname):
    fileinfo = fname.split(".")[0].split('_')
    try:
        telescope, freq = fileinfo[-2].split("-")
        freq = str(int(freq))
    except ValueError:
        telescope = "all"
        freq = "all"
    unit = fileinfo[-3]
    pixelization = "healpix"
    nside = fileinfo[-1].replace("nside", "")
    return [telescope, freq, pixelization, nside, unit]

def write_dataset(dset, n_files, data_size, file_table_rows):
    dset_table_header = ["File Name", "Telescope", "Frequency Band (GHz)", "Pixelization", "Nside", "Unit", "Size"]
    writer = MarkdownTableWriter(
        headers=dset_table_header,
        value_matrix=file_table_rows,
        margin=1
        )

    dsettext = dset.replace("_", " ")

    dset_text = f"""---
title: "Dataset: PanEx V1 Skies Simons Observatory {dsettext}"
author: "Simons Observatory Collaboration"
description: "PanEx V1 Skies SO {dset}"
date_created: "2023-03-21"
seo:
  type: Dataset
---

[Back to release](./{RELEASE_NAME}.html#datasets)
See [data access](./{RELEASE_NAME}.html#data-access) on the Data Release page.

Access the data through the Globus web interface: [![Download via Globus](images/globus-logo.png)](https://app.globus.org/file-manager?origin_id={ENDPOINT}&origin_path=%2F{FOLDER}%2F{dset}%2F)

Download the [file manifest](https://{DOMAIN}.data.globus.org/{FOLDER}/{dset}/manifest.json) for the exact file sizes and checksums.

## Files

- Number of files: {n_files}
- Total size: {data_size}
- [JSON format file manifest](https://{DOMAIN}.data.globus.org/{FOLDER}/{dset}/manifest.json)

"""

    with open(f'{RELEASE_NAME}-{ref_frame}-{dset}.md', 'w') as f:
        f.write(dset_text)
        f.write(writer.dumps())


dsets_table_header = ["Link", "Dataset", "Number of Files", "Total Size"]
dsets_table_data = []

for ref_frame in ["equatorial", "galactic"]:
    for dset in dsets:
        dset_table_data = []
        # load file list
        with open(f'{RELEASE_NAME}-{ref_frame}-{dset}.json') as f:
            file_data = json.load(f)
            file_list = file_data["DATA"]
            # loop over files, build file table info for dataset
            # remove manifest from list
            # total up bytes in dataset
            total_bytes = 0
            n_files = len(file_list) - 1
            for file_entry in file_list:
                fname = file_entry['name']
                if not fname == 'manifest.json':
                    total_bytes += file_entry['size']
                    fsize = sizeof_fmt(file_entry['size'])
                    columns = get_fileinfo(fname)
                    flink = f'[`{fname}`](https://g-456d30.0ed28.75bc.data.globus.org/{FOLDER}/{ref_frame}/{dset}/{fname})'
                    dset_table_data.append([flink]+columns+[fsize])
            dset_size = sizeof_fmt(total_bytes)
            write_dataset(dset, n_files, dset_size, dset_table_data)
            dset_url = f'[Link]({RELEASE_NAME}-{ref_frame}-{dset}.html)'
            dsets_table_data.append([dset_url, f'{dset}', f'`{n_files}`', dset_size])

    writer = MarkdownTableWriter(
        headers=dsets_table_header,
        value_matrix=dsets_table_data,
        margin=1
        )

    with open(f'{RELEASE_NAME}-{ref_frame}-dset-table.md', 'w') as f:
        f.write(writer.dumps())
