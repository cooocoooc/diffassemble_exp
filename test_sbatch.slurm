#!/bin/bash
#SBATCH --job-name=test_sbatch
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --gres=gpu:ampere:1
#SBATCH --mem=28g
#SBATCH --time=00:02:00
#SBATCH --output=slurm-%x-%j.out
#SBATCH --partition=tpg-gpu-small

#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=nkwb43@durham.ac.uk



cd DiffAssemble-release/DiffAssemble-release
source venv309/bin/activate
module load cuda/11.6

python test_slurm.py