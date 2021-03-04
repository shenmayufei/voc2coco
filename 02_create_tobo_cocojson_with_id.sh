#!/usr/bin/env bash

# Usage: sh　02_create_tobo_cocojson_with_id.sh

for split in train val trainval test
do
    python voc2coco.py \
        --ann_dir /media/yzh/data/comma/tobo_detect/tobo_2833_dataset/Annotations \
        --ann_ids /media/yzh/data/comma/tobo_detect/tobo_2833_dataset/ImageSets/Main/${split}.txt \
        --labels /media/yzh/data/comma/tobo_detect/tobo_2833_dataset/label.txt \
        --output /media/yzh/data/comma/tobo_detect/tobo_2833_dataset/${split}.json \
        --ext xml
done
