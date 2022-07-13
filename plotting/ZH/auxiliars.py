import ROOT
import numpy as np

##### SF files #####
#####  -UL18-  #####

muIDfile = ROOT.TFile("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/data/MuUL18/MuID.root","READ")
muID = muIDfile.Get("NUM_LooseID_DEN_TrackerMuons_abseta_pt")
muTrkfile = ROOT.TFile("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/data/MuUL18/MuTracking.root","READ")
muTrk = muIDfile.Get("NUM_TrackerMuons_DEN_genTracks")

eIDfile = ROOT.TFile("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/data/EGammaUL18/EGamma_Loose.root","READ")
eID = eIDfile.Get("EGamma_SF2D").Clone("eID") #Clone just in case pyroot does its thing
eRECOfile = ROOT.TFile("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/data/EGammaUL18/EGamma_recohighpt.root", "READ")
eRECO = eRECOfile.Get("EGamma_SF2D").Clone("eRECO") #Clone just in case pyroot does its thing

def SF(x):
  w = np.array([])
  for i in range(len(x)):
    np.append(w, getSF(x["nmuons"][i], x["leadlep_pt"][i], x["leadlep_eta"][i], x["subleadlep_pt"][i], x["subleadlep_eta"][i]))
  return w

def getSF(nmu, lep1pt, lep1eta, lep2pt, lep2eta):
  if nmu == 2:
    sf = getSF2Mu(lep1pt, lep1eta, lep2pt, lep2eta)
  else:
    sf = getSF2El(lep1pt, lep1eta, lep2pt, lep2eta)
  return sf


def getSFMu(lep1pt, lep1eta, lep2pt, lep2eta):
  return getSFMu(lep1pt, lep1eta)*getSFMu(lep2pt, lep2eta)

def getSFEl(lep1pt, lep1eta, lep2pt, lep2eta):
  return getSFEl(lep1pt, lep1eta)*getSFEl(lep2pt, lep2eta)


def getSFMu(pt, eta):
  sf  = muID.GetBinContent(min(1,muID.GetXaxis().FindBin(abs(eta))), min(1,muID.GetYaxis().FindBin(pt)))
  sf *= muTrk.GetBinContent(min(1,muTrk.GetXaxis().FindBin(abs(eta))), min(1,muTrk.GetYaxis().FindBin(pt)))
  return sf

def getSFEl(pt, eta):
  sf  = eID.GetBinContent(min(1,eID.GetXaxis().FindBin(eta)), min(1,eID.GetYaxis().FindBin(pt)))
  sf *= eRECO.GetBinContent(min(1,eRECO.GetXaxis().FindBin(eta)), min(1,eRECO.GetYaxis().FindBin(pt)))
  return sf

