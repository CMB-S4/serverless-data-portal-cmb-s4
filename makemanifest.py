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

import sys
import json

baseurl = sys.argv[1]
# baseurl = 'https://g-456d30.0ed28.75bc.data.globus.org/datareleases/npipe6v20/fullsky/'

# URL that filename will be appended to
# https://g-456d30.0ed28.75bc.data.globus.org/datareleases/npipe6v20/fullsky/

manifest_dict = {}

f = open('manifest.txt')
line = f.readline()
while line:
    sha512, fname = line.strip().split()
    manifest_dict[fname] = {'sha512': sha512,
                                'filename': fname,
                                'url': baseurl + fname}
    line = f.readline()
   
with open('file-list.json') as f:
    file_list = json.load(f)

file_list = file_list['DATA']

for file in file_list:
    fname = file['name']
    if fname != 'manifest.txt':
        manifest_dict[fname]['length'] = file['size']

with open('manifest.json', 'w') as f:
    json.dump(list(manifest_dict.values()), f, indent=4)
