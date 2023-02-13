import ROOT
import sys
import pandas as pd
import os

ROOT.gStyle.SetOptStat(0)
ddir = sys.argv[1] #pd.HDFStore(sys.argv[1], "r")
var1eval1  = eval(sys.argv[2])
var2eval1  = eval(sys.argv[3])
var1eval2 = eval(sys.argv[4])
var2eval2 = eval(sys.argv[5]) 
histogram = eval(sys.argv[6])
var1      = sys.argv[7]
var2      = sys.argv[8]
filt = False

tha = histogram.Clone("thA")
thb1 = histogram.Clone("thB1")
thb2 = histogram.Clone("thB2")
thc1 = histogram.Clone("thC1")
thd1 = histogram.Clone("thD1")
thc2 = histogram.Clone("thC2")
thd2 = histogram.Clone("thD2")
the1 = histogram.Clone("thE1")
the2 = histogram.Clone("thE2")

ifile = 0
for f in os.listdir(ddir):
 if not("hdf5" in f): continue
 ifile += 1
 print(ifile, len(os.listdir(ddir)))
 try:
   fullThing = pd.HDFStore(ddir + "/" + f, "r")
 except:
   continue
 dic       = fullThing["SR"]
 for i in range(len(dic)):
  #print(i, len(dic))
  #if filt and (dic["leadcluster_ntracks"][i] < 20): continue
  #print(dic[var1][i], dic[var2][i])
  if var1eval1(dic[var1][i]):
    if var2eval1(dic[var2][i]):
      tha.Fill(dic[var1][i])
    elif var2eval2(dic[var2][i]):
      thb1.Fill(dic[var1][i])
    else:
      thb2.Fill(dic[var1][i])
  elif var2eval1(dic[var2][i]):
    if var1eval2(dic[var1][i]):
      thc1.Fill(dic[var1][i])
      #print("Is C2")
    else:
      thc2.Fill(dic[var1][i])
      #print("Is C1")
  elif var2eval2(dic[var2][i]):
    if var1eval2(dic[var1][i]):
      thd1.Fill(dic[var1][i])
      #print("Is D2")
    else:
      thd2.Fill(dic[var1][i])
      #print("Is D1")
  else:
    if var1eval2(dic[var1][i]):
      the1.Fill(dic[var1][i])
      #print("Is D2")
    else:
      the2.Fill(dic[var1][i])
      #print("Is D1")


 
 if ifile >= int(sys.argv[9]): break

tha.Sumw2()
thb1.Sumw2()
thb2.Sumw2()
thc1.Sumw2()
thd1.Sumw2()
thc2.Sumw2()
thd2.Sumw2()
the1.Sumw2()
the2.Sumw2()

errb1 = ROOT.Double()
errb2 = ROOT.Double()
errc1 = ROOT.Double()
errc2 = ROOT.Double()
errd1 = ROOT.Double()
errd2 = ROOT.Double()
erre1 = ROOT.Double()
erre2 = ROOT.Double()

b1 = thb1.IntegralAndError(1, thb1.GetNbinsX(), errb1)
b2 = thb2.IntegralAndError(1, thb2.GetNbinsX(), errb2)
c1 = thc1.IntegralAndError(1, thc1.GetNbinsX(), errc1)
d1 = thd1.IntegralAndError(1, thd1.GetNbinsX(), errd1)
c2 = thc2.IntegralAndError(1, thc2.GetNbinsX(), errc2)
d2 = thd2.IntegralAndError(1, thd2.GetNbinsX(), errd2)
e1 = the1.IntegralAndError(1, the1.GetNbinsX(), erre1)
e2 = the2.IntegralAndError(1, the2.GetNbinsX(), erre2)

print(b1,b2,c1,c2,d1,d2,e1,e2)
# For standard ABCD
b_4 = b1 + b2
c_4 = c1 + c2
d_4 = d1 + d2 + e1 +e2
b_4_err = (errb1**2+ errb2**2)**0.5
c_4_err = (errc1**2+ errc2**2)**0.5
d_4_err = (errd1**2+ errd2**2+ erre1**2+ erre2**2)**0.5
ABCD_4_commerr = (c_4_err**2/c_4**2 + d_4_err**2/d_4**2)**0.5

# For ABCEDF, 2 bins in X
d1_6X = d1 + e1
d2_6X = d2 + e2
d1_6X_err = (errd1**2+ erre1**2)**0.5
d2_6X_err = (errd2**2+ erre2**2)**0.5
b_6X  = b1 + b2
b_6X_err = b_4_err
ABCD_6X_comerr = (errc1**2/c1**2 + errc2**2/c2**2 +  d1_6X_err**2/d1_6X**2+ d2_6X_err**2/d2_6X**2)**0.5

# For ABCDEF, 2 bins in Y
d1_6Y = d1 + d2
d2_6Y = e1 + e2
d1_6Y_err = (errd1**2+ errd2**2)**0.5
d2_6Y_err = (erre1**2+ erre2**2)**0.5
c_6Y  = c1 + c2
c_6Y_err = c_4_err
ABCD_6Y_comerr = (errc1**2/c1**2 + errc2**2/c2**2 +  d1_6Y_err**2/d1_6Y**2+ d2_6Y_err**2/d2_6Y**2)**0.5

