#!/bin/bash

# get a list of files and sizes for each dataset
# could do this as a single big JSON file
# but it will be easier to work with the individual grpups of files
# already broken out

NERSC_CMB_ENDPOINT='53b2a147-ae9d-4bbf-9d18-3b46d133d4bb'

for dset in ame_a1    dust_d9                                       radio_rg1 ame_a2    freefree_f1                                   radio_rg2 cib_cib1  galactic_foregrounds_d1s1                     radio_rg3 cmb_c3    galactic_foregrounds_highcomplexity           synchrotron_s1 cmb_c4    galactic_foregrounds_highcomplexity_websky    synchrotron_s4 co_co1    galactic_foregrounds_lowcomplexity            synchrotron_s5 co_co3    galactic_foregrounds_lowcomplexity_websky     synchrotron_s7 dust_d1   galactic_foregrounds_mediumcomplexity         tsz_tsz1 dust_d10  galactic_foregrounds_mediumcomplexity_websky dust_d12  ksz_ksz1
do
    globus ls -lrF json  $NERSC_CMB_ENDPOINT:/panexp_v1_bk18/$dset/ > panexv1-bk18-$dset.json
done
