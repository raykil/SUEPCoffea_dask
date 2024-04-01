#!/usr/bin/env python
import os
import sys

conda_source  = "/afs/cern.ch/user/%s/%s/miniconda3/etc/profile.d/conda.sh"%(os.getlogin()[0], os.getlogin())
doSingularity = False 
print()
print('START')
print()
########   YOU ONLY NEED TO FILL THE AREA BELOW   #########
########   customization  area #########
NumberOfJobs= int(sys.argv[1]) # number of jobs to be submitted
FileFolder  = sys.argv[2]      # File folder with all the files
OutputDir   = sys.argv[3]      # Where to put the stuff
queue       = sys.argv[4]      # Which queue to use: expresso (20min), microcentury (1h), longlunch (2h), workday (8h), tomorrow (1d), testmatch (3d), nextweek (1w)
doSubmit    = (sys.argv[5] != "0")     # Whether to submit or not
analyzer    = sys.argv[6]
era         = int(sys.argv[7])
isData      = bool(int(sys.argv[8]))
interval    = int(sys.argv[9])
doSRonly    = bool(int(sys.argv[10]))
filt = None
isDY = False
resubmission = False
doSubmit = True
if len(sys.argv) > 11:
  filt = sys.argv[11]
if len(sys.argv) > 12:
  if int(sys.argv[12])==1:  
    isDY = True
#files = [FileFolder + "/" + f for f in os.listdir(FileFolder)] # list with all the files  
#newfiles = []
#for f in files:
#  if ".json" in f or (f=="skims.root"): continue
#  newfiles.append(f)
#files = newfiles

'''
if filt:
  newfiles = []
  for f in files:
    if filt in f: newfiles.append(f)
  print("Filtered files to %i/%i"%(len(newfiles), len(files)))
  files =  newfiles


if resubmission:
  import json 
  with open(FileFolder + "/tags.json", "r") as read:
    tags = json.load(read)
  #print(tags)
  newfiles = []
  for iff, f in enumerate(files):
    #print(f)
    if not("root" in f) or ("skims.root" in f): continue
    testout = "out_%s.hdf5"%(tags[("/".join(f.split("/")[-3:])).replace("//","/")])
    if not(os.path.isfile(OutputDir +"/" + testout)):
      newfiles.append(f)
    elif doSubmit != 0:
      print("File %s already exists, won't resubmit"%(OutputDir +"/" + testout))
  files = newfiles
  print("%i files will be ran"%(len(files)))
'''
tag=OutputDir

########   customization end   #########

path = os.getcwd()
print()
print('do not worry about folder creation:')
os.system("mkdir %s" %OutputDir)
os.system("rm %s/tmp/*"%tag)
os.system("rm %s/exec/*"%tag)
os.system("rm %s/batchlogs/*"%tag)
if not os.path.isdir("%s/tmp"%tag): os.system("mkdir %s/tmp"%tag)
if not os.path.isdir("%s/exec"%tag): os.system("mkdir %s/exec"%tag)
print()
print(era)
if era == 2018:
  files = ["/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunA2018_501.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunA2018_1172.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunB2018_304.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunA2018_261.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunA2018_845.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunA2018_239.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunD2018_3754.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunC2018_987.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunD2018_722.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunD2018_508.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunD2018_371.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunD2018_524.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunB2018_436.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunD2018_96.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunD2018_3806.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunB2018_378.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunC2018_124.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunC2018_81.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunD2018_764.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunB2018_160.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunB2018_204.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunA2018_1610.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunC2018_624.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunA2018_331.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunD2018_706.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunA2018_1786.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunD2018_2021.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/SingleMu_RunD2018_76.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunA2018_627.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunD2018_3260.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunA2018_1904.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunA2018_264.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunA2018_187.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunA2018_58.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunD2018_432.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunB2018_179.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunD2018_634.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunA2018_234.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunA2018_280.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunC2018_863.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunA2018_1855.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunD2018_238.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/SingleMu_RunA2018_493.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunC2018_172.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunA2018_67.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunD2018_3674.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunD2018_258.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunD2018_368.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunD2018_765.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunC2018_68.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunA2018_40.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunB2018_29.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunD2018_658.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/SingleMu_RunD2018_991.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunD2018_216.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunD2018_983.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunD2018_3527.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunD2018_3280.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunD2018_653.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunD2018_379.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunD2018_279.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunD2018_3183.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunA2018_238.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunA2018_230.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunA2018_308.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunD2018_245.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunA2018_2313.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunC2018_65.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunD2018_694.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunC2018_980.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunB2018_152.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunA2018_373.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunA2018_2108.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunD2018_4216.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunD2018_92.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunD2018_4140.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunC2018_538.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/SingleMu_RunD2018_1737.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunD2018_791.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunD2018_692.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunB2018_212.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunD2018_372.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunD2018_2005.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunC2018_522.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/EGamma_RunD2018_169.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunD2018_840.root",
  "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/DoubleMu_RunD2018_295.root",] # 2018 Excess

