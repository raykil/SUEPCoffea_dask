import ROOT


def cut(x):
  return (x["njets"] >= 0) & (abs(x["Z_m"]-90) < 30) & (x["nBLoose"] == 0) & (x["leadcluster_pt"] > 60) & (x["Z_pt"] > 25)

plots = {
}

var = {
"leadlep_pt" : ["leadlep_pt", "p_{T}^{l1} [GeV]", 10, [10, 15, 20, 30, 40, 60, 80, 100, 125, 150, 200]],
"leadlep_eta" : ["leadlep_eta", "#eta^{l1}", 6, [-2.4, -1.2, -0.8, 0, 0.8, 1.2, 2.4]],
"subleadlep_pt" : ["subleadlep_pt", "p_{T}^{l2} [GeV]", 10, [10, 15, 20, 30, 40, 60, 80, 100, 125, 150, 200]],
"subleadlep_eta" : ["subleadlep_eta", "#eta^{l2}", 6, [-2.4, -1.2, -0.8, 0, 0.8, 1.2, 2.4]],

}

for v1 in var:
  for v2 in var:
    name = "2D_%s_%s"%(v1,v2)
    plots[name] = {}
    plots[name]["name"]    = name
    plots[name]["bins"]    = ["2Dlimits", var[v1][2], var[v1][3], var[v2][2], var[v2][3]]
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


