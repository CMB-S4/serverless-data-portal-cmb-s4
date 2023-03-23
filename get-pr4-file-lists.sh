#!/bin/bash

# get a list of files and sizes for each dataset
# could do this as a single big JSON file
# but it will be easier to work with the individual grpups of files
# already broken out

for something in fullsky half_ring lowres quickpol single
do
    globus ls -lrF json  38f01147-f09e-483d-a552-3866669a846d:/public/planck/planck_pr4/$something/ > pr4-$something.json
done
