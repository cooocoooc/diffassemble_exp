#!/bin/bash
#SBATCH --job-name=Diff-celea-200
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --gres=gpu:ampere:1
#SBATCH --mem=28g
#SBATCH --time=12:00:00
#SBATCH --output=slurm-%x-%j.out
#SBATCH --partition=tpg-gpu-small

#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=nkwb43@durham.ac.uk

cd DiffAssemble-release/DiffAssemble-release
source venv309/bin/activate
module load cuda/11.6

# Define variables
dataset='celeba'
puzzles='6 8 10 12'
steps=200
gpus=1
cpus=4
batch_size=4
sampling='DDIM'
checkpoint_path='../Puzzle-Diff/etzpjrkl/checkpoints/epoch=379-step=152380.ckpt'
inference_ratio=1

# Construct arguments
ARGS="-dataset $dataset -puzzle_sizes $puzzles -inference_ratio $inference_ratio -sampling $sampling -gpus $gpus -batch_size $batch_size -steps $steps -num_workers $cpus --noise_weight 0 --predict_xstart True --rotation True "

# Print job info
echo "Job Name: Diff-${dataset}-${steps}"
echo "Running with arguments:"
echo "$ARGS"

# Run the Python script
python puzzle_diff/train_script.py $ARGS
