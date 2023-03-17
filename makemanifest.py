#!/usr/bin/env python

# looks for files named 'manifest.txt' and 'file-list.json' in cwd
# merges into manifest.json based on remote file manifest format
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

# globus ls command
# globus ls -l --format json 38f01147-f09e-483d-a552-3866669a846d:datareleases/npipe6v20/fullsky/ > file-list.json

# checksum command
# sha512sum *.fits > manifest.txt

import os
import sys
import json
import glob
import hashlib

baseurl = sys.argv[1]
# baseurl = 'https://g-456d30.0ed28.75bc.data.globus.org/datareleases/npipe6v20/fullsky/'

# URL that filename will be appended to
# https://g-456d30.0ed28.75bc.data.globus.org/datareleases/npipe6v20/fullsky/

BUFFER = 4*1073741824

manifest_dict = {}
l = glob.glob("**", recursive=True)
try:
    l.remove('manifest.json')
except:
    pass
for i in l:
    if not os.path.isdir(i):
        sha512 = hashlib.sha512()
        with open(i, "rb") as f:
            while True:
                data = f.read(BUFFER)
                if not data:
                    break
                sha512.update(data)
        length = os.stat(i).st_size
        manifest_dict[i] = {'sha512': sha512.hexdigest(),
                            'filename': i,
                            'url': baseurl + i,
                            'length': length}

with open('manifest.json', 'w') as f:
    json.dump(list(manifest_dict.values()), f, indent=4)
