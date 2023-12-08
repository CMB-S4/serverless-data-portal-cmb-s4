#!/bin/bash

# get a list of files and sizes for each dataset
# could do this as a single big JSON file
# but it will be easier to work with the individual grpups of files
# already broken out

ENDPOINT='c9dc477a-3db5-4946-874d-a5dc7efcabcf'
DOMAIN='g-456d30.0ed28.75bc' # NERSC`

for mission in chlat splat spsat
do
    for split in 01 02 04 08 16 32
    do
        echo $mission $split
        BANDS="025 040 085 095 145 155 230 280" #spsat
        if [ "$mission" = "chlat" ]; then
            BANDS="025 040 090 150 230 280"
        fi
        if [ "$mission" = "splat" ]; then
            BANDS="020 025 040 090 150 230 280"
        fi
        for band in $BANDS
        do
        # globus ls -lrF json  38f01147-f09e-483d-a552-3866669a846d:/datareleases/dc0/mission/chlat/split$split/$band/ > dc0-chlat-split$split-$band.json
        globus ls -lrF json $ENDPOINT:/datareleases/dc0/mission/$mission/split$split/$band/ > dc0-$mission-split$split-$band.json
        done
    done
done
