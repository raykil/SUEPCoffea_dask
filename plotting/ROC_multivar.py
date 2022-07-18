import matplotlib.pyplot as plt
import numpy as np
import sys
import imp
import ROOT

samplesFile = imp.load_source("samples",sys.argv[1])
plotsFile   = imp.load_source("plots",  sys.argv[2])
samples = samplesFile.samples
plots   = plotsFile.plots
del samples["data"] # Not needed


def getROC(p):
  print("Getting ROC for %s..."%p["name"])
  fil = ROOT.TFile("/eos/user/%s/%s/www/SUEP/stack_clusterpt60/%s.root"%(os.getlogin()[0], os.getlogin(), p["name"]),"READ") 
  backs = []
  totback = False
  for s in samples:
    if "isSig" in s: continue
    backs.append(fil.Get("%s_%s"%(p["name"], s)))
    if not totback:
      totback = backs[-1]
    else:
      totback.Add(backs[-1])
  sigs  = fil.Get("%s_SUEP_ZH_hadronic"%p["name"])

  sigInt = sigs.Integral(1,sigs.GetNbinsX())
  bkgInt = totback.Integral(1, sigs.GetNbinsX())
  sigeff  = []
  backeff = []
  quantiles = []
  integral = 0.
  for ibin in range(1,sigs.GetNbinsX()+1):
      #if ibin == 0:
      sigeff.append(sigs.GetBinContent(ibin)/sigInt)
      backeff.append(totback.GetBinContent(ibin)/bkgInt)
      #else:
      #sigeff.append(sigs.GetBinContent(ibin)/sigInt)
      #backeff.append(totback.GetBinContent(ibin)/bkgInt)
      quantiles.append(sigeff[-1]/(0.00001* sigeff[-1] + backeff[-1] + 0.00000000001))
  zipped  = zip(quantiles, sigeff, backeff)
  szipped = sorted(zipped)
  tuples = zip(*szipped)
  quantiles, sigtemp, backtemp = [ list(tuple) for tuple in tuples]
  sigeff = []
  backeff = []
  for i in range(len(sigtemp)):
    if i == 0:
      sigeff.append(sigtemp[i])
      backeff.append(backtemp[i])
    else:
      sigeff.append(sigtemp[i] + sigeff[-1])
      backeff.append(backtemp[i] + backeff[-1])

    if len(sigeff) >= 2: integral += abs(backeff[-2]-backeff[-1])*sigeff[-1]
  #print(sigeff, backeff, integral)
  if integral < 0.5:
      integral = 1 - integral
      sigeff = [1-i for i in sigeff]
      backeff = [1-i for i in backeff]
  print(p["name"], integral)
  if integral == 1.0: integral = 0.0
  return sigeff, backeff, integral

rValues = {}
pointsS = {}
pointsB = {}
for p in plots:
  #if "jet" in p: continue
  pointsS[p], pointsB[p], rValues[p] = getROC(plots[p])

rValues = dict(sorted(rValues.items(), key=lambda item: -item[1]))

colors = ["r", "g", "b", "k", "y", "c"]
ic = 0
for v in rValues:
  plt.plot(pointsB[v], pointsS[v], "%s--"%colors[ic], label="%s, r=%1.5f"%(v, rValues[v]))
  ic += 1
  if ic > len(colors)-1: break
plt.xlabel("Background efficiency")
plt.ylabel("Signal efficiency")
plt.legend(loc="best")
plt.axis([0., 1., 0., 1.1])

plt.savefig("/eos/user/%s/%s/www/roc.pdf"%(os.getlogin()[0], os.getlogin())
plt.clf()
