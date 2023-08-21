import csv

csv_file_path = 'HDF5s_NewSimple_SR/HDF5Dataframes.csv'
txt_file_path = 'EDMEvents.txt'

# Read the CSV file and extract values from the first three columns
with open(csv_file_path, 'r') as csv_file:
    reader = csv.reader(csv_file)
    data = [row[:3] for row in reader]

# Format the values as first column : third column : second column
formatted_values = [f"{row[0]}:{row[2]}:{row[1]}" for row in data]

# Save the formatted values to a .txt file
with open(txt_file_path, 'w') as txt_file:
    txt_file.write('\n'.join(formatted_values))
