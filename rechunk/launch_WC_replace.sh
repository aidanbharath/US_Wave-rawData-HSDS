#!/bin/bash

username=
allocation=hindcastra

for year in 2002
do
    squeue -u ${username} -t R,PD -n rechunk_WC_${year} | grep ${username} || sbatch -A ${allocation} -J rechunk_WC_${year} --export=year="${year}" rechunk_WC_replace.sbatch
done