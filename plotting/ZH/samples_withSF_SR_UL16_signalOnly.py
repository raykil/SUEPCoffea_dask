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
samples = {
  "SUEP_ZH_generic_nominal": {
         "name"     : "SUEP_ZH_generic", #Here plain text
         "label"    : "ZS^{gen}", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kBlue,
         "fillcolor": ROOT.kBlue,
         "isSig"    : False, # So this is a histogram
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*SF(x,16),
  },
  "SUEP_ZH_generic_ElSFUp": {
         "name"     : "SUEP_ZH_generic_ElSFUp", #Here plain text
         "label"    : "ZS^{gen}, ElSF Up", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kGreen,
         "fillcolor": ROOT.kGreen,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*SF(x,16, 2),
  },

  "SUEP_ZH_generic_ElSFDn": {
         "name"     : "SUEP_ZH_generic_ElSFDn", #Here plain text
         "label"    : "ZS^{gen}, ElSF Down", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kRed,
         "fillcolor": ROOT.kRed,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*SF(x,16,-2),
  },

  "SUEP_ZH_generic_MuSFUp": {
         "name"     : "SUEP_ZH_generic_MuSFUp", #Here plain text
         "label"    : "ZS^{gen}, MuSF Up", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kGreen,
         "fillcolor": ROOT.kGreen,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*SF(x,16, 1),
  },

  "SUEP_ZH_generic_MuSFDn": {
         "name"     : "SUEP_ZH_generic_MuSFDn", #Here plain text
         "label"    : "ZS^{gen}, MuSF Down", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kRed,
         "fillcolor": ROOT.kRed,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*SF(x,16,-1),
  },

  "SUEP_ZH_generic_PUUp": {
         "name"     : "SUEP_ZH_generic_PUUp", #Here plain text
         "label"    : "ZS^{gen}, PU Up", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kGreen,
         "fillcolor": ROOT.kGreen,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["PUWeight_Up"]*x["L1prefireWeight"]*x["bTagWeight"]*SF(x,16),
  },

  "SUEP_ZH_generic_PUDn": {
         "name"     : "SUEP_ZH_generic_PUDn", #Here plain text
         "label"    : "ZS^{gen}, PU Down", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kRed,
         "fillcolor": ROOT.kRed,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["PUWeight_Dn"]*x["L1prefireWeight"]*x["bTagWeight"]*SF(x,16),
  },

  "SUEP_ZH_generic_L1Up": {
         "name"     : "SUEP_ZH_generic_L1Up", #Here plain text
         "label"    : "ZS^{gen}, L1 Up", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kGreen,
         "fillcolor": ROOT.kGreen,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight_Up"]*x["bTagWeight"]*SF(x,16),
  },

  "SUEP_ZH_generic_L1Dn": {
         "name"     : "SUEP_ZH_generic_L1Dn", #Here plain text
         "label"    : "ZS^{gen}, L1 Down", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kRed,
         "fillcolor": ROOT.kRed,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight_Dn"]*x["bTagWeight"]*SF(x,16),
  },

  "SUEP_ZH_generic_HFCorrUp": {
         "name"     : "SUEP_ZH_generic_HFCorrUp", #Here plain text
         "label"    : "ZS^{gen}, HFCorr Up", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kGreen,
         "fillcolor": ROOT.kGreen,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight_HFCorr_Up"]*SF(x,16),
  },

  "SUEP_ZH_generic_HFCorrDn": {
         "name"     : "SUEP_ZH_generic_HFCorrDn", #Here plain text
         "label"    : "ZS^{gen}, HFCorr Down", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kRed,
         "fillcolor": ROOT.kRed,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight_HFCorr_Dn"]*SF(x,16),
  },

  "SUEP_ZH_generic_LFCorrUp": {
         "name"     : "SUEP_ZH_generic_LFCorrUp", #Here plain text
         "label"    : "ZS^{gen}, LFCorr Up", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kGreen,
         "fillcolor": ROOT.kGreen,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight_LFCorr_Up"]*SF(x,16),
  },

  "SUEP_ZH_generic_LFCorrDn": {
         "name"     : "SUEP_ZH_generic_LFCorrDn", #Here plain text
         "label"    : "ZS^{gen}, LFCorr Down", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kRed,
         "fillcolor": ROOT.kRed,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight_LFCorr_Dn"]*SF(x,16),
  },

  "SUEP_ZH_generic_HFUnCorrUp": {
         "name"     : "SUEP_ZH_generic_HFUnCorrUp", #Here plain text
         "label"    : "ZS^{gen}, HFUnCorr Up", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kGreen,
         "fillcolor": ROOT.kGreen,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight_HFUnCorr_Up"]*SF(x,16),
  },

  "SUEP_ZH_generic_HFUnCorrDn": {
         "name"     : "SUEP_ZH_generic_HFUnCorrDn", #Here plain text
         "label"    : "ZS^{gen}, HFUnCorr Down", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kRed,
         "fillcolor": ROOT.kRed,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight_HFUnCorr_Dn"]*SF(x,16),
  },

  "SUEP_ZH_generic_LFUnCorrUp": {
         "name"     : "SUEP_ZH_generic_LFUnCorrUp", #Here plain text
         "label"    : "ZS^{gen}, LFUnCorr Up", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kGreen,
         "fillcolor": ROOT.kGreen,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight_LFUnCorr_Up"]*SF(x,16),
  },

  "SUEP_ZH_generic_LFUnCorrDn": {
         "name"     : "SUEP_ZH_generic_LFUnCorrDn", #Here plain text
         "label"    : "ZS^{gen}, LFUnCorr Down", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kRed,
         "fillcolor": ROOT.kRed,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight_LFUnCorr_Dn"]*SF(x,16),
  },

  "SUEP_ZH_generic_ISRUp": {
         "name"     : "SUEP_ZH_generic_ISRUp", #Here plain text
         "label"    : "ZS^{gen}, ISR Up", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kGreen,
         "fillcolor": ROOT.kGreen,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["ISRWeight_Up"]*x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*SF(x,16),
  },

  "SUEP_ZH_generic_ISRDn": {
         "name"     : "SUEP_ZH_generic_ISRDn", #Here plain text
         "label"    : "ZS^{gen}, ISR Down", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kRed,
         "fillcolor": ROOT.kRed,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["ISRWeight_Dn"]*x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*SF(x,16),
  },

  "SUEP_ZH_generic_FSRUp": {
         "name"     : "SUEP_ZH_generic_FSRUp", #Here plain text
         "label"    : "ZS^{gen}, FSR Up", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kGreen,
         "fillcolor": ROOT.kGreen,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["FSRWeight_Up"]*x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*SF(x,16),
  },

  "SUEP_ZH_generic_FSRDn": {
         "name"     : "SUEP_ZH_generic_FSRDn", #Here plain text
         "label"    : "ZS^{gen}, FSR Down", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kRed,
         "fillcolor": ROOT.kRed,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["FSRWeight_Dn"]*x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*SF(x,16),
  },

  "SUEP_ZH_generic_JESUp": {
         "name"     : "SUEP_ZH_generic_JESUp", #Here plain text
         "label"    : "ZS^{gen}, JES Up", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kGreen,
         "fillcolor": ROOT.kGreen,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*SF(x,16),
         "replaceChannel": {"SR":"SR_JECUP"}
  },

  "SUEP_ZH_generic_JESDn": {
         "name"     : "SUEP_ZH_generic_JESDn", #Here plain text
         "label"    : "ZS^{gen}, JES Down", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kRed,
         "fillcolor": ROOT.kRed,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*SF(x,16),
         "replaceChannel": {"SR":"SR_JECDOWN"}
  },

  "SUEP_ZH_generic_JERUp": {
         "name"     : "SUEP_ZH_generic_JERUp", #Here plain text
         "label"    : "ZS^{gen}, JER Up", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kGreen,
         "fillcolor": ROOT.kGreen,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*SF(x,16),
         "replaceChannel": {"SR":"SR_JERUP"}
  },

  "SUEP_ZH_generic_JERDn": {
         "name"     : "SUEP_ZH_generic_JERDn", #Here plain text
         "label"    : "ZS^{gen}, JER Down", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kRed,
         "fillcolor": ROOT.kRed,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*SF(x,16),
         "replaceChannel": {"SR":"SR_JERDOWN"}
  },

  "SUEP_ZH_generic_TRACKUp": {
         "name"     : "SUEP_ZH_generic_TRACKUp", #Here plain text
         "label"    : "ZS^{gen}, TRACK Up", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kGreen,
         "fillcolor": ROOT.kGreen,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*SF(x,16),
         "replaceChannel": {"SR":"SR_TRACKUP"}
  },
  "SUEP_ZH_generic_ElScaleUp": {
         "name"     : "SUEP_ZH_generic_ElScaleUp", #Here plain text
         "label"    : "ZS^{gen}, ElScale Up", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kGreen,
         "fillcolor": ROOT.kGreen,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*SF(x,16),
         "replaceChannel": {"SR":"SR_ElScaleUp"}
  },
  "SUEP_ZH_generic_ElScaleDown": {
         "name"     : "SUEP_ZH_generic_ElScaleDown", #Here plain text
         "label"    : "ZS^{gen}, ElScale Down", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kRed,
         "fillcolor": ROOT.kRed,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*SF(x,16),
         "replaceChannel": {"SR":"SR_ElScaleDown"}
  },
  "SUEP_ZH_generic_ElSigmaUp": {
         "name"     : "SUEP_ZH_generic_ElSigmaUp", #Here plain text
         "label"    : "ZS^{gen}, ElSigma Up", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kGreen,
         "fillcolor": ROOT.kGreen,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*SF(x,16),
         "replaceChannel": {"SR":"SR_ElSigmaUp"}
  },
  "SUEP_ZH_generic_ElSigmaDown": {
         "name"     : "SUEP_ZH_generic_ElSigmaDown", #Here plain text
         "label"    : "ZS^{gen}, ElSigma Down", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kRed,
         "fillcolor": ROOT.kRed,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*SF(x,16),
         "replaceChannel": {"SR":"SR_ElSigmaDown"}
  },
  "SUEP_ZH_generic_MuScaleUp": {
         "name"     : "SUEP_ZH_generic_MuScaleUp", #Here plain text
         "label"    : "ZS^{gen}, MuScale Up", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kGreen,
         "fillcolor": ROOT.kGreen,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*SF(x,16),
         "replaceChannel": {"SR":"SR_MuScaleUp"}
  },
  "SUEP_ZH_generic_MuScaleDown": {
         "name"     : "SUEP_ZH_generic_MuScaleDown", #Here plain text
         "label"    : "ZS^{gen}, MuScale Down", #Here we can use weird glyphs
         "xsec"     : 870 * 0.0336 * 2, # in fb
         "linecolor": ROOT.kRed,
         "fillcolor": ROOT.kRed,
         "isSig"    : True,
         "files"    : hdf5inpath("/eos/home-c/cericeci/SUEP/SUEPCoffea_dask/scaleTests/UL16/"),
         "extraWeights": lambda x: x["PUWeight"]*x["L1prefireWeight"]*x["bTagWeight"]*SF(x,16),
         "replaceChannel": {"SR":"SR_MuScaleDown"}
  },

}
