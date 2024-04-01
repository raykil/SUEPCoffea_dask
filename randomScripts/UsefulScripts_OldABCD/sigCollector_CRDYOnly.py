import os
import ROOT
import numpy as np

def getLimits(f, ty):
    rF   = ROOT.TFile(f, "READ")
    tree = rF.Get("limit")   
    lims = [999.] * 6 
    if ty == "UL":
        if tree.GetEntries() > 1:  # We have the five limits
            lims = [ev.limit for ev in tree]
        elif tree.GetEntries() == 1:  # No UL found
            lims = [tree.limit] * 6
    elif ty == "SIG":
        lims = [ev.limit for ev in tree]
    return lims

limList = {"generic": open("generic_sig_SR.txt", "w"),
           "hadronic": open("hadronic_sig_CRDY.txt", "w"),
           "leptonic": open("leptonic_sig_SR.txt", "w")}

# Arrays to store significance values for computing mean and std
significance_values = {"generic": [], "hadronic": [], "leptonic": []}

for k in limList:
    limList[k].write("# mS : mD : T : significance \n")

for fil in os.listdir("./"):
    if not("higgsCombineCombinedCRDY_" in fil):
        continue
    if not("Significance" in fil):
        continue
    print(fil)
    higgs, SUEP, mode, mass, mDark, T = fil.split("_")
    mass = mass.replace("mS", "")
    mDark = mDark.replace("mD", "")
    T = ".".join(T.split(".")[0:2]).replace("T", "")
    
    significance_values[mode].extend(getLimits(fil, "SIG"))

    limList[mode].write("%s : %s : %s : %s\n" % (mass, mDark, T, getLimits(fil, "SIG")))

# Compute mean and std of significance
for mode in significance_values:
    if significance_values[mode]:
        mean_significance = np.mean(significance_values[mode])
        std_significance = np.std(significance_values[mode])
        print(f"Mean Significance ({mode}): {mean_significance}, Std Significance ({mode}): {std_significance}")
    else:
        print(f"No significance values found for mode {mode}")
