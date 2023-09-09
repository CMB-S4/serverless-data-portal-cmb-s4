#!/usr/bin/env python

# Get a listings of the files in each dataset
# see get-dc0-file-lists.sh

import json
from pytablewriter import MarkdownTableWriter

missions = {'chlat':
                {'fullname': 'Chilean Large Aperture Telescope',
                     'splits': ["01", "02"],
                'bands': ["025", "040", "090", "150", "230", "280"]},
                'spsat':
                {'fullname': 'South Pole Small Aperture Telescope',
                     'splits': ["01", "02"],
                'bands': ["025", "040", "085", "095", "145", "155", "230", "280"]}

    }

components = {
    '0001': 'unlensed primary CMB',
    '0010': 'lensing perturbation',
    '0100': 'extragalactic+galactic+dipole',
    '1000': 'atmosphere+noise',
    '1111': 'CMB+galactic+extragalactic+atmosphere+noise'
    }

    
# from https://stackoverflow.com/questions/1094841/get-human-readable-version-of-file-size
def sizeof_fmt(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f} {unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f} Yi{suffix}"

def get_datatype(fname):
    # for _map02 files
    datatype = 'Map: filter+bin iqu map'

    if '_map02' in fname:
        component = components[fname[-9:-5]]
        datatype = f'{datatype}; {component}'
    elif '_map03' in fname:
        datatype = 'Map: tp depth'
    elif '_mat02' in fname:
        datatype = 'Matrix: white noise covariance'
    return datatype

def write_dataset(mission, split, band, n_files, data_size, file_table_rows):
    dset_table_header = ["File Name", "Datatype", "Size"]
    writer = MarkdownTableWriter(
        headers=dset_table_header,
        value_matrix=file_table_rows,
        margin=1
        )

    dset_text = f"""---
title: "CMB-S4 DC0 {mission.upper()} Split{split} {band}GHz"
author: "CMB-S4 Collaboration"
description: "CMB-S4 DC0 {mission.upper()} Split{split} {band}GHz"
date_created: "2023-09-09"
seo:
  type: Dataset
---

[Back to release](./dc0.html#datasets)

# Dataset: CMB-S4 DC0 {mission.upper()} Split{split} {band}GHz

- Telescope: {missions[mission]["fullname"]} ({mission.upper()}) 
- Split: `{split}`
- Frequency Band (GHz): `{band}`

See [data access](./dc0.html#data-access) on the DC0 page.

Access the data through the Globus web interface: [![Download via Globus](images/globus-logo.png)](https://app.globus.org/file-manager?origin_id=38f01147-f09e-483d-a552-3866669a846d&origin_path=%2Fdatareleases%2Fdc0%2Fmission%2F{mission}%2Fsplit{split}%2F{band}%2F)

Download the [file manifest](https://g-456d30.0ed28.75bc.data.globus.org/datareleases/dc0/mission/{mission}/split{split}/{band}/manifest.json) for the exact file sizes and checksums.

## Files

- Number of files: {n_files}
- Total size: {data_size}
- [JSON format file manifest](https://g-456d30.0ed28.75bc.data.globus.org/datareleases/dc0/mission/{mission}/split{split}/{band}/manifest.json)

"""
    
    with open(f'dc0-{mission}-split{split}-{band}.md', 'w') as f:
        f.write(dset_text)
        f.write(writer.dumps())

    
# dc0-chlat-split$split-$band.json

# Rows for data release page
# | [Link](dc0-chlat-split01-025.html) | CHLAT     | `01`  | `025`                | `2`             | 3.8 GiB    |

dc0_dsets_table_header = ["Link", "Telescope", "Split", "Frequency Band (GHz)", "Number of Files", "Total Size"]
dc0_dsets_table_data = []

for mission in ('chlat', 'spsat'):
    for split in missions[mission]['splits']:
        for band in missions[mission]['bands']:
            dset_table_data = []
            # load file list
            with open(f'dc0-{mission}-split{split}-{band}.json') as f:
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
                        ftype = get_datatype(fname)
                        flink = f'[`{fname}`](https://g-456d30.0ed28.75bc.data.globus.org/datareleases/dc0/mission/{mission}/split{split}/{band}/{fname})'
                        dset_table_data.append([flink, ftype, fsize])
                dset_size = sizeof_fmt(total_bytes)
                write_dataset(mission, split, band, n_files, dset_size, dset_table_data)
                dset_url = f'[Link](dc0-{mission}-split{split}-{band}.html)'
                dc0_dsets_table_data.append([dset_url, f'{mission.upper()}', f'`{split}`', f'`{band}`', f'`{n_files}`', dset_size])

writer = MarkdownTableWriter(
    headers=dc0_dsets_table_header,
    value_matrix=dc0_dsets_table_data,
    margin=1
    )

with open('dc0-dset-table.md', 'w') as f:
    f.write(writer.dumps())

with open('dc0-sidebar.yml', 'w') as f:
    f.write('  - title: CMB-S4 Data Challenge 0 (DC0)\n')
    f.write('    output: web\n')
    f.write('    folderitems:\n')
    f.write('    - title: Data Challenge 0 Release Page\n')
    f.write('      url: "dc0.html"\n')
    f.write('      output: web\n')
    for mission in ('chlat', 'spsat'):
        for split in missions[mission]['splits']:
            for band in missions[mission]['bands']:
                f.write(f'    - title: DC0 {mission.upper()} Split{split} {band}\n')
                f.write(f'      url: "dc0-{mission}-split{split}-{band}.html"\n')
                f.write(f'      output: web\n')
