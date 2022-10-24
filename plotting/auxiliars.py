import ROOT
import numpy as np
import os

##### SF files #####

#####  -UL18-  #####
SUEP_BASE = os.path.dirname(os.path.realpath(__file__).replace("/plotting",""))

muIDfile[18] = ROOT.TFile(SUEP_BASE + "/data/MuUL18/MuID.root","READ")
muID[18] = muIDfile.Get("NUM_LooseID_DEN_TrackerMuons_abseta_pt")
maxmidx[18] = muID.GetNbinsX()
maxmidy[18] = muID.GetNbinsY()

muISOfile[18] = ROOT.TFile(SUEP_BASE + "/data/MuUL18/MuISO.root","READ")
muISO[18] = muISOfile.Get("NUM_LooseRelIso_DEN_LooseID_abseta_pt")
maxmisox[18] = muISO.GetNbinsX()
maxmisoy[18] = muISO.GetNbinsY()

muTrkfile[18] = ROOT.TFile(SUEP_BASE + "/data/MuUL18/MuTracking.root","READ")
muTrk[18] = muTrkfile.Get("NUM_TrackerMuons_DEN_genTracks")
maxmtx[18] = muTrk.GetNbinsX()
maxmty[18] = muTrk.GetNbinsY()

eIDfile[18] = ROOT.TFile(SUEP_BASE + "/data/EGammaUL18/egammaEffi.txt_Ele_wp90iso_EGM2D.root","READ")
eID[18] = eIDfile.Get("EGamma_SF2D").Clone("eID18") #Clone just in case pyroot does its thing
maxeidx[18] = eID.GetNbinsX()
maxeidy[18] = eID.GetNbinsY()

eRECOfile[18] = ROOT.TFile(SUEP_BASE + "/data/EGammaUL18/EGamma_recohighpt.root", "READ")
eRECO[18] = eRECOfile.Get("EGamma_SF2D").Clone("eRECO18") #Clone just in case pyroot does its thing
maxerex[18] = eRECO.GetNbinsX()
maxerey[18] = eRECO.GetNbinsY()

#####  -UL17-  #####
muIDfile[17] = ROOT.TFile(SUEP_BASE + "/data/MuUL17/MuID.root","READ")
muID[17] = muIDfile.Get("NUM_LooseID_DEN_TrackerMuons_abseta_pt")
maxmidx[17] = muID.GetNbinsX()
maxmidy[17] = muID.GetNbinsY()

muISOfile[17] = ROOT.TFile(SUEP_BASE + "/data/MuUL17/MuISO.root","READ")
muISO[17] = muISOfile.Get("NUM_LooseRelIso_DEN_LooseID_abseta_pt")
maxmisox[17] = muISO.GetNbinsX()
maxmisoy[17] = muISO.GetNbinsY()

muTrkfile[17] = ROOT.TFile(SUEP_BASE + "/data/MuUL17/MuTracking.root","READ")
muTrk[17] = muTrkfile.Get("NUM_TrackerMuons_DEN_genTracks")
maxmtx[17] = muTrk.GetNbinsX()
maxmty[17] = muTrk.GetNbinsY()

eIDfile[17] = ROOT.TFile(SUEP_BASE + "/data/EGammaUL17/egammaEffi.txt_Ele_wp90iso_EGM2D.root","READ")
eID[17] = eIDfile.Get("EGamma_SF2D").Clone("eID17") #Clone just in case pyroot does its thing
maxeidx[17] = eID.GetNbinsX()
maxeidy[17] = eID.GetNbinsY()

eRECOfile[17] = ROOT.TFile(SUEP_BASE + "/data/EGammaUL17/EGamma_recohighpt.root", "READ")
eRECO[17] = eRECOfile.Get("EGamma_SF2D").Clone("eRECO17") #Clone just in case pyroot does its thing
maxerex[17] = eRECO.GetNbinsX()
maxerey[17] = eRECO.GetNbinsY()

#####  -UL16-  #####
muIDfile[16] = ROOT.TFile(SUEP_BASE + "/data/MuUL16/MuID.root","READ")
muID[16] = muIDfile.Get("NUM_LooseID_DEN_TrackerMuons_abseta_pt")
maxmidx[16] = muID.GetNbinsX()
maxmidy[16] = muID.GetNbinsY()

muISOfile[16] = ROOT.TFile(SUEP_BASE + "/data/MuUL16/MuISO.root","READ")
muISO[16] = muISOfile.Get("NUM_LooseRelIso_DEN_LooseID_abseta_pt")
maxmisox[16] = muISO.GetNbinsX()
maxmisoy[16] = muISO.GetNbinsY()

muTrkfile[16] = ROOT.TFile(SUEP_BASE + "/data/MuUL16/MuTracking.root","READ")
muTrk[16] = muTrkfile.Get("NUM_TrackerMuons_DEN_genTracks")
maxmtx[16] = muTrk.GetNbinsX()
maxmty[16] = muTrk.GetNbinsY()

eIDfile[16] = ROOT.TFile(SUEP_BASE + "/data/EGammaUL16/egammaEffi.txt_Ele_wp90iso_EGM2D.root","READ")
eID[16] = eIDfile.Get("EGamma_SF2D").Clone("eID16") #Clone just in case pyroot does its thing
maxeidx[16] = eID.GetNbinsX()
maxeidy[16] = eID.GetNbinsY()

