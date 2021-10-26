#!/bin/bash

username=
allocation=hindcastra

declare -a DSETS=("significant_wave_height" "peak_period" "energy_period" "omni-directional_wave_power" "spectral_width" "maximum_energy_direction" "directionality_coefficient" "mean_zero-crossing_period" "mean_absolute_period")

domain=$1

for dset in "${DSETS[@]}"
do
    squeue -u ${username} -t R,PD -n wave_${domain}-${dset} | grep ${username} || sbatch -A ${allocation} -J wave_${domain}-${dset} --export=domain="${domain}",dset="${dset}" run_wave_means.sbatch
done
