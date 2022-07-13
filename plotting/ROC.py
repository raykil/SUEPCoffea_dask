import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

signal     = pd.HDFStore("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/plotting/../signal/out_1_1_1001.hdf5","r") 
background = pd.HDFStore("/eos/user/c/cericeci/SUEP/SUEPCoffea_dask/plotting/../background/out_256441424_94909_1.hdf5","r")
signal = signal["onecluster"]
background = background["onecluster"]
#theVars = ["leadclusterSpher_C", "leadstripSpher_C_dEta0.6", "leadstripSpher_C_dEta0.2", "leadstripSpher_C_dEta1.0", 
theVars = ["leadcluster_ntracks", "leadstrip_ntracks_dEta1.0", "leadstrip_ntracks_dEta0.8", "leadstrip_ntracks_dEta0.6", "leadstrip_ntracks_dEta0.4", "leadstrip_ntracks_dEta0.2"]


def getROC(sigs, backs, var):
  print("Getting ROC...")
  goods = sigs.loc[sigs["Z_pt"] < 100,var]
  bads  = backs.loc[backs["Z_pt"] < 100,var]
  ng    = len(goods)
  nb    = len(bads)
  minim = min(min(goods), min(bads))
  maxim = max(max(goods), max(bads))
  print(var, minim, maxim)
  sigeff  = []
  backeff = []
  integral = 0.
  for val in np.linspace(minim, maxim, 500):
    sigeff.append(float(sum(goods >= val)*1./ng))
    backeff.append(float(sum(bads >= val)*1./nb))
    if len(sigeff) >= 2: integral += abs(backeff[-2]-backeff[-1])*sigeff[-1]
  print(integral)
  if integral < 0.5:
      integral = 1 - integral
      sigeff = [1-i for i in sigeff]
      backeff = [1-i for i in backeff]
  return sigeff, backeff, integral

colors = ["r", "g", "b", "k", "y", "c"]
ic = 0
for v in theVars:
  s, b, i = getROC(signal, background, v)
  plt.plot(b, s, "%s--"%colors[ic], label="%s, r=%1.5f"%(v, i))
  ic += 1
plt.xlabel("Background efficiency")
plt.ylabel("Signal efficiency")
plt.legend(loc="best")
plt.axis([0., 1., 0., 1.1])

plt.savefig("/eos/user/c/cericeci/www/roc.pdf")
plt.clf()

