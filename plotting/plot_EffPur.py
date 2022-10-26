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

ZH = [pd.HDFStore("../outputSimTracks/"+f, 'r') for f in os.listdir("../outputSimTracks/")]
output = "/eos/user/j/jkil/www/EfficiencyAndPurity"

plotStripEff = False
plotStripPur = False
plotClusterEff = False
plotClusterPur = False
bothEff = True
bothPur = True

###### CLUSTER ######

clusterEff = [0]*len(ZH)
clusterPur = [0]*len(ZH)

for i in range(len(ZH)):
    nSUEPtracks = ZH[i]["onecluster"]["nSUEPtracks"]
    nInCluster = ZH[i]["onecluster"]["nInCluster"] 
    nSUEPinCluster = ZH[i]["onecluster"]["nSUEPinCluster"] 

    clusterEff[i] = pd.Series.tolist(nSUEPinCluster/nSUEPtracks)
    clusterPur[i] = pd.Series.tolist(nSUEPinCluster/nInCluster)

clusterEff = sum(clusterEff,[])
clusterPur = sum(clusterPur,[])

clusterPurCut = (np.array(clusterPur)[:] <= 1)
clusterPur = np.array(clusterPur)[clusterPurCut]


if plotClusterEff:
    plt.figure()
    plt.hist(clusterEff)
    plt.title("Efficiency of Cluster")
    plt.xlabel("Efficiency of Cluster")
    plt.ylabel("Counts")
    plt.savefig("{}/clusterEff.png".format(output))

if plotClusterPur:
    plt.figure()
    plt.hist(clusterPur)
    plt.title("Purity of Cluster")
    plt.xlabel("Purity of Cluster")
    plt.ylabel("Counts")
    plt.savefig("{}/clusterPur.png".format(output))

###### STRIPS ######

#EtaWidths = ["0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0"]
#EtaWidths = ["0.1","0.2","0.3","0.4","0.5"]
#EtaWidths = ["0.6","0.7","0.8","0.9","1.0"]
EtaWidths = ["1.0"]

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

    if plotStripEff:
        plt.figure()
        plt.hist(stripEff)
        plt.title("Efficiency of Strip{}".format(etaWidth))
        plt.xlabel("Efficiency of Strip{}".format(etaWidth))
        plt.ylabel("Counts")
        plt.savefig("{}/strip{}Eff.png".format(output,etaWidth))

    if plotStripPur:
        plt.figure()
        plt.hist(stripPur)
        plt.title("Purity of Strip{}".format(etaWidth))
        plt.xlabel("Purity of Strip{}".format(etaWidth))
        plt.ylabel("Counts")
        plt.savefig("{}/strip{}Pur.png".format(output,etaWidth))

    if bothEff:
        plt.figure()
        plt.hist(clusterEff, alpha=0.5, color="tab:blue")
        plt.hist(stripEff, alpha=0.5, color="tab:green")
        plt.title("Efficiency of Cluster and Strip{}".format(etaWidth))
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