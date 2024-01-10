import os
import ROOT
from auxiliars import *
import copy

def hdf5inpath(path):
  ret = []
  for f in os.listdir(path):
    if "hdf5" in f: 
      ret.append(path + "/" + f)
  return ret

# Main path where samples are stored
main_path = "/eos/cms/store/group/phys_exotica/SUEPs/ZH_HDF5s/2018/"
main_path_signal = "/eos/cms/store/group/phys_exotica/SUEPs/ZH_HDF5s/2018/"
samples = {
  "data": {
         "name" : "data",
         "label": "Data",
         "xsec" : -1,
         "lineColor": ROOT.kBlack,
         "fillcolor": ROOT.kBlack,
         "isSig"    : False,
         "files"    : hdf5inpath(main_path + "data/"),#+ hdf5inpath(main_path + "data_RunB/")+hdf5inpath(main_path + "data_RunC/")+hdf5inpath(main_path + "data_RunD/"),
         "markerstyle": 20,
         "markersize" : 1,
  },
  "SUEP_hadronic_mS125_mD3.00_T3.00": {
         "name"     : "SUEP_hadronic_mS125_mD3.00_T3.00", #Here plain text
         "label"    : "ZS, hadronic, T=3, m_{\phi}=3 GeV", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 3, # in fb
         "linecolor": ROOT.kBlue,
         "fillcolor": ROOT.kBlue,
         "isSig"    : True,
         "doPlot"   : True,
         "files"    : hdf5inpath(main_path_signal+"SUEP_hadronic_mS125_mD3.00_T3.00/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*x["TrigSF"]*x["LepSF"],
  },
#  "ttH_generic_mS125_mD2.00_T2.00" :{
#         "name"     : "ttH_generic_mS125_mD2.00_T2.00", #Here plain text
#         "label"    : "ttS, m_{S} = 125 GeV", #Here we can use weird glyphs
#         "xsec"     : 498.7, # in fb
#         "linecolor": ROOT.kBlack,
#         "fillcolor": ROOT.kBlack,
#         "isSig"    : True,
#         "doPlot"   : False,
#         "files"    : ["/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/test_ttH_unskimmed/out_1_1_1001.hdf5"], 
#         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*x["TrigSF"]*x["LepSF"],
#  }
}

for sample in samples:
  if "data" in sample: continue
  #if not(samples[sample]["isSig"]): 
  #  samples[sample]["variations"] = {}
  #  continue

  samples[sample]["variations"] = {
  "TrigSFUp": {
           "name"            :   "TrigSFUp",
           "isSyst"          :       True,
           "replaceChannel"  :         {},
           "extraWeights"    :   lambda x: (x["TrigSF"]+x["TrigSF_Up"])/x["TrigSF"], # Relative to central
           "symmetrize"      :      False, 
  },
  "TrigSFDn": {
           "name"            :   "TrigSFDn",
           "isSyst"          :       True,
           "replaceChannel"  :         {},
           "extraWeights"    :   lambda x: (x["TrigSF"]-x["TrigSF_Dn"])/x["TrigSF"], # Relative to central
           "symmetrize"      :      False,
  },
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

  if (samples[sample]["isSig"]): 
    samples[sample]["variations"]["JESUp"] = {
           "name"            : "JES",
           "isSyst"          :      True,
           "replaceChannel"  :  {"SR":"SR_JECUP", "onecluster":"onecluster_JECUP", "twoleptons":"twoleptons_JECUP"},
           "extraWeights"    :  lambda x, sample=sample: samples[sample]["extraWeights"](x),
           "symmetrize"      :      False,
    }
    samples[sample]["variations"]["JESDn"] = {
           "name"            : "JES",
           "isSyst"          :      True,
           "replaceChannel"  :  {"SR":"SR_JECDOWN", "onecluster":"onecluster_JECDOWN", "twoleptons":"twoleptons_JECDOWN"},
           "extraWeights"    :  lambda x, sample=sample: samples[sample]["extraWeights"](x),
           "symmetrize"      :      False,
    }
    samples[sample]["variations"]["JERUp"] = {
           "name"            : "JER",
           "isSyst"          :      True,
           "replaceChannel"  :  {"SR":"SR_JERUP", "onecluster":"onecluster_JERUP", "twoleptons":"twoleptons_JERUP"},
           "extraWeights"    :  lambda x, sample=sample: samples[sample]["extraWeights"](x),
           "symmetrize"      :      False,
    }
    samples[sample]["variations"]["JERDn"] = {
           "name"            : "JER",
           "isSyst"          :      True,
           "replaceChannel"  :  {"SR":"SR_JERDOWN", "onecluster":"onecluster_JERDOWN", "twoleptons":"twoleptons_JERDOWN"},
           "extraWeights"    :  lambda x, sample=sample: samples[sample]["extraWeights"](x),
           "symmetrize"      :      False,
    }