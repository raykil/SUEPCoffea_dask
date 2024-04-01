import os
import ROOT

def calculate_ratios(input_file_path):
    root_file = ROOT.TFile(input_file_path)

    hist_px = root_file.Get("newHistogram")
    hist_ratio = root_file.Get("thABCD_8AC")

    bin_edges = [21, 26, 31, 36, 41, 46]

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

def process_subdirectory(directory):
    results = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == "total_background.root":
                file_path = os.path.join(root, file)

                ratios = calculate_ratios(file_path)

                folder_name = os.path.basename(root)
                region, _, year = folder_name.split("_")

                new_folder_name = f"r20{year}{region}"

                results.append(new_folder_name)
                results.extend(ratios)

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

    output_file_path = "/eos/user/g/gdecastr/SUEPCoffea_dask/CommonClosures_Integrate45/Comparing/ClosureSFs.txt"

    open(output_file_path, "w").close()

    main(root_directory, output_file_path)