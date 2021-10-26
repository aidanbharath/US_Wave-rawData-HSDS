#!/bin/bash
#SBATCH --time=04:00:00
#SBATCH --output=%x-%j.out
#SBATCH --error=%x-%j.err
#SBATCH --partition=short
#SBATCH --qos=high

source activate /shared-projects/rev/modulefiles/conda_env

h5_src=/scratch/abharath/alaska_spatial_combine/alaska_wave_${year}.h5
h5_dst=/datasets/US_wave/v1.0.0/Alaska/alaska_wave_${year}.h5
var_attrs_path=$(dirname $PWD)/creation_files/alaska_hsds_attrs.json
meta_path=$(dirname $PWD)/creation_files/alaska_wave_meta.npy

rechunk -src ${h5_src} -dst ${h5_dst} -vap ${var_attrs_path} -m ${meta_path} -v -rm
