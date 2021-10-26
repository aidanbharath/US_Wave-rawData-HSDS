#!/bin/bash

username=
allocation=hindcastra

for domain in Alaska
do
    for year in {1979..2010}
    do
        squeue -u ${username} -t R,PD -n clean-wave_${domain}-${year} | grep ${username} || sbatch -A ${allocation} -J clean-wave_${domain}-${year} --export=domain="${domain}",year="${year}" run_clean_wave.sbatch
    done
done