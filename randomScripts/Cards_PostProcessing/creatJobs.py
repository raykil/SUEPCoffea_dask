import os
import argparse

parser = argparse.ArgumentParser(description='Creat Jobs')
parser.add_argument('Directory', type=str, help='The directory we are processing.')
parser.add_argument('Region', type=str, help='The region we are processing.')
parser.add_argument('--run-AsymptoticLimits', action='store_true', help='Enable running AsymptoticLimits command')
parser.add_argument('--run-FitDiagnostics', action='store_true', help='Enable running FitDiagnostics command')
parser.add_argument('--run-Significance', action='store_true', help='Enable running Significance command')
args = parser.parse_args()

def checkFile(fi):
    if os.path.isfile(fi) and os.path.getsize(fi) > 6500:
        return True
    return False

iJ = 0
allFiles = os.listdir("RunII")

for f in os.listdir("RunII"):
    if not("Combined"+args.Region in f) or not("txt" in f) or "higgsCombine" in f:
        continue
    print(f)
    froot = f.replace(".txt","")
    if checkFile(f"RunII/higgsCombine{froot}.Significance.mH120.root") and args.run_Significance:
        continue
    print("Pass")
    iJ += 1
    fil = open(f"exec/job_{iJ}.sh", "w")
    fil.write("#!/bin/csh\n")
    fil.write("cd /eos/user/g/gdecastr/CMSSW_11_3_4/src/\n")
    fil.write("source /cvmfs/cms.cern.ch/cmsset_default.csh\n")
    fil.write("cmsenv\n")
    fil.write(f"cd {args.Directory}/RunII/\n")
    fil.write("limit stacksize unlimited\n")
    fil.write(f"text2workspace.py {f}\n")

    if args.run_AsymptoticLimits and not checkFile(f"RunII/higgsCombine{froot}.AsymptoticLimits.mH120.root"):
        fil.write(f"combine -M AsymptoticLimits {f.replace('txt','root')} -n {f.replace('.txt','')}\n")

    if args.run_Significance and not checkFile(f"RunII/higgsCombine{froot}.Significance.mH120.root"):
        fil.write(f"combine -M Significance {f.replace('txt','root')} -n {f.replace('.txt','')}\n")

    if args.run_FitDiagnostics and not checkFile(f"RunII/higgsCombine{froot}.FitDiagnostics.mH120.root"):
        fil.write(f"combine -M FitDiagnostics --rMin -100 --rMax 400 {f.replace('txt','root')} -n {f.replace('.txt','')}\n")
