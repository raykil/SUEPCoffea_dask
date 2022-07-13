import ROOT


def cut(x):
  return (x["genZpt"] >= -1)

plots = {
  "genZpt": {
             "name"     : "genZpt",
             "bins"     : ["uniform", 800, 0, 800],
             "channel"  : "twoleptons",
             "value"    : lambda x, y : (x["genZpt"], y*cut(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 1.1,
             "ratiominY": 0.9,
             "plotname" : "genZpt",
             "xlabel"   : "p_{T}^{Z, gen} [GeV]",
             "vars"     : ["genZpt"]
  },
}

 
