import os
import shutil
import subprocess
import re

def modify_card(directory, card_name, cases):
    new_card_name = card_name.replace('.txt', '_B1B2Scaled' + '.txt')
    new_card_path = os.path.join(directory, new_card_name)
    if os.path.exists(new_card_path):
        os.remove(new_card_path)
        print(f"Deleted existing file: {new_card_path}")
    with open(os.path.join(directory, card_name), 'r') as file:
        lines = file.readlines()
    with open(new_card_path, 'w') as new_file:
        for line in lines:
            if cases[0] in line or cases[1] in line:
                modified_line = line.replace('.root', '_0Sig_B1B2Scaled.root')
                new_file.write(modified_line)
            else:
                new_file.write(line)

def combine_across_years(base_directory):
    runII_dir = os.path.join(base_directory, 'RunII')
    if not os.path.exists(runII_dir):
        print(f"RunII directory {runII_dir} does not exist. Skipping.")
        return
    print(f"Combining across years in: {runII_dir}")
    variants = ['SR', 'B1', 'B2', 'C1', 'C2', 'D1', 'D2', 'E1', 'E2']
    for variant in variants:
        cmd = 'combineCards.py '
        for year in ['2016', '2016APV', '2017', '2018']:
            if year == '2016APV':
                year_dir = f"../{year}/"
                cmd += f"UL{year[-5:]}={year_dir}CombinedCRDY_SUEP_hadronic_mS125_mD5.00_T5.00_0Sig{variant}_B1B2Scaled.txt "
            else:
                year_dir = f"../{year}/"
                cmd += f"UL{year[-2:]}={year_dir}CombinedCRDY_SUEP_hadronic_mS125_mD5.00_T5.00_0Sig{variant}_B1B2Scaled.txt "
        output_name = f"CombinedCRDY_SUEP_hadronic_mS125_mD5.00_T5.00_0Sig{variant}_B1B2Scaled.txt"
        cmd += f">> {output_name}"
        print(cmd)
        subprocess.run(cmd, shell=True, cwd=runII_dir)

def process_directory(base_directory):
    year_folders = ['2016', '2016APV', '2017', '2018']
    for year_folder in year_folders:
        current_dir = os.path.join(base_directory, year_folder)
        if not os.path.exists(current_dir):
            print(f"Directory {current_dir} does not exist. Skipping.")
            continue
        print(f"Processing directory: {current_dir}")
        for file_name in os.listdir(current_dir):
            if file_name.endswith('.txt') and file_name.startswith('CombinedCRDY_') and 'SUEP_hadronic_mS125_mD5.00_T5.00' in file_name and '0Sig' in file_name:
                modify_card(current_dir, file_name, cases)
                print(f"Processed card: {file_name}")
    combine_across_years(base_directory)

cases = ['$PROCESS_B1', '$PROCESS_B2']

base_directory = input("Enter the base directory path: ")
process_directory(base_directory)
