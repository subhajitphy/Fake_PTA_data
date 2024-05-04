#!/bin/bash

echo "starting calculation at $(date)"
export OMP_SCHEDULE=dynamic

export KMP_BLOCKTIME=0

export OMP_NUM_THREADS=1


files=(*.par)

for idx in "${!files[@]}"; do
    file=${files[index]}
    echo "Index: $idx, File: $file"
    python inj.py $idx &
    ((count++))
    if ((count % 31 == 0)); then
        wait
    fi
done

echo "finishing at $(date)"