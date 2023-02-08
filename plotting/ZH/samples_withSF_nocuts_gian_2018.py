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
         "name"     : "GenericSignals_SFs", #Here plain text
         "label"    : "GenericSignals_SFs",# (p_{T} < 50 GeV)", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kMagenta,
         "isSig"    : True,
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["triggerSFs"]*SF(x,18),
         "files"    : hdf5inpath("/eos/user/g/gdecastr/SUEPCoffea_dask/testWorkflow/SUEP_Signal_m2T2_UL18/"),
  },
    "GenericSignal_SFs_UP": {
         "name"     : "GenericSignals_SFs_UP", #Here plain text
         "label"    : "GenericSignals_SF_UP",# (p_{T} < 50 GeV)", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kGreen,
         "isSig"    : True,
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*(x["triggerSFs"]+x["triggerSFs_up"])*SF(x,18),
         "files"    : hdf5inpath("/eos/user/g/gdecastr/SUEPCoffea_dask/testWorkflow/SUEP_Signal_m2T2_UL18/"),
  },
      "GenericSignal_SFs_DOWN": {
         "name"     : "GenericSignals_SFs_DOWN", #Here plain text
         "label"    : "GenericSignals_SF_DOWN",# (p_{T} < 50 GeV)", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kRed,
         "isSig"    : True,
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*(x["triggerSFs"]-x["triggerSFs_down"])*SF(x,18),
         "files"    : hdf5inpath("/eos/user/g/gdecastr/SUEPCoffea_dask/testWorkflow/SUEP_Signal_m2T2_UL18/"),
  },
    "GenericSignal": {
         "name"     : "GenericSignals", #Here plain text
         "label"    : "GenericSignals",# (p_{T} < 50 GeV)", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kBlue,
         "fillcolor": ROOT.kBlue, 
         "isSig"    : False,
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*SF(x,18),
         "files"    : hdf5inpath("/eos/user/g/gdecastr/SUEPCoffea_dask/testWorkflow/SUEP_Signal_m2T2_UL18/"),
  },
  
}

