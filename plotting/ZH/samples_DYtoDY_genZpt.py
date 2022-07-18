import os
import ROOT

def hdf5inpath(path):
  ret = []
  for f in os.listdir(path):
    if "hdf5" in f: 
      ret.append(path + "/" + f)
  #if len(ret) > 3: ret = ret[:2]
  return ret

order   = ["ttZ","VV", "WJets","ttto1l", "ttto2l", "DY_Pt650ToInf", "DY_Pt400To650","DY_Pt250To400","DY_Pt100To250","DY_Pt50To100", "DY_Pt0To50"]
samples = {
  "DY_Pt0To50": {
         "name"     : "DY_Pt0To50", #Here plain text
         "label"    : "DY (p_{T} < 50 GeV)", #Here we can use weird glyphs
         "xsec"     : 1469.*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 7, # Light blue
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/Zpt_xsectests_twolep/DY_Pt0To50/"),
         "skim"     : "/eos/user/c/cericeci/SUEP_signals/skim_UL18/DYToLL_M50_Pt0To50/skims.root"
  },
  "DY_Pt50To100": {
         "name"     : "DY_Pt50To100", #Here plain text
         "label"    : "DY (50 < p_{T} < 100 GeV)", #Here we can use weird glyphs
         "xsec"     : 391.14*1000., # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": ROOT.kCyan+1, # Light blue
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/Zpt_xsectests_twolep/DY_Pt50To100/"),
         "skim"     : "/eos/user/c/cericeci/SUEP_signals/skim_UL18/DYToLL_M50_Pt50To100/skims.root"
  },
  "DY_Pt100To250": {
         "name"     : "DY_Pt100To250", #Here plain text
         "label"    : "DY (100 < p_{T} < 250 GeV)", #Here we can use weird glyphs
         "xsec"     : 96.23*1000., # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": ROOT.kCyan+2, # Light blue
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/Zpt_xsectests_twolep/DY_Pt100To250/"),
         "skim"     : "/eos/user/c/cericeci/SUEP_signals/skim_UL18/DYToLL_M50_Pt100To250/skims.root"
  },
  "DY_Pt250To400": {
         "name"     : "DY_Pt250To400", #Here plain text
         "label"    : "DY (250 < p_{T} < 400 GeV)", #Here we can use weird glyphs
         "xsec"     : 3.499*1000., # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": ROOT.kCyan+3, # Light blue
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/Zpt_xsectests_twolep/DY_Pt250To400/"),
         "skim"     : "/eos/user/c/cericeci/SUEP_signals/skim_UL18/DYToLL_M50_Pt250To400/skims.root"
  },
  "DY_Pt400To650": {
         "name"     : "DY_Pt400To650", #Here plain text
         "label"    : "DY (400 < p_{T} < 650 GeV)", #Here we can use weird glyphs
         "xsec"     : 0.4765*1000., # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": ROOT.kCyan+4, # Light blue
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/Zpt_xsectests_twolep/DY_Pt400To650/"),
         "skim"     : "/eos/user/c/cericeci/SUEP_signals/skim_UL18/DYToLL_M50_Pt400To650/skims.root"
  },
  "DY_Pt650ToInf": {
         "name"     : "DY_Pt650ToInf", #Here plain text
         "label"    : "DY (p_{T} > 650 GeV)", #Here we can use weird glyphs
         "xsec"     : 0.04489*1000., # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": ROOT.kOrange, # Light blue
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/Zpt_xsectests_twolep/DY_Pt650ToInf/"),
         "skim"     : "/eos/user/c/cericeci/SUEP_signals/skim_UL18/DYToLL_M50_Pt650ToInf/skims.root" 
  },
  "DY" : {
         "name"     : "DY", #Here plain text
         "label"    : "DY (inclusive)", #Here we can use weird glyphs
         "xsec"     : 6309*1000., # in fb
         "linecolor": ROOT.kBlue,
         "fillcolor": ROOT.kBlue,
         "isSig"    : True,
         "files"    :  hdf5inpath("/eos/home-c/cericeci/SUEP/Zpt_xsectests_twolep/DY_inclusive"),
  },
}
