import ROOT


def cut(x):
  return (x["njets"] >= 0) & (abs(x["Z_m"]-90) < 30) & (x["Z_pt"] >= 25) & (x["nBLoose"] == 0) & (x["leadcluster_pt"] >= 60) 

plots = {
  "leadclustertracks": {
             "name"     : "leadclustertracks",
             "bins"     : ["uniform", 200, 0, 200],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["leadcluster_ntracks"], y*cut(x)),
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
  "leadclustermuons": {
             "name"     : "leadclustermuons",
             "bins"     : ["uniform", 10, 0, 10],
             "channel"  : "SR", 
             "value"    : lambda x, y : (x["leadcluster_nmuon"], y*cut(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "leadclustermuons",
             "xlabel"   : "N_{#mu}^{SUEP}",
             "vars"     : ["leadcluster_nmuon"]
  }, 
  "leadclusterelecs": {
             "name"     : "leadclusterelecs",
             "bins"     : ["uniform", 10, 0, 10],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["leadcluster_nelectron"], y*cut(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "leadclusterelecs",
             "xlabel"   : "N_{e}^{SUEP}",
             "vars"     : ["leadcluster_nelec"]
  },
  "leadclusterpions": {
             "name"     : "leadclusterpions",
             "bins"     : ["uniform", 10, 0, 10],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["leadcluster_npion"], y*cut(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "leadclusterpions",
             "xlabel"   : "N_{#pi}^{SUEP}",
             "vars"     : ["leadcluster_npion"]
  },  
  "leadclusterleps": {
             "name"     : "leadclusterleps",
             "bins"     : ["uniform", 10, 0, 10],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["leadcluster_nelectron"]+x["leadcluster_nmuon"], y*cut(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "leadclusterleps",
             "xlabel"   : "N_{#mu}^{SUEP}+N_{e}^{SUEP}",
             "vars"     : []
  },

}

 
