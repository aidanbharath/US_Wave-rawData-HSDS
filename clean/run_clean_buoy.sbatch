#!/bin/bash
#SBATCH --time=04:00:00
#SBATCH --output=%x-%j.out
#SBATCH --error=%x-%j.err
#SBATCH --partition=short

source activate /shared-projects/rev/modulefiles/conda_env

h5_src=/datasets/US_wave/v1.0.0/virtual_buoy/${domain}/${domain}_virtual_buoy_${year}.h5

python clean_wave_data.py -src ${h5_src}