# For full 9 bins shenanigans
ABCD_8_comerr = (errc1**2/c1**2 + errc2**2/c2**2 + errd1**2/d1**2 + errd2**2/d2**2 +erre1**2/e1**2 + erre2**2/e2**2)**0.5

print(tha.Integral(), b1, b2, c1, c2, d1,d2, e1, e2)
thABCD_8    = tha.Clone("thABCD_8")
thABCD_4    = tha.Clone("thABCD_4")
thABCD_6X   = tha.Clone("thABCD_6X")
thABCD_6Y   = tha.Clone("thABCD_6Y")

for i in range(1,thABCD_8.GetNbinsX()+1):
  bb1 = thb1.GetBinContent(i)
  if bb1 != 0: bb1err = thb1.GetBinError(i)
  bb2 = thb2.GetBinContent(i)
  if bb2 != 0: bb2err = thb2.GetBinError(i)
  if bb1 != 0 and bb2 != 0: bballerr = (bb2err**2/bb2**2 + bb1err**2/bb1**2)**0.5 
  bb_sum = bb1 + bb2
  if e2==0 or d1==0 or c2==0 or bb1==0 or bb2==0 or c1 == 0:
    thABCD_8.SetBinContent(i,0)
  else:
    thABCD_8.SetBinContent(i, ((bb2*c2)/(e2))*((c1**4*bb1**4)/(d1**4))*((d2**2)/(c2**2*bb1**2))*((e1**2)/(c1**2*bb2**2)))
    thABCD_8.SetBinError(i, (ABCD_8_comerr + (bb1err/bb1) ** 2 + (bb2err/bb2)**2)**0.5)

  if d1_6X==0 or c2==0 or bb1==0 or bb2==0:
    thABCD_6X.SetBinContent(i,0)
  else:
    thABCD_6X.SetBinContent(i,(bb_sum*c1**2*d2_6X)/(d1_6X**2*c2))
    thABCD_6X.SetBinError(i,(ABCD_6X_comerr + (bb1err/bb1) ** 2 + (bb2err/bb2)**2)**0.5)

  if d1_6Y==0 or bb2==0 or bb1==0:
    thABCD_6Y.SetBinContent(i,0)
  else:
    thABCD_6Y.SetBinContent(i,(c_6Y*bb1**2*d2_6Y)/(d1_6Y**2*bb2))
    thABCD_6Y.SetBinError(i,(ABCD_6Y_comerr + (bb1err/bb1) ** 2 + (bb2err/bb2)**2)**0.5)

  if d_4 == 0 or bb2==0 or bb1==0:
    thABCD_4.SetBinContent(i,0)
  else:
    thABCD_4.SetBinContent(i,(bb_sum*c_4)/(d_4))
    thABCD_4.SetBinError(i,(ABCD_4_commerr + (bb1err/bb1) ** 2 + (bb2err/bb2)**2)**0.5)



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
tha.SetMaximum(1.2*max(tha.GetMaximum(), thABCD_8.GetMaximum()))
tha.SetLineColor(ROOT.kRed)
thABCD_8.SetLineColor(ROOT.kBlue)
thABCD_6X.SetLineColor(ROOT.kBlack)
thABCD_6Y.SetLineColor(ROOT.kGreen)
thABCD_4.SetLineColor(ROOT.kYellow)

tl.AddEntry(tha, "MC", "l")
tl.AddEntry(thABCD_8, "ABCD (8 CR)", "l")
tl.AddEntry(thABCD_6X, "ABCD (6 CR - X)", "l")
tl.AddEntry(thABCD_6Y, "ABCD (6 CR - Y)", "l")
tl.AddEntry(thABCD_4, "ABCD (4 CR)", "l")

tha.GetYaxis().SetTitle("Events (A.U.)")
tha.GetXaxis().SetTitle("")

tha.Draw("P")
thABCD_8.Draw("P same")
thABCD_6X.Draw("P same")
thABCD_6Y.Draw("P same")
thABCD_4.Draw("P same")

#tha.Print("all")
#thb.Print("all")
#thc.Print("all")
#thd.Print("all")
tl.Draw("same")

p2.cd()

ra = tha.Clone("rha")
rABCD_8 = thABCD_8.Clone("rABCD_8")
rABCD_6X = thABCD_6X.Clone("rABCD_6X")
rABCD_6Y = thABCD_6Y.Clone("rABCD_6Y")
rABCD_4 = thABCD_4.Clone("rABCD_4")


ra.Divide(tha)
rABCD_8.Divide(tha)
rABCD_6X.Divide(tha)
rABCD_6Y.Divide(tha)
rABCD_4.Divide(tha)

ra.GetYaxis().SetTitle("Evs/MC evs")
ra.SetMaximum(2)
ra.SetMinimum(0)
ra.Draw("P")
rABCD_8.Draw("P same")
rABCD_6X.Draw("P same")
rABCD_6Y.Draw("P same")
rABCD_4.Draw("P same")

c.SaveAs("/eos/user/c/cericeci/www/%s.pdf"%sys.argv[10])
c.SaveAs("/eos/user/c/cericeci/www/%s.png"%sys.argv[10])

