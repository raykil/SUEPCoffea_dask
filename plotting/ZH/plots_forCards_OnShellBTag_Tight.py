import ROOT


def cut(x):
  return (x["njets"] >= 0) & (abs(x["Z_m"]-90) < 30) & (x["Z_pt"] >= 25) & (x["nBTight"] > 0) & (x["leadcluster_pt"] >= 60)

plots = {
  "leadclustertracks": {
             "name"     : "leadclustertracks",
             "bins"     : ["uniform", 25, 0, 100],
             "channel"  : "onecluster",
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
 "leadclustertracks_onecluster": {
             "name"     : "leadclustertracks_onecluster",
             "bins"     : ["uniform", 8, 20, 60],
             "channel"  : "onecluster",
             "value"    : lambda x, y : (x["leadcluster_ntracks"], y*cut(x)*(x["leadjet_pt"] < 100)*(x["leadcluster_ntracks"] >= 20)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "leadclustertracks_onecluster",
             "xlabel"   : "N_{tracks}^{SUEP}",
             "vars"     : ["leadcluster_ntracks"]
  },
 "leadclustertracks_B1": {
             "name"     : "leadclustertracks_B1",
             "bins"     : ["uniform", 8, 20, 60],
             "channel"  : "onecluster",
             "value"    : lambda x, y : (x["leadcluster_ntracks"], y*cut(x)*(x["leadjet_pt"] > 100)*(x["leadjet_pt"] < 250)*(x["leadcluster_ntracks"] >= 20)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "leadclustertracks_B1",
             "xlabel"   : "N_{tracks}^{SUEP}",
             "vars"     : ["leadcluster_ntracks"]
  },
 "leadclustertracks_B2": {
             "name"     : "leadclustertracks_B2",
             "bins"     : ["uniform", 8, 20, 60],
             "channel"  : "onecluster",
             "value"    : lambda x, y : (x["leadcluster_ntracks"], y*cut(x)*(x["leadjet_pt"] > 250)*(x["leadcluster_ntracks"] >= 20)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "leadclustertracks_B2",
             "xlabel"   : "N_{tracks}^{SUEP}",
             "vars"     : ["leadcluster_ntracks"]
  },
}

 