eRECOfile[16] = ROOT.TFile(SUEP_BASE + "/data/EGammaUL16/EGamma_recohighpt.root", "READ")
eRECO[16] = eRECOfile.Get("EGamma_SF2D").Clone("eRECO16") #Clone just in case pyroot does its thing
maxerex[16] = eRECO.GetNbinsX()
maxerey[16] = eRECO.GetNbinsY()

#####  -UL16APV- => 15 (not true but helpful way to classify it)  #####
muIDfile[15] = ROOT.TFile(SUEP_BASE + "/data/MuUL16APV/MuID.root","READ")
muID[15] = muIDfile.Get("NUM_LooseID_DEN_TrackerMuons_abseta_pt")
maxmidx[15] = muID.GetNbinsX()
maxmidy[15] = muID.GetNbinsY()

muISOfile[15] = ROOT.TFile(SUEP_BASE + "/data/MuUL16APV/MuISO.root","READ")
muISO[15] = muISOfile.Get("NUM_LooseRelIso_DEN_LooseID_abseta_pt")
maxmisox[15] = muISO.GetNbinsX()
maxmisoy[15] = muISO.GetNbinsY()

muTrkfile[15] = ROOT.TFile(SUEP_BASE + "/data/MuUL16APV/MuTracking.root","READ")
muTrk[15] = muTrkfile.Get("NUM_TrackerMuons_DEN_genTracks")
maxmtx[15] = muTrk.GetNbinsX()
maxmty[15] = muTrk.GetNbinsY()

eIDfile[15] = ROOT.TFile(SUEP_BASE + "/data/EGammaUL16APV/egammaEffi.txt_Ele_wp90iso_EGM2D.root","READ")
eID[15] = eIDfile.Get("EGamma_SF2D").Clone("eID16APV") #Clone just in case pyroot does its thing
maxeidx[15] = eID.GetNbinsX()
maxeidy[15] = eID.GetNbinsY()

eRECOfile[15] = ROOT.TFile(SUEP_BASE + "/data/EGammaUL16APV/EGamma_recohighpt.root", "READ")
eRECO[15] = eRECOfile.Get("EGamma_SF2D").Clone("eRECO16APV") #Clone just in case pyroot does its thing
maxerex[15] = eRECO.GetNbinsX()
maxerey[15] = eRECO.GetNbinsY()


def getSFMu(pt, eta, year):
  sf  = muID[year].GetBinContent(min(max(1,muID.GetXaxis().FindBin(abs(eta))),maxmidx), min(max(1,muID.GetYaxis().FindBin(pt)),maxmidy))
  sf *= muTrk[year].GetBinContent(min(max(1,muTrk.GetXaxis().FindBin(abs(eta))),maxmtx), min(max(1,muTrk.GetYaxis().FindBin(pt)),maxmty))
  sf *= muISO[year].GetBinContent(min(max(1,muISO.GetXaxis().FindBin(abs(eta))),maxmisox), min(max(1,muISO.GetYaxis().FindBin(pt)),maxmisoy))
  return sf

def getSFEl(pt, eta, year):
  sf  = eID[year].GetBinContent(min(max(1,eID.GetXaxis().FindBin(eta)),maxeidx), min(max(1,eID.GetYaxis().FindBin(pt)),maxeidy))
  sf *= eRECO[year].GetBinContent(min(max(1,eRECO.GetXaxis().FindBin(eta)),maxerex), min(max(1,eRECO.GetYaxis().FindBin(pt)),maxerey))
  return sf

def getSF2Mu(lep1pt, lep1eta, lep2pt, lep2eta, year):
  return getSFMu(lep1pt, lep1eta, year)*getSFMu(lep2pt, lep2eta, year)

def getSF2El(lep1pt, lep1eta, lep2pt, lep2eta, year):
  return getSFEl(lep1pt, lep1eta, year)*getSFEl(lep2pt, lep2eta, year)


def getSF(nmu, lep1pt, lep1eta, lep2pt, lep2eta, year):
  if nmu == 2:
    sf = getSF2Mu(lep1pt, lep1eta, lep2pt, lep2eta, year)
  else:
    sf = getSF2El(lep1pt, lep1eta, lep2pt, lep2eta, year)
  return sf

def SF(x, year):
  w = np.array([])
  for i in range(len(x)):
    w = np.append(w, getSF(x["nmuons"][i], x["leadlep_pt"][i], x["leadlep_eta"][i], x["subleadlep_pt"][i], x["subleadlep_eta"][i]), year)
    #print(w)
  return w


Zptfile = ROOT.TFile(SUEP_BASE + "/data/ZptUL18/Zpt_corr.root","READ")
ZptHist = Zptfile.Get("Zpt_SF")
maxZx   = ZptHist.GetNbinsX()
maxZy   = ZptHist.GetNbinsY()

def correctZpt(x):
  sf = ZptHist.GetBinContent(min(max(1, ZptHist.GetXaxis().FindBin(x["Z_pt"])), maxZx), min(max(1, ZptHist.GetYaxis().FindBin(x["Z_eta"])), maxZy))
  return sf

