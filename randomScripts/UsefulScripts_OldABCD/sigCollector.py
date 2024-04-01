import os, sys
import ROOT

def getLimits(f, ty):
    rF   = ROOT.TFile(f, "READ")
    tree = rF.Get("limit")   
    lims = [str(999.)]*6 
    if ty == "UL":
        if tree.GetEntries() > 1: #We have the five limits
            lims = []
            for ev in tree:
                lims.append(str(ev.limit))       
        elif tree.GetEntries() == 1: #No UL found
            for ev in tree:
                lims = [str(ev.limit)]*6
    if ty == "SIG":
        for ev in tree:
            lims = ev.limit
    return lims

limList = {"generic":open("generic_sig.txt","w"), "hadronic":open("hadronic_sig.txt","w"),"leptonic":open("leptonic_sig.txt","w")}

for k in limList:
    limList[k].write("# mS : mD : T : significance \n")
for fil in os.listdir("./"):
    if not("higgs" in fil): continue
    if not("Significance" in fil): continue
    print(fil)
    higgs, SUEP, mode, mass, mDark, T = fil.split("_")
    mass = mass.replace("mS","")
    mDark = mDark.replace("mD", "")
    T = ".".join(T.split(".")[0:2]).replace("T", "")
    limList[mode].write("%s : %s : %s : %s\n"%(mass, mDark, T ,getLimits(fil, "SIG")))
