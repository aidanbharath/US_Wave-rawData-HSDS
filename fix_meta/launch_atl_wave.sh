#!/bin/bash

username=mrossol
alloc=hindcastra

ROOT=/datasets/US_wave/v1.0.0/Atlantic

h5_dir=$ROOT
name=atl_wave
meta_path=$(dirname $PWD)/creation_files/atlantic_wave_meta.npy

squeue -u ${username} -t R,PD -n ${name} | grep ${username} || sbatch -A ${alloc} -J ${name} --export=h5_dir="${h5_dir}",meta_path="${meta_path}",chunks=62499 fix_meta.sbatch
