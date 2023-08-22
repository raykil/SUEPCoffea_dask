import ROOT
import numpy as np

def cut(x, region=False):
  if not(region):
    return (x["njets"] >= 0) & (abs(x["Z_m"]-90) < 30) & (x["Z_pt"] >= 25) & (x["nBLoose"] == 0) & (x["leadcluster_pt"] >= 60) 
  elif region == "A":
    return (x["njets"] >= 0) & (abs(x["Z_m"]-90) < 30) & (x["Z_pt"] >= 25) & (x["nBLoose"] == 0) & (x["leadcluster_pt"] >= 60) & (x["leadcluster_ntracks"] >= 20) & (x["leadjet_pt"] <= 100)
  elif region == "B1":
    return (x["njets"] >= 0) & (abs(x["Z_m"]-90) < 30) & (x["Z_pt"] >= 25) & (x["nBLoose"] == 0) & (x["leadcluster_pt"] >= 60) & (x["leadcluster_ntracks"] >= 20) & (x["leadjet_pt"] <= 250) &  (x["leadjet_pt"] > 100)
  elif region == "B2":
    return (x["njets"] >= 0) & (abs(x["Z_m"]-90) < 30) & (x["Z_pt"] >= 25) & (x["nBLoose"] == 0) & (x["leadcluster_pt"] >= 60) & (x["leadcluster_ntracks"] >= 20) & (x["leadjet_pt"] > 250)
  elif region == "C1":
    return (x["njets"] >= 0) & (abs(x["Z_m"]-90) < 30) & (x["Z_pt"] >= 25) & (x["nBLoose"] == 0) & (x["leadcluster_pt"] >= 60) & (x["leadcluster_ntracks"] >= 10) & (x["leadcluster_ntracks"] < 20) & (x["leadjet_pt"] <= 100)
  elif region == "D1":
    return (x["njets"] >= 0) & (abs(x["Z_m"]-90) < 30) & (x["Z_pt"] >= 25) & (x["nBLoose"] == 0) & (x["leadcluster_pt"] >= 60) & (x["leadcluster_ntracks"] >= 10) & (x["leadcluster_ntracks"] < 20) & (x["leadjet_pt"] <= 250) &  (x["leadjet_pt"] > 100)
  elif region == "E1":
    return (x["njets"] >= 0) & (abs(x["Z_m"]-90) < 30) & (x["Z_pt"] >= 25) & (x["nBLoose"] == 0) & (x["leadcluster_pt"] >= 60) & (x["leadcluster_ntracks"] >= 10) & (x["leadcluster_ntracks"] < 20) & (x["leadjet_pt"] > 250)
  elif region == "C2":
    return (x["njets"] >= 0) & (abs(x["Z_m"]-90) < 30) & (x["Z_pt"] >= 25) & (x["nBLoose"] == 0) & (x["leadcluster_pt"] >= 60) & (x["leadcluster_ntracks"] < 10) & (x["leadjet_pt"] <= 100)
  elif region == "D2":
    return (x["njets"] >= 0) & (abs(x["Z_m"]-90) < 30) & (x["Z_pt"] >= 25) & (x["nBLoose"] == 0) & (x["leadcluster_pt"] >= 60) & (x["leadcluster_ntracks"] < 10) & (x["leadjet_pt"] <= 250) &  (x["leadjet_pt"] > 100)
  elif region == "E2":
    return (x["njets"] >= 0) & (abs(x["Z_m"]-90) < 30) & (x["Z_pt"] >= 25) & (x["nBLoose"] == 0) & (x["leadcluster_pt"] >= 60) & (x["leadcluster_ntracks"] < 10) & (x["leadjet_pt"] > 250)
  elif region == "NT0to10":
    return (x["njets"] >= 0) & (abs(x["Z_m"]-90) < 30) & (x["Z_pt"] >= 25) & (x["nBLoose"] == 0) & (x["leadcluster_pt"] >= 60) & (x["leadcluster_ntracks"] < 10)
  elif region == "NT10to20":
    return (x["njets"] >= 0) & (abs(x["Z_m"]-90) < 30) & (x["Z_pt"] >= 25) & (x["nBLoose"] == 0) & (x["leadcluster_pt"] >= 60) & (x["leadcluster_ntracks"] < 20) & (x["leadcluster_ntracks"] >= 10) 
  elif region == "NT20toInf":
    return (x["njets"] >= 0) & (abs(x["Z_m"]-90) < 30) & (x["Z_pt"] >= 25) & (x["nBLoose"] == 0) & (x["leadcluster_pt"] >= 60) & (x["leadcluster_ntracks"] >= 20) 
  elif region == "NT40toInf":
    return (x["njets"] >= 0) & (abs(x["Z_m"]-90) < 30) & (x["Z_pt"] >= 25) & (x["nBLoose"] == 0) & (x["leadcluster_pt"] >= 60) & (x["leadcluster_ntracks"] >= 40)


