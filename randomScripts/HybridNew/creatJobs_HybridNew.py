import os
import re
import sys

def checkFile(fi):
    if os.path.isfile(fi):
        if os.path.getsize(fi) > 6500:
            return True
    return False

if len(sys.argv) < 3:
    print("Usage: python script.py <directory_path1> <directory_path2>")
    sys.exit(1)

directory_path1 = sys.argv[1]
directory_path2 = sys.argv[2]

iJ = 0
for f in os.listdir(directory_path1):
    if not f.startswith("Combined") or "txt" not in f:
        continue
    if any(substring in f for substring in ["0Sig", "Scaled", "Closure"]) or "higgsCombine" in f:
        continue
    print(f)
    froot = f.replace(".txt", "")
    files = os.listdir(directory_path2)
    prefix = f'higgsCombine{froot}.HybridNew.mH120.'
    flag = False
    for j in files:
        if j.startswith(prefix):
            flag = True
            break
    if flag:
        continue
    print("Pass")
    iJ += 1
    fil = open("exec/job_%i.sh" % iJ, "w")
    fil.write("#!/bin/sh\n")
    fil.write("ulimit -s unlimited\n")
    fil.write("cd /eos/user/g/gdecastr/CMSSW_11_3_4/src\n")
    fil.write("cmsenv\n")
    fil.write("cd " + directory_path2 + "\n")
    fil.write("combine --LHCmode LHC-significance --saveToys --fullBToys --saveHybridResult -T 2000 -M HybridNew -s -1 -d " + directory_path1 + "/%s -n %s\n" % (f, f.replace(".txt", "")))
