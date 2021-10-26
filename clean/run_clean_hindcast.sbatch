#!/bin/bash
#SBATCH --time=04:00:00
#SBATCH --output=%x-%j.out
#SBATCH --error=%x-%j.err
#SBATCH --partition=short

source activate /shared-projects/rev/modulefiles/conda_env

h5_src=/datasets/US_wave/v1.0.0/${domain}_old/${domain}_wave_${year}.h5
h5_dst=/datasets/US_wave/v1.0.0/${domain}/${domain}_wave_${year}.h5

python clean_hindcast.py -src ${h5_src} -dst ${h5_dst}