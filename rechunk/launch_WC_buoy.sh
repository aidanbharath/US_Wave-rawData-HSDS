#!/bin/bash

username=
allocation=hindcastra

for year in {1979..2010}
do
    squeue -u ${username} -t R,PD -n rechunk_buoy_${year} | grep ${username} || sbatch -A ${allocation} -J rechunk_buoy_${year} --export=year="${year}" rechunk_WC_buoy.sbatch
done