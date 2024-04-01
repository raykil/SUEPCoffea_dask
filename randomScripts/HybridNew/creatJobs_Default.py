import os
import re

def checkFile(fi):
  #print("--->", fi)
  if os.path.isfile(fi):
    #print(fi,os.path.getsize(fi))
    if os.path.getsize(fi) > 6500: 
      return True
  return False

iJ = 0
allFiles = os.listdir("/eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/ManualMC_Integrate45/RunII")

for f in os.listdir("/eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/ManualMC_Integrate45/RunII"):
  if not(f.startswith("Combined")): continue
  if not("txt" in f): continue
  #if ("Split" in f): continue
  if "0Sig" in f or "Scaled" in f or "Closure" in f or "SRCR" in f: continue
  if "higgsCombine" in f: continue
  print(f)
  froot = f.replace(".txt","")
  files = os.listdir('SigFiles')
  prefix = f'higgsCombine{froot}.HybridNew.mH120.'
  flag = False
  for j in files:
    if j.startswith(prefix):
        flag = True
  if flag:
    continue
  #if checkFile("SigFiles/higgsCombine%s.Significance.mH120.root"%froot): continue #and checkFile("RunII/higgsCombine%s.Significance.mH120.root"%froot) and checkFile("RunII/higgsCombine%s.FitDiagnostics.mH120.root"%froot): continue
  print("Pass")
  iJ += 1
  fil = open("exec/job_%i.sh"%iJ, "w")
  fil.write("#!/bin/sh\n")
  fil.write("ulimit -s unlimited\n")
  fil.write("cd /eos/user/g/gdecastr/CMSSW_11_3_4/src\n")
  fil.write("cmsenv\n")
  fil.write("cd /afs/cern.ch/user/g/gdecastr/HybridNew/ManualMC_Integrate45/Significances/SigFiles\n")
  #if not checkFile("RunII/higgsCombine%s.AsymptoticLimits.mH120.root"%f): fil.write("combine -M AsymptoticLimits %s -n %s\n"%(f.replace("txt","root"), f.replace(".txt","")))
  fil.write("combine --LHCmode LHC-significance --saveToys --fullBToys --saveHybridResult -T 2000 -M HybridNew -s -1 -d /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/ManualMC_Integrate45/RunII/%s -n %s\n"%(f, f.replace(".txt",""))) 
  #if not checkFile("RunII/higgsCombine%s.FitDiagnostics.mH120.root"%f):   fil.write("combine -M FitDiagnostics --rMin -100 --rMax 400 %s -n %s\n"%(f.replace("txt","root"), f.replace(".txt","")))
