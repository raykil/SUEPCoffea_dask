import os
import ROOT
from auxiliars import *

def hdf5inpath(path):
  ret = []
  for f in os.listdir(path):
    if "hdf5" in f: 
      ret.append(path + "/" + f)
  #if len(ret) > 3: ret = ret[:3]
  #elif len(ret) < 4000: ret = ret[2000:]
  #elif len(ret) > 3000: ret = ret[3000:3010]
  return ret

order   = ["ttZ","VV", "WJets","ttto1l", "ttto2l", "DY_Pt650ToInf", "DY_Pt400To650","DY_Pt250To400","DY_Pt100To250","DY_Pt50To100", "DY_Pt0To50"]
samples = {
"""  "data": {
         "name" : "data",
         "label": "Data",
         "xsec" : -1,
         "lineColor": ROOT.kBlack,
         "fillcolor": ROOT.kBlack,
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/25_07_2022_SRonly/data/"),#+ hdf5inpath("/eos/user/c/cericeci/SUEP/25_07_2022_SRonly/data_RunB/")+hdf5inpath("/eos/user/c/cericeci/SUEP/25_07_2022_SRonly/data_RunC/")+hdf5inpath("/eos/user/c/cericeci/SUEP/25_07_2022_SRonly/data_RunD/"),
         "markerstyle": 20,
         "markersize" : 1,
  },"""
  "DY_Pt0": {
         "name"       : "DY_Pt0", #Here plain text
         "label"      : "DY", #Here we can use weird glyphs
         "xsec"       : 6309*1000., # in fb
         "linecolor"  : ROOT.kBlack,
         "fillcolor"  : 7, # White
         "isSig"      : False,
         "extraWeights": lambda x: 1*(x["genZpt"]==0.0)*SF(x) , 
         "files"      : hdf5inpath("/eos/user/c/cericeci/SUEP/25_07_2022_SRonly/DY_nano_Autumn18/"),
  },      
  "DY_Pt0To50": {
         "name"     : "DY_Pt0To50", #Here plain text
         "label"    : "DY", #Here we can use weird glyphs
         "xsec"     : 1510.*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 7, # Light blue
         "isSig"    : False,
         "extraWeights": lambda x: SF(x),
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/25_07_2022_SRonly/DYToLL_M50_Pt0To50/"),
         "skim"     : "/eos/user/c/cericeci/SUEP_signals/skim_UL18/DYToLL_M50_Pt0To50/skims.root"
  },
  "DY_Pt50To100": {
         "name"     : "DY_Pt50To100", #Here plain text
         "label"    : "DY", #Here we can use weird glyphs
         "xsec"     : 392.1*1000., # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 7, # Light blue
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/25_07_2022_SRonly/DYToLL_M50_Pt50To100/"),
         "skim"     : "/eos/user/c/cericeci/SUEP_signals/skim_UL18/DYToLL_M50_Pt50To100/skims.root",
         "extraWeights": lambda x: SF(x),
  },
  "DY_Pt100To250": {
         "name"     : "DY_Pt100To250", #Here plain text
         "label"    : "DY", #Here we can use weird glyphs
         "xsec"     : 91.23*1000., # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 7, # Light blue
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/25_07_2022_SRonly/DYToLL_M50_Pt100To250/"),
         "skim"     : "/eos/user/c/cericeci/SUEP_signals/skim_UL18/DYToLL_M50_Pt100To250/skims.root",
         "extraWeights": lambda x: SF(x),
  },
  "DY_Pt250To400": {
         "name"     : "DY_Pt250To400", #Here plain text
         "label"    : "DY", #Here we can use weird glyphs
         "xsec"     : 3.499*1000., # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 7, # Light blue
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/25_07_2022_SRonly/DYToLL_M50_Pt250To400/"),
         "skim"     : "/eos/user/c/cericeci/SUEP_signals/skim_UL18/DYToLL_M50_Pt250To400/skims.root",
         "extraWeights": lambda x: SF(x),
  },
  "DY_Pt400To650": {
         "name"     : "DY_Pt400To650", #Here plain text
         "label"    : "DY", #Here we can use weird glyphs
         "xsec"     : 0.4765*1000., # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 7, # Light blue
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/25_07_2022_SRonly/DYToLL_M50_Pt400To650/"),
         "skim"     : "/eos/user/c/cericeci/SUEP_signals/skim_UL18/DYToLL_M50_Pt400To650/skims.root",
         "extraWeights": lambda x: SF(x),
  },
  "DY_Pt650ToInf": {
         "name"     : "DY_Pt650ToInf", #Here plain text
         "label"    : "DY", #Here we can use weird glyphs
         "xsec"     : 0.04489*1000., # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 7, # Light blue
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/25_07_2022_SRonly/DYToLL_M50_Pt650ToInf/"),
         "skim"     : "/eos/user/c/cericeci/SUEP_signals/skim_UL18/DYToLL_M50_Pt650ToInf/skims.root", 
         "extraWeights": lambda x: SF(x),
  },
  "ttto2l": {
         "name"     : "ttto2l", #Here plain text
         "label"    : "t#bar{t} (2l)", #Here we can use weird glyphs
         "xsec"     : 831.76*((3*0.108)**2)*1000., # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 2, # Red
         "isSig"    : False,
         "files"    :  hdf5inpath("/eos/user/c/cericeci/SUEP/25_07_2022_SRonly/TTTo2L2Nu/"),
         "skim"     : "/eos/user/c/cericeci/SUEP_signals/skim_UL18/TTTo2L2Nu/skims.root",
         "extraWeights": lambda x: SF(x),
  },
  "tW": {
         "name"     : "tW", #Here plain text
         "label"    : "tW", #Here we can use weird glyphs
         "xsec"     : 3.289*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": ROOT.kMagenta, # Red
         "isSig"    : False,
         "files"    :  hdf5inpath("/eos/user/c/cericeci/SUEP/25_07_2022_SRonly/tW/"),
         "skim"     : "/eos/cms/store/user/cericeci/SUEPS/UL18/tW/skims.root",
         "extraWeights": lambda x: SF(x),
  },
  "DY_lowmass": {
         "name"     : "DY_lowmass", #Here plain text
         "label"    : "DY", #Here we can use weird glyphs
         "xsec"     : 15810.0*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 7, # Red
         "isSig"    : False,
         "files"    :  hdf5inpath("/eos/user/c/cericeci/SUEP/25_07_2022_SRonly/DY_lowmass/"),
         "skim"     : "/eos/user/c/cericeci/SUEP_signals/skim_UL18/DY_lowmass/skims.root",
         "extraWeights": lambda x: SF(x),
  },

  "ttto1l": {
         "name"     : "ttto1l", #Here plain text
         "label"    : "t#bar{t} (1l)", #Here we can use weird glyphs
         "xsec"     : 831.76*(3*0.108)*(1-3*0.108)*1000., # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 5, # Yellow
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/25_07_2022_SRonly/TTTo1L1Nu2Q/"),
         "skim"     : "/eos/cms/store/user/cericeci/SUEPS/UL18/TTTo1L1Nu2Q/skims.root",
         "extraWeights": lambda x: SF(x),
  },
"""  "Wjets": {
         "name"     : "Wjets", #Here plain text
         "label"    : "W", #Here we can use weird glyphs
         "xsec"     : 20508.9*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 6, # Purple
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/25_07_2022_SRonly/WJets/"), 
         "skim"     : "/eos/cms/store/user/cericeci/SUEPS/UL18//WJets/skims.root",
         "extraWeights": lambda x: SF(x),
  },

  "QCD": {
         "name"     : "QCD", #Here plain text
         "label"    : "QCD", #Here we can use weird glyphs
         "xsec"     : 1375000000*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": ROOT.kPink, # Purple
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/25_07_2022_SRonly/QCD/"),
         "skim"     : "/eos/cms/store/user/cericeci/SUEPS/UL18/QCD/skims.root",
         "extraWeights": lambda x: SF(x),
  },"""

  "WW": {
         "name"     : "WW", #Here plain text
         "label"    : "VV", #Here we can use weird glyphs
         "xsec"     : 10.481*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 3, # Green
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/25_07_2022_SRonly/WWTo2L2Nu/"),
         "WW"       : "/eos/cms/store/user/cericeci/SUEPS/UL18/WWTo2L2Nu/skims.root",
         "extraWeights": lambda x: SF(x),
  },

  "WZ2l2q": {
         "name"     : "WZ2l2q", #Here plain text
         "label"    : "VV", #Here we can use weird glyphs
         "xsec"     : 6.419*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 3, # Green
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/25_07_2022_SRonly/WZTo2l2Q/"),
         "extraWeights": lambda x: SF(x),
         "skim"     : "/eos/cms/store/user/cericeci/SUEPS/UL18/WZTo2l2Q/skims.root"
  },
  "WZ3lnu": {
         "name"     : "WZ3lnu", #Here plain text
         "label"    : "VV", #Here we can use weird glyphs
         "xsec"     : 4.664*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 3, # Green
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/25_07_2022_SRonly/WZTo3LNu/"),
         "extraWeights": lambda x: SF(x),
         "skim"     : "/eos/cms/store/user/cericeci/SUEPS/UL18/WZTo3LNu/skims.root"
  },
  "ZZ2l2q": {
         "name"     : "ZZ2l2q", #Here plain text
         "label"    : "VV", #Here we can use weird glyphs
         "xsec"     : 3.74*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 3, # Green
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/25_07_2022_SRonly/ZZTo2L2Q/"),
         "extraWeights": lambda x: SF(x),
         "skim"     : "/eos/cms/store/user/cericeci/SUEPS/UL18/ZZTo2L2Q/skims.root"
  },
  "ZZ2l2nu": {
         "name"     : "ZZ2l2nu", #Here plain text
         "label"    : "VV", #Here we can use weird glyphs
         "xsec"     : 0.8738*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 3, # Green
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/25_07_2022_SRonly/ZZTo2L2Nu/"),
         "extraWeights": lambda x: SF(x),
         "skim"     : "/eos/cms/store/user/cericeci/SUEPS/UL18/ZZTo2L2Nu/skims.root"
  },
  "ZZ4l": {
         "name"     : "ZZ4l", #Here plain text
         "label"    : "VV", #Here we can use weird glyphs
         "xsec"     : 1.325*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 3, # Green
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/25_07_2022_SRonly/ZZTo4L/"),
         "extraWeights": lambda x: SF(x),
         "skim"     : "/eos/cms/store/user/cericeci/SUEPS/UL18/ZZTo4L/skims.root"
  },

 "ZG": {
         "name"     : "ZG", #Here plain text
         "label"    : "VV", #Here we can use weird glyphs
         "xsec"     : 51.1*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 3, # Green
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/25_07_2022_SRonly/ZG/"),
         "extraWeights": lambda x: SF(x),
         "skim"     : "/eos/cms/store/user/cericeci/SUEPS/UL18/ZG/skims.root"
  },
"""  "WG": {
         "name"     : "WG", #Here plain text
         "label"    : "VV", #Here we can use weird glyphs
         "xsec"     : 412.7*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 3, # Green
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/25_07_2022_SRonly/WG/"),
         "extraWeights": lambda x: SF(x),
         "skim"     : "/eos/cms/store/user/cericeci/SUEPS/UL18/WG/skims.root"
  },"""

  "ttZll": { "name"     : "ttZll", #Here plain text
         "label"    : "t#bar{t}X", #Here we can use weird glyphs
         "xsec"     : 0.2439*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 9, # Dark blue
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/25_07_2022_SRonly/TTZToLL/"),
         "extraWeights": lambda x: SF(x),
         "skim"     : "/eos/cms/store/user/cericeci/SUEPS/UL18/TTZToLL/skims.root"
  },
  "ttZqq": {
         "name"     : "ttZqq", #Here plain text
         "label"    : "t#bar{t}X", #Here we can use weird glyphs
         "xsec"     : 0.5104*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 9, # Dark blue
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/25_07_2022_SRonly/TTZToQQ/"),
         "extraWeights": lambda x: SF(x),
         "skim"     : "/eos/cms/store/user/cericeci/SUEPS/UL18/TTZToQQ/skims.root"
  },
  "ttWlnu": {
         "name"     : "ttWlnu", #Here plain text
         "label"    : "t#bar{t}X", #Here we can use weird glyphs
         "xsec"     : 0.2161*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 9, # Dark blue
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/25_07_2022_SRonly/TTWToLNu/"),
         "extraWeights": lambda x: SF(x),
         "skim"     : "/eos/cms/store/user/cericeci/SUEPS/UL18/TTWToLNu/skims.root"
  },
  "ttWqq": {
         "name"     : "ttWqq", #Here plain text
         "label"    : "t#bar{t}X", #Here we can use weird glyphs
         "xsec"     : 0.4377*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 9, # Dark blue
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/25_07_2022_SRonly/TTWToQQ/"),
         "extraWeights": lambda x: SF(x),
         "skim"     : "/eos/cms/store/user/cericeci/SUEPS/UL18/TTWToQQ/skims.root"
  },
  "SUEP_ZH_generic": {
         "name"     : "SUEP_ZH_generic", #Here plain text
         "label"    : "ZS^{gen}, m_{S} = 125 GeV", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": ROOT.kBlack,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/user/c/cericeci/SUEP/25_07_2022_SRonly/SUEP_generic_mS125/"),
         "extraWeights": lambda x: SF(x),
  },
}
