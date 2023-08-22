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

