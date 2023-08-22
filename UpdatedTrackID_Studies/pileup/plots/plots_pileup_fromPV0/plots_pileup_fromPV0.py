import ROOT

def cut(x):
  return (x["ntracks"] >= 0) 

plots = {
  "ntracks": {
             "name"     : "ntracks",
             "bins"     : ["uniform", 10, 0, 3200],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["ntracks"], y*cut(x)),
             "logY"     : True,
             "normalize": True,
             "maxY"     : 100,
             "minY"     : .001,
             "ratiomaxY": 2,
             "ratiominY": 0,
             "plotname" : "ntracks",
             "xlabel"   : "N_{tracks}",
             "vars"     : ["ntracks"]
  },
  "leadclustertracks": {
             "name"     : "leadclustertracks",
             "bins"     : ["uniform", 10, 0, 400],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["leadcluster_ntracks"], y*cut(x)),
             "logY"     : True,
             "normalize": True,
             "maxY"     : 100,
             "minY"     : .001,
             "ratiomaxY": 2,
             "ratiominY": 0,
             "plotname" : "leadclustertracks",
             "xlabel"   : "N_{tracks}^{SUEP}",
             "vars"     : ["leadcluster_ntracks"]
  },
}

 