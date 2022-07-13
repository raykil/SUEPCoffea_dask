import ROOT
import sys

arootAtoB = ROOT.TFile(sys.argv[1], "READ")
brootAtoB = ROOT.TFile(sys.argv[2], "READ")
crootAtoB = ROOT.TFile(sys.argv[3], "READ")
drootAtoB = ROOT.TFile(sys.argv[4], "READ")

samples = ["DY_Pt0To50", "DY_Pt50To100", "DY_Pt100To250", "DY_Pt250To400", "DY_Pt400To650", "DY_Pt650ToInf"]

varAtoB  = "leadclusterspher" 
varAtoC  = "leadclustertracks"

c = ROOT.TCanvas("c1","c1", 800, 600)

tha = arootAtoB.Get(varAtoB + "_" + samples[0])
thb = brootAtoB.Get(varAtoB + "_" + samples[0])
thc = crootAtoB.Get(varAtoB + "_" + samples[0])
thd = drootAtoB.Get(varAtoB + "_" + samples[0])

for s in samples[1:]:
  tha.Add(arootAtoB.Get(varAtoB + "_" +s))
  thb.Add(brootAtoB.Get(varAtoB + "_" +s))
  thc.Add(crootAtoB.Get(varAtoB + "_" +s))
  thd.Add(drootAtoB.Get(varAtoB + "_" +s))

thABCD = tha.Clone("thABCD")
c1 = thc.Integral(1, 15)
d1 = thd.Integral(1, 15)
c2 = thc.Integral(16, 30)
d2 = thd.Integral(16, 30)
print(c1,c2,d1,d2)
for i in range(1,thABCD.GetNbinsX()+1):
  b1 = thb.GetBinContent(i)
  if b1 == 0:
    thABCD.SetBinContent(i,0)
  else:
    thABCD.SetBinContent(i, (c2*c2*b1*b1*d1)/(c1*b1*d2*d2))

tha.SetMaximum(max(tha.GetMaximum(), thABCD.GetMaximum()))
tha.Draw("hist")
thABCD.Draw("P same")

c.SaveAs("/eos/user/c/cericeci/www/test.pdf")

