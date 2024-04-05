import uproot
import matplotlib.pyplot as plt
import numpy as np

def plot_likelihood_scan(root_filename, color, label):
    root_file = uproot.open(root_filename)
    tree = root_file["limit;1"]
    nll_values = tree["deltaNLL"].array()
    r_values = tree["r"].array()
    plt.scatter(r_values, 2*nll_values, marker='.', c=color, label=label)

plt.figure(figsize=(8, 6))

plot_likelihood_scan("/eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/Integrate45/2018/higgsCombineLLScan_4_6_Split.MultiDimFit.mH120.root", 'b', 'CRDY 2018 mD4 T6')
#plot_likelihood_scan("/eos/user/g/gdecastr/SUEPCoffea_dask/Cards/PUQuad2/Combined/higgsCombineHadronic_3_3_NLLScan.MultiDimFit.mH120.root", 'g', r'$22 < PU \leq 29$')
#plot_likelihood_scan("/eos/user/g/gdecastr/SUEPCoffea_dask/Cards/PUQuad3/Combined/higgsCombineHadronic_3_3_NLLScan.MultiDimFit.mH120.root", 'r', r'$29 < PU \leq 37$')
#plot_likelihood_scan("/eos/user/g/gdecastr/SUEPCoffea_dask/Cards/PUQuad4/Combined/higgsCombineHadronic_3_3_NLLScan_v2.MultiDimFit.mH120.69.root", 'c', r'$37 < PU$')
#plot_likelihood_scan("/eos/user/g/gdecastr/SUEPCoffea_dask/Cards/PUQuad4/Combined/higgsCombineHadronic_3_3_NLLScan_freezeTrack.MultiDimFit.mH120.1283363224.root", 'c', r'$37 < PU$')
#plot_likelihood_scan("/eos/user/g/gdecastr/SUEPCoffea_dask/Cards/DefaultAnalysis/RunII/higgsCombineHadronic_3_3_NLLScan.MultiDimFit.mH120.root", 'orange', r'Inclusive PU')

plt.xlabel('r')
plt.ylabel(r'2$\times$ $\Delta$NLL')
plt.title(r'2D Plot of $\Delta$NLL vs r')
plt.grid(True)
plt.legend()
#plt.axhline(y=1, color='k', linestyle='--', label='y=1')
#plt.axhline(y=4, color='k', linestyle='--', label='y=4')
plt.ylim(-10, 10)
plt.xlim(-500, 500)

#plt.savefig('LikelihoodScan_Overlay.png')
plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/Integrate45/LLScan_Fit_CRDY_4_6_2018_Split.png')
plt.show()
