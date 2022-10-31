import ROOT
import numpy as np
import os

##### SF files #####

muIDfile = {}
muID     = {}
maxmidx  = {}
maxmidy  = {}

muISOfile = {}
muISO     = {}
maxmisox  = {}
maxmisoy  = {}

muTrkfile = {}
muTrk     = {}
maxmtx    = {}
maxmty    = {}

eIDfile   = {}
eID       = {}
maxeidx   = {}
maxeidy   = {}

eRECOfile = {}
eRECO     = {}
maxerex   = {}
maxerey   = {}

#####  -UL18-  #####
SUEP_BASE = os.path.dirname(os.path.realpath(__file__).replace("/plotting",""))

muIDfile[18] = ROOT.TFile(SUEP_BASE + "/data/MuUL18/MuID.root","READ")
muID[18] = muIDfile[18].Get("NUM_LooseID_DEN_TrackerMuons_abseta_pt")
maxmidx[18] = muID[18].GetNbinsX()
maxmidy[18] = muID[18].GetNbinsY()

muISOfile[18] = ROOT.TFile(SUEP_BASE + "/data/MuUL18/MuISO.root","READ")
muISO[18] = muISOfile[18].Get("NUM_LooseRelIso_DEN_LooseID_abseta_pt")
maxmisox[18] = muISO[18].GetNbinsX()
maxmisoy[18] = muISO[18].GetNbinsY()

muTrkfile[18] = ROOT.TFile(SUEP_BASE + "/data/MuUL18/MuTracking.root","READ")
muTrk[18] = muTrkfile[18].Get("NUM_TrackerMuons_DEN_genTracks")
maxmtx[18] = muTrk[18].GetNbinsX()
maxmty[18] = muTrk[18].GetNbinsY()

eIDfile[18] = ROOT.TFile(SUEP_BASE + "/data/EGammaUL18/egammaEffi.txt_Ele_wp90iso_EGM2D.root","READ")
eID[18] = eIDfile[18].Get("EGamma_SF2D").Clone("eID18") #Clone just in case pyroot does its thing
maxeidx[18] = eID[18].GetNbinsX()
maxeidy[18] = eID[18].GetNbinsY()

eRECOfile[18] = ROOT.TFile(SUEP_BASE + "/data/EGammaUL18/EGamma_recohighpt.root", "READ")
eRECO[18] = eRECOfile[18].Get("EGamma_SF2D").Clone("eRECO18") #Clone just in case pyroot does its thing
maxerex[18] = eRECO[18].GetNbinsX()
maxerey[18] = eRECO[18].GetNbinsY()

#####  -UL17-  #####
muIDfile[17] = ROOT.TFile(SUEP_BASE + "/data/MuUL17/MuID.root","READ")
muID[17] = muIDfile[17].Get("NUM_LooseID_DEN_TrackerMuons_abseta_pt")
maxmidx[17] = muID[17].GetNbinsX()
maxmidy[17] = muID[17].GetNbinsY()

muISOfile[17] = ROOT.TFile(SUEP_BASE + "/data/MuUL17/MuISO.root","READ")
muISO[17] = muISOfile[17].Get("NUM_LooseRelIso_DEN_LooseID_abseta_pt")
maxmisox[17] = muISO[17].GetNbinsX()
maxmisoy[17] = muISO[17].GetNbinsY()

muTrkfile[17] = ROOT.TFile(SUEP_BASE + "/data/MuUL17/MuTracking.root","READ")
muTrk[17] = muTrkfile[17].Get("NUM_TrackerMuons_DEN_genTracks")
maxmtx[17] = muTrk[17].GetNbinsX()
maxmty[17] = muTrk[17].GetNbinsY()

eIDfile[17] = ROOT.TFile(SUEP_BASE + "/data/EGammaUL17/egammaEffi.txt_Ele_wp90iso_EGM2D.root","READ")
eID[17] = eIDfile[17].Get("EGamma_SF2D").Clone("eID17") #Clone just in case pyroot does its thing
maxeidx[17] = eID[17].GetNbinsX()
maxeidy[17] = eID[17].GetNbinsY()

