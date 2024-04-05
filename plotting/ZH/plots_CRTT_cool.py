import ROOT
import numpy as np
import pandas as pd

def compute_deltaR(eta1, phi1, eta2, phi2):
    deta = eta1 - eta2
    dphi = np.arccos(np.cos(phi1 - phi2))
    return np.sqrt(deta ** 2 + dphi ** 2)

def leadDeltaR(x):
  x['deltaR_leadjet'] = compute_deltaR(x['leadjet_eta'], x['leadjet_phi'], x['leadcluster_eta'], x['leadcluster_phi'])
  return x['deltaR_leadjet']

def cut(x):
  return (x["njets"] >= 0) & (x["Z_m"] > 120) & (x["Z_pt"] >= 25) & (x["nBLoose"] > 0) & (x["leadcluster_pt"] >= 60) & (compute_deltaR(x['leadjet_eta'], x['leadjet_phi'], x['leadcluster_eta'], x['leadcluster_phi']) <= 1.5)

def byRegion(x):
  nTrackReg = (x["njets"] < 0)
  ptReg1 = (x["leadjet_pt"] < 100)*1 
  ptReg2 = (x["leadjet_pt"] < 250)*1
  nTrackReg = (x["leadcluster_ntracks"] >= 10) + np.where((x["leadcluster_ntracks"]-14.99)/5 > 0 , (x["leadcluster_ntracks"]-14.99)/5, 0)
  #print(ptReg1[:10], ptReg2[:10], nTrackReg[:10], x["leadjet_pt"][:10], x["leadcluster_ntracks"][:10])
  ret = (10*ptReg1) + (10*ptReg2) + nTrackReg
  #print(ret) 
  return ret 
plots = {
  "bins": {
             "name"     : "bins",
             "bins"     : ["uniform", 30, 0, 30],
             "channel"  : "onecluster",
             "value"    : lambda x, y : (byRegion(x), y*cut(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 5e10,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "bins",
             "xlabel"   : "N_{Tracks}^{SUEP}",
             "legendPosition": [0.12, 0.65, 0.90, 0.86],
             "xbinlabels": ["0-10","10-20","20-25","25-30","30-35", "35-40","40-45","45-50","50-55",">55", "0-10","10-20","20-25","25-30","30-35", "35-40","40-45","45-50","50-55",">55","0-10","10-20","20-25","25-30","30-35", "35-40","40-45","45-50","50-55",">55"],
             "vars"     : ["njets"],
             "lines"    : [ [1,2e-1,1,1e7,7,3,48], [2,2e-1,2,1e7,7,3,48], [10,2e-1,10,1e8,9,5,ROOT.kBlack], [11,2e-1,11,1e7,7,3,48], [12,2e-1,12,1e7,7,3,48],  [20,2e-1,20,1e8,9,5,ROOT.kBlack],[21,2e-1,21,1e7,7,3,48], [22,2e-1,22,1e7,7,3,48]],
             "text"     : [["p_{T}^{jet1} > 250 GeV", [2.4,3e7], 0.05, ROOT.kBlack], ["100 GeV < p_{T}^{jet1} #leq 250 GeV", [10.4,3e7], 0.045, ROOT.kBlack],["p_{T}^{jet1} #leq 100 GeV", [22.4,3e7], 0.05, ROOT.kBlack], ["E2", [0.25,5e6], 0.03, 48], ["E1", [1.25,5e6], 0.03, 48], ["B2", [5.25,5e6], 0.03, 48], ["D2", [10.25,5e6], 0.03, 48], ["D1", [11.25,5e6], 0.03, 48], ["B1", [15.25,5e6], 0.03, 48], ["C2", [20.25,5e6], 0.03, 48], ["C1", [21.25,5e6], 0.03, 48], ["A", [25.25,5e6], 0.03, 48]],
             "rlines"   : [[1,0.0,1,2.0,7,3,48], [2,0.0,2,2.0,7,3,48], [10,0.0,10,2.0,9,5,ROOT.kBlack],[11,0.0,11,2.0,7,3,48], [12,0.0,12,2.0,7,3,48], [20,0.0,20,2.0,9,5,ROOT.kBlack],[21,0.0,21,2.0,7,3,48], [22,0.0,22,2.0,7,3,48]],
  },
}

 
