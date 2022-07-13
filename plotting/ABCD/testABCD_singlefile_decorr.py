import ROOT
import sys
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fullThing = pd.HDFStore(sys.argv[1], "r")
dic       = fullThing["onecluster"]
var1eval  = eval(sys.argv[2])
var2eval  = eval(sys.argv[3])
histogram = eval(sys.argv[4])
var1      = sys.argv[5]
var2      = sys.argv[6]

val1 = dic[var1]/np.real(dic.cov()[var1][var1])**0.5
val2 = dic[var2]/np.real(dic.cov()[var2][var2])**0.5
print(min(val1+val2), max(val1+val2), min(val1-val2), max(val1-val2))
print(np.cov(np.array(val1+val2), np.array(val1-val2)))
tha = histogram.Clone("thA")
thb = histogram.Clone("thB")
thc = histogram.Clone("thC")
thd = histogram.Clone("thD")

plt.plot(val1-val2, val1+val2, "b.")
plt.savefig("/eos/user/c/cericeci/www/scatter.pdf")

for i in range(len(dic)):
  #print(i, len(dic))
  if var1eval(val1[i] + val2[i]) and var2eval(val1[i] - val2[i]):
    tha.Fill(val1[i] + val2[i])
  if var1eval(val1[i] + val2[i]) and not(var2eval(val1[i] - val2[i])):
    thb.Fill(val1[i] + val2[i])
  if not(var1eval(val1[i] + val2[i])) and var2eval(val1[i] - val2[i]):
    thc.Fill(val1[i] + val2[i])
  if not(var1eval(val1[i] + val2[i])) and not(var2eval(val1[i] - val2[i])):
    thd.Fill(val1[i] + val2[i])

tha.Sumw2()
thb.Sumw2()
thc.Sumw2()
thd.Sumw2()

c = ROOT.TCanvas("c1","c1", 800, 600)
thABCD = tha.Clone("thABCD")
for i in range(1,thABCD.GetNbinsX()+1):
  thABCD.SetBinContent(i, thb.GetBinContent(i)*thc.Integral()/thd.Integral())

tha.SetMaximum(1.2*max(tha.GetMaximum(), thABCD.GetMaximum()))
tha.Draw("hist")
thABCD.Draw("P same")
tha.Print("all")
thb.Print("all")
thc.Print("all")
thd.Print("all")


c.SaveAs("/eos/user/c/cericeci/www/test.pdf")

