import os
import ROOT
import argparse

def calculate_nominal(input_file_path, bin_edges):
    root_file = ROOT.TFile(input_file_path)

    hist_px = root_file.Get("newHistogram")
    hist_ratio = root_file.Get("thABCD_8AC")

    ratios = []

    for edge in bin_edges:
        bin_index = hist_px.FindFixBin(edge)
        if hist_ratio.GetBinContent(bin_index) <= 0 or hist_px.GetBinContent(bin_index) <= 0:
            ratio_value = 1
        else:
            ratio_value = hist_px.GetBinContent(bin_index) / hist_ratio.GetBinContent(bin_index)
        ratios.append(ratio_value)

    root_file.Close()

    return ratios

def calculate_uncs(input_file_path, bin_edges):
    root_file = ROOT.TFile(input_file_path)

    hist_px = root_file.Get("newHistogram")
    hist_ratio = root_file.Get("thABCD_8AC")

    uncertainties = []

    for edge in bin_edges:
        bin_index = hist_px.FindFixBin(edge)
        A = hist_px.GetBinContent(bin_index)
        B = hist_ratio.GetBinContent(bin_index)
        deltaA = hist_px.GetBinError(bin_index)
        deltaB = hist_ratio.GetBinError(bin_index)

        # Avoid division by zero
        if A > 0 and B > 0:
            ratio = A / B
            deltaR = ratio * ((deltaA / A) ** 2 + (deltaB / B) ** 2) ** 0.5
        else:
            deltaR = 0

        uncertainties.append(deltaR)

    root_file.Close()

    return uncertainties

def process_subdirectory(directory, isData, bin_edges, isRunII):
    results = []
    results_uncs = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if isData:
                if file == "total_data.root":
                    file_path = os.path.join(root, file)
                else:
                    continue
            else:
                if file == "total_background.root":
                    file_path = os.path.join(root, file)
                else: 
                    continue

            nominal = calculate_nominal(file_path, bin_edges)
            uncs = calculate_uncs(file_path, bin_edges)

            folder_name = os.path.basename(root)
            region, _, year = folder_name.split("_")

            if isRunII:
                new_folder_name = f"r{year}{region}"
            else:
                new_folder_name = f"r20{year}{region}"

            results.append(new_folder_name)
            results.extend(nominal)

            results_uncs.append(new_folder_name)
            results_uncs.append(uncs)

    return results, results_uncs

def save_to_txt(results, output_file):
    with open(output_file, "a") as file:
        for entry in results:
            file.write(str(entry) + " ")
        file.write("\n")

def main(root_directory, output_nominal, output_uncs, isData, bin_edges, isRunII):
    for subdirectory in os.listdir(root_directory):
        subdirectory_path = os.path.join(root_directory, subdirectory)

        nominal, nominal_uncs = process_subdirectory(subdirectory_path, isData, bin_edges, isRunII)

        save_to_txt(nominal, output_nominal)
        save_to_txt(nominal_uncs, output_uncs)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate nominal values and uncertainties from ROOT files.')
    parser.add_argument('input_directory', type=str, help='Directory containing the input ROOT files.')
    parser.add_argument('output_directory', type=str, help='Directory where the output text files will be saved.')
    parser.add_argument('--isData', action='store_true', help='Set this flag if processing data files.')
    parser.add_argument('--isRunII', action='store_true', help='Set this flag if processing data files.')
    parser.add_argument('--bin_edges', nargs='+', type=float, help='Custom bin edges for histograms.')
    args = parser.parse_args()

    root_directory = args.input_directory

    if args.isData:
        output_nominal = args.output_directory + "/ClosureSFs_Data.txt"
        output_uncs = args.output_directory + "/ClosureSFs_Uncs_Data.txt"
    else:
        output_nominal = args.output_directory + "/ClosureSFs.txt"
        output_uncs = args.output_directory + "/ClosureSFs_Uncs.txt"

    open(output_nominal, "w").close()
    open(output_uncs, "w").close()

    main(root_directory, output_nominal, output_uncs, args.isData, args.bin_edges, args.isRunII)