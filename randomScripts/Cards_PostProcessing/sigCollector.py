import os
import sys
import ROOT

def getLimits(f, ty):
    try:
        rF   = ROOT.TFile(f, "READ")
        tree = rF.Get("limit")   
        lims = [str(999.)]*6 
        if ty == "UL":
            if tree.GetEntries() > 1: # We have the five limits
                lims = []
                for ev in tree:
                    lims.append(str(ev.limit))       
            elif tree.GetEntries() == 1: # No UL found
                for ev in tree:
                    lims = [str(ev.limit)]*6
        if ty == "SIG":
            for ev in tree:
                lims = ev.limit
        return lims
    except:
        print(f"Error occurred while processing file: {f}")
        os.remove(f)
        return None

if len(sys.argv) != 3:
    print("Usage: python script.py MODE SPLIT")
    sys.exit(1)

mode = sys.argv[1]
if mode not in ["CRDY", "CRTT", "SR", "SRCR"]:
    print("Invalid mode. Mode should be one of: CRDY, CRTT, SR, SRCR")
    sys.exit(1)

split_arg = int(sys.argv[2])
if split_arg not in [0, 1]:
    print("Invalid value for SPLIT argument. Should be 0 or 1.")
    sys.exit(1)

split = bool(split_arg)

output_file = f"sig_{mode}"
if split:
    output_file += "_Split"
output_file += ".txt"

with open(output_file, "w") as f:
    f.write("# mS : mD : T : significance \n")

for fil in os.listdir("./"):
    if f"higgsCombineCombined{mode}_" in fil and not("HybridNew" in fil) and ("Split" in fil) == split:
        print(fil)
        higgs, SUEP, _, mass, mDark, T = fil.split("_")
        mass = mass.replace("mS","")
        mDark = mDark.replace("mD", "")
        T = ".".join(T.split(".")[0:2]).replace("T", "")
        limits = getLimits(fil, "SIG")
        if limits is not None:
            with open(output_file, "a") as f:
                f.write("%s : %s : %s : %s\n" % (mass, mDark, T, getLimits(fil, "SIG")))
