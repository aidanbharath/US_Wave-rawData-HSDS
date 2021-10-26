#!/bin/bash

username=mrossol
alloc=hindcastra

ROOT=/datasets/US_wave/v1.0.0/virtual_buoy/Atlantic

h5_dir=$ROOT
name=atl_buoy
meta_path=$(dirname $PWD)/creation_files/atlantic_buoy_meta.npy

squeue -u ${username} -t R,PD -n ${name} | grep ${username} || sbatch -A ${alloc} -J ${name} --export=h5_dir="${h5_dir}",meta_path="${meta_path}",chunks=0 fix_meta.sbatch