elif era == 2017:
  files = ["/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_E/DoubleMuon_E_81.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_E/DoubleMuon_E_110.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_E/DoubleMuon_E_376.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_E/DoubleMuon_E_464.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_F/DoubleMuon_F_18.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_E/DoubleEG_E_188.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_E/DoubleMuon_E_302.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_C/DoubleMuon_C_209.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_F/DoubleMuon_F_897.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_B/DoubleEG_B_402.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_F/DoubleMuon_F_222.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_C/DoubleMuon_C_124.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_E/DoubleEG_E_279.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_E/DoubleMuon_E_586.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_C/DoubleMuon_C_281.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_F/DoubleMuon_F_833.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_B/DoubleEG_B_187.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/SingleMuon_F/SingleMuon_F_2305.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_E/DoubleEG_E_76.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_F/DoubleMuon_F_532.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_C/DoubleMuon_C_338.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/SingleElectron_E/SingleElectron_E_1145.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_F/DoubleMuon_F_467.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/SingleElectron_F/SingleElectron_F_300.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_F/DoubleMuon_F_367.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/SingleElectron_C/SingleElectron_C_161.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_E/DoubleMuon_E_367.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/SingleMuon_B/SingleMuon_B_830.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_E/DoubleEG_E_338.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_C/DoubleMuon_C_368.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_E/DoubleMuon_E_412.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_C/DoubleMuon_C_434.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_C/DoubleEG_C_445.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_E/DoubleMuon_E_500.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_C/DoubleEG_C_412.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_D/DoubleEG_D_131.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_C/DoubleEG_C_209.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_F/DoubleMuon_F_265.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_F/DoubleMuon_F_819.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_E/DoubleMuon_E_129.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_C/DoubleMuon_C_136.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_E/DoubleEG_E_29.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_B/DoubleEG_B_525.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_E/DoubleMuon_E_204.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_C/DoubleEG_C_638.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_C/DoubleMuon_C_61.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/SingleMuon_C/SingleMuon_C_597.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_F/DoubleMuon_F_243.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_C/DoubleMuon_C_384.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_E/DoubleMuon_E_287.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_E/DoubleMuon_E_57.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_D/DoubleEG_D_125.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_C/DoubleEG_C_394.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_C/DoubleMuon_C_32.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_C/DoubleEG_C_470.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_E/DoubleEG_E_382.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_C/DoubleMuon_C_113.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_D/DoubleEG_D_113.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_C/DoubleMuon_C_80.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/SingleElectron_D/SingleElectron_D_485.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_E/DoubleMuon_E_229.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_B/DoubleMuon_B_72.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_C/DoubleEG_C_410.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_B/DoubleMuon_B_101.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_D/DoubleMuon_D_47.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_C/DoubleEG_C_276.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/SingleMuon_E/SingleMuon_E_1019.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_C/DoubleMuon_C_203.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_C/DoubleEG_C_316.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_D/DoubleEG_D_56.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_C/DoubleMuon_C_11.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_B/DoubleEG_B_329.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_F/DoubleMuon_F_942.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_D/DoubleMuon_D_132.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_B/DoubleMuon_B_21.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_F/DoubleEG_F_1061.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_C/DoubleMuon_C_71.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_C/DoubleEG_C_422.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_C/DoubleEG_C_337.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_D/DoubleMuon_D_42.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_E/DoubleMuon_E_538.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_F/DoubleEG_F_349.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_F/DoubleEG_F_702.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_F/DoubleEG_F_504.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_F/DoubleMuon_F_218.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_F/DoubleMuon_F_951.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_B/DoubleEG_B_229.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_F/DoubleMuon_F_995.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_F/DoubleEG_F_744.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_F/DoubleMuon_F_530.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_F/DoubleMuon_F_279.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_F/DoubleMuon_F_1046.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/SingleElectron_F/SingleElectron_F_725.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_C/DoubleEG_C_474.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_C/DoubleMuon_C_75.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleEG_C/DoubleEG_C_526.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DoubleMuon_D/DoubleMuon_D_144.root"]

