#!/bin/bash

# get a list of files and sizes for each dataset
# could do this as a single big JSON file
# but it will be easier to work with the individual grpups of files
# already broken out

for split in 01 02 04 08 16 32
do
    for band in 025 040 090 150 230 280
    do
	globus ls -lrF json  38f01147-f09e-483d-a552-3866669a846d:/datareleases/dc0/mission/chlat/split$split/$band/ > dc0-chlat-split$split-$band.json
    done
done