eRECOfile[17] = ROOT.TFile(SUEP_BASE + "/data/EGammaUL17/EGamma_recohighpt.root", "READ")
eRECO[17] = eRECOfile[17].Get("EGamma_SF2D").Clone("eRECO17") #Clone just in case pyroot does its thing
maxerex[17] = eRECO[17].GetNbinsX()
maxerey[17] = eRECO[17].GetNbinsY()

#####  -UL16-  #####
muIDfile[16] = ROOT.TFile(SUEP_BASE + "/data/MuUL16/MuID.root","READ")
muID[16] = muIDfile[16].Get("NUM_LooseID_DEN_TrackerMuons_abseta_pt")
maxmidx[16] = muID[16].GetNbinsX()
maxmidy[16] = muID[16].GetNbinsY()

muISOfile[16] = ROOT.TFile(SUEP_BASE + "/data/MuUL16/MuISO.root","READ")
muISO[16] = muISOfile[16].Get("NUM_LooseRelIso_DEN_LooseID_abseta_pt")
maxmisox[16] = muISO[16].GetNbinsX()
maxmisoy[16] = muISO[16].GetNbinsY()

muTrkfile[16] = ROOT.TFile(SUEP_BASE + "/data/MuUL16/MuTracking.root","READ")
muTrk[16] = muTrkfile[16].Get("NUM_TrackerMuons_DEN_genTracks")
maxmtx[16] = muTrk[16].GetNbinsX()
maxmty[16] = muTrk[16].GetNbinsY()

eIDfile[16] = ROOT.TFile(SUEP_BASE + "/data/EGammaUL16/egammaEffi.txt_Ele_wp90iso_EGM2D.root","READ")
eID[16] = eIDfile[16].Get("EGamma_SF2D").Clone("eID16") #Clone just in case pyroot does its thing
maxeidx[16] = eID[16].GetNbinsX()
maxeidy[16] = eID[16].GetNbinsY()

eRECOfile[16] = ROOT.TFile(SUEP_BASE + "/data/EGammaUL16/EGamma_recohighpt.root", "READ")
eRECO[16] = eRECOfile[16].Get("EGamma_SF2D").Clone("eRECO16") #Clone just in case pyroot does its thing
maxerex[16] = eRECO[16].GetNbinsX()
maxerey[16] = eRECO[16].GetNbinsY()

#####  -UL16APV- => 15 (not true but helpful way to classify it)  #####
muIDfile[15] = ROOT.TFile(SUEP_BASE + "/data/MuUL16APV/MuID.root","READ")
muID[15] = muIDfile[15].Get("NUM_LooseID_DEN_TrackerMuons_abseta_pt")
maxmidx[15] = muID[15].GetNbinsX()
maxmidy[15] = muID[15].GetNbinsY()

muISOfile[15] = ROOT.TFile(SUEP_BASE + "/data/MuUL16APV/MuISO.root","READ")
muISO[15] = muISOfile[15].Get("NUM_LooseRelIso_DEN_LooseID_abseta_pt")
maxmisox[15] = muISO[15].GetNbinsX()
maxmisoy[15] = muISO[15].GetNbinsY()

muTrkfile[15] = ROOT.TFile(SUEP_BASE + "/data/MuUL16APV/MuTracking.root","READ")
muTrk[15] = muTrkfile[15].Get("NUM_TrackerMuons_DEN_genTracks")
maxmtx[15] = muTrk[15].GetNbinsX()
maxmty[15] = muTrk[15].GetNbinsY()

eIDfile[15] = ROOT.TFile(SUEP_BASE + "/data/EGammaUL16APV/egammaEffi.txt_Ele_wp90iso_EGM2D.root","READ")
eID[15] = eIDfile[15].Get("EGamma_SF2D").Clone("eID16APV") #Clone just in case pyroot does its thing
maxeidx[15] = eID[15].GetNbinsX()
maxeidy[15] = eID[15].GetNbinsY()

