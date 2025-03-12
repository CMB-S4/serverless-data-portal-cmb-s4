#!/bin/bash

# get a list of files and sizes for each dataset
# could do this as a single big JSON file
# but it will be easier to work with the individual grpups of files
# already broken out

NERSC_CMB_ENDPOINT='53b2a147-ae9d-4bbf-9d18-3b46d133d4bb'

for dset in cmb halos lensing
do
    globus ls -lrF json  $NERSC_CMB_ENDPOINT:/halfdome/full_res/$dset/ > halfdome-$dset.json
done
