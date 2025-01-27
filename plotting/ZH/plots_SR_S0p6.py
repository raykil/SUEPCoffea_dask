import ROOT


def cut(x):
  return (x["njets"] >= 0) & (abs(x["Z_m"]-90) < 30) & (x["Z_pt"] >= 25) & (x["nBLoose"] == 0) & (x["leadcluster_pt"] >= 60) & (x["leadclusterSpher_C"] >= 0.6) 

plots = {
  "njets": {
             "name"     : "njets",
             "bins"     : ["uniform", 20, 0, 20],
             "channel"  : "onecluster",
             "value"    : lambda x, y : (x["njets"], y*cut(x)),
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
             "channel"  : "onecluster",
             "value"    : lambda x, y : (x["H_T"], y*cut(x)),
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
             "channel"  : "onecluster",
             "value"    : lambda x, y : (x["H_T"]+x["L_T"], y*cut(x)),
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
             "channel"  : "onecluster", 
             "value"    : lambda x, y : (x["nBLoose"], y*cut(x)),
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
             "channel"  : "onecluster",
             "value"    : lambda x, y : (x["nBMedium"], y*cut(x)),
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
             "channel"  : "onecluster",
             "value"    : lambda x, y : (x["nBTight"], y*cut(x)),
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
             "channel"  : "onecluster",
             "value"    : lambda x, y : (x["leadjet_pt"], y*cut(x)),
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
             "channel"  : "onecluster",
             "value"    : lambda x, y : (x["subleadjet_pt"], y*cut(x)),
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
             "channel"  : "onecluster",
             "value"    : lambda x, y : (x["trailjet_pt"], y*cut(x)),
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
             "channel"  : "onecluster",
             "value"    : lambda x, y : (x["Z_m"], y*cut(x)),
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
             "channel"  : "onecluster",
             "value"    : lambda x, y : (x["leadjet_eta"], y*cut(x)),
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
             "channel"  : "onecluster",
             "value"    : lambda x, y : (x["subleadjet_eta"], y*cut(x)),
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
             "channel"  : "onecluster",
             "value"    : lambda x, y : (x["trailjet_eta"], y*cut(x)),
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
             "channel"  : "onecluster",
             "value"    : lambda x, y : (x["leadlep_pt"], y*cut(x)),
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
             "channel"  : "onecluster",
             "value"    : lambda x, y : (x["subleadlep_pt"], y*cut(x)),
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
             "channel"  : "onecluster",
             "value"    : lambda x, y : (x["leadlep_eta"], y*cut(x)),
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
             "channel"  : "onecluster",
             "value"    : lambda x, y : (x["subleadlep_eta"], y*cut(x)),
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
             "channel"  : "onecluster",
             "value"    : lambda x, y : (abs(x["leadlep_eta"]-x["subleadlep_eta"]), y*cut(x)),
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
             "channel"  : "onecluster",
             "value"    : lambda x, y : (abs(x["leadlep_phi"]-x["subleadlep_phi"]), y*cut(x)),
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
             "channel"  : "onecluster",
             "value"    : lambda x, y : (x["ntracks"], y*cut(x)),
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
             "channel"  : "onecluster",
             "value"    : lambda x, y : (x["Z_pt"], y*cut(x)),
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
             "channel"  : "onecluster",
             "value"    : lambda x, y : (x["Z_eta"], y*cut(x)),
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
             "channel"  : "onecluster",
             "value"    : lambda x, y : (x["Z_phi"], y*cut(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
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
             "channel"  : "onecluster",
             "value"    : lambda x, y : (x["leadcluster_pt"], y*cut(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "leadclusterpt",
             "xlabel"   : "p_{T}^{leadcluster} [GeV]",
             "vars"     : ["leadcluster_pt"]
  },
  "leadclustereta": {
             "name"     : "leadclustereta",
             "bins"     : ["uniform", 40, -5, 5],
             "channel"  : "onecluster",
             "value"    : lambda x, y : (x["leadcluster_eta"], y*cut(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "leadclustereta",
             "xlabel"   : "#eta^{leadcluster}",
             "vars"     : ["leadcluster_eta"]
  },
  "leadclusterphi": {
             "name"     : "leadclusterphi",
             "bins"     : ["uniform", 40, -3.14, 3.14],
             "channel"  : "onecluster",
             "value"    : lambda x, y : (x["leadcluster_phi"], y*cut(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "leadclusterphi",
             "xlabel"   : "#phi^{leadcluster}",
             "vars"     : ["leadcluster_phi"]
  },
  "leadclustertracks": {
             "name"     : "leadclustertracks",
             "bins"     : ["uniform", 200, 0, 200],
             "channel"  : "onecluster",
             "value"    : lambda x, y : (x["leadcluster_ntracks"], y*cut(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "leadclustertracks",
             "xlabel"   : "N_{tracks}^{leadcluster}",
             "vars"     : ["leadcluster_ntracks"]
  },
  "leadclusterspher": {
             "name"     : "leadclusterspher",
             "bins"     : ["uniform", 50, 0, 1],
             "channel"  : "onecluster",
             "value"    : lambda x, y : (x["leadclusterSpher_C"], y*cut(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "leadclusterspher",
             "xlabel"   : "S^{leadcluster}",
             "vars"     : ["leadclusterSpher_C"]
  },
  "leadclusterspherlab": {
             "name"     : "leadclusterspherlab",
             "bins"     : ["uniform", 50, 0, 1],
             "channel"  : "onecluster",
             "value"    : lambda x, y : (x["leadclusterSpher_L"], y*cut(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "leadclusterspherlab",
             "xlabel"   : "S^{leadcluster}_{lab}",
             "vars"     : ["leadclusterSpher_L"]
  },
}

 
