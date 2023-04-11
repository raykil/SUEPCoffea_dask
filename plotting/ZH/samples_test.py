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
main_path = "/eos/cms/store/group/phys_exotica/SUEPs/UL16/hdf5_withsysts/"
samples = {
  "DY_Pt650ToInf": {
         "name"     : "DY_Pt650ToInf", #Here plain text
         "label"    : "DY",# (p_{T} > 650 GeV)", #Here we can use weird glyphs
         "xsec"     : 0.04489*1000., # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 7, # Light blue
         "isSig"    : False,
         "files"    : hdf5inpath(main_path + "DYToLL_M50_Pt650ToInf/"),
         "skim"     : "/eos/cms/store/group/phys_exotica/SUEPs/UL16/skim_2l_20_10/DYToLL_M50_Pt650ToInf/skims.root", 
         "extraWeights": lambda x: one(x),
  },
}


samples["DY_Pt650ToInf"]["variations"] = {
  "syst1": {
           "name"            : "syst1",
           "isSyst"          :      True,
           "replaceChannel"  :        {},
           "extraWeights"    :  lambda x: samples["DY_Pt650ToInf"]["extraWeights"](x) *(1- 0.25* (x["leadclusterSpher_C"] - 0.5)),
           "symmetrize"      :      True, 
  },
  "syst2Up": {
           "name"            : "syst2Up",
           "isSyst"          :      True,
           "replaceChannel"  :        {},
           "extraWeights"    :  lambda x: samples["DY_Pt650ToInf"]["extraWeights"](x)*2,
           "symmetrize"      :     False,
  },
  "syst2Dn": {
           "name"            : "syst2Up",
           "isSyst"          :      True,
           "replaceChannel"  :        {},
           "extraWeights"    :  lambda x: samples["DY_Pt650ToInf"]["extraWeights"](x)*0.5,
           "symmetrize"      :     False,
  },
  "syst3": {
           "name"            : "syst3",
           "isSyst"          :      True,
           "replaceChannel"  :  {"SR":"SR_TRACKUP", "onecluster":"onecluster_TRACKUP", "twoleptons":"twoleptons_TRACKUP"},
           "extraWeights"    :  lambda x: samples["DY_Pt650ToInf"]["extraWeights"](x),
           "symmetrize"      :     True,
  },
}

#samples["DY_Pt650ToInf_syst2Up"]                 = samples["DY_Pt650ToInf"]
#samples["DY_Pt650ToInf_syst2Up"]["isSyst"]       = True
#samples["DY_Pt650ToInf_syst2Up"]["extraWeights"] = lambda x: samples["DY_Pt650ToInf"]["extraWeights"](x)*1.10
#samples["DY_Pt650ToInf_syst2Dn"]                 = samples["DY_Pt650ToInf"]
#samples["DY_Pt650ToInf_syst2Dn"]["isSyst"]       = True
#samples["DY_Pt650ToInf_syst2Dn"]["extraWeights"] = lambda x: samples["DY_Pt650ToInf"]["extraWeights"](x)*0.90

