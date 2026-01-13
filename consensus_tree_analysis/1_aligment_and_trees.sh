#!/bin/bash

input_dir="./genolevures_uniquefamilies"
aligned_dir="./aligned"
trees_dir="./trees_iqtree"

mkdir -p "$aligned_dir"
mkdir -p "$trees_dir"

JOBS=8

process_file() {
    f="$1"
    base=$(basename "$f" .fasta)

    echo ">>> Processing family $base"

    mafft --auto "$f" > "$aligned_dir/${base}_aligned.fasta"

    iqtree2 -s "$aligned_dir/${base}_aligned.fasta" -m MFP -bb 1000 -nt AUTO  -pre "$trees_dir/${base}"


    for file in "$trees_dir/${base}."*; do
        if [[ "$file" != "$trees_dir/${base}.treefile" ]]; then
            rm -f "$file"
        fi
    done


    echo ">>> Done $base"
}

export aligned_dir trees_dir
export -f process_file

ls "$input_dir"/*.fasta | head -n 500 | xargs -n 1 -P $JOBS -I {} bash -c 'process_file "$@"' _ {}

num_trees=$(ls "$trees_dir"/*.treefile | wc -l)
echo "Total number of treefile files in $trees_dir: $num_trees"
