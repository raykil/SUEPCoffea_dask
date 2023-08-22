import json

# Read the JSON dictionary file
with open('/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/tags.json', 'r') as dict_file:
    dictionary = json.load(dict_file)

# Read the original text file
with open('results.txt', 'r') as original_file:
    lines = original_file.readlines()

# Create the output file
output_file = open('dataTags.txt', 'w')

# Process each line in the original file, excluding the header
for line in lines[1:]:
    # Split the line into columns
    columns = line.strip().split('\t')
    file_name = columns[0]

    # Extract the number after "data_"
    file_number = file_name.split('_', 1)[1].rsplit('.', 1)[0]

    # Find the key in the dictionary that matches the file number value
    matching_key = next((key for key, value in dictionary.items() if value == file_number), None)
    if matching_key:
        # Write the results to the output file
        output_file.write(f"{file_name}\t{matching_key}\n")

# Close the output file
output_file.close()
