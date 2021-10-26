#!/bin/bash

username=
allocation=hindcastra

domain=$1

dset="maximum_energy_direction"
squeue -u ${username} -t R,PD -n buoy_${domain}-${dset} | grep ${username} || sbatch -A ${allocation} -J buoy_${domain}-${dset} --export=domain="${domain}",dset="${dset}" run_buoy_means.sbatch
