#!/bin/bash

username=
allocation=hindcastra

domain=$1

dset="maximum_energy_direction"
squeue -u ${username} -t R,PD -n wave_${domain}-${dset} | grep ${username} || sbatch -A ${allocation} -J wave_${domain}-${dset} --export=domain="${domain}",dset="${dset}" run_wave_means.sbatch
