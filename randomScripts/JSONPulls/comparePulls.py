import json
import matplotlib.pyplot as plt

def process_entry(entry, scale):
    central_value = entry["fit"][1]*scale
    unc_down = abs(entry["fit"][0] - entry["fit"][1])*scale
    unc_up = abs(entry["fit"][1] - entry["fit"][2])*scale
    return central_value, unc_down, unc_up

def filter_and_sort_entries(json_data):
    closure_entries = [param for param in json_data['params'] if param['name'].startswith("closure")]
    closure_entries.sort(key=lambda entry: int(entry["name"].split("_bin")[1]))
    return closure_entries

def plot_scatter(json_data, scale, label):
    closure_entries = filter_and_sort_entries(json_data)
    central_values, unc_down_values, unc_up_values = zip(*[process_entry(entry, scale) for entry in closure_entries])
    bins = range(1, len(closure_entries) + 1)

    plt.errorbar(bins, central_values, yerr=[unc_down_values, unc_up_values], fmt='o-', label=label, capsize=5)

with open('/eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats/ImpactsWithPurpose/SR_5_5/impactsd.json') as file1:
    data1 = json.load(file1)

with open('/eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats/ImpactsWithPurpose/SRCR_5_5/impactsd.json') as file2:
    data2 = json.load(file2)

with open('/eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats/ImpactsWithPurpose/SRDY_5_5/impactsd.json') as file1:
    data3 = json.load(file1)

with open('/eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats/ImpactsWithPurpose/SRTT_5_5/impactsd.json') as file1:
    data4 = json.load(file1)

with open('/eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats/ImpactsWithPurpose/CRDY_5_5/impactsd.json') as file1:
    data5 = json.load(file1)

with open('/eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats/ImpactsWithPurpose/CRTT_5_5/impactsd.json') as file1:
    data6 = json.load(file1)

with open('/eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats_Integrate45/ImpactsWithPurpose/SRCR_5_5/impactsd.json') as file1:
    data7 = json.load(file1)

#plot_scatter(data1, 1.0, label='Closure Unblind SR')
plot_scatter(data2, 1.0, label='Closure Unblind SRCR')
#plot_scatter(data4, 1.0, label='Closure Unblind SRDY')
#plot_scatter(data3, 1.0, label='Closure Unblind SRTT')
#plot_scatter(data5, 1.0, label='Closure Unblind CRDY')
#plot_scatter(data6, 1.0, label='Closure Unblind CRTT')
plot_scatter(data7, 1.0, label='Closure Unblind SRCR Integrate 45')

plt.xlabel('Closure Bin')
#plt.ylabel('Central Value')
#plt.ylabel('Pull')
plt.ylabel('Pull')
#plt.ylim(-2.5,1.5)
plt.ylim(-2.5,2.5)
plt.title('Compare Closure Pulls Between Unblind Regions')
plt.legend(fontsize='small')
plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/randomScripts/JSONPulls/Unblind/Integrate45/closure_5_5.png')
