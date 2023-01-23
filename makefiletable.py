#!/usr/bin/env python

# Takes a remote file manifest JSON file and creates a Markdown table
# https://github.com/fair-research/bdbag/blob/master/doc/config.md#remote-file-manifest

import json
from pytablewriter import MarkdownTableWriter

# from https://stackoverflow.com/questions/1094841/get-human-readable-version-of-file-size
def sizeof_fmt(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f} {unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f} Yi{suffix}"

with open('manifest.json') as f:
    file_list = json.load(f)

table_header = ["File Name", "Size", "Hash"]
table_data = []

for filedata in file_list:
    fname = f"[{filedata['filename']}]({filedata['url']})"
    fsize = sizeof_fmt(filedata['length'])
    fhash = f"`..{filedata['sha512'][:8]}`"
    table_data.append([fname, fsize, fhash])
    
writer = MarkdownTableWriter(
    table_name="example_table",
    headers=table_header,
    value_matrix=table_data,
    margin=1
    )

with open('file-table.md', 'w') as f:
    f.write(writer.dumps())
