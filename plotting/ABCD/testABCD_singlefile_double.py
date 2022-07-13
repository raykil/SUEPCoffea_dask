import ROOT
import sys
import pandas as pd
import os

ddir = sys.argv[1] #pd.HDFStore(sys.argv[1], "r")
var1eval  = eval(sys.argv[2])
var2eval  = eval(sys.argv[3])
var1eval2  = eval(sys.argv[4])
histogram = eval(sys.argv[5])
var1      = sys.argv[6]
var2      = sys.argv[7]
filt = True

tha = histogram.Clone("thA")
thb = histogram.Clone("thB")
thc1 = histogram.Clone("thC1")
thd1 = histogram.Clone("thD1")
thc2 = histogram.Clone("thC2")
thd2 = histogram.Clone("thD2")

ifile = 0
for f in os.listdir(ddir):
 if not("hdf5" in f): continue
 ifile += 1
 print(ifile, len(os.listdir(ddir)))
 try:
   fullThing = pd.HDFStore(ddir + "/" + f, "r")
 except:
   continue
 dic       = fullThing["onecluster"]
 for i in range(len(dic)):
  #print(i, len(dic))
  if filt and (dic["leadcluster_ntracks"][i] < 20): continue
  #print(dic[var1][i], dic[var2][i])
  if var1eval(dic[var1][i]):
    if var2eval(dic[var2][i]):
      tha.Fill(dic[var1][i])
      #print("Is A")
    else:
      thb.Fill(dic[var1][i])
      #print("Is B")
  elif var2eval(dic[var2][i]):
    if var1eval2(dic[var1][i]):
      thc2.Fill(dic[var1][i])
      #print("Is C2")
    else:
      thc1.Fill(dic[var1][i])
      #print("Is C1")
  else:
    if var1eval2(dic[var1][i]):
      thd2.Fill(dic[var1][i])
      #print("Is D2")
    else:
      thd1.Fill(dic[var1][i])
      #print("Is D1")
 
 if ifile >= int(sys.argv[8]): break

tha.Sumw2()
thb.Sumw2()
thc1.Sumw2()
thd1.Sumw2()
thc2.Sumw2()
thd2.Sumw2()

errc1 = ROOT.Double()
errc2 = ROOT.Double()
errd1 = ROOT.Double()
errd2 = ROOT.Double()

c1 = thc1.IntegralAndError(1, thc1.GetNbinsX(), errc1)
d1 = thd1.IntegralAndError(1, thd1.GetNbinsX(), errd1)
c2 = thc2.IntegralAndError(1, thc2.GetNbinsX(), errc2)
d2 = thd2.IntegralAndError(1, thd2.GetNbinsX(), errd2)
ctot = c1 + d1
dtot = c2 + d2
ctoterr = (errc1**2+ errc2**2)**0.5
dtoterr = (errd1**2+ errd2**2)**0.5
print(tha.Integral(), thb.Integral(),c1,d1,c2,d2)
comErrSq = (errc1*errc1)/(c1*c1) + (errd1*errd1)/(d1*d1) + 4*(errc2*errc2)/(c2*c2) + 4*(errd2*errd2)/(d2*d2)
comErrSq = (ctoterr**2)/(ctot**2) + (dtoterr**2)/(dtot**2)
thABCD      = tha.Clone("thABCD")
thABCD_base = tha.Clone("thABCD_base")
for i in range(1,thABCD.GetNbinsX()+1):
  b1 = thb.GetBinContent(i)
  b1err = thb.GetBinError(i)
  if b1 == 0:
    thABCD.SetBinContent(i, 0)
    thABCD_base.SetBinContent(i, 0)
  else:
    err = ((b1*b1*c2*c2*d1)/(d2*d2*b1*c1))*(comErrSq + (b1err*b1err)/(b1*b1))**0.5
    #print((b1*b1*c2*c2*d1)/(d2*d2*b1*c1), err)
    thABCD.SetBinContent(i, (b1*b1*c2*c2*d1)/(d2*d2*b1*c1))
    thABCD.SetBinError(i, err)
    thABCD_base.SetBinContent(i, (b1*(c1+c2))/(d1+d2))
    thABCD_base.SetBinError(i, ((b1err**2)/(b1**2) + comErrSq)**0.5)

c = ROOT.TCanvas("c1","c1", 800, 600)
p1 = ROOT.TPad("mainpad", "mainpad", 0, 0.30, 1, 1)
p1.SetBottomMargin(0.075)
p1.SetTopMargin(0.08)
p1.SetLeftMargin(0.12)
p1.Draw()
p2 = ROOT.TPad("ratiopad", "ratiopad", 0, 0, 1, 0.30)
p2.SetTopMargin(0.05)
p2.SetBottomMargin(0.45)
p2.SetLeftMargin(0.12)
p2.SetFillStyle(0)
p2.Draw()

p1.cd()
tl = ROOT.TLegend(0.2,0.2,0.5,0.5)
tha.SetMaximum(1.2*max(tha.GetMaximum(), thABCD.GetMaximum()))
tha.SetLineColor(ROOT.kRed)
thABCD.SetLineColor(ROOT.kBlue)
thABCD_base.SetLineColor(ROOT.kBlack)
tl.AddEntry(tha, "MC", "l")
tl.AddEntry(thABCD, "ABCD (double)", "l")
tl.AddEntry(thABCD_base, "ABCD (simple)", "l")

tha.GetYaxis().SetTitle("Events (A.U.)")
tha.GetXaxis().SetTitle("")

tha.Draw("P")
thABCD.Draw("P same")
thABCD_base.Draw("P same")
#tha.Print("all")
#thb.Print("all")
#thc.Print("all")
#thd.Print("all")
tl.Draw("same")

p2.cd()

ra = tha.Clone("rha")
rABCD = thABCD.Clone("rABCD")
rABCD_base = thABCD_base.Clone("rABCD_base")

ra.Divide(tha)
rABCD.Divide(tha)
rABCD_base.Divide(tha)
ra.GetYaxis().SetTitle("Evs/MC evs")
ra.SetMaximum(2)
ra.SetMinimum(0)
ra.Draw("P")
rABCD.Draw("P same")
rABCD_base.Draw("P same")
c.SaveAs("/eos/user/c/cericeci/www/%s.pdf"%sys.argv[9])

