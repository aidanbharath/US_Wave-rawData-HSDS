#!/bin/bash

username=
allocation=hindcastra

for year in {1979..2010}
do
    squeue -u ${username} -t R,PD -n rechunk_hawaii_wave_${year} | grep ${username} || sbatch -A ${allocation} -J rechunk_hawaii_wave_${year} --export=year="${year}" rechunk_hawaii_wave.sbatch
done