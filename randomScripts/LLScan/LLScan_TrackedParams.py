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


def plot_likelihood_scan(root_filename):
    root_file = uproot.open(root_filename)
    tree = root_file["limit;1"]
    tracked_params = find_tracked_params(tree)
    for param in tracked_params:       
        param_values = tree[param].array()
        r_values = tree["r"].array()
    
        plt.figure(figsize=(8, 6))
        plt.xlabel('r')
        plt.ylabel('Post-fit Systematic Value')
        cleaned_param_branch = param.replace("trackedParam_", "").replace("SUEP_hadronic_mS125_mD4.00_T6.00", "")
        if 'r2018' in cleaned_param_branch:
            plt.ylim(np.mean(param_values)-3*np.sqrt(np.mean(param_values)), np.mean(param_values)+3*np.sqrt(np.mean(param_values)))
        else:
            plt.ylim(-3, 3)
        plt.title(f'{cleaned_param_branch}')
        plt.grid(True)
        plt.tight_layout()
        plt.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
        plt.gca().yaxis.get_major_formatter().set_powerlimits((0, 1))
        plt.scatter(r_values, param_values, marker='.', label=param)
        plt.savefig('/eos/user/g/gdecastr/www/Plots/PUQuad4_TrackedParams_freezeTrack/'+param+'.png')
        plt.clf()


plot_likelihood_scan("/eos/user/g/gdecastr/SUEPCoffea_dask/Cards/PUQuad4/Combined/higgsCombineHadronic_3_3_NLLScan_freezeTrack.MultiDimFit.mH120.1283363224.root")