elif era == 2016:
  files = ["/eos/cms/store/group/phys_exotica/SUEPs/UL16/skim_2l_20_10/DoubleEG_G/DoubleEG_G_41.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16/skim_2l_20_10/DoubleEG_H/DoubleEG_H_880.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16/skim_2l_20_10/DoubleEG_G/DoubleEG_G_492.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16/skim_2l_20_10/DoubleEG_G/DoubleEG_G_558.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16/skim_2l_20_10/DoubleMuon_H/DoubleMuon_H_403.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16/skim_2l_20_10/DoubleMuon_G/DoubleMuon_G_81.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16/skim_2l_20_10/DoubleMuon_H/DoubleMuon_H_243.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16/skim_2l_20_10/DoubleEG_H/DoubleEG_H_478.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16/skim_2l_20_10/DoubleEG_H/DoubleEG_H_621.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16/skim_2l_20_10/DoubleMuon_H/DoubleMuon_H_314.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16/skim_2l_20_10/SingleMuon_H/SingleMuon_H_56.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16/skim_2l_20_10/DoubleMuon_G/DoubleMuon_G_25.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16/skim_2l_20_10/SingleMuon_G/SingleMuon_G_301.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16/skim_2l_20_10/DoubleMuon_G/DoubleMuon_G_280.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16/skim_2l_20_10/DoubleMuon_G/DoubleMuon_G_191.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16/skim_2l_20_10/DoubleMuon_G/DoubleMuon_G_157.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16/skim_2l_20_10/DoubleMuon_G/DoubleMuon_G_371.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16/skim_2l_20_10/DoubleEG_G/DoubleEG_G_73.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16/skim_2l_20_10/DoubleEG_H/DoubleEG_H_556.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16/skim_2l_20_10/DoubleMuon_H/DoubleMuon_H_219.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16/skim_2l_20_10/DoubleMuon_G/DoubleMuon_G_21.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16/skim_2l_20_10/DoubleEG_H/DoubleEG_H_834.root"]

