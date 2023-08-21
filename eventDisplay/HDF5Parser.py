import os
import pandas as pd

# Directory path where the files are located
directory = "/eos/user/g/gdecastr/SUEPCoffea_dask/eventDisplay/HDF5s_NewSimple_SR"

# Get the list of files in the directory
file_list = os.listdir(directory)

# Sort the file list
file_list.sort()

# List to store individual dataframes
dataframes = []

# Process each file in the directory
for file_name in file_list:

    file_path = os.path.join(directory, file_name)

    # Check if the file is an HDF5 file
    if file_name.endswith(".h5") or file_name.endswith(".hdf5"):
        print(file_name)
        # Read the 'SR' key as a Pandas dataframe
        try:
            dataframe = pd.read_hdf(file_path, key='SR')
            print(dataframe)
            dataframes.append(dataframe)
        except KeyError:
            print("No 'SR' key found in:", file_name)
        
    else:
        print("Skipping non-HDF5 file:", file_name)

# Concatenate all dataframes into one large dataframe
concatenated_df = pd.concat(dataframes)

# Save the concatenated dataframe as a CSV file
output_path = os.path.join(directory, 'HDF5Dataframes.csv')
concatenated_df.to_csv(output_path, index=False)

print("Concatenated dataframe saved as:", output_path)
