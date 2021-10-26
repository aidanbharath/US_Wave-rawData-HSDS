#!/bin/bash

username=
allocation=hindcastra

for domain in West_Coast Atlantic
do
    for year in {1979..2010}
    do
        squeue -u ${username} -t R,PD -n clean-buoy_${domain}-${year} | grep ${username} || sbatch -A ${allocation} -J clean-buoy_${domain}-${year} --export=domain="${domain}",year="${year}" run_clean_buoy.sbatch
    done
done