import os
import ROOT
from auxiliars import *
import copy

def hdf5inpath(path):
  ret = []
  for f in os.listdir(path):
    if "hdf5" in f and ".sys.v#" not in f: 
      ret.append(path + "/" + f)
  return ret

# Main path where samples are stored
samples = {  
  "GenericSignal_SFs": {
         "name"     : "GenericSignal_SFs", #Here plain text
         "label"    : "GenericSignal_SFs",# (p_{T} < 50 GeV)", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kBlue,
         "isSig"    : False,
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["TrigSF"]*SF(x,15),
         "files"    : hdf5inpath("/eos/user/g/gdecastr/SUEPCoffea_dask/testWorkflow/SUEP_Signal_m2T2_UL16APV/"),
  },
    "GenericSignal_SFs_UP": {
         "name"     : "GenericSignal_SFs_UP", #Here plain text
         "label"    : "GenericSignal_SFs_UP",# (p_{T} < 50 GeV)", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kGreen,
         "isSig"    : True,
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*(x["TrigSF"]+x["TrigSF_Up"])*SF(x,15),
         "files"    : hdf5inpath("/eos/user/g/gdecastr/SUEPCoffea_dask/testWorkflow/SUEP_Signal_m2T2_UL16APV/"),
  },
      "GenericSignal_SFs_DOWN": {
         "name"     : "GenericSignal_SFs_DOWN", #Here plain text
         "label"    : "GenericSignal_SFs_DOWN",# (p_{T} < 50 GeV)", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kRed,
         "isSig"    : True,
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*(x["TrigSF"]-x["TrigSF_Dn"])*SF(x,15),
         "files"    : hdf5inpath("/eos/user/g/gdecastr/SUEPCoffea_dask/testWorkflow/SUEP_Signal_m2T2_UL16APV/"),
  },
}


for sample in samples:
  if sample == "GenericSignal_SFs_UP" or sample == "GenericSignal_SFs_DOWN": 
    samples[sample]["variations"] = {}
    continue
  if "data" in sample: continue
  samples[sample]["variations"] = {
  "ElSFUp": {
           "name"            :   "ElSFUp",
           "isSyst"          :       True,
           "replaceChannel"  :         {},
           "extraWeights"    :   lambda x: SF(x,15, 2)/SF(x,15, 0), # Relative to central
           "symmetrize"      :      False,
  },
  "ElSFDn": {
           "name"            :   "ElSFDn",
           "isSyst"          :       True,
           "replaceChannel"  :         {},
           "extraWeights"    :   lambda x: SF(x,15, -2)/SF(x,15, 0),
           "symmetrize"      :      False,
  },
  "TrigSFUp": {
           "name"            :   "TrigSFUp",
           "isSyst"          :       True,
           "replaceChannel"  :         {},
           "extraWeights"    :   lambda x: (x["TrigSF"]+x["TrigSF_Up"])/(x["TrigSF"]), # Relative to central
           "symmetrize"      :      False,
  },
  "TrigSFDn": {
           "name"            :   "TrigSFDn",
           "isSyst"          :       True,
           "replaceChannel"  :         {},
           "extraWeights"    :   lambda x: (x["TrigSF"]-x["TrigSF_Dn"])/(x["TrigSF"]),
           "symmetrize"      :      False,
  },
  "MuSFUp": {
           "name"            :   "MuSFUp",
           "isSyst"          :       True,
           "replaceChannel"  :         {},
           "extraWeights"    :   lambda x: SF(x,15, 1)/SF(x,15, 0),
           "symmetrize"      :      False,
  },
  "MuSFDn": {
           "name"            :   "MuSFDn",
           "isSyst"          :       True,
           "replaceChannel"  :         {},
           "extraWeights"    :   lambda x: SF(x,15, -1)/SF(x,15, 0),
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

