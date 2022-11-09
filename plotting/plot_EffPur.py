"""
    This program plots the number of SUEP & BACK tracks in and out of selected strip.
    This is intended to directly observe the sensitivity of striptizing. 
"""
import pandas as pd
#import ROOT
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# stripEfficiency = nSUEPinBand / nSUEPtracks
# stripPurity = nSUEPinBand / nInBand
# clusterEfficiency = nSUEPinCluster / nSUEPtracks
# clusterPurity = nSUEPinCluster / nInCluster

ZH = [pd.HDFStore("../outputSimTracksTest/"+f, 'r') for f in os.listdir("../outputSimTracksTest/")]
output = "/eos/user/j/jkil/www/EfficiencyAndPurity"

bothEff = True
bothPur = True

HighPtOnly = False # Make it True to enable high pt cut. Careful! Make sure to disable LowPtOnly
LowPtOnly = False  # Make it True to enable low pt cut. Careful! Make sure to disable HighPtOnly

HighPzOnly = False
LowPzOnly = False

###### GEN VARS ######

Hpt = [0]*len(ZH)
Hpz = [0]*len(ZH)
ptCutVal = 50.0
pzCutVal = 0.0

for i in range(len(ZH)):
    genHpt = ZH[i]["onecluster"]["genHpt"]
    genHpz = ZH[i]["onecluster"]["genHpz"]
    Hpt[i] = pd.Series.tolist(genHpt)
    Hpz[i] = pd.Series.tolist(genHpz)

Hpt = sum(Hpt,[])
print(len(Hpt))
Hpz = sum(Hpz,[])

highHptCut = (np.array(Hpt)[:] > ptCutVal) # Only the ones with high pt survives
lowHptCut = (np.array(Hpt)[:] < ptCutVal)

highHpzCut = (np.array(Hpz)[:] > pzCutVal)
lowHpzCut = (np.array(Hpz)[:] < pzCutVal)


###### CLUSTER VARIABLES ######

clusterEff = [0]*len(ZH)
clusterPur = [0]*len(ZH)

for i in range(len(ZH)):
    nSUEPtracks = ZH[i]["onecluster"]["nSUEPtracks"]
    nInCluster = ZH[i]["onecluster"]["nInCluster"] 
    nSUEPinCluster = ZH[i]["onecluster"]["nSUEPinCluster"]

    clusterEff[i] = pd.Series.tolist(nSUEPinCluster/nSUEPtracks)
    clusterPur[i] = pd.Series.tolist(nSUEPinCluster/nInCluster)

clusterEff = np.array(sum(clusterEff,[]))
clusterPur = np.array(sum(clusterPur,[]))

clusterEffCut = (clusterEff[:] <= 1)
clusterEff = clusterEff[clusterEffCut]

# Applying pt cut
if HighPtOnly & (LowPtOnly == False):
    clusterEff = clusterEff[highHptCut]
    clusterPur = clusterPur[highHptCut]
elif LowPtOnly & (HighPtOnly == False):
    clusterEff = clusterEff[lowHptCut]
    clusterPur = clusterPur[lowHptCut]
elif HighPtOnly & LowPtOnly: print("Make sure you are choosing either high/low pt! Now drawing with no cuts.")

# Applying pz cut
if HighPzOnly & (LowPzOnly == False):
    clusterEff = clusterEff[highHpzCut]
    clusterPur = clusterPur[highHpzCut]
elif LowPzOnly & (HighPzOnly == False):
    clusterEff = clusterEff[lowHpzCut]
    clusterPur = clusterPur[lowHpzCut]
elif HighPzOnly & LowPzOnly: print("Make sure you are choosing either high/low pz! Now drawing with no cuts.")


###### STRIP VARIABLES ######

#EtaWidths = ["0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0"]
EtaWidths = ["0.2","0.4","0.8","1.0","1.2","1.4","1.6","1.8","2.0"]
#EtaWidths = ["1.2","1.4","1.6","1.8","2.0"]
#EtaWidths = ["0.6","0.7","0.8","0.9","1.0"]

for etaWidth in EtaWidths:
    stripEff = [0]*len(ZH)
    stripPur = [0]*len(ZH)

    for i in range(len(ZH)):
        nSUEPtracks = ZH[i]["onecluster"]["nSUEPtracks"]
        nInBand = ZH[i]["onecluster"]["nInBand{}".format(etaWidth)] 
        nSUEPinBand = ZH[i]["onecluster"]["nSUEPinBand{}".format(etaWidth)]

        stripEff[i] = pd.Series.tolist(nSUEPinBand/nSUEPtracks)
        stripPur[i] = pd.Series.tolist(nSUEPinBand/nInBand)

    stripEff = sum(stripEff,[])
    stripPur = sum(stripPur,[])

    if HighPtOnly & (LowPtOnly == False):
        stripEff = stripEff[highHptCut]
        stripPur = stripPur[highHptCut]
    elif LowPtOnly & (HighPtOnly == False):
        stripEff = stripEff[lowHptCut]
        stripPur = stripPur[lowHptCut]
    elif HighPtOnly & LowPtOnly: print("Make sure you are choosing either high/low pt! Now drawing with no cuts.")

    if HighPzOnly & (LowPzOnly == False):
        stripEff = stripEff[highHpzCut]
        stripPur = stripPur[highHpzCut]
    elif LowPzOnly & (HighPzOnly == False):
        stripEff = stripEff[lowHpzCut]
        stripPur = stripPur[lowHpzCut]
    elif HighPzOnly & LowPzOnly: print("Make sure you are choosing either high/low pz! Now drawing with no cuts.")

    if bothEff:
        plt.figure()
        plt.hist(clusterEff, alpha=0.5, color="tab:blue")
        plt.hist(stripEff, alpha=0.5, color="tab:green")
        plt.title("Efficiency of Cluster and Strip{}".format(etaWidth))
        if HighPtOnly: plt.text(.75,.75,"Hpt > {}".format(ptCutVal))
        #if LowPtOnly:  plt.text(x,y,"Hpt > {}".format(ptCutVal))
        #if HighPzOnly: plt.text(x,y,"Hpt > {}".format(ptCutVal))
        #if LowPzOnly:  plt.text(x,y,"Hpt > {}".format(ptCutVal))

        plt.xlabel("Efficiency")
        plt.ylabel("Counts")
        plt.legend(["cluster Efficiency", "Strip{} Efficiency".format(etaWidth)])
        plt.savefig("{}/botheff{}.png".format(output,etaWidth))

    if bothPur:
        plt.figure()
        plt.hist(clusterPur, alpha=0.5, color="tab:blue")
        plt.hist(stripPur, alpha=0.5, color="tab:green")
        plt.title("Purity of Cluster and Strip{}".format(etaWidth))
        plt.xlabel("Purity")
        plt.ylabel("Counts")
        plt.legend(["cluster Purity", "Strip{} Purity".format(etaWidth)])
        plt.savefig("{}/bothpur{}.png".format(output,etaWidth))