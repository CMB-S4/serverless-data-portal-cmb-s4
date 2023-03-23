#!/usr/bin/env python

# Get a listings of the files in each dataset
# see get-dc0-file-lists.sh

import json
from pytablewriter import MarkdownTableWriter

# from https://stackoverflow.com/questions/1094841/get-human-readable-version-of-file-size
def sizeof_fmt(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f} {unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f} Yi{suffix}"


def write_dataset(something, n_files, data_size, file_table_rows):
    dset_table_header = ["File Name", "Datatype", "Size"]
    writer = MarkdownTableWriter(
        headers=dset_table_header,
        value_matrix=file_table_rows,
        margin=1
        )

    
    dset_text = f"""---
title: "Planck PR4 {something.upper()}"
author: "CMB-S4 Collaboration"
description: "Planck Public Release 4 {something.upper()}"
date_created: "2023-03-22"
seo:
  type: Dataset
---

[Back to release](./planck_pr4.html#datasets)

# Dataset: Planck PR4 {something.upper()}

This dataset is publicly available via Globus Transfer or HTTPS. [Click here](https://app.globus.org/file-manager?origin_id=38f01147-f09e-483d-a552-3866669a846d&origin_path=%2Fpublic%2Fplanck%2Fplanck_pr4%2F{something}%2F) to view the files in the Globus web app.

Download the [file manifest](https://g-456d30.0ed28.75bc.data.globus.org/public/planck/planck_pr4/{something}/manifest.json) for the exact file sizes and checksums.

## Files

- Number of files: {n_files}
- Total size: {data_size}
- [JSON format file manifest](https://g-456d30.0ed28.75bc.data.globus.org/public/planck/planck_pr4/{something}/manifest.json)

"""
    
    with open(f'planck_pr4-{something}.md', 'w') as f:
        f.write(dset_text)
        f.write(writer.dumps())

things = ["fullsky", "half_ring", "lowres", "quickpol", "single"]

# dc0-chlat-split$split-$band.json

# Rows for data release page
# | [Link](dc0-chlat-split01-025.html) | CHLAT     | `01`  | `025`                | `2`             | 3.8 GiB    |

pr4_dsets_table_header = ["Link", "Category", "Number of Files", "Total Size"]
pr4_dsets_table_data = []

for something in things:
    dset_table_data = []
    # load file list
    with open(f'pr4-{something}.json') as f:
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
            flink = f'[`{fname}`](https://g-456d30.0ed28.75bc.data.globus.org/public/planck/planck_pr4/{something}/{fname})'
            dset_table_data.append([flink, fsize])
    dset_size = sizeof_fmt(total_bytes)
    write_dataset(something, n_files, dset_size, dset_table_data)
    dset_url = f'[Link](plank_pr4-{something}.html)'
    pr4_dsets_table_data.append([dset_url, f'{something.upper()}', f'`{n_files}`', dset_size])



        
writer = MarkdownTableWriter(
    headers=pr4_dsets_table_header,
    value_matrix=pr4_dsets_table_data,
    margin=1
    )

with open('pr4-dset-table.md', 'w') as f:
    f.write(writer.dumps())

with open('pr4-sidebar.yml', 'w') as f:
    f.write('  - title: Planck Public Release 4)\n')
    f.write('    output: web\n')
    f.write('    folderitems:\n')
    f.write('    - title: Planck PR4\n')
    f.write('      url: "planck_pr4.html"\n')
    f.write('      output: web\n')
    for something in things:
        f.write(f'    - title: Planck PR4 {something.upper()}\n')
        f.write(f'      url: "planck_pr4-{something}.html"\n')
        f.write(f'      output: web\n')
