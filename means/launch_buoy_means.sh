#!/bin/bash

username=
allocation=hindcastra

declare -a DSETS=("significant_wave_height" "peak_period", "energy_period"
 "omni-directional_wave_power" "spectral_width" "maximum_energy_direction"
 "mean_zero_crossing_period")

domain=$1

for dset in "${DSETS[@]}"
do
    squeue -u ${username} -t R,PD -n buoy_${domain}-${dset} | grep ${username} || sbatch -A ${allocation} -J buoy_${domain}-${dset} --export=domain="${domain}",dset="${dset}" run_buoy_means.sbatch
done