def deltaPhi(phi1,  phi2):
  p12 = np.abs(phi1-phi2)
  return np.where( (6.2832 - p12) > p12, p12, 6.2832 - p12)

def deltaEta(eta1, eta2):
  return np.abs(eta1-eta2) 

def deltaR(phi1, eta1, phi2, eta2):
  dphi = deltaPhi(phi1, phi2)
  deta = deltaEta(eta1, eta2)
  return (dphi**2 + dphi**2)**0.5

plots = {
  "njets": {
             "name"     : "njets",
             "bins"     : ["uniform", 20, 0, 20],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (x["njets"], y*cut(x, reg)),
             "logY"     : True,
             "normalize": False, 
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "njets",
             "xlabel"   : "N_{jets}",
             "vars"     : ["njets"]
  },
  "HT": {
             "name"     : "HT",
             "bins"     : ["uniform", 40, 0, 400],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (x["H_T"], y*cut(x, reg)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "HT",
             "xlabel"   : "H_{T}(p_{T}^{jet} > 30 GeV)",
             "vars"     : ["leadjet_pt", "subleadjet_pt", "trailjet_pt"]
  },
  "LHT":{
             "name"     : "LHT",
             "bins"     : ["uniform", 40, 0, 800],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (x["H_T"]+x["L_T"], y*cut(x, reg)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "LHT",
             "xlabel"   : "H_{T}(p_{T}^{jet} > 30 GeV) + L_{T}",
             "vars"     : ["leadjet_pt", "subleadjet_pt", "trailjet_pt", "leadlep_pt","subleadlep_pt"]
  },
  "nBLoose": {
             "name"     : "nBLoose",
             "bins"     : ["uniform", 6, 0, 6],
             "channel"  : "SR", 
             "value"    : lambda x, y, reg=False : (x["nBLoose"], y*cut(x, reg)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "nBLoose",
             "xlabel"   : "N_{b}(loose)",
             "vars"     : ["nBLoose"]
  },
  "nBMedium": {
             "name"     : "nBMedium",
             "bins"     : ["uniform", 6, 0, 6],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (x["nBMedium"], y*cut(x, reg)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "nBMedium",
             "xlabel"   : "N_{b}(Medium)",
             "vars"     : ["nBMedium"]
  },
  "nBTight": {
             "name"     : "nBTight",
             "bins"     : ["uniform", 6, 0, 6],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (x["nBTight"], y*cut(x, reg)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "nBTight",
             "xlabel"   : "N_{b}(Tight)",
             "vars"     : ["nBTight"]
  },

  "jet1pt": {
             "name"     : "jet1pt",
             "bins"     : ["uniform", 100, 0, 200],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (x["leadjet_pt"], y*cut(x, reg)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "jet1pt",
             "xlabel"   : "p_{T}^{jet1}",
             "vars"     : ["leadjet_pt"]
  },

  "jet2pt": {
             "name"     : "jet2pt",
             "bins"     : ["uniform", 100, 0, 200],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (x["subleadjet_pt"], y*cut(x, reg)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "jet2pt",
             "xlabel"   : "p_{T}^{jet2}",
             "vars"     : ["subleadjet_pt"]
  },
  "jet3pt": {
             "name"     : "jet3pt",
             "bins"     : ["uniform", 100, 0, 200],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (x["trailjet_pt"], y*cut(x, reg)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "jet3pt",
             "xlabel"   : "p_{T}^{jet3}",
             "vars"     : ["trailjet_pt"]
  },
  "mZ": {
             "name"     : "mZ",
             "bins"     : ["uniform", 60, 0, 300],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (x["Z_m"], y*cut(x, reg)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "mZ",
             "xlabel"   : "m(l1,l2) [GeV]",
             "vars"     : ["Z_m"]
  },
  "jet1_eta": {
             "name"     : "jet1_eta",
             "bins"     : ["uniform", 40, -5, 5],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (x["leadjet_eta"], y*cut(x, reg)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "jet1_eta",
             "xlabel"   : "#eta^{j1}",
             "vars"     : ["leadjet_eta"]
  },

  "jet2_eta": {
             "name"     : "jet2_eta",
             "bins"     : ["uniform", 40, -5, 5],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (x["subleadjet_eta"], y*cut(x, reg)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "jet2_eta",
             "xlabel"   : "#eta^{j2}",
             "vars"     : ["subleadjet_eta"]
  },
  "jet3_eta": {
             "name"     : "jet3_eta",
             "bins"     : ["uniform", 40, -5, 5],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (x["trailjet_eta"], y*cut(x, reg)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "jet3_eta",
             "xlabel"   : "#eta^{j3}",
             "vars"     : ["trailjet_eta"]
  },

  "leadlep_pt": {
             "name"     : "leadlep_pt",
             "bins"     : ["uniform", 100, 0, 200],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (x["leadlep_pt"], y*cut(x, reg)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "leadlep_pt",
             "xlabel"   : "p_{T}^{l1}",
             "vars"     : ["leadlep_pt"]
  },

  "subleadlep_pt": {
             "name"     : "subleadlep_pt",
             "bins"     : ["uniform", 100, 0, 200],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (x["subleadlep_pt"], y*cut(x, reg)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "subleadlep_pt",
             "xlabel"   : "p_{T}^{l2}",
             "vars"     : ["subleadlep_pt"]
  },

  "leadlep_eta": {
             "name"     : "leadlep_eta",
             "bins"     : ["uniform", 20, -2.5, 2.5],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (x["leadlep_eta"], y*cut(x, reg)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "leadlep_eta",
             "xlabel"   : "#eta^{l1}",
             "vars"     : ["leadlep_eta"]
  },

  "subleadlep_eta": {
             "name"     : "subleadlep_eta",
             "bins"     : ["uniform", 20, -2.5, 2.5],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (x["subleadlep_eta"], y*cut(x, reg)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "subleadlep_eta",
             "xlabel"   : "#eta^{l2}",
             "vars"     : ["subleadlep_eta"]
  },
  "leplep_deta": {
             "name"     : "leplep_deta",
             "bins"     : ["uniform", 20, 0, 5],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (abs(x["leadlep_eta"]-x["subleadlep_eta"]), y*cut(x, reg)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "leplep_deta",
             "xlabel"   : "|#eta^{l1}-#eta^{l2}|",
             "vars"     : ["leadlep_eta", "subleadlep_eta"]
  },

  "leplep_dphi": {
             "name"     : "leplep_dphi",
             "bins"     : ["uniform", 20, 0, 5],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (abs(x["leadlep_phi"]-x["subleadlep_phi"]), y*cut(x, reg)),
             "logY"     : True,
             "normalize": False, 
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "leplep_dphi",
             "xlabel"   : "|#phi^{l1}-#phi^{l2}|",
             "vars"     : ["leadlep_phi", "subleadlep_phi"]
  },

  "ntracks": {
             "name"     : "ntracks",
             "bins"     : ["uniform", 40, 0, 200],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (x["ntracks"], y*cut(x, reg)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "ntracks",
             "xlabel"   : "N_{tracks}",
             "vars"     : ["ntracks"]
  },

  "Zpt": {
             "name"     : "Zpt",
             "bins"     : ["uniform", 200, 0, 200],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (x["Z_pt"], y*cut(x, reg)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "Zpt",
             "xlabel"   : "p_{T}^{Z} [GeV]",
             "vars"     : ["Z_pt"]
  },

  "Zeta": {
             "name"     : "Zeta",
             "bins"     : ["uniform", 40, -5, 5],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (x["Z_eta"], y*cut(x, reg)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "Zeta",
             "xlabel"   : "#eta^{Z}",
             "vars"     : ["Z_eta"]
  },
  "Zphi": {
             "name"     : "Zphi",
             "bins"     : ["uniform", 40, -3.14, 3.14],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (x["Z_phi"], y*cut(x, reg)),
             "logY"     : False,
             "normalize": False,
             "maxY"     : 1e5,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "Zphi",
             "xlabel"   : "#phi^{Z}",
             "vars"     : ["Z_phi"]
  },

  "leadclusterpt": {
             "name"     : "leadclusterpt",
             "bins"     : ["uniform", 200, 0, 200],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (x["leadcluster_pt"], y*cut(x, reg)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "leadclusterpt",
             "xlabel"   : "p_{T}^{SUEP} [GeV]",
             "vars"     : ["leadcluster_pt"]
  },
  "leadclustereta": {
             "name"     : "leadclustereta",
             "bins"     : ["uniform", 40, -5, 5],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (x["leadcluster_eta"], y*cut(x, reg)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "leadclustereta",
             "xlabel"   : "#eta^{SUEP}",
             "vars"     : ["leadcluster_eta"]
  },
  "leadclusterphi": {
             "name"     : "leadclusterphi",
             "bins"     : ["uniform", 40, -3.14, 3.14],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (x["leadcluster_phi"], y*cut(x, reg)),
             "logY"     : False,
             "normalize": False,
             "maxY"     : 4e4, #1e9,
             "minY"     : 0, #1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "leadclusterphi",
             "xlabel"   : "#phi^{SUEP}",
             "vars"     : ["leadcluster_phi"]
  },
  "leadclustermass": {
             "name"     : "leadclustermass",
             "bins"     : ["uniform", 50, 0, 200],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (x["leadcluster_m"], y*cut(x, reg)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "leadclustermass",
             "xlabel"   : "m^{SUEP}",
             "vars"     : ["leadcluster_m"]
  },
  "leadclustertracks": {
             "name"     : "leadclustertracks",
             "bins"     : ["uniform", 200, 0, 200],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (x["leadcluster_ntracks"], y*cut(x, reg)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "leadclustertracks",
             "xlabel"   : "N_{tracks}^{SUEP}",
             "vars"     : ["leadcluster_ntracks"]
  },
  "leadclusterspher": {
             "name"     : "leadclusterspher",
             "bins"     : ["uniform", 50, 0, 1],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (x["leadclusterSpher_C"], y*cut(x, reg)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "leadclusterspher",
             "xlabel"   : "S^{SUEP}",
             "vars"     : ["leadclusterSpher_C"]
  },
  "leadclusterspherlab": {
             "name"     : "leadclusterspherlab",
             "bins"     : ["uniform", 50, 0, 1],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (x["leadclusterSpher_L"], y*cut(x, reg)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "leadclusterspherlab",
             "xlabel"   : "S^{SUEP}_{lab}",
             "vars"     : ["leadclusterSpher_L"]
  },
  "dPhiSZ": {
             "name"     : "dPhiSZ",
             "bins"     : ["uniform", 40, 0., 3.14],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (deltaPhi(x["leadcluster_phi"],x["Z_phi"])  , y*cut(x, reg)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9, #1e9,
             "minY"     : 1e0, #1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "dPhiSZ",
             "xlabel"   : "|#phi^{SUEP}-#phi^{Z}|",
             "vars"     : ["leadcluster_phi","Z_phi"]
  },
  "detaSZ": {
             "name"     : "detaSZ",
             "bins"     : ["uniform", 60, 0., 6.],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (deltaEta(x["leadcluster_eta"],x["Z_eta"])  , y*cut(x, reg)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9, #1e9,
             "minY"     : 1e0, #1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "detaSZ",
             "xlabel"   : "|#eta^{SUEP}-#eta^{Z}|",
             "vars"     : ["leadcluster_eta","Z_eta"]
  },
  "dRSZ": {
             "name"     : "dRSZ",
             "bins"     : ["uniform", 60, 0., 6.],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (deltaR(x["leadcluster_phi"],x["leadcluster_eta"],x["Z_phi"], x["Z_eta"])  , y*cut(x, reg)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9, #1e9,
             "minY"     : 1e0, #1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "dRSZ",
             "xlabel"   : "#Delta R(SUEP,Z)",
             "vars"     : ["leadcluster_R","Z_R"]
  },
  "met": {
             "name"     : "met",
             "bins"     : ["uniform", 50, 0., 200.],
             "channel"  : "SR",
             "value"    : lambda x, y, reg=False : (x["MET_pt"]  , y*cut(x, reg)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9, #1e9,
             "minY"     : 1e0, #1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "met",
             "xlabel"   : "p_{T}^{miss} [GeV]",
             "vars"     : ["MET_pt"]
  },
}


allPlots = plots.keys()
for region in ["A","B1","B2","C1","C2","D1","D2","E1","E2","NT0to10","NT10to20","NT20toInf", "NT40toInf"]:
  for oldPlot in allPlots:
    name = oldPlot + "_" + region
    plots[name] = {}
    plots[name]["name"]    = name
    plots[name]["bins"]    = plots[oldPlot]["bins"]
    plots[name]["channel"] = "SR"
    plots[name]["value"]   = lambda x, y, z=region, t=oldPlot: plots[t]["value"](x,y,z)
    plots[name]["logY"     ]= plots[oldPlot]["logY"]
    plots[name]["normalize"]= plots[oldPlot]["normalize"]
    plots[name]["maxY"]     = plots[oldPlot]["maxY"]
    plots[name]["minY"]     = plots[oldPlot]["minY"]
    plots[name]["ratiomaxY"]= plots[oldPlot]["ratiomaxY"]
    plots[name]["ratiominY"]= plots[oldPlot]["ratiominY"]
    plots[name]["plotname"] = name
    plots[name]["xlabel"]   = plots[oldPlot]["xlabel"]
    plots[name]["vars"]     = plots[oldPlot]["vars"]

