import ROOT
import matplotlib.pyplot as plt
import numpy as np

def plot_combined_histogram(bin_centers, yields, uncertainties, output_filename):
    fig, ax = plt.subplots(figsize=(12, 8))
    print(bin_centers)
    plt.errorbar(bin_centers, yields, yerr=uncertainties, fmt='o', color='b', label='Combined Data', capsize=5, capthick=2)
    plt.xlim(0, 100)
    #plt.yscale('log')
    plt.ylim(0, 13000)
    plt.axvline(x=10, linestyle='--', color='gray', linewidth=1)
    plt.axvline(x=20, linestyle='--', color='gray', linewidth=1)
    plt.xlabel('Bin Center')
    plt.ylabel('Yield')
    plt.title('Combined Leadclustertracks Data - Total Background')
    plt.legend()
    plt.tight_layout()
    plt.savefig('/eos/user/g/gdecastr/www/PrefitPlots/' + output_filename)

def get_combined_histogram_info(root_file, data_histogram_names, background_histogram_name):
    bin_centers_combined = []
    yields_combined = []
    uncertainties_combined = np.zeros(100)  # Initialize uncertainties_combined as a NumPy array

    for histogram_name in data_histogram_names:
        histogram = root_file.Get(histogram_name)

        if histogram:
            bin_centers = []
            yields = []
            uncertainties = []

            for i in range(1, histogram.GetNbinsX() + 1):
                bin_centers.append(histogram.GetBinCenter(i) - 1)
                yields.append(histogram.GetBinContent(i))
                uncertainties.append(histogram.GetBinError(i))

            bin_centers_combined = bin_centers  # Assuming all histograms have the same bin centers
            yields_combined = np.sum([yields_combined, yields], axis=0)

            # Pad uncertainties with zeros to match the length
            uncertainties_combined = np.zeros_like(uncertainties)
            uncertainties_combined[:len(uncertainties)] += uncertainties

            uncertainties_combined = np.sqrt(np.sum([uncertainties_combined**2, np.array(uncertainties)**2], axis=0))
        else:
            print(f"Histogram '{histogram_name}' not found.")


    # Subtract total_background histogram
    background_histogram = root_file.Get(background_histogram_name)

    if background_histogram:
        yields_combined -= np.array([background_histogram.GetBinContent(i) for i in range(1, background_histogram.GetNbinsX() + 1)])
        uncertainties_combined = np.sqrt(np.sum([uncertainties_combined**2, np.array([background_histogram.GetBinError(i) for i in range(1, background_histogram.GetNbinsX() + 1)])**2], axis=0))
    else:
        print(f"Total Background Histogram '{background_histogram_name}' not found.")

    return bin_centers_combined, yields_combined, uncertainties_combined


def main():
    input_file_path = "/eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_RunII_HighStats/leadclustertracks.root"
    output_filename = "combined_leadclustertracks_data.png"
    
    root_file = ROOT.TFile(input_file_path, "READ")

    if root_file and not root_file.IsZombie():
        data_histogram_names = [
            "leadclustertracks_data;1",
            "leadclustertracks_data;2",
            "leadclustertracks_data;3",
            "leadclustertracks_data;4",
        ]
        total_background_histogram_name = "total_background;1"

        bin_centers_combined, yields_combined, uncertainties_combined = get_combined_histogram_info(root_file, data_histogram_names, total_background_histogram_name)

        if bin_centers_combined:
            plot_combined_histogram(bin_centers_combined, yields_combined, uncertainties_combined, output_filename)
        else:
            print("Skipping plot due to missing information.")
    else:
        print(f"Error: Unable to open the ROOT file '{input_file_path}'.")

if __name__ == "__main__":
    main()
