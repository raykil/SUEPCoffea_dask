import ROOT
import os

# Directory path where the root files are located
directory = "/eos/cms/store/group/phys_exotica/SUEPs/UL18/hdf5_ANv4/histos_withsyst/SR_cards_ANv4/"

# Create the output text file
output_file = open("results.txt", "w")

# Write the header to the text file
output_file.write("File name\tSR Key\tB1 Key\tB1_7\tB1_8\tSR_5\tSR_6\tSR_7\tSR_8\n")

# Loop through files in the directory
for filename in os.listdir(directory):
    if filename.startswith("data") and filename.endswith(".root"):
        file_path = os.path.join(directory, filename)
        file = ROOT.TFile(file_path)

        # Get the list of all keys in the file
        keys = file.GetListOfKeys()

        # Initialize variables to track conditions
        has_SR_key = 0
        has_B1_key = 0
        bin_B1_7_yields = 0
        bin_B1_8_yields = 0
        bin_SR_5_yields = 0
        bin_SR_6_yields = 0
        bin_SR_7_yields = 0
        bin_SR_8_yields = 0

        # Loop through the keys and check for the desired keys
        for key in keys:
            key_name = key.GetName()
            if key_name.startswith("leadclustertracks_SR_data"):
                obj = key.ReadObj()
                histogram = obj
                bin_SR_5_yields = histogram.GetBinContent(5)
                bin_SR_6_yields = histogram.GetBinContent(6)
                bin_SR_7_yields = histogram.GetBinContent(7)
                bin_SR_8_yields = histogram.GetBinContent(8)
                if (bin_SR_5_yields > 0) or (bin_SR_6_yields > 0) or (bin_SR_7_yields > 0) or (bin_SR_8_yields > 0):
                    has_SR_key = 1
            elif key_name.startswith("leadclustertracks_B1_data"):
                obj = key.ReadObj()
                histogram = obj
                bin_B1_7_yields = histogram.GetBinContent(7)
                bin_B1_8_yields = histogram.GetBinContent(8)
                if (bin_B1_7_yields > 0) or (bin_B1_8_yields > 0):
                    has_B1_key = 1

        # Check the conditions for saving to the text file
        if ((has_B1_key) or (has_SR_key)):
            if (bin_SR_5_yields > 0) or (bin_SR_6_yields > 0) or (bin_SR_7_yields > 0) or (bin_SR_8_yields > 0) or (bin_B1_7_yields > 0) or (bin_B1_8_yields > 0):
               output_file.write(f"{filename}\t{has_SR_key}\t{has_B1_key}\t{bin_B1_7_yields}\t{bin_B1_8_yields}\t{bin_SR_5_yields}\t{bin_SR_6_yields}\t{bin_SR_7_yields}\t{bin_SR_8_yields}\n")

        # Close the file
        file.Close()

# Close the output text file
output_file.close()
