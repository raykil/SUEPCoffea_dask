#!/bin/bash

# Define directories
source_dir="../"
target_dir=""

# Loop through CRDY, CRTT, and SR
for region in "CRDY" "CRTT" "SR" "EMu"; do
    # Loop through years 18, 17, 16, 16APV
    for year in "18" "17" "16" "16APV"; do
        # Loop through Data and Background
        rm -rf "${region}_2D_${year}"
        mkdir "${region}_2D_${year}"
        for data_type in "total_data" "total_background"; do
            # Define source and target file names
            if [ "$region" == "SR" ]; then
                source_file="${source_dir}${year}_Default_${data_type}.root"
                target_file="${region}_2D_${year}/${data_type}.root"
            else
                source_file="${source_dir}${year}_${region}_${data_type}.root"
                target_file="${region}_2D_${year}/${data_type}.root"
            fi
            # Copy the file
            cp "$source_file" "${target_dir}$target_file"
            echo "$source_file" "${target_dir}$target_file"
        done
    done
done
