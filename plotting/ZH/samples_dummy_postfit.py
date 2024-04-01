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
main_path = "/eos/cms/store/group/phys_exotica/SUEPs/UL18/hdf5_ANv8/"
main_path_signal = "/eos/cms/store/user/gdecastr/HDF5s_NewSigs/2018/"
samples = {
  "data": {
         "name" : "data",
         "label": "Data",
         "xsec" : -1,
         "lineColor": ROOT.kBlack,
         "fillcolor": ROOT.kBlack,
         "isSig"    : False,
         "files"    : hdf5inpath(main_path + "ZG/"), # Just whatever so it reads quickly, we are not using it anywhere
         "markerstyle": 20,
         "markersize" : 1,
         "th1" : {"":"data_prefit","Up":"data_prefitUp","Dn":"data_prefitDn"},
  },
  "background": {
         "name"       : "background", #Here plain text
         "label"      : "Background (post-fit)",# (p_{T} = 0 GeV)", #Here we can use weird glyphs
         "xsec"       : 1., # in fb
         "linecolor"  : ROOT.kBlack,
         "fillcolor"  : ROOT.kWhite, # White
         "isSig"      : False,
         "extraWeights": lambda x: 1*(x["genZpt"]==0.0)*x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*x["TrigSF"]*x["LepSF"], 
         "files"      : hdf5inpath(main_path + "ZG/"), # Just whatever so it reads quickly, we are not using it anywhere
         "th1": {"":"total_background_fits","Up":"total_background_fitsUp","Dn":"total_background_fitsDn"},
  },      
  "SUEP_ZH_generic": {
         "name"     : "SUEP_ZH_generic", #Here plain text
         "label"    : "ZS^{gen}, m_{S} = 125 GeV (pre-fit)", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kBlue,
         "fillcolor": ROOT.kBlue,
         "isSig"    : True,
         "doPlot"   : True,
         "files"    : hdf5inpath(main_path_signal + "SUEP_hadronic_mS125_mD8.00_T12.00/"), # Just whatever so it reads quickly, we are not using it anywhere
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*x["TrigSF"]*x["LepSF"],
         "th1": {"":"SUEP_hadronic_mS125_mD8.00_T12.00_fits","Up":"SUEP_hadronic_mS125_mD8.00_T12.00_fitsUp","Dn":"SUEP_hadronic_mS125_mD8.00_T12.00_fitsDn"},
  }

}

for sample in samples:
  if "data" in sample: continue
  samples[sample]["variations"] = {
  "Up": {
           "name"            :   "Up",
           "isSyst"          :       True,
           "replaceChannel"  :         {},
           "extraWeights"    :   lambda x: x["TrigSF"]/x["TrigSF"], # Relative to central
           "symmetrize"      :      False, 
  },
  "Dn": {
           "name"            :   "Dn",
           "isSyst"          :       True,
           "replaceChannel"  :         {},
           "extraWeights"    :   lambda x: x["TrigSF"]/x["TrigSF"], # Relative to central
           "symmetrize"      :      False,
  },
  }
