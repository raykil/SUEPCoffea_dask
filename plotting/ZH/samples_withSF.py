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
  "data": {
         "name" : "data",
         "label": "Data",
         "xsec" : -1,
         "lineColor": ROOT.kBlack,
         "fillcolor": ROOT.kBlack,
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/17_05_2022/data_RunA/"),#+ hdf5inpath("/eos/home-c/cericeci/SUEP/17_05_2022/data_RunB/")+hdf5inpath("/eos/home-c/cericeci/SUEP/17_05_2022/data_RunC/")+hdf5inpath("/eos/home-c/cericeci/SUEP/17_05_2022/data_RunD/"),
         "markerstyle": 20,
         "markersize" : 1,
  },
  "DY_Pt0": {
         "name"       : "DY_Pt0", #Here plain text
         "label"      : "DY (p_{T} = 0 GeV)", #Here we can use weird glyphs
         "xsec"       : 6309*1000., # in fb
         "linecolor"  : ROOT.kBlack,
         "fillcolor"  : ROOT.kWhite, # White
         "isSig"      : False,
         "extraWeights": lambda x: 1*(x["genZpt"]==0.0)*SF(x) , 
         "files"      : hdf5inpath("/eos/home-c/cericeci/SUEP/17_05_2022/DY_inclusive/"),
  },      
  "DY_Pt0To50": {
         "name"     : "DY_Pt0To50", #Here plain text
         "label"    : "DY (p_{T} < 50 GeV)", #Here we can use weird glyphs
         "xsec"     : 1510.*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 7, # Light blue
         "isSig"    : False,
         "extraWeights": lambda x: SF(x),
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/17_05_2022/DYToLL_MLL50_Pt0To50/"),
         "skim"     : "/eos/user/c/cericeci/SUEP_signals/skim_UL18/DYToLL_M50_Pt0To50/skims.root"
  },
  "DY_Pt50To100": {
         "name"     : "DY_Pt50To100", #Here plain text
         "label"    : "DY (50 < p_{T} < 100 GeV)", #Here we can use weird glyphs
         "xsec"     : 392.1*1000., # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": ROOT.kCyan+1, # Light blue
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/17_05_2022/DYToLL_MLL50_Pt50To100/"),
         "skim"     : "/eos/user/c/cericeci/SUEP_signals/skim_UL18/DYToLL_M50_Pt50To100/skims.root",
         "extraWeights": lambda x: SF(x),
  },
  "DY_Pt100To250": {
         "name"     : "DY_Pt100To250", #Here plain text
         "label"    : "DY (100 < p_{T} < 250 GeV)", #Here we can use weird glyphs
         "xsec"     : 91.23*1000., # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": ROOT.kCyan+2, # Light blue
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/17_05_2022/DYToLL_MLL50_Pt100To250/"),
         "skim"     : "/eos/user/c/cericeci/SUEP_signals/skim_UL18/DYToLL_M50_Pt100To250/skims.root",
         "extraWeights": lambda x: SF(x),
  },
  "DY_Pt250To400": {
         "name"     : "DY_Pt250To400", #Here plain text
         "label"    : "DY (250 < p_{T} < 400 GeV)", #Here we can use weird glyphs
         "xsec"     : 3.499*1000., # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": ROOT.kCyan+3, # Light blue
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/17_05_2022/DYToLL_MLL50_Pt250To400/"),
         "skim"     : "/eos/user/c/cericeci/SUEP_signals/skim_UL18/DYToLL_M50_Pt250To400/skims.root",
         "extraWeights": lambda x: SF(x),
  },
  "DY_Pt400To650": {
         "name"     : "DY_Pt400To650", #Here plain text
         "label"    : "DY (400 < p_{T} < 650 GeV)", #Here we can use weird glyphs
         "xsec"     : 0.4765*1000., # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": ROOT.kCyan+4, # Light blue
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/17_05_2022/DYToLL_MLL50_Pt400To650/"),
         "skim"     : "/eos/user/c/cericeci/SUEP_signals/skim_UL18/DYToLL_M50_Pt400To650/skims.root",
         "extraWeights": lambda x: SF(x),
  },
  "DY_Pt650ToInf": {
         "name"     : "DY_Pt650ToInf", #Here plain text
         "label"    : "DY (p_{T} > 650 GeV)", #Here we can use weird glyphs
         "xsec"     : 0.04489*1000., # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": ROOT.kOrange, # Light blue
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/17_05_2022/DYToLL_MLL50_Pt650ToInf/"),
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
         "files"    :  hdf5inpath("/eos/home-c/cericeci/SUEP/17_05_2022/TTTpo2L2Nu/"),
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
         "files"    :  hdf5inpath("/eos/home-c/cericeci/SUEP/17_05_2022/tW/"),
         "skim"     : "/eos/cms/store/user/cericeci/SUEPS/UL18/tW/skims.root",
         "extraWeights": lambda x: SF(x),
  },
  "DY_lowmass": {
         "name"     : "DY_lowmass", #Here plain text
         "label"    : "DY (m_{ll} < 50 GeV)", #Here we can use weird glyphs
         "xsec"     : 15810.0*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": ROOT.kAzure, # Red
         "isSig"    : False,
         "files"    :  hdf5inpath("/eos/home-c/cericeci/SUEP/17_05_2022/DY_lowmass/"),
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
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/10_05_2022/TT_semilep/"),
         "extraWeights": lambda x: SF(x),
  },

  #"Wjets": {
  #       "name"     : "Wjets", #Here plain text
  #       "label"    : "W", #Here we can use weird glyphs
  #       "xsec"     : 20508.9*1000, # in fb
  #       "linecolor": ROOT.kBlack,
  #       "fillcolor": 6, # Purple
  #       "isSig"    : False,
  #       "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/17_05_2022/WJets/"), 
  #       "skim"     : "/eos/user/c/cericeci/SUEP_signals/skim_UL18/WJets/skims.root",
  #       "extraWeights": lambda x: SF(x),
  #},
  "VV": {
         "name"     : "VV", #Here plain text
         "label"    : "VV", #Here we can use weird glyphs
         "xsec"     : 10.481*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 3, # Green
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/10_05_2022/WW/"),
         "extraWeights": lambda x: SF(x),
  },
  "ttZ": {
         "name"     : "ttZ", #Here plain text
         "label"    : "t#bar{t}X", #Here we can use weird glyphs
         "xsec"     : 0.78*1000*0.4, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 9, # Dark blue
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/10_05_2022/TTZ_LL/"),
         "extraWeights": lambda x: SF(x),
  },
  "SUEP_ZH_generic": {
         "name"     : "SUEP_ZH_generic", #Here plain text
         "label"    : "ZS^{gen}, m_{S} = 125 GeV", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": ROOT.kBlack,
         "isSig"    : True,
         "files"    : ["/eos/home-c/cericeci/SUEP/10_05_2022/ZH_generic//out_1_1_1001.hdf5"],
         "extraWeights": lambda x: SF(x),
  },
  "SUEP_ZH_leptonic": {
         "name"     : "SUEP_ZH_leptonic", #Here plain text
         "label"    : "ZS^{lep}, m_{S} = 125 GeV", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kGreen,
         "fillcolor": ROOT.kGreen,
         "isSig"    : True,
         "files"    : ["/eos/home-c/cericeci/SUEP/10_05_2022/ZH_leptonic//out_1_1_1101.hdf5"],
         "extraWeights": lambda x: SF(x),
  },

  "SUEP_ZH_hadronic": {
         "name"     : "SUEP_ZH_hadronic", #Here plain text
         "label"    : "ZS^{had}, m_{S} = 125 GeV", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kBlue,
         "fillcolor": ROOT.kBlue,
         "isSig"    : True,
         "files"    : ["/eos/home-c/cericeci/SUEP/10_05_2022/ZH_hadronic//out_1_1_1001.hdf5"],
         "extraWeights": lambda x: SF(x),
  },

}
