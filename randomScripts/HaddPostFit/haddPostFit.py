import ROOT
import sys
import ctypes

inROOT  = ROOT.TFile(sys.argv[1],"READ")
shapesS = "shapes_fit_s"
shapesB = "shapes_fit_b"
shapesP = "shapes_prefit"


channels = ["E2", "E1","B2_B2bin1","B2_B2bin2","B2_B2bin3","B2_B2bin4","B2_B2bin5","B2_B2bin6","B2_B2bin7","B2_B2bin8","D2","D1","B1_B1bin1","B1_B1bin2","B1_B1bin3","B1_B1bin4","B1_B1bin5","B1_B1bin6","B1_B1bin7","B1_B1bin8","C2","C1","SR_SRbin1","SR_SRbin2","SR_SRbin3","SR_SRbin4","SR_SRbin5","SR_SRbin6","SR_SRbin7","SR_SRbin8"]
nc = len(channels)
processes = ["total_background","SUEP_hadronic_mS125_mD3.00_T3.00", "data"]
years = ["UL16", "UL16APV", "UL17", "UL18"] if sys.argv[3] == "RunII" else ['']
#years = ["SR"]

shapes_fit_s =  {}
shapes_fit_b =  {}
shapes_prefit = {} 

def buildHisto(f, p, tag):
  out   = ROOT.TH1F(p + tag, p+tag, nc, 0, nc)
  outUp = ROOT.TH1F(p + tag+"Up", p+tag+"Up", nc, 0, nc) 
  outDn = ROOT.TH1F(p + tag+"Dn", p+tag+"Dn", nc, 0, nc)
  extraR = 1 if (not("SUEP" in p) or not("pre" in tag)) else 1. # In the prefit, the initial value for mu is 0.05, so we correct
  for ic, c in enumerate(channels):
    yields = 0.
    unc    = 0.
    for y in years:
      #print(f + "/"+ y +"_"+c +"/"+p)
      #read = inROOT.Get(f + "/"+ y +"_"+c +"/"+p)
      print(f + "/"+ y +c +"/"+p)
      read = inROOT.Get(f + "/"+ y +c +"/"+p)
      if not p == "data":
        yields += read.GetBinContent(1)*extraR
        unc    = (unc**2 + (extraR*read.GetBinError(1))**2)**0.5 #Assume decorrelation
      else:
        #xP = ROOT.Double()
        #yP = ROOT.Double()
        xP = ctypes.c_double() #ROOT.Double()
        yP = ctypes.c_double() #ROOT.Double()
        read.GetPoint(0, xP, yP)
        #yields += yP
        #unc = (unc**2+ yP**2)**0.5
        yields += yP.value
        unc     = (unc**2+ yP.value**2)**0.5
    if p != "data":
      if yields == 0:#For 0 yields case, add the asymptotic upper limit on yields 
        yields = 0.01
        unc = 1.4
     
    unc = max(0, min(unc, yields)) 
    if p=="data": unc = yields**0.5
    out.SetBinContent(ic+1, yields)
    out.SetBinError(ic+1, unc)
    outUp.SetBinContent(ic+1, max(0,yields+unc))
    outDn.SetBinContent(ic+1, max(0,yields-unc))
  if tag == "_fits":
    shapes_fit_s[p] = [out, outUp, outDn]
  if tag == "_fitb":
    shapes_fit_b[p] = [out, outUp, outDn]
  if tag == "_prefit":
    shapes_prefit[p] = [out, outUp, outDn]
  print(f, p, tag)
  out.Print("all")
  outUp.Print("all")
  outDn.Print("all")
for p in processes:
  buildHisto(shapesS, p, "_fits")
  buildHisto(shapesB, p, "_fitb")
  buildHisto(shapesP, p, "_prefit")
outROOT = ROOT.TFile(sys.argv[2], "RECREATE")
outROOT.cd()
for p in processes:
  for k in [shapes_fit_s, shapes_fit_b, shapes_prefit]:
    for pp in k[p]:
      pp.Write()

outROOT.Close()   