elif era == 2015:
  files = ["/eos/cms/store/group/phys_exotica/SUEPs/UL16APV/skim_2l_20_10/DoubleMuon_F/DoubleMuon_F_124.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16APV/skim_2l_20_10/DoubleEG_B2/DoubleEG_B2_20.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16APV/skim_2l_20_10/DoubleEG_E/DoubleEG_E_253.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16APV/skim_2l_20_10/DoubleEG_B2/DoubleEG_B2_682.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16APV/skim_2l_20_10/DoubleMuon_C/DoubleMuon_C_110.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16APV/skim_2l_20_10/SingleMuon_B2/SingleMuon_B2_521.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16APV/skim_2l_20_10/DoubleEG_B2/DoubleEG_B2_916.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16APV/skim_2l_20_10/DoubleMuon_F/DoubleMuon_F_29.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16APV/skim_2l_20_10/DoubleEG_F/DoubleEG_F_281.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16APV/skim_2l_20_10/DoubleMuon_B2/DoubleMuon_B2_450.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16APV/skim_2l_20_10/DoubleEG_E/DoubleEG_E_145.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16APV/skim_2l_20_10/DoubleEG_C/DoubleEG_C_406.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16APV/skim_2l_20_10/DoubleEG_C/DoubleEG_C_29.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16APV/skim_2l_20_10/SingleMuon_C/SingleMuon_C_160.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16APV/skim_2l_20_10/DoubleMuon_D/DoubleMuon_D_237.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16APV/skim_2l_20_10/DoubleEG_B2/DoubleEG_B2_414.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16APV/skim_2l_20_10/DoubleEG_D/DoubleEG_D_112.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16APV/skim_2l_20_10/DoubleEG_B2/DoubleEG_B2_356.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16APV/skim_2l_20_10/DoubleMuon_D/DoubleMuon_D_53.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16APV/skim_2l_20_10/DoubleEG_B2/DoubleEG_B2_531.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16APV/skim_2l_20_10/DoubleMuon_B2/DoubleMuon_B2_243.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16APV/skim_2l_20_10/DoubleEG_D/DoubleEG_D_228.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16APV/skim_2l_20_10/DoubleMuon_D/DoubleMuon_D_115.root", 
  "/eos/cms/store/group/phys_exotica/SUEPs/UL16APV/skim_2l_20_10/DoubleMuon_B2/DoubleMuon_B2_335.root"]

print(files)
if NumberOfJobs == -1: NumberOfJobs = len(files)

##### loop for creating and sending jobs #####
ifile = 0
ijob  = 1
while ifile < NumberOfJobs:
    print(ifile)
    ##### creates jobs #######
    with open('%s/exec/job_'%tag+str(ijob)+'.sh', 'w') as fout:
        fout.write("#!/bin/bash\n")
        fout.write("echo 'START---------------'\n")
        fout.write("echo 'WORKDIR ' ${PWD}\n")
        fout.write("cd "+str(path)+"\n")
        if not(doSingularity): # If you are not running on singularity, need to load the coffea environment
          fout.write("source %s\n\n"%conda_source)
          fout.write("conda activate coffea\n")
          fout.write("export HOME=\"/afs/cern.ch/user/g/gdecastr\"\n")
        for i in range(interval):
          if ifile == NumberOfJobs: continue # Last one will have less
          fout.write("python condor_SUEP_WS.py  --isMC=%i --era=%s --dataset=%s --analyzer=%s --infile=%s --outputdir=%s %s %s\n"%(0 if isData else 1, era, "DATA", analyzer, files[ifile], OutputDir, "--isDY" if isDY else "", "--SR" if doSRonly else "")) 
          print(files[ifile])
          ifile += 1

        fout.write("echo 'STOP---------------'\n")
        fout.write("echo\n")
        fout.write("echo\n")

    os.system("chmod 755 %s/exec/job_"%tag+str(ijob)+".sh")
    ijob += 1

###### create submit.sub file ####
    
if not os.path.isdir("%s/batchlogs"%tag): os.mkdir("%s/batchlogs"%tag)
with open('submit.sub', 'w') as fout:
    fout.write("executable              = $(filename)\n")
    fout.write("arguments               = $(Proxy_path) $(ClusterId)$(ProcId)\n")
    fout.write("output                  = %s/batchlogs/$(ClusterId).$(ProcId).out\n"%tag)
    fout.write("error                   = %s/batchlogs/$(ClusterId).$(ProcId).err\n"%tag)
    fout.write("log                     = %s/batchlogs/$(ClusterId).log\n"%tag)
    if doSingularity: fout.write("+SingularityImage       = \"/cvmfs/unpacked.cern.ch/registry.hub.docker.com/coffeateam/coffea-dask:latest\"\n")
    fout.write('+JobFlavour = "%s"\n' %(queue))
    fout.write("\n")
    fout.write("queue filename matching (%s/exec/job_*sh)\n"%tag)
    
###### sends bjobs ######
if int(doSubmit) > 0 and NumberOfJobs > 0:
  os.system("echo submit.sub")
  os.system("condor_submit -spool submit.sub")
   
print()
print("your jobs:")
#os.system("condor_q")
print()
print('END')
print()
