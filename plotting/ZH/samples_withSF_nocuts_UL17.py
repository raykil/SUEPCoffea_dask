import os
import ROOT
from auxiliars import *

def hdf5inpath(path):
  ret = []
  for f in os.listdir(path):
    if "hdf5" in f: 
      ret.append(path + "/" + f)
  return ret

# Main path where samples are stored
main_path = "/eos/cms/store/user/cericeci/SUEPS/hdf5_24_11_2022_leptonID_2017/"
samples = {
#  "data": {
#         "name" : "data",
#         "label": "Data",
#         "xsec" : -1,
#         "lineColor": ROOT.kBlack,
#         "fillcolor": ROOT.kBlack,
#         "isSig"    : False,
#         "files"    : hdf5inpath(main_path + "data_RunD/"),#+ hdf5inpath(main_path + "data_RunB/")+hdf5inpath(main_path + "data_RunC/")+hdf5inpath(main_path + "data_RunD/"),
#         "markerstyle": 20,
#         "markersize" : 1,
#  },
  "DY_Pt0": {
         "name"       : "DY_Pt0", #Here plain text
         "label"      : "DY",# (p_{T} = 0 GeV)", #Here we can use weird glyphs
         "xsec"       : 6309*1000., # in fb
         "linecolor"  : ROOT.kBlack,
         "fillcolor"  : 7, # White
         "isSig"      : False,
         "extraWeights": lambda x: 1*(x["genZpt"]==0.0)*SF(x,17) , 
         "files"      : hdf5inpath(main_path + "DYToLL_M50/"),
         "skim"     : "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DYToLL_M50/skims.root"
  },      
  "DY_Pt0To50": {
         "name"     : "DY_Pt0To50", #Here plain text
         "label"    : "DY",# (p_{T} < 50 GeV)", #Here we can use weird glyphs
         "xsec"     : 1510.*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 7, # Light blue
         "isSig"    : False,
         "extraWeights": lambda x: SF(x,17),
         "files"    : hdf5inpath(main_path + "DYToLL_M50_Pt0To50/"),
         "skim"     : "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DYToLL_M50_Pt0To50/skims.root"
  },
  "DY_Pt50To100": {
         "name"     : "DY_Pt50To100", #Here plain text
         "label"    : "DY",# (50 < p_{T} < 100 GeV)", #Here we can use weird glyphs
         "xsec"     : 392.1*1000., # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 7, # Light blue
         "isSig"    : False,
         "files"    : hdf5inpath(main_path + "DYToLL_M50_Pt50To100/"),
         "skim"     : "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DYToLL_M50_Pt50To100/skims.root",
         "extraWeights": lambda x: SF(x,17),
  },
  "DY_Pt100To250": {
         "name"     : "DY_Pt100To250", #Here plain text
         "label"    : "DY",# (100 < p_{T} < 250 GeV)", #Here we can use weird glyphs
         "xsec"     : 91.23*1000., # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 7, # Light blue
         "isSig"    : False,
         "files"    : hdf5inpath(main_path + "DYToLL_M50_Pt100To250/"),
         "skim"     : "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DYToLL_M50_Pt100To250/skims.root",
         "extraWeights": lambda x: SF(x,17),
  },
  "DY_Pt250To400": {
         "name"     : "DY_Pt250To400", #Here plain text
         "label"    : "DY",# (250 < p_{T} < 400 GeV)", #Here we can use weird glyphs
         "xsec"     : 3.499*1000., # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 7, # Light blue
         "isSig"    : False,
         "files"    : hdf5inpath(main_path + "DYToLL_M50_Pt250To400/"),
         "skim"     : "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DYToLL_M50_Pt250To400/skims.root",
         "extraWeights": lambda x: SF(x,17),
  },
  "DY_Pt400To650": {
         "name"     : "DY_Pt400To650", #Here plain text
         "label"    : "DY",# (400 < p_{T} < 650 GeV)", #Here we can use weird glyphs
         "xsec"     : 0.4765*1000., # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 7, # Light blue
         "isSig"    : False,
         "files"    : hdf5inpath(main_path + "DYToLL_M50_Pt400To650/"),
         "skim"     : "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DYToLL_M50_Pt400To650/skims.root",
         "extraWeights": lambda x: SF(x,17),
  },
  "DY_Pt650ToInf": {
         "name"     : "DY_Pt650ToInf", #Here plain text
         "label"    : "DY",# (p_{T} > 650 GeV)", #Here we can use weird glyphs
         "xsec"     : 0.04489*1000., # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 7, # Light blue
         "isSig"    : False,
         "files"    : hdf5inpath(main_path + "DYToLL_M50_Pt650ToInf/"),
         "skim"     : "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DYToLL_M50_Pt650ToInf/skims.root", 
         "extraWeights": lambda x: SF(x,17),
  },
  "ttto2l": {
         "name"     : "ttto2l", #Here plain text
         "label"    : "t#bar{t} (2l)", #Here we can use weird glyphs
         "xsec"     : 831.76*((3*0.108)**2)*1000., # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 2, # Red
         "isSig"    : False,
         "files"    :  hdf5inpath(main_path + "TTTo2L2Nu/"),
         "skim"     : "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/TTTo2L2Nu/skims.root",
         "extraWeights": lambda x: SF(x,17),
  },
  "tW": {
         "name"     : "tW", #Here plain text
         "label"    : "tW", #Here we can use weird glyphs
         "xsec"     : 3.289*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": ROOT.kMagenta, # Red
         "isSig"    : False,
         "files"    :  hdf5inpath(main_path + "tW/"),
         "skim"     : "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/tW/skims.root",
         "extraWeights": lambda x: SF(x,17),
  },
  "DY_lowmass": {
         "name"     : "DY_lowmass", #Here plain text
         "label"    : "DY (m_{ll} < 50 GeV)", #Here we can use weird glyphs
         "xsec"     : 15810.0*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": ROOT.kAzure, # Red
         "isSig"    : False,
         "files"    :  hdf5inpath(main_path + "DY_lowmass/"),
         "skim"     : "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/DY_lowmass/skims.root",
         "extraWeights": lambda x: SF(x,17),
  },

  "ttto1l": {
         "name"     : "ttto1l", #Here plain text
         "label"    : "t#bar{t} (1l)", #Here we can use weird glyphs
         "xsec"     : 831.76*(3*0.108)*(1-3*0.108)*1000., # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 5, # Yellow
         "isSig"    : False,
         "files"    : hdf5inpath(main_path + "TTTo1L1Nu2Q/"),
         "extraWeights": lambda x: SF(x,17),
         "skim"     : "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/TTTo1L1Nu/skims.root",
  },
  "Wjets": {
         "name"     : "Wjets", #Here plain text
         "label"    : "W", #Here we can use weird glyphs
         "xsec"     : 20508.9*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 6, # Purple
         "isSig"    : False,
         "files"    : hdf5inpath(main_path + "WJets/"), 
         "skim"     : "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/WJets/skims.root",
         "extraWeights": lambda x: SF(x,17),
  },

  "WW": {
         "name"     : "WW", #Here plain text
         "label"    : "VV", #Here we can use weird glyphs
         "xsec"     : 10.481*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 3, # Green
         "isSig"    : False,
         "files"    : hdf5inpath(main_path + "WWTo2L2Nu/"),
         "WW"       : "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/WWTo2L2Nu/skims.root",
         "extraWeights": lambda x: SF(x,17),
  },
#  "WZ2l2q": {
#         "name"     : "WZ2l2q", #Here plain text
#         "label"    : "VV", #Here we can use weird glyphs
#         "xsec"     : 6.419*1000, # in fb
#         "linecolor": ROOT.kBlack,
#         "fillcolor": 3, # Green
#         "isSig"    : False,
#         "files"    : hdf5inpath(main_path + "WZTo2L2Q/"),
#         "extraWeights": lambda x: SF(x,17),
#         "skim"     : "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/WZTo2L2Q/skims.root"
#  },
  "WZ3lnu": {
         "name"     : "WZ3lnu", #Here plain text
         "label"    : "VV", #Here we can use weird glyphs
         "xsec"     : 4.664*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 3, # Green
         "isSig"    : False,
         "files"    : hdf5inpath(main_path + "WZTo3LNu/"),
         "extraWeights": lambda x: SF(x,17),
         "skim"     : "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/WZTo3LNu/skims.root"
  },
  "ZZ2l2q": {
         "name"     : "ZZ2l2q", #Here plain text
         "label"    : "VV", #Here we can use weird glyphs
         "xsec"     : 3.74*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 3, # Green
         "isSig"    : False,
         "files"    : hdf5inpath(main_path + "ZZTo2L2Q/"),
         "extraWeights": lambda x: SF(x,17),
         "skim"     : "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/ZZTo2L2Q/skims.root"
  },
  "ZZ2l2nu": {
         "name"     : "ZZ2l2nu", #Here plain text
         "label"    : "VV", #Here we can use weird glyphs
         "xsec"     : 0.8738*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 3, # Green
         "isSig"    : False,
         "files"    : hdf5inpath(main_path + "ZZTo2L2Nu/"),
         "extraWeights": lambda x: SF(x,17),
         "skim"     : "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/ZZTo2L2Nu/skims.root"
  },

  "ZZ4l": {
         "name"     : "ZZ4l", #Here plain text
         "label"    : "VV", #Here we can use weird glyphs
         "xsec"     : 1.325*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 3, # Green
         "isSig"    : False,
         "files"    : hdf5inpath(main_path + "ZZTo4L/"),
         "extraWeights": lambda x: SF(x,17),
         "skim"     : "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/ZZTo4L/skims.root"
  },
  "ZG": {
         "name"     : "ZG", #Here plain text
         "label"    : "VV", #Here we can use weird glyphs
         "xsec"     : 51.1*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 3, # Green
         "isSig"    : False,
         "files"    : hdf5inpath(main_path + "ZG/"),
         "extraWeights": lambda x: SF(x,17),
         "skim"     : "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/ZG/skims.root"
  },
  "WG": {
         "name"     : "WG", #Here plain text
         "label"    : "VV", #Here we can use weird glyphs
         "xsec"     : 412.70*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 3, # Green
         "isSig"    : False,
         "files"    : hdf5inpath(main_path + "WG/"),
         "extraWeights": lambda x: SF(x,17),
         "skim"     : "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/WG/skims.root"
  },
  "ttZll": {
         "name"     : "ttZll", #Here plain text
         "label"    : "t#bar{t}X", #Here we can use weird glyphs
         "xsec"     : 0.2439*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 9, # Dark blue
         "isSig"    : False,
         "files"    : hdf5inpath(main_path + "TTZToLL/"),
         "extraWeights": lambda x: SF(x,17),
         "skim"     : "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/TTZToLL/skims.root"
  },
#  "ttWlnu": {
#         "name"     : "ttWlnu", #Here plain text
#         "label"    : "t#bar{t}X", #Here we can use weird glyphs
#         "xsec"     : 0.2161*1000*0.4, # in fb
#         "linecolor": ROOT.kBlack,
#         "fillcolor": 9, # Dark blue
#         "isSig"    : False,
#         "files"    : hdf5inpath(main_path + "TTWToLNu/"),
#         "extraWeights": lambda x: SF(x,17),
#         "skim"     : "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/TTWToLNu/skims.root"
#  },
  "ttWqq": {
         "name"     : "ttWqq", #Here plain text
         "label"    : "t#bar{t}X", #Here we can use weird glyphs
         "xsec"     : 0.4377*1000*0.4, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 9, # Dark blue
         "isSig"    : False,
         "files"    : hdf5inpath(main_path + "TTWToQQ/"),
         "extraWeights": lambda x: SF(x,17),
         "skim"     : "/eos/cms/store/group/phys_exotica/SUEPs/UL17/skim_2l_20_10/TTWToQQ/skims.root"
  },
  "SUEP_ZH_generic_new": {
         "name"     : "SUEP_ZH_generic_new", #Here plain text
         "label"    : "ZS^{gen, new}, m_{S} = 125 GeV", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kRed,
         "fillcolor": ROOT.kRed,
         "isSig"    : True,
         "files"    : hdf5inpath(main_path + "SUEP_generic_new_mS125_mD2_T2/"),
         "extraWeights": lambda x: SF(x,17),
  },
  "SUEP_ZH_leptonic": {
         "name"     : "SUEP_ZH_leptonic", #Here plain text
         "label"    : "ZS^{lep}, m_{S} = 125 GeV", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kBlue,
         "fillcolor": ROOT.kBlue,
         "isSig"    : True,
         "files"    : hdf5inpath(main_path + "SUEP_leptonic_mS125_mD2_T2/"),
         "extraWeights": lambda x: SF(x,17),
  },
  "SUEP_ZH_hadronic": {
         "name"     : "SUEP_ZH_hadronic", #Here plain text
         "label"    : "ZS^{had}, m_{S} = 125 GeV", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kGreen,
         "fillcolor": ROOT.kGreen,
         "isSig"    : True,
         "files"    : hdf5inpath(main_path + "SUEP_hadronic_mS125_mD2_T2/"),
         "extraWeights": lambda x: SF(x,17),
  },
}
