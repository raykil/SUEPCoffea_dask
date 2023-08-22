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
allddaattaa = hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/hdf5_extraTests/UL16/data")+hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/hdf5_extraTests/UL16APV/data")+hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/hdf5_extraTests/UL18/data")+hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/hdf5_extraTests/UL17/data")

samples = {
  "ddaattaa_PU0to17": {
         "name" : "ddaattaa_PU0to17",
         "label": "Data (0<=PU<=17;10.6 fb^{-1})",
         "xsec" : -1,
         "linecolor": ROOT.kRed,
         "fillcolor": ROOT.kRed,
         "isSig"    : True,
         "files"    : allddaattaa,
         "extraWeights": lambda x: x["nPU"] <= 17,
         "scale": 0.8381*137.8/10.6,
         "noWeight" : True,
  },
  "ddaattaa_PU44toInf": {
         "name" : "ddaattaa_PU44toInf",
         "label": "Data (44<PU;10.7 fb^{-1})",
         "xsec" : -1,
         "linecolor": ROOT.kBlue,
         "fillcolor": ROOT.kBlue,
         "isSig"    : True,
         "files"    : allddaattaa,
         "extraWeights": lambda x: x["nPU"] > 44,
         "scale": 1.4109*137.8/10.7,
         "noWeight" : True,
  },
  "ddaattaa_PU0to22": {
         "name" : "ddaattaa_PU0to22",
         "label": "Data (0<=PU<=22;33.8 fb^{-1})",
         "xsec" : -1,
         "linecolor": ROOT.kGreen,
         "fillcolor": ROOT.kGreen,
         "isSig"    : True,
         "files"    : allddaattaa,
         "extraWeights": lambda x: x["nPU"] <= 22,
         "scale": 0.8578*137.8/33.8,
         "noWeight" : True,
  },
  "ddaattaa_PU23to29": {
         "name" : "ddaattaa_PU23to29",
         "label": "Data (22<PU<=29;36.6 fb^{-1})",
         "xsec" : -1,
         "linecolor": ROOT.kViolet,
         "fillcolor": ROOT.kViolet,
         "isSig"    : True,
         "files"    : allddaattaa,
         "extraWeights": lambda x: (x["nPU"] > 22) & (x["nPU"] <= 29),
         "scale": 0.9369*137.8/36.6,
         "noWeight" : True,
  },
  "ddaattaa_PU30to37": {
         "name" : "ddaattaa_PU30to37",
         "label": "Data (29<PU<=37;35.8 fb^{-1})",
         "xsec" : -1,
         "linecolor": ROOT.kYellow,
         "fillcolor": ROOT.kYellow,
         "isSig"    : True,
         "files"    : allddaattaa,
         "extraWeights": lambda x: (x["nPU"] > 29) & (x["nPU"] <= 37),
         "scale": 1.0190*137.8/35.8,
         "noWeight" : True,
  },
  "ddaattaa_PU38toInf": {
         "name" : "ddaattaa_PU38toInf",
         "label": "Data (37<PU;31.0 fb^{-1})",
         "xsec" : -1,
         "linecolor": ROOT.kCyan,
         "fillcolor": ROOT.kCyan,
         "isSig"    : True,
         "files"    : allddaattaa,
         "extraWeights": lambda x: (x["nPU"] > 37),
         "scale": 1.2808*137.8/31.0,
         "noWeight" : True,
  },
  "ddaattaa_total": {
         "name" : "ddaattaa_total",
         "label": "Data (Total)",
         "xsec" : -1,
         "linecolor": ROOT.kBlack,
         "fillcolor": ROOT.kWhite,
         "isSig"    : False,
         "files"    : allddaattaa,
         "markerstyle": 20,
         "markersize" : 1,
         "extraWeights": lambda x: x["run"] > 0,
         "noWeight" : True,
  },      
}

