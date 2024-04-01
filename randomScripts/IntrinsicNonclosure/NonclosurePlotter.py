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

hist_difference = hist_data.Clone("difference")
hist_difference.Add(hist_total_background, -1)

hist_difference_3 = hist_data_3.Clone("difference")
hist_difference_3.Add(hist_total_background_3, -1)


for bin in range(1, hist_difference.GetNbinsX() + 1):
    error_data = hist_data.GetBinError(bin)
    error_total_background = hist_total_background.GetBinError(bin)
    error_difference = (error_data**2 + error_total_background**2)**0.5
    hist_difference.SetBinError(bin, error_difference)

for bin in range(1, hist_difference_3.GetNbinsX() + 1):
    error_data = hist_data_3.GetBinError(bin)
    error_total_background = hist_total_background_3.GetBinError(bin)
    error_difference = (error_data**2 + error_total_background**2)**0.5
    hist_difference_3.SetBinError(bin, error_difference)



# Plot using matplotlib
bins = np.linspace(hist_difference.GetXaxis().GetXmin(), hist_difference.GetXaxis().GetXmax(), hist_difference.GetNbinsX() + 1)
bins -= 5

fig = plt.figure(figsize=(8, 12))

main_plot_height = 0.6  # Adjust as needed
ratio_plot_height = 0.25  # Adjust as needed
main_plot_position = [0.1, 0.35, 0.8, main_plot_height]  # Left, Bottom, Width, Height
ratio_plot_position = [0.1, 0.05, 0.8, ratio_plot_height]
ax_main = fig.add_axes(main_plot_position)

# Plot Data - Total Background
plt.errorbar(bins[5:13], [hist_difference.GetBinContent(i) for i in range(5, 13)],
             yerr=[hist_difference.GetBinError(i) for i in range(5, 13)],
             label="SM MC - ABCD Estimation (CRTT)", fmt='o-', color='black', linestyle='None')

plt.errorbar(bins[5:13], [hist_difference_3.GetBinContent(i) for i in range(5, 13)],
             yerr=[hist_difference_3.GetBinError(i) for i in range(5, 13)],
             label="Data - ABCD Estimation (CRTT)", fmt='o-', color='red', linestyle='None')
scaled_yields_prefit = [value * 100 for value in yields_prefit]
scaled_uncertainties_prefit = [value * 100 for value in uncertainties_prefit]
scaled_yields_prefit_4 = [value * 100 for value in yields_prefit_4]
scaled_uncertainties_prefit_4 = [value * 100 for value in uncertainties_prefit_4]
# Plot SUEP (mD3.00_T3.00)
plt.errorbar(bins[5:13], scaled_yields_prefit, yerr=scaled_uncertainties_prefit, label="SUEP (mD3.00_T3.00) High Stats (scaled by 100)", fmt='o-', color='blue', linestyle='None')
plt.errorbar(bins[5:13], scaled_yields_prefit_4, yerr=scaled_uncertainties_prefit_4, label="SUEP (mD3.00_T3.00) Low Stats (scaled by 100)", fmt='o-', color='green', linestyle='None')

ax_main.set_xlabel('NTracks')
ax_main.set_ylabel('Yields')
ax_main.set_title(f'Comparing MC and Data Nonclosures {args.year}')
plt.legend(fontsize='small')

ax_ratio = fig.add_axes(ratio_plot_position)

ratio = []
for i in range(5, 13):
    bin_content_difference = hist_difference.GetBinContent(i)
    bin_content_difference_3 = hist_difference_3.GetBinContent(i)
    if bin_content_difference_3 != 0:
        ratio.append(bin_content_difference / bin_content_difference_3)
    else:
        ratio.append(0.0)
print(ratio)
error_ratio = []
for i in range(5, 13):
    bin_content_difference = hist_difference.GetBinContent(i)
    bin_content_difference_3 = hist_difference_3.GetBinContent(i)
    bin_error_difference = hist_difference.GetBinError(i)
    bin_error_difference_3 = hist_difference_3.GetBinError(i)
    
    if bin_content_difference_3 != 0:
        error_ratio.append(ratio[i - 5] * ((bin_error_difference / bin_content_difference)**2
                                           + (bin_error_difference_3 / bin_content_difference_3)**2)**0.5)
    else:
        error_ratio.append(0.0)
plt.errorbar(bins[5:13], ratio, yerr=error_ratio, fmt='o-', color='blue', linestyle='None')
plt.axhline(y=1.0, color='gray', linestyle='--')
ax_ratio.set_xlabel('NTracks')
ax_ratio.set_ylabel('Ratio')
ax_ratio.set_title('Ratio of Differences MC/Data')
plt.subplots_adjust(hspace=0.55)
ax_ratio.set_ylim(-2,2)
plt.savefig(f'CRTT_{args.year}_ratio_33.png')
