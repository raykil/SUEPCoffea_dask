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
main_path = "/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/UL18data_forHEM/"
samples = {
  "data_postHEM": {
         "name" : "data_postHEM",
         "label": "Data (run #geq 319077, Scaled)",
         "xsec" : -1,
         "lineColor": ROOT.kRed,
         "fillcolor": ROOT.kRed,
         "isSig"    : False,
         "files"    : hdf5inpath(main_path + "data/"),#+ hdf5inpath(main_path + "data_RunB/")+hdf5inpath(main_path + "data_RunC/")+hdf5inpath(main_path + "data_RunD/"),
         #"markerstyle": 20,
         #"markersize" : 1,
         "extraWeights": lambda x: x["run"] >= 319077,
         "skim": "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/skims.root",
         "scale": 0.54,
         "noWeight" : True,
  },
  "data": {
         "name" : "data",
         "label": "Data (run < 319077)",
         "xsec" : -1,
         "lineColor": ROOT.kBlack,
         "fillcolor": ROOT.kBlack,
         "isSig"    : False,
         "files"    : hdf5inpath(main_path + "data/"),#+ hdf5inpath(main_path + "data_RunB/")+hdf5inpath(main_path + "data_RunC/")+hdf5inpath(main_path + "data_RunD/"),
         "markerstyle": 20,
         "markersize" : 1,
         "extraWeights": lambda x: x["run"] < 319077,
         "skim": "/eos/cms/store/group/phys_exotica/SUEPs/UL18/skim_2l_20_10/data/skims.root",
         "noWeight" : True,
  },      
}

