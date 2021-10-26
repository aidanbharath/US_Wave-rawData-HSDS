#!/bin/bash

username=
allocation=hindcastra

domain=Atlantic
dset='omni-directional_wave_power'
squeue -u ${username} -t R,PD -n wave_${domain}-${dset} | grep ${username} || sbatch -A ${allocation} -J wave_${domain}-${dset} --export=domain="${domain}",dset="${dset}" run_wave_means.sbatch

domain=West_Coast
dset='spectral_width'
squeue -u ${username} -t R,PD -n buoy_${domain}-${dset} | grep ${username} || sbatch -A ${allocation} -J buoy_${domain}-${dset} --export=domain="${domain}",dset="${dset}" run_buoy_means.sbatch

domain=West_Coast
dset='energy_period'
squeue -u ${username} -t R,PD -n buoy_${domain}-${dset} | grep ${username} || sbatch -A ${allocation} -J buoy_${domain}-${dset} --export=domain="${domain}",dset="${dset}" run_buoy_means.sbatch
