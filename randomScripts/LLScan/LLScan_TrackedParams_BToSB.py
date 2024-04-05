import uproot
import matplotlib.pyplot as plt
import numpy as np

def find_tracked_params(tree):
    tracked_param_branches = []
    branch_names = tree.keys()
    for branch_name in branch_names:
        if branch_name.decode().startswith('trackedParam_'):
            tracked_param_branches.append(branch_name.decode())
    return tracked_param_branches

def get_entries_by_name(tree, name):
    return tree[name].array()

def plot_horizontal_lines(ax, name, values_b_only, values_s_plus_b, y_position):
    ax.plot(values_b_only, y_position * np.ones_like(values_b_only), 'o-', color='blue')
    ax.plot(values_s_plus_b, y_position * np.ones_like(values_s_plus_b), 'o-', color='red')
    ax.text(values_b_only[0], y_position - 0.1, name.replace("trackedParam_", ""), ha='right', va='center', color='black', fontsize=8)

def plot_likelihood_scan(root_filename1, root_filename2):
    root_file1 = uproot.open(root_filename1)
    root_file2 = uproot.open(root_filename2)
    
    tree1 = root_file1["limit;1"]
    tree2 = root_file2["limit;1"]
    
    tracked_params1 = find_tracked_params(tree1)
    tracked_params2 = find_tracked_params(tree2)
    
    # Ensure that parameter names are shared between files
    assert set(tracked_params1) == set(tracked_params2), "Parameter names don't match between files"
    
    # Sort the parameter names for consistency
    tracked_params1.sort()
    tracked_params2.sort()
    
    num_params = len(tracked_params1)
    num_plots = num_params // 10 + (num_params % 10 > 0)  # Calculate the number of plots needed
    
    for plot_index in range(num_plots):
        start_param_index = plot_index * 10
        end_param_index = min((plot_index + 1) * 10, num_params)
        
        fig, axs = plt.subplots(figsize=(12, 3))
        
        for param_index in range(start_param_index, end_param_index):
            param_name = tracked_params1[param_index]
            
            values_b_only = get_entries_by_name(tree1, param_name)
            values_s_plus_b = get_entries_by_name(tree2, param_name)
            
            y_position = param_index - start_param_index
            plot_horizontal_lines(axs, param_name, values_b_only, values_s_plus_b, y_position)
        
        axs.set_yticks([])  # Hide y-axis ticks
        plt.xlabel('Parameter Value')
        plt.title(f'Comparison of Parameters {start_param_index + 1} to {end_param_index}')
        plt.tight_layout()
        plt.savefig(f'/eos/user/g/gdecastr/www/BToSBComparison/comparison_plot_{plot_index}.png')
        plt.close()

plot_likelihood_scan(
    "/eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/Integrate45/2018/higgsCombinemD4.00_T6.00_r0.MultiDimFit.mH120.root",
    "/eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/Integrate45/2018/higgsCombinemD4.00_T6.00_r216.854.MultiDimFit.mH120.root"
)
