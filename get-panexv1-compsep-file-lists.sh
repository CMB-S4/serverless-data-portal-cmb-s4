#!/bin/bash

# get a list of files and sizes for each dataset
# could do this as a single big JSON file
# but it will be easier to work with the individual grpups of files
# already broken out

NERSC_CMB_ENDPOINT='53b2a147-ae9d-4bbf-9d18-3b46d133d4bb'

for dset in freefree_f1 ame_a1     galactic_foregrounds_d1s1 ame_a2     galactic_foregrounds_highcomplexity cib_cib1   galactic_foregrounds_lowcomplexity cmb_c3     galactic_foregrounds_mediumcomplexity cmb_c4     ksz_ksz1 co_co1     co_co3     synchrotron_s1 dust_d1    synchrotron_s4 dust_d10   synchrotron_s5 dust_d12   synchrotron_s7 dust_d9    tsz_tsz1
do
    globus ls -lrF json  $NERSC_CMB_ENDPOINT:/panexp_v1_compsep/$dset/ > panexv1-compsep-$dset.json
done
