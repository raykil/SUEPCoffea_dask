import os


def checkFile(fi):
  #print("--->", fi)
  if os.path.isfile(fi):
    #print(fi,os.path.getsize(fi))
    if os.path.getsize(fi) > 6500: 
      return True
  return False

iJ = 0
allFiles = os.listdir("RunII")

for f in os.listdir("RunII"):
  if not("CombinedCRTT" in f): continue
  if not("txt" in f): continue
  if "0Sig" in f or "Scaled" in f or "Closure" in f or "SRCR" in f: continue
  if "higgsCombine" in f: continue
  print(f)
  froot = f.replace(".txt","")
  if checkFile("RunII/higgsCombine%s.Significance.mH120.root"%froot): continue #and checkFile("RunII/higgsCombine%s.Significance.mH120.root"%froot) and checkFile("RunII/higgsCombine%s.FitDiagnostics.mH120.root"%froot): continue
  print("Pass")
  iJ += 1
  fil = open("exec/job_%i.sh"%iJ, "w")
  fil.write("#!/bin/csh\n")
  fil.write("cd /eos/user/g/gdecastr/CMSSW_11_3_4/src/\n")
  fil.write("source /cvmfs/cms.cern.ch/cmsset_default.csh\n")
  fil.write("cmsenv\n")
  fil.write("cd /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/Default/RunII/\n")
  fil.write("limit stacksize unlimited\n")
  fil.write("text2workspace.py %s\n"%(f))
  #if not checkFile("RunII/higgsCombine%s.AsymptoticLimits.mH120.root"%f): fil.write("combine -M AsymptoticLimits %s -n %s\n"%(f.replace("txt","root"), f.replace(".txt","")))
  if not checkFile("RunII/higgsCombine%s.Significance.mH120.root"%f):     fil.write("combine -M Significance %s -n %s\n"%(f.replace("txt","root"), f.replace(".txt",""))) 
  #if not checkFile("RunII/higgsCombine%s.FitDiagnostics.mH120.root"%f):   fil.write("combine -M FitDiagnostics --rMin -100 --rMax 400 %s -n %s\n"%(f.replace("txt","root"), f.replace(".txt","")))
