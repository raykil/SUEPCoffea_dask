import ROOT


def cut(x):
  return (x["njets"] >= 0) & (abs(x["Z_m"]-90) < 30) & (x["nBLoose"] == 0) & (x["leadcluster_pt"] > 60) & (x["Z_pt"] > 25)

plots = {
}

var = {
"S_phi" : ["leadcluster_phi", "#phi^{SUEP}", 30, -3.1415,3.1415],
"S_eta": ["leadcluster_eta", "#eta^{SUEP} [GeV]", 30, -3, 3],
}

for v1 in var:
  for v2 in var:
    name = "2D_%s_%s"%(v1,v2)
    plots[name] = {}
    plots[name]["name"]    = name
    plots[name]["bins"]    = ["2Duniform", var[v1][2], var[v1][3], var[v1][4], var[v2][2], var[v2][3], var[v2][4]]
    plots[name]["channel"] = "SR"
    plots[name]["value"]   = lambda x, y, v1=v1, v2=v2: (x[var[v1][0]], x[var[v2][0]], y*cut(x))
    plots[name]["logY"     ]= True
    plots[name]["normalize"]= False
    plots[name]["maxY"]     = 1e9
    plots[name]["minY"]     = 1e0
    plots[name]["ratiomaxY"]= 2.
    plots[name]["ratiominY"]= 0.
    plots[name]["plotname"] = name
    plots[name]["xlabel"]   = var[v1][1]
    plots[name]["ylabel"]   = var[v2][1]
    plots[name]["vars"]     = [var[v1][0], var[v2][0]]
    plots[name]["mode"]     = "colz"


