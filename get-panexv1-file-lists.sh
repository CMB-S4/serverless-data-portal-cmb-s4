#!/bin/bash

# get a list of files and sizes for each dataset
# could do this as a single big JSON file
# but it will be easier to work with the individual grpups of files
# already broken out

for dset in combined_cmb_lensing_signal \
		combined_cmb_unlensed_dipole \
		combined_foregrounds_highcomplexity \
		combined_foregrounds_lowcomplexity \
		combined_foregrounds_mediumcomplexity
do
    globus ls -lrF json  38f01147-f09e-483d-a552-3866669a846d:/datareleases/panexv1/$dset/ > panexv1-$dset.json
done
