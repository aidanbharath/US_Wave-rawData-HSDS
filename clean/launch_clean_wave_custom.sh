#!/bin/bash

username=
allocation=hindcastra

domain=$1
year=$2

squeue -u ${username} -t R,PD -n clean_${domain}-${year} | grep ${username} || sbatch -A ${allocation} -J clean_${domain}-${year} --export=domain="${domain}",year="${year}" run_clean_wave.sbatch
