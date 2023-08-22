import os
import ROOT
from auxiliars import *
import copy

def hdf5inpath(path1, path2):
  ret1 = []
  for p in os.listdir(path1):
    if not("SUEP" in p) or not("leptonic" in p): continue
    ppath = path1 + "/" + p
    for f in os.listdir(ppath):
      if "hdf5" in f: 
        ret1.append(p)
  ret2 = []
  for p in os.listdir(path2):
    if not("SUEP" in p) or  not("leptonic" in p): continue
    ppath = path2 + "/" + p
    for f in os.listdir(ppath):
      if "hdf5" in f and p in ret1:
        ret2.append(ppath + "/" + f)
  return ret2

# Main path where samples are stored
samples = {
  "SUEP_generic_mS125_mD2.00_T2.00": {
         "name"     : "SUEP_generic_mS125_mD2.00_T2.00", #Here plain text
         "label"    : "With TightLepVeto jets", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kBlue,
         "fillcolor": ROOT.kBlue,
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/testJetID16APV/","/eos/cms/store/group/phys_exotica/SUEPs/UL16APV/hdf5_ANv4/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*x["TrigSF"]*x["LepSF"],
  },
  "SUEP_generic_mS125_mD2.00_T2.00_withIP": {
         "name"     : "SUEP_generic_mS125_mD2.00_T2.00_withIP", #Here plain text
         "label"    : "With Tight jets", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kRed,
         "fillcolor": ROOT.kRed,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/cms/store/group/phys_exotica/SUEPs/UL16APV/hdf5_ANv4/", "/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/testJetID16APV/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*x["TrigSF"]*x["LepSF"],
  },
}

