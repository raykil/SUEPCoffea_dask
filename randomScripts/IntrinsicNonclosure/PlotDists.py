import ROOT
import matplotlib.pyplot as plt
import numpy as np
import argparse

def get_prefit_histogram_info(root_file, base_histogram_name):
    bin_centers_concat = []
    yields_concat = []
    uncertainties_concat = []

    total_yields = []
    total_uncertainties_squared = []

    #for suffix in [";1", ";2", ";3", ";4"]:
    #   histogram_name = base_histogram_name + suffix
    #   histogram = root_file.Get(histogram_name)
    histogram = root_file.Get(base_histogram_name)

    if histogram:
        for i in range(1, histogram.GetNbinsX() + 1):
            bin_center = histogram.GetBinCenter(i) - 1
            yield_value = histogram.GetBinContent(i)
            uncertainty_value = histogram.GetBinError(i)

            index = bin_centers_concat.index(bin_center) if bin_center in bin_centers_concat else -1

            if index != -1:
                # Bin center already exists, add values
                yields_concat[index] += yield_value
                uncertainties_concat[index] = (uncertainties_concat[index]**2 + uncertainty_value**2)**0.5
            else:
                # Bin center doesn't exist, append new values
                bin_centers_concat.append(bin_center)
                yields_concat.append(yield_value)
                uncertainties_concat.append(uncertainty_value)
    else:
        print(f"Histogram '{base_histogram_name}' not found.")

    return bin_centers_concat, yields_concat, uncertainties_concat

def get_prefit_histogram_info_RunII(root_file, base_histogram_name):
    bin_centers_concat = []
    yields_concat = []
    uncertainties_concat = []

    for suffix in [";1", ";2", ";3", ";4"]:
        histogram_name = base_histogram_name + suffix
        histogram = root_file.Get(histogram_name)

        if histogram:
            for i in range(1, histogram.GetNbinsX() + 1):
                bin_center = histogram.GetBinCenter(i)
                yield_value = histogram.GetBinContent(i)
                uncertainty_value = histogram.GetBinError(i)

                index = bin_centers_concat.index(bin_center) if bin_center in bin_centers_concat else -1

                if index != -1:
                    # Bin center already exists, add values
                    yields_concat[index] += yield_value
                    uncertainties_concat[index] = (uncertainties_concat[index]**2 + uncertainty_value**2)**0.5
                else:
                    # Bin center doesn't exist, append new values
                    bin_centers_concat.append(bin_center)
                    yields_concat.append(yield_value)
                    uncertainties_concat.append(uncertainty_value)
        else:
            print(f"Histogram '{base_histogram_name}' not found.")

    return bin_centers_concat, yields_concat, uncertainties_concat

parser = argparse.ArgumentParser(description='Plotting script with year option')
parser.add_argument('--year', choices=['16', '17', '18', '16APV', 'RunII'], default='18', help='Specify the year (16, 17, 18, 16APV, or RunII)')
args = parser.parse_args()

if args.year == 'RunII':
    file1 = ROOT.TFile(f"/eos/user/g/gdecastr/SUEPCoffea_dask/Plots/ANClosure/{args.year}_TT_background.root", "READ")
    file2 = ROOT.TFile(f"/eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_{args.year}_HighStats/leadclustertracks_onecluster.root", "READ")
    file3 = ROOT.TFile(f"/eos/user/g/gdecastr/SUEPCoffea_dask/Plots/ANClosure/{args.year}_TT_data.root", "READ")
    file4 = ROOT.TFile(f"/eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_{args.year}_All/leadclustertracks_SR.root", "READ")
else:
    file1 = ROOT.TFile(f"/eos/user/g/gdecastr/SUEPCoffea_dask/Plots/ANClosure/UL{args.year}_TT_background.root", "READ")
    file2 = ROOT.TFile(f"/eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_{args.year}_HighStats/leadclustertracks_SR.root", "READ")
    file3 = ROOT.TFile(f"/eos/user/g/gdecastr/SUEPCoffea_dask/Plots/ANClosure/UL{args.year}_TT_data.root", "READ")
    file4 = ROOT.TFile(f"/eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_{args.year}_All/leadclustertracks_SR.root", "READ")


hist_total_background = file1.Get("thABCD_8AC;1")
hist_data = file1.Get("tha_px;1")

hist_total_background_3 = file3.Get("thABCD_8AC;1")
hist_data_3 = file3.Get("tha_px;1")

if args.year == 'RunII':
    bin_centers_prefit, yields_prefit, uncertainties_prefit = get_prefit_histogram_info_RunII(file2, "leadclustertracks_onecluster_SUEP_hadronic_mS125_mD3.00_T3.00")
    bin_centers_prefit_4, yields_prefit_4, uncertainties_prefit_4 = get_prefit_histogram_info_RunII(file4, "leadclustertracks_onecluster_SUEP_hadronic_mS125_mD3.00_T3.00")
else:
    bin_centers_prefit, yields_prefit, uncertainties_prefit = get_prefit_histogram_info(file2, "leadclustertracks_onecluster_SUEP_hadronic_mS125_mD3.00_T3.00")
    bin_centers_prefit_4, yields_prefit_4, uncertainties_prefit_4 = get_prefit_histogram_info(file4, "leadclustertracks_onecluster_SUEP_hadronic_mS125_mD3.00_T3.00")

# Plot using matplotlib
bins = np.linspace(hist_total_background.GetXaxis().GetXmin(), hist_total_background.GetXaxis().GetXmax(), hist_total_background.GetNbinsX() + 1)
bins -= 5

fig, ax = plt.subplots(figsize=(8, 6))

# Plot Data - Total Background
plt.errorbar(bins[5:13], [hist_total_background_3.GetBinContent(i) for i in range(5, 13)],
             yerr=[hist_total_background_3.GetBinError(i) for i in range(5, 13)],
             label="ABCD Estimation (CRTT)", fmt='o-', color='black', linestyle='None')

plt.errorbar(bins[5:13], [hist_data_3.GetBinContent(i) for i in range(5, 13)],
             yerr=[hist_data_3.GetBinError(i) for i in range(5, 13)],
             label="Data (CRTT)", fmt='o-', color='red', linestyle='None')


scaled_yields_prefit = [value * 100 for value in yields_prefit]
scaled_uncertainties_prefit = [value * 100 for value in uncertainties_prefit]

scaled_yields_prefit_4 = [value * 100 for value in yields_prefit_4]
scaled_uncertainties_prefit_4 = [value * 100 for value in uncertainties_prefit_4]

plt.errorbar(bins[5:13], scaled_yields_prefit, yerr=scaled_uncertainties_prefit, label="SUEP (mD3.00_T3.00) High Stats (scaled by 100)", fmt='o-', color='blue', linestyle='None')
plt.errorbar(bins[5:13], scaled_yields_prefit_4, yerr=scaled_uncertainties_prefit_4, label="SUEP (mD3.00_T3.00) Low Stats (scaled by 100)", fmt='o-', color='green', linestyle='None')

plt.xlabel("NTracks")
plt.ylabel("Yields")
plt.legend(fontsize='small')
if args.year == 'RunII':
    plt.ylim(0.01,1000000)
else:
    plt.ylim(0.01,100000)
plt.yscale('log')  # Set y-axis to log scale
plt.title(f'Comparing Distributions in CRTT {args.year}')
plt.savefig(f'CRTT_Dists_{args.year}_33.png')
