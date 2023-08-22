import ROOT


def cut(x, region=False):
  if not region:
    return (x["njets"] >= 0) & (abs(x["Z_m"]-90) < 30) & (x["nBLoose"] == 0) & (x["leadcluster_pt"] > 60) & (x["Z_pt"] > 25)
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
  else:
    return (x["njets"] >= 0) & (abs(x["Z_m"]-90) < 30) & (x["nBLoose"] == 0) & (x["leadcluster_pt"] > 60) & (x["Z_pt"] > 25)

plots = {
}

var = {
"S_phi" : ["leadcluster_phi", "#phi^{SUEP}", 10, -3.1416,3.1416],
"S_eta": ["leadcluster_eta", "#eta^{SUEP}", 10, -3,3],
}


for v1 in var:
  for v2 in var:
    if v1 == v2: continue
    name = "2D_%s_%s"%(v1,v2)
    plots[name] = {}
    plots[name]["name"]    = name
    plots[name]["bins"]    = ["2Duniform", var[v1][2], var[v1][3], var[v1][4], var[v2][2], var[v2][3], var[v2][4]]
    plots[name]["channel"] = "SR"
    plots[name]["value"]   = lambda x, y, v1=v1, v2=v2, reg=False: (x[var[v1][0]], x[var[v2][0]], y*cut(x, reg))
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
    plots[name]["normalizeX"] = True
    #plots[name]["maxZ"]     = -1
    #plots[name]["minZ"]     = 1

var = {
"Z_phi" : ["Z_phi", "#phi^{Z}", 10, -3.1416,3.1416],
"Z_eta": ["Z_eta", "#eta^{Z}", 10, -3,3],
}



for v1 in var:
  for v2 in var:
    if v1 == v2: continue
    name = "2D_%s_%s"%(v1,v2)
    plots[name] = {}
    plots[name]["name"]    = name
    plots[name]["bins"]    = ["2Duniform", var[v1][2], var[v1][3], var[v1][4], var[v2][2], var[v2][3], var[v2][4]]
    plots[name]["channel"] = "SR"
    plots[name]["value"]   = lambda x, y, v1=v1, v2=v2, reg=False: (x[var[v1][0]], x[var[v2][0]], y*cut(x, reg))
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
    plots[name]["normalizeX"] = True
    #plots[name]["maxZ"]     = -1
    #plots[name]["minZ"]     = 1


var = {
"jet1_phi" : ["leadjet_phi", "#phi^{jet1}", 10, -3.1416,3.1416],
"jet1_eta": ["leadjet_eta", "#eta^{jet1}", 10, -3,3],
}



for v1 in var:
  for v2 in var:
    if v1 == v2: continue
    name = "2D_%s_%s"%(v1,v2)
    plots[name] = {}
    plots[name]["name"]    = name
    plots[name]["bins"]    = ["2Duniform", var[v1][2], var[v1][3], var[v1][4], var[v2][2], var[v2][3], var[v2][4]]
    plots[name]["channel"] = "SR"
    plots[name]["value"]   = lambda x, y, v1=v1, v2=v2, reg=False: (x[var[v1][0]], x[var[v2][0]], y*cut(x, reg))
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
    plots[name]["normalizeX"] = True
    #plots[name]["maxZ"]     = -1
    #plots[name]["minZ"]     = 1

var = {
"jet3_phi" : ["trailjet_phi", "#phi^{jet3}", 10, -3.1416,3.1416],
"jet3_eta": ["trailjet_eta", "#eta^{jet3}", 10, -3,3],
}



for v1 in var:
  for v2 in var:
    if v1 == v2: continue
    name = "2D_%s_%s"%(v1,v2)
    plots[name] = {}
    plots[name]["name"]    = name
    plots[name]["bins"]    = ["2Duniform", var[v1][2], var[v1][3], var[v1][4], var[v2][2], var[v2][3], var[v2][4]]
    plots[name]["channel"] = "SR"
    plots[name]["value"]   = lambda x, y, v1=v1, v2=v2, reg=False: (x[var[v1][0]], x[var[v2][0]], y*cut(x, reg))
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
    plots[name]["normalizeX"] = True
    #plots[name]["maxZ"]     = -1
    #plots[name]["minZ"]     = 1


var = {
"jet2_phi" : ["subleadjet_phi", "#phi^{jet2}", 10, -3.1416,3.1416],
"jet2_eta": ["subleadjet_eta", "#eta^{jet2}", 10, -3,3],
}



for v1 in var:
  for v2 in var:
    if v1 == v2: continue
    name = "2D_%s_%s"%(v1,v2)
    plots[name] = {}
    plots[name]["name"]    = name
    plots[name]["bins"]    = ["2Duniform", var[v1][2], var[v1][3], var[v1][4], var[v2][2], var[v2][3], var[v2][4]]
    plots[name]["channel"] = "SR"
    plots[name]["value"]   = lambda x, y, v1=v1, v2=v2, reg=False: (x[var[v1][0]], x[var[v2][0]], y*cut(x, reg))
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
    plots[name]["normalizeX"] = True
    #plots[name]["maxZ"]     = -1
    #plots[name]["minZ"]     = 1

var = { 
"S_phi" : ["leadcluster_phi", "#phi^{SUEP}", 10, -3.1416,3.1416],
"S_eta": ["leadcluster_eta", "#eta^{SUEP}", 10, -3,3],
"Z_phi" : ["Z_phi", "#phi^{Z}", 10, -3.1416,3.1416],
"Z_eta": ["Z_eta", "#eta^{Z}", 10, -3,3],
"jet1_phi" : ["leadjet_phi", "#phi^{jet1}", 10, -3.1416,3.1416],
"jet1_eta": ["leadjet_eta", "#eta^{jet1}", 10, -3,3],
"jet3_phi" : ["trailjet_phi", "#phi^{jet3}", 10, -3.1416,3.1416],
"jet3_eta": ["trailjet_eta", "#eta^{jet3}", 10, -3,3],
"jet2_phi" : ["subleadjet_phi", "#phi^{jet2}", 10, -3.1416,3.1416],
"jet2_eta": ["subleadjet_eta", "#eta^{jet2}", 10, -3,3],
}


allPlots = plots.keys()
for region in ["A"]:
  for oldPlot in allPlots:
    name = oldPlot + "_" + region
    plots[name] = {}
    plots[name]["name"]    = name
    plots[name]["bins"]    = plots[oldPlot]["bins"]
    plots[name]["channel"] = "SR"
    plots[name]["value"]   = lambda x, y, reg=region, t=oldPlot: plots[t]["value"](x,y,reg=region)
    plots[name]["logY"     ]= plots[oldPlot]["logY"]
    plots[name]["normalize"]= plots[oldPlot]["normalize"]
    plots[name]["maxY"]     = plots[oldPlot]["maxY"]
    plots[name]["minY"]     = plots[oldPlot]["minY"]
    plots[name]["ratiomaxY"]= plots[oldPlot]["ratiomaxY"]
    plots[name]["ratiominY"]= plots[oldPlot]["ratiominY"]
    plots[name]["plotname"] = name
    plots[name]["xlabel"]   = plots[oldPlot]["xlabel"]
    plots[name]["ylabel"]   = plots[oldPlot]["ylabel"]
    plots[name]["mode"]   = plots[oldPlot]["mode"]
    plots[name]["vars"]     = plots[oldPlot]["vars"]
    plots[name]["normalizeX"] = True

