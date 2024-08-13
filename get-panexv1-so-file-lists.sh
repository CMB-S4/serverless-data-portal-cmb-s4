#!/bin/bash

# get a list of files and sizes for each dataset
# could do this as a single big JSON file
# but it will be easier to work with the individual grpups of files
# already broken out

NERSC_CMB_ENDPOINT='53b2a147-ae9d-4bbf-9d18-3b46d133d4bb'

for dset in cmb_unlensed galactic_foregrounds_highcomplexity galactic_foregrounds_mediumcomplexity cmb        extragalactic galactic_foregrounds_lowcomplexity
do
    globus ls -lrF json  $NERSC_CMB_ENDPOINT:/mbs-s0012-20230321/$dset/ > panexv1-so-$dset.json
done
