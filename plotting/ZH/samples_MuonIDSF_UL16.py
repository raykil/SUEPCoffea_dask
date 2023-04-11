import os
import ROOT
from auxiliars import *
import copy

def hdf5inpath(path):
  ret = []
  for p in os.listdir(path):
    if not("DY" in p): continue
    ppath = path + "/" + p
    for f in os.listdir(ppath):
      if "hdf5" in f: 
        ret.append(ppath + "/" + f)
  return ret

# Main path where samples are stored
samples = {
  "DY": {
         "name"     : "DY", #Here plain text
         "label"    : "No IP cuts", #Here we can use weird glyphs
         "xsec"     : 1, # in fb
         "linecolor": ROOT.kBlue,
         "fillcolor": ROOT.kBlue,
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/MuonID/UL16/hdf5/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*x["TrigSF"]*x["LepSF"],
         "noWeight": True
  },
  "DY_withIP": {
         "name"     : "DY_withIP", #Here plain text
         "label"    : "With Muon IP cuts", #Here we can use weird glyphs
         "xsec"     : 1, # in fb
         "linecolor": ROOT.kRed,
         "fillcolor": ROOT.kRed,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/MuonID/UL16/hdf5/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*x["TrigSF"]*x["LepSF"]*(abs(x["leadlep_dxy"])<0.02)*(abs(x["subleadlep_dxy"])<0.02)*(abs(x["leadlep_dxz"])<0.1)*(abs(x)["subleadlep_dxz"]<0.1),
         "noWeight": True
  },
}

