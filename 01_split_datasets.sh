#!/usr/bin/env bash

#usage: bash 01_split_datasets.sh data_dir
data_dir=$1
mkdir -p "${data_dir}/ImageSets/Main"
python3 split_data.py \
        --trainval_percent 1 \
        --train_percent 0.85 \
        --xml_file_path "${data_dir}/Annotations" \
        --txt_save_path "${data_dir}/ImageSets/Main"
