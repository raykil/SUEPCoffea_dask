import os
import ROOT

def calculate_ratios(input_file_path):
    root_file = ROOT.TFile(input_file_path)

    hist_px = root_file.Get("newHistogram")
    hist_ratio = root_file.Get("thABCD_8AC")

    bin_edges = [21, 26, 31, 36, 41, 46]

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

def process_subdirectory(directory):
    results = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith("total_background.root"):  # Ensure it only processes .root files
                file_path = os.path.join(root, file)

                uncertainties = calculate_ratios(file_path)

                folder_name = os.path.basename(root)
                region, _, year = folder_name.split("_")

                new_folder_name = f"r20{year}{region}"

                results.append(new_folder_name)

                results.extend(uncertainties)

    return results

def save_to_txt(results, output_file):
    with open(output_file, "a") as file:
        for entry in results:
            file.write(str(entry) + " ")
        file.write("\n")

def main(root_directory, output_file):
    for subdirectory in os.listdir(root_directory):
        if subdirectory == 'FirstCheck':
            continue
        subdirectory_path = os.path.join(root_directory, subdirectory)

        results = process_subdirectory(subdirectory_path)

        save_to_txt(results, output_file)

if __name__ == "__main__":
    root_directory = "/eos/user/g/gdecastr/SUEPCoffea_dask/CommonClosures_Integrate45/Comparing"

    output_file_path = "/eos/user/g/gdecastr/SUEPCoffea_dask/CommonClosures_Integrate45/Comparing/ClosureSFs_Uncs.txt"

    # Clear the output file at the start
    open(output_file_path, "w").close()

    main(root_directory, output_file_path)
