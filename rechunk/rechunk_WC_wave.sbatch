#!/bin/bash
#SBATCH --time=04:00:00
#SBATCH --output=%x-%j.out
#SBATCH --error=%x-%j.err
#SBATCH --partition=short
#SBATCH --qos=high

source activate /shared-projects/rev/modulefiles/conda_env

h5_src=/projects/wec/cloud_wave_data/wc2/parser/hdf5_datasets/Station_CG_${year}.h5
h5_dst=/datasets/US_wave/v1.0.0/West_Coast/West_Coast_wave_${year}.h5
var_attrs_path=$(dirname $PWD)/creation_files/wave_hsds_attrs.json
meta_path=$(dirname $PWD)/creation_files/wave_meta.npy

rechunk -src ${h5_src} -dst ${h5_dst} -vap ${var_attrs_path} -m ${meta_path} -v
