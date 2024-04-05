import json
import matplotlib.pyplot as plt
import numpy as np

def process_entry(entry, scale):
    central_value = entry["fit"][1] * scale
    unc_down = abs(entry["fit"][1] - entry["fit"][0]) * scale
    unc_up = abs(entry["fit"][1] - entry["fit"][2]) * scale
    return central_value, unc_down, unc_up

def get_entries_by_name(json_data, name):
    return [param for param in json_data['params'] if param['name'] == name]

def plot_horizontal_line(ax, name, entries, scale, animal, pair_label, y_position, is_closure=False):
    central_values, unc_down_values, unc_up_values = zip(*[process_entry(entry, scale) for entry in entries])

    if is_closure:
        if animal == 'meow':
            ax.errorbar(central_values, y_position * np.ones_like(central_values), xerr=[unc_down_values, unc_up_values], fmt='o-', label=name, capsize=5, color='red')
        else:
            ax.errorbar(central_values, y_position * np.ones_like(central_values), xerr=[unc_down_values, unc_up_values], fmt='o-', label=name, capsize=5, color='blue')
    else:
        ax.errorbar(central_values, y_position * np.ones_like(central_values),
                    xerr=[unc_down_values, unc_up_values], fmt='o-', label=name, capsize=5)

    text_offset = 0.02  # Adjust this value for the desired offset
    if animal == 'meow':
        ax.text(central_values[0], y_position + text_offset, pair_label+' SRCR - Integrate 45', ha='right', va='bottom', color=ax.lines[-1].get_color(), fontsize=8)
    else:
        ax.text(central_values[0], y_position - text_offset, pair_label+' SRCR', ha='right', va='top', color=ax.lines[-1].get_color(), fontsize=8)


def main():
    with open('/eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats_Integrate45/ImpactsWithPurpose/SRCR_5_5/impactsd.json') as file1:
        data1 = json.load(file1)

    with open('/eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats/ImpactsWithPurpose/SRCR_5_5/impactsd.json') as file2:
        data2 = json.load(file2)

    names1 = set(entry['name'] for entry in data1['params'] if not (entry['name'].startswith('r') or entry['name'].startswith('prop')))
    names2 = set(entry['name'] for entry in data2['params'] if not (entry['name'].startswith('r') or entry['name'].startswith('prop')))

    common_names = names1.intersection(names2)

    # Separate closure names and other names
    closure_names = [name for name in common_names if name.startswith('closure')]
    other_names = [name for name in common_names if not name.startswith('closure')]

    # Sort closure names based on the ending number
    closure_names.sort(key=lambda x: int(x.split('_bin')[-1]))

    # Create a list of all names, grouped by 8
    all_names = closure_names + other_names
    grouped_names = [all_names[i:i+8] for i in range(0, len(all_names), 8)]

    for group_index, group in enumerate(grouped_names):
        # Set the figure size
        fig, ax = plt.subplots(figsize=(12, 8))

        for i, name in enumerate(group):
            entries1 = get_entries_by_name(data1, name)
            entries2 = get_entries_by_name(data2, name)

            y_position = i * 0.1  # Separate each pair by an equal y-amount
            is_closure = name.startswith('closure')
            plot_horizontal_line(ax, name, entries1, 1.0, 'meow', pair_label=name, y_position=y_position, is_closure=is_closure)
            plot_horizontal_line(ax, name, entries2, 1.0, 'woof', pair_label=name, y_position=y_position, is_closure=is_closure)

        ax.set_yticks([])  # Hide y-axis ticks
        plt.xlabel('Central Value')
        plt.title(f'Compare Pulls Between Nominal and Integrate45 (Group {group_index + 1})')
        plt.tight_layout()
        plt.savefig(f'Unblind/Integrate45/group_{group_index + 1}_pairs.png')
        plt.close()

if __name__ == "__main__":
    main()
