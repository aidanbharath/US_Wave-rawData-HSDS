#!/bin/bash
#SBATCH --time=04:00:00
#SBATCH --output=%x-%j.out
#SBATCH --error=%x-%j.err
#SBATCH --partition=short

source activate /shared-projects/rev/modulefiles/conda_env

for h5_path in ${h5_dir}/*
do
    python -m fix_meta -h5 ${h5_path} -meta ${meta_path} -c ${chunks}
done