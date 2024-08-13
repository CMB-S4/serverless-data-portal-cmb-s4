#!/bin/bash

# get a list of files and sizes for each dataset
# could do this as a single big JSON file
# but it will be easier to work with the individual grpups of files
# already broken out

NERSC_CMB_ENDPOINT='53b2a147-ae9d-4bbf-9d18-3b46d133d4bb'

for ref in equatorial galactic
do
    for dset in cmb_c3 combined_cmb_lensing_signal combined_foregrounds_mediumcomplexity dust_d9 synchrotron_s4 ame_a1 cmb_c4 combined_cmb_unlensed_dipole dipole freefree_f1 synchrotron_s5 ame_a2 co_co1 combined_foregrounds_highcomplexity dust_d10 ksz_ksz1 synchrotron_s7 cib_cib1 co_co3 combined_foregrounds_lowcomplexity dust_d12 radio_rg1 tsz_tsz1
    do
        globus ls -lrF json  $NERSC_CMB_ENDPOINT:/panexp_v1_litebird/$ref/$dset/ > panexv1-litebird-$ref-$dset.json
    done
done
