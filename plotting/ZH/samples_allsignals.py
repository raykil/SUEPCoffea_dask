import os
import ROOT
from auxiliars import *
import copy

def hdf5inpath(path):
  ret = []
  for p in os.listdir(path):
    if not ("SUEP" in p): continue
    ppath = path + "/" + p
    for f in os.listdir(ppath):
      if "hdf5" in f: 
        ret.append(ppath + "/" + f)
  return ret

# Main path where samples are stored
samples = {
  "Inclusive": {
         "name"     : "Inclusive", #Here plain text
         "label"    : "Inclusive", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kGray,
         "fillcolor": ROOT.kGray,
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/testPU16/")+hdf5inpath("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/testPU16APV/")+hdf5inpath("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/testPU17/")+hdf5inpath("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/testPU18/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*x["TrigSF"]*x["LepSF"],
  },
  "PUg60": {
         "name"     : "PUg60", #Here plain text
         "label"    : "<PU> #geq 60", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb 
         "linecolor": ROOT.kBlack,
         "fillcolor": ROOT.kBlack,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/testPU16/")+hdf5inpath("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/testPU16APV/")+hdf5inpath("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/testPU17/")+hdf5inpath("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/testPU18/"),
         "extraWeights": lambda x: (x["nTrueInt"] >= 60)*x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*x["TrigSF"]*x["LepSF"],
  },
  "PU40to60": {
         "name"     : "PU40to60", #Here plain text
         "label"    : "40 #geq <PU> < 60", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb 
         "linecolor": ROOT.kViolet,
         "fillcolor": ROOT.kViolet,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/testPU16/")+hdf5inpath("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/testPU16APV/")+hdf5inpath("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/testPU17/")+hdf5inpath("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/testPU18/"),
         "extraWeights": lambda x: (x["nTrueInt"] >= 40)*(x["nTrueInt"] < 60)*x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*x["TrigSF"]*x["LepSF"],
  },
  "PU30to40": {
         "name"     : "PU30to40", #Here plain text
         "label"    : "30 #geq <PU> < 40", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb 
         "linecolor": ROOT.kBlue,
         "fillcolor": ROOT.kBlue,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/testPU16/")+hdf5inpath("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/testPU16APV/")+hdf5inpath("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/testPU17/")+hdf5inpath("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/testPU18/"),
         "extraWeights": lambda x: (x["nTrueInt"] >= 30)*(x["nTrueInt"] < 40)*x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*x["TrigSF"]*x["LepSF"],
  },
  "PU20to30": {
         "name"     : "PU20to30", #Here plain text
         "label"    : "20 #geq <PU> < 30", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb 
         "linecolor": ROOT.kGreen,
         "fillcolor": ROOT.kGreen,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/testPU16/")+hdf5inpath("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/testPU16APV/")+hdf5inpath("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/testPU17/")+hdf5inpath("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/testPU18/"),
         "extraWeights": lambda x: (x["nTrueInt"] >= 20)*(x["nTrueInt"] < 30)*x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*x["TrigSF"]*x["LepSF"],
  },
  "PU10to20": {
         "name"     : "PU10to20", #Here plain text
         "label"    : "10 #geq <PU> < 20", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb 
         "linecolor": ROOT.kOrange,
         "fillcolor": ROOT.kOrange,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/testPU16/")+hdf5inpath("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/testPU16APV/")+hdf5inpath("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/testPU17/")+hdf5inpath("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/testPU18/"),
         "extraWeights": lambda x: (x["nTrueInt"] >= 10)*(x["nTrueInt"] < 20)*x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*x["TrigSF"]*x["LepSF"],
  },
  "PU0to10": {
         "name"     : "PU0to10", #Here plain text
         "label"    : "0 #geq <PU> < 10", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb 
         "linecolor": ROOT.kRed,
         "fillcolor": ROOT.kRed,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/testPU16/")+hdf5inpath("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/testPU16APV/")+hdf5inpath("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/testPU17/")+hdf5inpath("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/testPU18/"),
         "extraWeights": lambda x: (x["nTrueInt"] >= 0)*(x["nTrueInt"] < 10)*x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*x["TrigSF"]*x["LepSF"],
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

