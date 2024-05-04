#!/usr/bin/bash

echo "starting calculation at $(date)"
export OMP_SCHEDULE=dynamic

export KMP_BLOCKTIME=0

export OMP_NUM_THREADS=1


#Run 32 instances of tempo2 in parallel
for f in *.par; do
    tempo2 -gr fake -f "$f" -ndobs 10 -nobsd 1 -randha y -start 50000 -end 53652 -rms 1e-3 &
    ((count++))
    if ((count % 32 == 0)); then
        wait
    fi
done

wait 

for file in *simulate; do
    filename="${file%.*}"
    mv "$file" "${filename}_fake.tim"
done

echo "finishing at $(date)"