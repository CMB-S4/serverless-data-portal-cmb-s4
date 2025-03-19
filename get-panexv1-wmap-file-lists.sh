#!/bin/bash

# get a list of files and sizes for each dataset
# could do this as a single big JSON file
# but it will be easier to work with the individual grpups of files
# already broken out

NERSC_CMB_ENDPOINT='53b2a147-ae9d-4bbf-9d18-3b46d133d4bb'

for dset in  cib_cib1  co_co1   dust_d10  freefree_f1                          galactic_foregrounds_lowcomplexity     synchrotron_s1  synchrotron_s7 ame_a1  cmb_c3    co_co3   dust_d12  galactic_foregrounds_d1s1            galactic_foregrounds_mediumcomplexity  synchrotron_s4  tsz_tsz1 ame_a2  cmb_c4    dust_d1  dust_d9   galactic_foregrounds_highcomplexity  ksz_ksz1                               synchrotron_s5
do
    globus ls -lrF json  $NERSC_CMB_ENDPOINT:/panexp_v1_wmap/$dset/ > panexv1-wmap-$dset.json
done
