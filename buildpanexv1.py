#!/usr/bin/env python

# Get a listings of the files in each dataset
# see get-panexv1-file-lists.sh

import json
from pytablewriter import MarkdownTableWriter

dsets = ('combined_cmb_lensing_signal',
             'combined_cmb_unlensed_dipole',
             'combined_foregrounds_highcomplexity',
             'combined_foregrounds_lowcomplexity',
             'combined_foregrounds_mediumcomplexity')
    
# from https://stackoverflow.com/questions/1094841/get-human-readable-version-of-file-size
def sizeof_fmt(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f} {unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f} Yi{suffix}"

def get_fileinfo(fname):
    fileinfo = fname.split('_')
    telescope = fileinfo[-3]
    freq = fileinfo[-2][1:]
    nside = fileinfo[-1][5:-5]
    return (telescope, freq, nside)

def write_dataset(dset, n_files, data_size, file_table_rows):
    dset_table_header = ["File Name", "Telescope", "Frequency Band (GHz)", "Nside", "Size"]
    writer = MarkdownTableWriter(
        headers=dset_table_header,
        value_matrix=file_table_rows,
        margin=1
        )

    dset_text = f"""---
title: "PanEx V1 Skies {dset}"
author: "CMB-S4 Collaboration"
description: "PanEx V1 Skies {dset}"
date_created: "2023-09-12"
seo:
  type: Dataset
---

[Back to release](./panexv1.html#datasets)

# Dataset: PanEx V1 Skies {dset}

See [data access](./panexv1.html#data-access) on the PanEx V1 page.

Access the data through the Globus web interface: [![Download via Globus](images/globus-logo.png)](https://app.globus.org/file-manager?origin_id=38f01147-f09e-483d-a552-3866669a846d&origin_path=%2Fdatareleases%2Fpanexv1%2F{dset}%2F)

Download the [file manifest](https://g-456d30.0ed28.75bc.data.globus.org/datareleases/panexv1/{dset}/manifest.json) for the exact file sizes and checksums.

## Files

- Number of files: {n_files}
- Total size: {data_size}
- [JSON format file manifest](https://g-456d30.0ed28.75bc.data.globus.org/datareleases/panexv1/{dset}/manifest.json)

"""
    
    with open(f'panexv1-{dset}.md', 'w') as f:
        f.write(dset_text)
        f.write(writer.dumps())

    
panexv1_dsets_table_header = ["Link", "Dataset", "Number of Files", "Total Size"]
panexv1_dsets_table_data = []

for dset in dsets:
    dset_table_data = []
    # load file list
    with open(f'panexv1-{dset}.json') as f:
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
                (telescope, freq, nside) = get_fileinfo(fname)
                flink = f'[`{fname}`](https://g-456d30.0ed28.75bc.data.globus.org/datareleases/panexv1/{dset}/{fname})'
                dset_table_data.append([flink, telescope, freq, nside, fsize])
        dset_size = sizeof_fmt(total_bytes)
        write_dataset(dset, n_files, dset_size, dset_table_data)
        dset_url = f'[Link](panexv1-{dset}.html)'
        panexv1_dsets_table_data.append([dset_url, f'{dset}', f'`{n_files}`', dset_size])

writer = MarkdownTableWriter(
    headers=panexv1_dsets_table_header,
    value_matrix=panexv1_dsets_table_data,
    margin=1
    )

with open('panexv1-dset-table.md', 'w') as f:
    f.write(writer.dumps())

with open('panexv1-sidebar.yml', 'w') as f:
    f.write('  - title: PanEx V1 Skies (PanExV1)\n')
    f.write('    output: web\n')
    f.write('    folderitems:\n')
    f.write('    - title: PanEx V1 Skies Release Page\n')
    f.write('      url: "panexv1.html"\n')
    f.write('      output: web\n')
    for dset in dsets:
        f.write(f'    - title: PanExV1 {dset}\n')
        f.write(f'      url: "panexv1-{dset}.html"\n')
        f.write(f'      output: web\n')
