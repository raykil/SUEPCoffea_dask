import ROOT
import sys
import pandas as pd
import os

ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch(True)
ddir = sys.argv[1] #pd.HDFStore(sys.argv[1], "r")
var1eval  = eval(sys.argv[2])
var2eval  = eval(sys.argv[3])
histogram = eval(sys.argv[4])
var1      = sys.argv[5]
var2      = sys.argv[6]

tha = histogram.Clone("thA")
thb = histogram.Clone("thB")
thc = histogram.Clone("thC")
thd = histogram.Clone("thD")

ifile = 0
for f in os.listdir(ddir):
 ifile += 1
 print(ifile, len(os.listdir(ddir)))
 fullThing = pd.HDFStore(ddir + "/" + f, "r")
 dic       = fullThing["onecluster"]
 for i in range(len(dic)):
  #print(i, len(dic))
  if var1eval(dic[var1][i]) and var2eval(dic[var2][i]):
    tha.Fill(dic[var1][i])
  if var1eval(dic[var1][i]) and not(var2eval(dic[var2][i])):
    thb.Fill(dic[var1][i])
  if not(var1eval(dic[var1][i])) and var2eval(dic[var2][i]):
    thc.Fill(dic[var1][i])
  if not(var1eval(dic[var1][i])) and not(var2eval(dic[var2][i])):
    thd.Fill(dic[var1][i])
 if ifile > int(sys.argv[7]): break

tha.Sumw2()
thb.Sumw2()
thc.Sumw2()
thd.Sumw2()

c = ROOT.TCanvas("c1","c1", 800, 600)
thABCD = tha.Clone("thABCD")
for i in range(1,thABCD.GetNbinsX()+1):
  thABCD.SetBinContent(i, thb.GetBinContent(i)*thc.Integral()/thd.Integral())

tha.SetMaximum(1.2*max(tha.GetMaximum(), thABCD.GetMaximum()))
tha.SetLineColor(ROOT.kRed)
tha.Draw("P")
thABCD.Draw("P same")
#tha.Print("all")
#thb.Print("all")
#thc.Print("all")
#thd.Print("all")


c.SaveAs("/eos/user/c/cericeci/www/%s.pdf"%sys.argv[8])