for sample in samples:
  if "data" in sample: continue
  if not(samples[sample]["isSig"]): 
    samples[sample]["variations"] = {}
    continue

  samples[sample]["variations"] = {
  "ElSFUp": {
           "name"            :   "ElSFUp",
           "isSyst"          :       True,
           "replaceChannel"  :         {},
           "extraWeights"    :   lambda x: x["LepSF_ElUp"]/x["LepSF"], # Relative to central
           "symmetrize"      :      False,
  },
  "ElSFDn": {
           "name"            :   "ElSFDn",
           "isSyst"          :       True,
           "replaceChannel"  :         {},
           "extraWeights"    :   lambda x: x["LepSF_ElDn"]/x["LepSF"],
           "symmetrize"      :      False,
  },
  "MuSFUp": {
           "name"            :   "MuSFUp",
           "isSyst"          :       True,
           "replaceChannel"  :         {},
           "extraWeights"    :   lambda x: x["LepSF_MuUp"]/x["LepSF"],
           "symmetrize"      :      False,
  },
  "MuSFDn": {
           "name"            :   "MuSFDn",
           "isSyst"          :       True,
           "replaceChannel"  :         {},
           "extraWeights"    :   lambda x: x["LepSF_MuDn"]/x["LepSF"],
           "symmetrize"      :      False,
  },
  "PUUp": {
           "name"            :   "PUUp",
           "isSyst"          :       True,
           "replaceChannel"  :         {},
           "extraWeights"    :   lambda x: x["PUWeight_Up"]/x["PUWeight"],
           "symmetrize"      :      False,
  },
  "PUDn": {
           "name"            :   "PUDn",
           "isSyst"          :       True,
           "replaceChannel"  :         {},
           "extraWeights"    :   lambda x: x["PUWeight_Dn"]/x["PUWeight"],
           "symmetrize"      :      False,
  },
  "L1Up": {
           "name"            :   "L1Up",
           "isSyst"          :       True,
           "replaceChannel"  :         {},
           "extraWeights"    :   lambda x: x["L1prefireWeight_Up"]/x["L1prefireWeight"],
           "symmetrize"      :      False,
  },
  "L1Dn": {
           "name"            :   "L1Dn",
           "isSyst"          :       True,
           "replaceChannel"  :         {},
           "extraWeights"    :   lambda x: x["L1prefireWeight_Dn"]/x["L1prefireWeight"],
           "symmetrize"      :      False,
  },
  "ISRUp": {
           "name"            :   "ISRUp",
           "isSyst"          :       True,
           "replaceChannel"  :         {},
           "extraWeights"    :   lambda x: x["ISRWeight_Up"],
           "symmetrize"      :      False,
  },
  "ISRDn": {
           "name"            :   "ISRDn",
           "isSyst"          :       True,
           "replaceChannel"  :         {},
           "extraWeights"    :   lambda x: x["ISRWeight_Dn"],
           "symmetrize"      :      False,
  },
  "FSRUp": {
           "name"            :   "FSRUp",
           "isSyst"          :       True,
           "replaceChannel"  :         {},
           "extraWeights"    :   lambda x: x["FSRWeight_Up"],
           "symmetrize"      :      False,
  },
  "FSRDn": {
           "name"            :   "FSRDn",
           "isSyst"          :       True,
           "replaceChannel"  :         {},
           "extraWeights"    :   lambda x: x["FSRWeight_Dn"],
           "symmetrize"      :      False,
  },
  "LFCorrUp": {
           "name"            :   "LFCorrUp",
           "isSyst"          :       True,
           "replaceChannel"  :         {},
           "extraWeights"    :   lambda x: x["bTagWeight_LFCorr_Up"]/x["bTagWeight"],
           "symmetrize"      :      False,
  },
  "LFCorrDn": {
           "name"            :   "LFCorrDn",
           "isSyst"          :       True,
           "replaceChannel"  :         {},
           "extraWeights"    :   lambda x: x["bTagWeight_LFCorr_Dn"]/x["bTagWeight"],
           "symmetrize"      :      False,
  },
  "HFCorrUp": {
           "name"            :   "HFCorrUp",
           "isSyst"          :       True,
           "replaceChannel"  :         {},
           "extraWeights"    :   lambda x: x["bTagWeight_HFCorr_Up"]/x["bTagWeight"],
           "symmetrize"      :      False,
  },
  "HFCorrDn": {
           "name"            :   "HFCorrDn",
           "isSyst"          :       True,
           "replaceChannel"  :         {},
           "extraWeights"    :   lambda x: x["bTagWeight_HFCorr_Dn"]/x["bTagWeight"],
           "symmetrize"      :      False,
  },
  "LFUnCorrUp": {
           "name"            :   "LFUnCorrUp",
           "isSyst"          :       True,
           "replaceChannel"  :         {},
           "extraWeights"    :   lambda x: x["bTagWeight_LFUnCorr_Up"]/x["bTagWeight"],
           "symmetrize"      :      False,
  },
  "LFUnCorrDn": {
           "name"            :   "LFUnCorrDn",
           "isSyst"          :       True,
           "replaceChannel"  :         {},
           "extraWeights"    :   lambda x: x["bTagWeight_LFUnCorr_Dn"]/x["bTagWeight"],
           "symmetrize"      :      False,
  },
  "HFUnCorrUp": {
           "name"            :   "HFUnCorrUp",
           "isSyst"          :       True,
           "replaceChannel"  :         {},
           "extraWeights"    :   lambda x: x["bTagWeight_HFUnCorr_Up"]/x["bTagWeight"],
           "symmetrize"      :      False,
  },
  "HFUnCorrDn": {
           "name"            :   "HFUnCorrDn",
           "isSyst"          :       True,
           "replaceChannel"  :         {},
           "extraWeights"    :   lambda x: x["bTagWeight_HFUnCorr_Dn"]/x["bTagWeight"],
           "symmetrize"      :      False,
  },
  "Track": {
           "name"            : "Track",
           "isSyst"          :      True,
           "replaceChannel"  :  {"SR":"SR_TRACKUP", "onecluster":"onecluster_TRACKUP", "twoleptons":"twoleptons_TRACKUP"},
           "extraWeights"    :  lambda x, sample=sample: samples[sample]["extraWeights"](x),
           "symmetrize"      :     True,
  },
}

