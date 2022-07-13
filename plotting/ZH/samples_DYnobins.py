import os
import ROOT

def hdf5inpath(path):
  ret = []
  for f in os.listdir(path):
    if "hdf5" in f: 
      ret.append(path + "/" + f)
  #if len(ret) > 3: ret = ret[:2]
  return ret

order   = ["ttZ","VV", "WJets","ttto1l", "ttto2l", "DY"]
samples = {
  "data": {
         "name" : "data",
         "label": "Data",
         "xsec" : -1,
         "lineColor": ROOT.kBlack,
         "fillcolor": ROOT.kBlack,
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/17_05_2022/data/"),
         "markerstyle": 20,
         "markersize" : 1,
  },      
  "DY" : {
         "name"     : "ttto2l", #Here plain text
         "label"    : "DY", #Here we can use weird glyphs
         "xsec"     : 2008.*3*1000., # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 7, # Red
         "isSig"    : False,
         "files"    :  hdf5inpath("/eos/home-c/cericeci/SUEP/10_05_2022/DY"),
  },
  "ttto2l": {
         "name"     : "ttto2l", #Here plain text
         "label"    : "t#bar{t} (2l)", #Here we can use weird glyphs
         "xsec"     : 831.76*((3*0.108)**2)*1000., # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 2, # Red
         "isSig"    : False,
         "files"    :  hdf5inpath("/eos/home-c/cericeci/SUEP/17_05_2022/TTTpo2L2Nu/"),
         "skim"     : "/eos/user/c/cericeci/SUEP_signals/skim_UL18/TTTo2L2Nu/skims.root"
  },
  "ttto1l": {
         "name"     : "ttto1l", #Here plain text
         "label"    : "t#bar{t} (1l)", #Here we can use weird glyphs
         "xsec"     : 831.76*(3*0.108)*(1-3*0.108)*1000., # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 5, # Yellow
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/10_05_2022/TT_semilep/")
  },

  "Wjets": {
         "name"     : "Wjets", #Here plain text
         "label"    : "W", #Here we can use weird glyphs
         "xsec"     : 20508.9*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 6, # Purple
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/17_05_2022/WJets/"), 
         "skim"     : "/eos/user/c/cericeci/SUEP_signals/skim_UL18/WJets/skims.root",
  },
  "VV": {
         "name"     : "VV", #Here plain text
         "label"    : "VV", #Here we can use weird glyphs
         "xsec"     : 10.481*1000, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 3, # Green
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/10_05_2022/WW/"),
  },
  "ttZ": {
         "name"     : "ttZ", #Here plain text
         "label"    : "t#bar{t}X", #Here we can use weird glyphs
         "xsec"     : 0.78*1000*0.4, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": 9, # Dark blue
         "isSig"    : False,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/10_05_2022/TTZ_LL/")
  },
  "SUEP_ZH_generic": {
         "name"     : "SUEP_ZH_generic", #Here plain text
         "label"    : "ZS^{gen}, m_{S} = 125 GeV", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kBlack,
         "fillcolor": ROOT.kBlack,
         "isSig"    : True,
         "files"    : ["/eos/home-c/cericeci/SUEP/10_05_2022/ZH_generic//out_1_1_1001.hdf5"],
  },
  "SUEP_ZH_leptonic": {
         "name"     : "SUEP_ZH_leptonic", #Here plain text
         "label"    : "ZS^{lep}, m_{S} = 125 GeV", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kGreen,
         "fillcolor": ROOT.kGreen,
         "isSig"    : True,
         "files"    : ["/eos/home-c/cericeci/SUEP/10_05_2022/ZH_leptonic//out_1_1_1101.hdf5"],
  },

  "SUEP_ZH_hadronic": {
         "name"     : "SUEP_ZH_hadronic", #Here plain text
         "label"    : "ZS^{had}, m_{S} = 125 GeV", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kBlue,
         "fillcolor": ROOT.kBlue,
         "isSig"    : True,
         "files"    : ["/eos/home-c/cericeci/SUEP/10_05_2022/ZH_hadronic//out_1_1_1001.hdf5"],
  },

}
