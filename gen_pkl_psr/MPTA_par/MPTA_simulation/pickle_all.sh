#!/bin/bash



echo "starting calculation at $(date)"
export OMP_SCHEDULE=dynamic

export KMP_BLOCKTIME=0

export OMP_NUM_THREADS=1

num_cpus=$(lscpu | grep '^CPU(s):' | awk '{print $2}')


files=(*.par)

for idx in "${!files[@]}"; do
    file=${files[index]}
    echo "Index: $idx, File: $file"
    python create_pkl.py $idx &
    ((count++))
    if ((count % num_cpus == 0)); then
        wait
    fi
done

echo "finishing at $(date)"
