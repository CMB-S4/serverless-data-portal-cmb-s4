#!/usr/bin/env python

# creates manifest.json files in any folder that contains files in a hierarchy of folders
# based on:
# https://github.com/fair-research/bdbag/blob/master/doc/config.md#remote-file-manifest

# Example
# [
#     {
#         "url":"https://raw.githubusercontent.com/fair-research/bdbag/master/profiles/bdbag-profile.json",
#         "length":699,
#         "filename":"bdbag-profile.json",
#         "sha256":"eb42cbc9682e953a03fe83c5297093d95eec045e814517a4e891437b9b993139"
#     },
#     {
#         "url":"ark:/88120/r8059v",
#         "length": 632860,
#         "filename": "minid_v0.1_Nov_2015.pdf",
#         "sha256": "cacc1abf711425d3c554277a5989df269cefaa906d27f1aaa72205d30224ed5f"
#     }
# ]

import os
import sys
import json
import glob
import hashlib

folder = sys.argv[1]
# CMB collection at NERSC
baseurl = "https://g-0a470a.6b7bd8.0ec8.data.globus.org/"
# example NERSC
# baseurl = "https://g-9fdb0b.6b7bd8.0ec8.data.globus.org/datareleases/dc0/mission/"
# example UCSD
# baseurl = 'https://g-456d30.0ed28.75bc.data.globus.org/datareleases/npipe6v20/fullsky/'

BUFFER = 4 * 1073741824

for dirpath, dirnames, filenames in os.walk(folder):
    print(dirpath)
    manifest_dict = {}
    for filename in filenames:
        if filename not in ["manifest.json"]:
            print(filename)
            path = os.path.join(dirpath, filename)
            sha512 = hashlib.sha512()
            with open(path, "rb") as f:
                while True:
                    data = f.read(BUFFER)
                    if not data:
                        break
                    sha512.update(data)
            length = os.stat(path).st_size
            manifest_dict[path] = {
                "sha512": sha512.hexdigest(),
                "filename": os.path.basename(path),
                "url": baseurl + path,
                "length": length,
            }

    if len(filenames) > 0:
        with open(os.path.join(dirpath, "manifest.json"), "w") as f:
            json.dump(list(manifest_dict.values()), f, indent=4)
        print(dirpath)
