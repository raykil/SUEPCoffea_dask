import matplotlib.pyplot as plt
import numpy as np

# Read ratios
with open('../ClosureSFs.txt', 'r') as file:
    lines = file.readlines()

data = {}
for line in lines:
    parts = line.split()
    if 'APV' in parts[0]:
        year = '2016APV'
        region = parts[0][8:]
    else:
        year = parts[0][1:5]
        region = parts[0][5:]
    ratios = [float(part) for part in parts[1:]]
    if region not in data:
        data[region] = {}
    data[region][year] = ratios

with open('../ClosureSFs_Data.txt', 'r') as file:
    lines = file.readlines()

data_data = {}
for line in lines:
    parts = line.split()
    if 'APV' in parts[0]:
        year = '2016APV'
        region = parts[0][8:]
    else:
        year = parts[0][1:5]
        region = parts[0][5:]
    ratios = [float(part) for part in parts[1:]]
    if region not in data_data:
        data_data[region] = {}
    data_data[region][year] = ratios

# Read uncertainties
uncertainties = {}
with open('../ClosureSFs_Uncs.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    parts = line.split()
    if 'APV' in parts[0]:
        year = '2016APV'
        region = parts[0][8:]
    else:
        year = parts[0][1:5]
        region = parts[0][5:]
    uncs = [float(part) for part in parts[1:]]
    if region not in uncertainties:
        uncertainties[region] = {}
    uncertainties[region][year] = uncs

# Read uncertainties
uncertainties_data = {}
with open('../ClosureSFs_DataUncs.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    parts = line.split()
    if 'APV' in parts[0]:
        year = '2016APV'
        region = parts[0][8:]
    else:
        year = parts[0][1:5]
        region = parts[0][5:]
    uncs = [float(part) for part in parts[1:]]
    if region not in uncertainties_data:
        uncertainties_data[region] = {}
    uncertainties_data[region][year] = uncs

# Plotting
for region in data.keys():
    if region == 'SR':  # Skip the specified region
        continue

    for year in data[region].keys():
        plt.figure(figsize=(10, 6))

        # Data for the original dataset
        ratios = np.array(data[region][year])
        uncs = np.array(uncertainties[region][year])
        # Data for the 'data_data' dataset
        ratios_data = np.array(data_data[region][year])
        uncs_data = np.array(uncertainties_data[region][year])

        # First subplot: Original vs Data
        plt.subplot(2, 1, 1)
        plt.errorbar(range(1, 7), ratios[0:6], yerr=uncs[0:6], fmt='o', label='MC', capsize=5, color = 'green')
        plt.errorbar(range(1, 7), ratios_data[0:6], yerr=uncs_data[0:6], fmt='o', label='Data', capsize=5, color = 'blue')
        plt.title(f'Scatterplot of SFs for {region} in {year}')
        plt.xlabel('Bin')
        plt.ylabel('Ratios')
        plt.legend()

        # Second subplot: Ratio of data_data/data and its uncertainty
        plt.subplot(2, 1, 2)
        
        # Calculate the ratio
        ratio = ratios_data / ratios

        # Calculate the uncertainty of the ratio
        ratio_uncs = np.sqrt((uncs_data / ratios) ** 2 + (ratios_data * uncs / ratios ** 2) ** 2)

        plt.errorbar(range(1, 7), ratio[0:6], yerr=ratio_uncs[0:6], fmt='o', label='Data/MC', capsize=5, color = 'blue')
        plt.axhline(y=1.0, linestyle='--', color='black')
        plt.title(f'Ratio of Data/MC for {region} in {year}')
        plt.xlabel('Bin')
        plt.ylabel('Data / MC')
        plt.legend()
        plt.ylim(0,2)

        plt.tight_layout()
        plt.savefig(f'Comparison_{region}_{year}.png')
        plt.close()  # Close the figure to avoid memory issues