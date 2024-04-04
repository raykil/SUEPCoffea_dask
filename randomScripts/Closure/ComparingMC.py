import matplotlib.pyplot as plt
import numpy as np

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

for region, years_data in data.items():
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    for year, ratios in years_data.items():
        color = 'red' if year == '2018' else 'green' if year == '2017' else 'purple' if year == '2016' else 'blue'
        uncs = uncertainties[region][year]
        plt.errorbar(range(1, 7), ratios[0:6], yerr=uncs[0:6], fmt='o', label=year, capsize=5, color = color)
    plt.title(f'Scatterplot of SFs for {region}')
    plt.xlabel('Bin')
    plt.ylabel('Ratios')
    plt.legend()

    plt.subplot(2, 1, 2)
    ratios_2018 = years_data['2018']
    uncs_2018 = uncertainties[region]['2018']  # Uncertainties for 2018
    for year, ratios in years_data.items():
        uncs = uncertainties[region][year]
        ratios_relative = []
        uncs_relative = []
        
        for r, r_2018, unc, unc_2018 in zip(ratios, ratios_2018, uncs, uncs_2018):
            ratio_relative = r / r_2018
            unc_relative = np.sqrt((unc / r_2018) ** 2 + (r * unc_2018 / r_2018 ** 2) ** 2)
            
            ratios_relative.append(ratio_relative)
            uncs_relative.append(unc_relative)
        color = 'red' if year == '2018' else 'green' if year == '2017' else 'purple' if year == '2016' else 'blue'
        if year == '2018':
            continue
        else:
            plt.errorbar(range(1, 7), ratios_relative[0:6], yerr=uncs_relative[0:6], fmt='o', label=year, capsize=5, color = color)

    plt.axhline(y = 1.0, linestyle = '--', color = 'black')
    plt.title(f'SFs Compared to 2018 for {region}')
    plt.xlabel('Bin')
    plt.ylabel('Year / 2018')
    plt.ylim(0,2)
    plt.legend()

    plt.tight_layout()
    plt.savefig('RatioOfRatios_'+region+'.png')

years = list(data['SR'].keys())

for year in years:
    plt.figure(figsize=(10, 8))

    plt.subplot(2, 1, 1)
    for region, years_data in data.items():
        if region == 'SR':
            continue
        color = 'red' if region == 'SR' else 'green' if region == 'CRTT' else 'purple' if region == 'EMu' else 'blue'
        uncs = uncertainties[region][year]
        plt.errorbar(range(1, 7), years_data[year][0:6], yerr=uncs[0:6], fmt='o', label=region, capsize=5, color = color)
    plt.title(f'Scatterplot of SFs for {year}')
    plt.xlabel('Bin')
    plt.ylabel('SFs')
    plt.legend()

    plt.subplot(2, 1, 2)
    ratios_tt = data['CRTT'][year]
    uncs_tt = uncertainties['CRTT'][year]
    
    for region, ratios in data.items():        
        uncs = uncertainties[region][year]
        ratios_relative = []
        uncs_relative = []
        if region == 'SR':
            continue
        for r, tt, unc, unc_tt in zip(ratios[year], ratios_tt, uncs, uncs_tt):
            ratio_relative = r / tt
            unc_relative = np.sqrt((unc / tt) ** 2 + (r * unc_tt / tt ** 2) ** 2)
            
            ratios_relative.append(ratio_relative)
            uncs_relative.append(unc_relative)
        color = 'red' if region == 'SR' else 'green' if region == 'CRTT' else 'purple' if region == 'EMu' else 'blue'
        if region == 'CRTT':
            continue
        else:
            plt.errorbar(range(1, 7), ratios_relative[0:6], yerr=uncs_relative[0:6], fmt='o', label=f'{region} / CRTT', capsize=5, color = color)
    plt.axhline(y=1.0, linestyle='--', color='black')
    plt.title(f'SFs Compared to CRTT for {year}')
    plt.xlabel('Bin')
    plt.ylabel('Region / CRTT')
    plt.legend()
    plt.ylim(0,2)

    plt.tight_layout()
    plt.savefig('RatioOfRatios_'+year+'.png')