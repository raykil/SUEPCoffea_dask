import os
import ROOT

def hdf5inpath(path):
  ret = []
  for f in os.listdir(path):
    if "hdf5" in f: 
      ret.append(path + "/" + f)
  if len(ret) > 5: ret = ret[:4]
  return ret

order   = ["VV", "WJets","ttto2l", "DY_Pt650ToInf"]
samples = {
  #"DY": {
  #       "name"     : "DY", #Here plain text
  #       "label"    : "DY", #Here we can use weird glyphs
  #       "xsec"     : 2008.*3*1000., # in fb
  #       "linecolor": ROOT.kBlack,
  #       "fillcolor": 7, # Light blue
  #       "isSig"    : False, 
  #       "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/10_05_2022/DY/") 
  #},
  "DY_Pt650ToInf": {
         "name"     : "DY_Pt650ToInf", #Here plain text
         "label"    : "DY (p_{T} > 650 GeV)", #Here we can use weird glyphs
         "xsec"     : 0.04704*1000., # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": ROOT.kBlack, # Light blue
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/17_05_2022/DYToLL_MLL50_Pt650ToInf/"),
         "skim"     : "/eos/user/c/cericeci/SUEP_signals/skim_UL18/DYToLL_M50_Pt650ToInf/skims.root"
  },
 
  "ttto2l": {
         "name"     : "TT", #Here plain text
         "label"    : "t#bar{t} (2l)", #Here we can use weird glyphs
         "xsec"     : 831.76*((3*0.108)**2)*1000., # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 2, # Red
         "isSig"    : False,
         "files"    :  hdf5inpath("/eos/home-c/cericeci/SUEP/17_05_2022/TTTpo2L2Nu/"),
         "skim"     : "/eos/user/c/cericeci/SUEP_signals/skim_UL18/TTTo2L2Nu/skims.root"
  },
}


