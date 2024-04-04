import os
import re
import argparse

def read_ratios_from_file(file_path):
    ratios = {}
    with open(file_path, "r") as file:
        for line in file:
            values = line.strip().split()
            subdirectory = values[0]
            ratios[subdirectory] = [float(value) for value in values[1:]]
    return ratios

def closureSyst(line, new_name, new_type, replacement_values):
    words = line.split()
    
    words[0] = new_name
    words[1] = new_type
    
    dash_indices = [i for i, word in enumerate(words) if word == "-"]
    for i, value in zip(dash_indices, replacement_values):
        words[i] = str(value)
    
    words = ['-' if word == '1.0' else word for word in words]
    
    modified_line = ' '.join(words)
    return modified_line

def closureUncSyst(line, new_name, new_type, replacement_value, replacement_index):
    words = line.split()
    
    words[0] = new_name
    words[1] = new_type
    
    words = ['20.0' if word == '1.0' else word for word in words]
    
    dash_indices = [i for i, word in enumerate(words) if word == "-"]
    if replacement_index < len(dash_indices):
        words[dash_indices[replacement_index]] = str(replacement_value)
    
    words = ['-' if word == '20.0' else word for word in words]

    modified_line = ' '.join(words)
    return modified_line

def modify_script(input_file, output_file, closureShapes_f, closureShapeUncs_f, Normalization_f, year, region, nBins):
    closureShapes = read_ratios_from_file(closureShapes_f)
    closureShapeUncs = read_ratios_from_file(closureShapeUncs_f)
    Normalization = read_ratios_from_file(Normalization_f)

    if year == 'RunII':
        pattern_BackNorm = r"r"+region+"nII\s*rateParam"
    else:
        pattern_BackNorm = r"r"+region+"(?:16APV|16|17|18)\s*rateParam"
    pattern_Closure = r"closure_bin\w*"
    pattern_ClosureSkeleton = r"MuSF\w*"

    with open(input_file, "r") as input_file, open(output_file, "w") as output_file:
        for line in input_file:
            if re.match(pattern_Closure, line) or re.match(pattern_BackNorm, line): # or :
                continue
            if re.match(pattern_ClosureSkeleton, line):
                closureSkeleton = line
            if 'kmax' in line:
                modified_line = re.sub(r'^(kmax\s+)[0-9]+(\s+number of nuisance parameters)$', r'\g<1>' + '*' + r'\2', line)
                output_file.write(modified_line+ "\n")
                continue

            if line.startswith(("r2018"+region+"_SRbin",
                                "r2017"+region+"_SRbin",
                                "r2016"+region+"_SRbin",
                                "r2016APV"+region+"_SRbin",
                                "rRunII"+region+"_SRbin")):
                
                parts = line.strip().split()
                subdirectory = parts[0].split('_')[0]
                ratio_index = int(parts[0].split('_SRbin')[1]) - 1
                
                if subdirectory in closureShapes and subdirectory in Normalization:
                    product = closureShapes[subdirectory][ratio_index] * Normalization[subdirectory][0]
                    modified_expression = f"{product}*{parts[4]}"
                    new_line = " ".join(parts[:4] + [modified_expression] + parts[5:])
                    output_file.write(new_line + "\n")
                else:
                    output_file.write(line+ "\n")
            else:
                output_file.write(line+ "\n")
        print()
        output_file.write(closureSyst(closureSkeleton, 'Normalization'+year, 'lnN', [Normalization['r'+year+region][0] for element in closureShapes['r'+year+region]]))
        output_file.write('\n')
        output_file.write(closureSyst(closureSkeleton, 'closure'+year, 'lnN', [element for element in closureShapes['r'+year+region]]))
        output_file.write('\n')
        for i in range(0,nBins):
            output_file.write(closureUncSyst(closureSkeleton, 'closure'+year+'_bin'+str(i+1), 'lnN', closureShapeUncs['r'+year+region][i] + 1, i))
            output_file.write('\n')
            output_file.write(closureUncSyst(closureSkeleton, 'Normalization'+year+'_bin'+str(i+1), 'lnN', Normalization['r'+year+region][1] + 1, i))
            output_file.write('\n')
            

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a directory.')
    parser.add_argument('directory', type=str, help='The path to the directory.')
    parser.add_argument('cards_directory', type=str, help='Path to the directory containing card files.')
    parser.add_argument('SF_directory', type=str, help='Path to the directory containing Scale Factor files.')
    parser.add_argument('region', type=str, help='Region to process.')
    parser.add_argument('nBins', type=int, help='Number of bins.')
    
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"The directory {args.directory} does not exist.")
    else:
        print(f"Processing directory: {args.directory}")

    closureShapes_path = os.path.join(args.SF_directory, "ClosureSFs.txt")
    closureShapesUncs_path = os.path.join(args.SF_directory, "ClosureSFs_Uncs.txt")
    Normalization_path = os.path.join(args.SF_directory, "Normalization.txt")

    all_files = os.listdir(args.directory)

    filtered_files = [file for file in all_files if file.startswith("Combined"+args.region+"_SUEP_hadronic_mS125_mD") and file.endswith(".txt") and "Split" not in file]

    year = 'MEOW'
    if 'RunII' in args.directory:
        year = 'RunII'
    elif '2018' in args.directory:
        year = '2018'
    elif '2017' in args.directory:
        year = '2017'
    elif '2016APV' in args.directory:
        year = '2016APV'
    else:
        year = '2016'

    for input_file in filtered_files:
        input_path = os.path.join(args.directory, input_file)
        output_file = input_file.replace('.txt', '_Split.txt')
        output_path = os.path.join(args.directory, output_file)
        modify_script(input_path, output_path, closureShapes_path, closureShapesUncs_path, Normalization_path, year, args.region, args.nBins)