eRECOfile[15] = ROOT.TFile(SUEP_BASE + "/data/EGammaUL16APV/EGamma_recohighpt.root", "READ")
eRECO[15] = eRECOfile[15].Get("EGamma_SF2D").Clone("eRECO16APV") #Clone just in case pyroot does its thing
maxerex[15] = eRECO[15].GetNbinsX()
maxerey[15] = eRECO[15].GetNbinsY()


def getSFMu(pt, eta, year):
  sf  = muID[year].GetBinContent(min(max(1,muID[year].GetXaxis().FindBin(abs(eta))),maxmidx[year]), min(max(1,muID[year].GetYaxis().FindBin(pt)),maxmidy[year]))
  #print("SFMuID:", sf, min(max(1,muID[year].GetXaxis().FindBin(abs(eta))),maxmidx[year]), min(max(1,muID[year].GetYaxis().FindBin(pt)),maxmidy[year]))
  sf *= muTrk[year].GetBinContent(min(max(1,muTrk[year].GetXaxis().FindBin(abs(eta))),maxmtx[year]), min(max(1,muTrk[year].GetYaxis().FindBin(pt)),maxmty[year]))
  #print("SFMuTrk:", sf, min(max(1,muTrk[year].GetXaxis().FindBin(abs(eta))),maxmtx[year]), min(max(1,muTrk[year].GetYaxis().FindBin(pt)),maxmty[year]))
  sf *= muISO[year].GetBinContent(min(max(1,muISO[year].GetXaxis().FindBin(abs(eta))),maxmisox[year]), min(max(1,muISO[year].GetYaxis().FindBin(pt)),maxmisoy[year]))
  #print("SFMuISO:", sf, min(max(1,muISO[year].GetXaxis().FindBin(abs(eta))),maxmisox[year]), min(max(1,muISO[year].GetYaxis().FindBin(pt)),maxmisoy[year]))
  return sf

def getSFEl(pt, eta, year):
  sf  = eID[year].GetBinContent(min(max(1,eID[year].GetXaxis().FindBin(eta)),maxeidx[year]), min(max(1,eID[year].GetYaxis().FindBin(pt)),maxeidy[year]))
  #print("SFElID:", sf, min(max(1,eID[year].GetXaxis().FindBin(eta)),maxeidx[year]), min(max(1,eID[year].GetYaxis().FindBin(pt)),maxeidy[year]))
  sf *= eRECO[year].GetBinContent(min(max(1,eRECO[year].GetXaxis().FindBin(eta)),maxerex[year]), min(max(1,eRECO[year].GetYaxis().FindBin(pt)),maxerey[year]))
  #print("SFElReco:", sf, min(max(1,eRECO[year].GetXaxis().FindBin(eta)),maxerex[year]), min(max(1,eRECO[year].GetYaxis().FindBin(pt)),maxerey[year]))
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
    w = np.append(w, getSF(x["nmuons"][i], x["leadlep_pt"][i], x["leadlep_eta"][i], x["subleadlep_pt"][i], x["subleadlep_eta"][i], year))
    #print(w[i], x["nmuons"][i], x["leadlep_pt"][i], x["leadlep_eta"][i], x["subleadlep_pt"][i], x["subleadlep_eta"][i], year)
  return w

#### Zpt Corrections, so far unused ####
Zptfile = ROOT.TFile(SUEP_BASE + "/data/ZptUL18/Zpt_corr.root","READ")
ZptHist = Zptfile.Get("Zpt_SF")
maxZx   = ZptHist.GetNbinsX()
maxZy   = ZptHist.GetNbinsY()

def correctZpt(x):
  sf = ZptHist.GetBinContent(min(max(1, ZptHist.GetXaxis().FindBin(x["Z_pt"])), maxZx), min(max(1, ZptHist.GetYaxis().FindBin(x["Z_eta"])), maxZy))
  return sf

#### Identity ####

def one(x):
  return np.ones(len(x))
