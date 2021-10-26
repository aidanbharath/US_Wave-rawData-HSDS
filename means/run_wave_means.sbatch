#!/bin/bash
#SBATCH --time=04:00:00
#SBATCH --output=%x-%j.out
#SBATCH --error=%x-%j.err
#SBATCH --partition=short

source activate /shared-projects/rev/modulefiles/conda_env

python wave_means.py ${domain} ${dset}