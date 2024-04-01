import ROOT
import sys
import os

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)
def doABCDEFGH(vals, errs, tha, thb1, thb2, tag, doPlot=False, doSig=None):
  b1, b2, c1, c2, d1, d2, e1, e2 = vals
  errb1, errb2, errc1, errc2, errd1, errd2, erre1, erre2 = errs
  b2err = errb2
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
  ABCD_8_comerr = (2*errc1**2/c1**2 + errc2**2/c2**2 + 4*errd1**2/d1**2 + 2*errd2**2/d2**2 +2*erre1**2/e1**2 + erre2**2/e2**2)**0.5
  #print(ABCD_8_comerr)
  tha.SetMarkerStyle(0)
  thABCD_8    = tha.Clone("thABCD_8")
  thABCD_4    = tha.Clone("thABCD_4")
  thABCD_6X   = tha.Clone("thABCD_6X")
  thABCD_6Y   = tha.Clone("thABCD_6Y")
  check_bb1 = []
  check_bb2 = []
  check_sr = []
  check_c1, check_c2, check_d1, check_d2, check_e1, check_e2 = [], [], [], [], [], []
  for i in range(1,thABCD_8.GetNbinsX()+1):
    bb1 = thb1.GetBinContent(i)
    if bb1 != 0: bb1err = thb1.GetBinError(i)
    bb2 = thb2.GetBinContent(i)
    if bb2 != 0: b2err = thb2.GetBinError(i)
    if bb1 != 0 and bb2 != 0: bballerr = (b2err**2/bb2**2 + bb1err**2/bb1**2)**0.5 
    bb_sum = bb1 + bb2
    if e2==0 or d1==0 or c2==0 or bb1==0 or bb2==0 or c1 == 0:
      check_bb1.append(bb1)
      check_bb2.append(bb2)
      check_sr.append(0)
      check_c1.append(c1)
      check_c2.append(c2)
      check_d1.append(d1)
      check_d2.append(d2)
      check_e1.append(e1)
      check_e2.append(e2)
      thABCD_8.SetBinContent(i,0)
    else:
      thABCD_8.SetBinContent(i, ((bb2*c2)/(e2))*(((c1**4*bb1**4)/(d1**4))*((d2**2)/(c2**2*bb1**2))*((e1**2)/(c1**2*bb2**2))))
      check_bb1.append(bb1)
      check_bb2.append(bb2)
      check_sr.append(((bb2*c2)/(e2))*(((c1**4*bb1**4)/(d1**4))*((d2**2)/(c2**2*bb1**2))*((e1**2)/(c1**2*bb2**2))))
      check_c1.append(c1)
      check_c2.append(c2)
      check_d1.append(d1)
      check_d2.append(d2)
      check_e1.append(e1)
      check_e2.append(e2)
      #thABCD_8.SetBinContent(i, ((bb2*c2)/(e2))*(((c1**4*b1**4)/(d1**4))*((d2**2)/(c2**2*b1**2))*((e1**2)/(c1**2*b2**2))))
      thABCD_8.SetBinError(i, thABCD_8.GetBinContent(i)*(ABCD_8_comerr**2 + 2*(bb1err/bb1) ** 2 + (b2err/b2)**2)**0.5)
      if thABCD_8.GetBinError(i) > thABCD_8.GetBinContent(i): thABCD_8.SetBinError(i, thABCD_8.GetBinContent(i))
    if d1_6X==0 or c2==0 or bb1==0 or bb2==0:
      thABCD_6X.SetBinContent(i,0)
    else:
      thABCD_6X.SetBinContent(i,(bb_sum*c1**2*d2_6X)/(d1_6X**2*c2))
      thABCD_6X.SetBinError(i,(ABCD_6X_comerr + (bb1err/bb1) ** 2 + (b2err/b2)**2)**0.5)

    if d1_6Y==0 or bb2==0 or bb1==0:
      thABCD_6Y.SetBinContent(i,0)
    else:
      thABCD_6Y.SetBinContent(i,(c_6Y*bb1**2*d2_6Y)/(d1_6Y**2*b2))
      thABCD_6Y.SetBinError(i,(ABCD_6Y_comerr + (bb1err/bb1) ** 2 + (b2err/b2)**2)**0.5)

    if d_4 == 0 or bb2==0 or bb1==0:
      thABCD_4.SetBinContent(i,0)
    else:
      thABCD_4.SetBinContent(i,(bb_sum*c_4)/(d_4))
      thABCD_4.SetBinError(i,(ABCD_4_commerr + (bb1err/bb1) ** 2 + (b2err/b2)**2)**0.5)
    if "data" in sys.argv[2]:
      tha.SetBinError(i, tha.GetBinContent(i)**0.5)
  #print(check_bb1)
  #print(check_bb2)
  #print(check_sr)
  #print(check_c1)
  #print(check_c2)
  #print(check_d1)
  #print(check_d2)
  #print(check_e1)
  #print(check_e2)
  thABCD_8AC = thABCD_8.Clone("thABCD_8AC")
  #thABCD_8AC.Print("all")

  def get_total_statistical_uncertainty(histogram):
    total_uncertainty_squared = 0.0
    for i in range(histogram.GetNbinsX() + 2):
        bin_error = histogram.GetBinError(i)
        total_uncertainty_squared += bin_error**2
    return total_uncertainty_squared**0.5
  
  tha_uncertainty = get_total_statistical_uncertainty(tha)
  thABCD_8_uncertainty = get_total_statistical_uncertainty(thABCD_8)
  ratio = tha.Integral() / thABCD_8.Integral()
  ratio_uncertainty = ratio * ((tha_uncertainty / tha.Integral())**2 + (thABCD_8_uncertainty / thABCD_8.Integral())**2)**0.5
  print("Ratio:", ratio)
  print("Ratio Uncertainty:", ratio_uncertainty)
  
  thABCD_8AC.Scale(tha.Integral()/thABCD_8.Integral())
   #thABCD_8AC.Print("all")
  if not(doPlot): return tha, thABCD_4, thABCD_6Y, thABCD_6X, thABCD_8
  c = ROOT.TCanvas("c1","c1", 800, 600)
  p1 = ROOT.TPad("mainpad", "mainpad", 0, 0.30, 1, 1)
  p1.SetBottomMargin(0.075)
  p1.SetTopMargin(0.14)
  p1.SetLeftMargin(0.12)
  p1.SetLogy(True)
  p1.Draw()
  p2 = ROOT.TPad("ratiopad", "ratiopad", 0, 0, 1, 0.30)
  p2.SetTopMargin(0.05)
  p2.SetBottomMargin(0.45)
  p2.SetLeftMargin(0.12)
  p2.SetFillStyle(0)
  p2.Draw()

  p1.cd()
  tl = ROOT.TLegend(0.55,0.55,0.85,0.86)
  tha.SetMaximum(2.5*max(tha.GetMaximum(), thABCD_8.GetMaximum()))
  tha.SetLineColor(ROOT.kRed)
  thABCD_8.SetLineColor(ROOT.kBlue)
  #thABCD_6X.SetLineColor(ROOT.kBlack)
  #thABCD_6Y.SetLineColor(ROOT.kGreen)
  thABCD_8AC.SetLineColor(ROOT.kGreen)
  thABCD_4.SetLineColor(ROOT.kBlue)
  if doSig:
    for iss in range(len(doSig)): doSig[i].SetLineColor(ROOT.kBlack)
  tl.AddEntry(tha, "Direct", "fl")
  #tl.AddEntry(thABCD_8, "ABCD (8 CR)", "l")
  tl.AddEntry(thABCD_8AC, "ABCD (8 CR)", "l")
  #tl.AddEntry(thABCD_6X, "ABCD (6 CR - X)", "l")
  #tl.AddEntry(thABCD_6Y, "ABCD (6 CR - Y)", "l")
  tl.AddEntry(thABCD_4, "ABCD (4 CR)", "l")
  #if doSig:
  #  #: tl.AddEntry(sig, "Signal", "l")


  tha.SetTitle("")
  tha.GetXaxis().SetLabelSize(0)
  tha.GetYaxis().SetLabelSize(0.04)
  tha.GetYaxis().SetTitleSize(0.08)
  tha.GetYaxis().SetTitleOffset(0.72)

  tha.GetYaxis().SetTitle("Events")
  tha.GetXaxis().SetTitle("")

  tha.SetFillColor(ROOT.kRed)
  tha.SetLineColor(ROOT.kRed)
  tha.SetFillStyle(3244)
  thah = tha.Clone("thah")
  thah.SetFillColor(0)
  thah.Draw("hist")
  tha.Draw("E2 same")
  thABCD_4.Draw("P same")
  #thABCD_8.Draw("P same")
  thABCD_8AC.Draw("P same")
  #print("Last, 8CR")
  #thABCD_8.Print("all")
  #print("Last, Obs")
  #tha.Print("all")
  #thABCD_6X.Draw("P same")
  #thABCD_6Y.Draw("P same")
  if doSig:
    for iss in range(len(doSig)):
     doSig[i].SetFillStyle(0) 
     doSig[i].Draw("hist same")
  tl.Draw("same")

  p2.cd()

  ra = tha.Clone("rha")
  rABCD_8 = thABCD_8.Clone("rABCD_8")
  rABCD_8AC = thABCD_8AC.Clone("rABCD_8AC")

  #rABCD_6X = thABCD_6X.Clone("rABCD_6X")
  #rABCD_6Y = thABCD_6Y.Clone("rABCD_6Y")
  rABCD_4 = thABCD_4.Clone("rABCD_4")
  #if doSig:
  #  for sig in doSig:
  #  rSig = doSig.Clone("rsig")
  #  rSig.Divide(tha)
  ra.Divide(tha)
  rABCD_8.Divide(tha)
  rABCD_8AC.Divide(tha)

  #rABCD_6X.Divide(tha)
  #rABCD_6Y.Divide(tha)
  rABCD_4.Divide(tha)

  ra.SetTitle("")
  ra.GetYaxis().SetTitle("X/Direct Est.")
  ra.GetXaxis().SetTitle(doPlot[1])
  ra.GetYaxis().SetTitleSize(0.12)
  ra.GetYaxis().SetTitleOffset(0.32)
  ra.GetXaxis().SetTitleSize(0.12)
  ra.GetXaxis().SetLabelSize(0.1)
  ra.GetYaxis().SetLabelSize(0.06)

  for ibin in range(0, rABCD_8.GetNbinsX()+1):
    rABCD_8.SetBinError(ibin, rABCD_8.GetBinContent(ibin)*thABCD_8.GetBinError(ibin)/max(0.001, thABCD_8.GetBinContent(ibin)))
    rABCD_8AC.SetBinError(ibin, rABCD_8AC.GetBinContent(ibin)*thABCD_8AC.GetBinError(ibin)/max(0.001, thABCD_8AC.GetBinContent(ibin)))
    rABCD_4.SetBinError(ibin, rABCD_4.GetBinContent(ibin)*thABCD_4.GetBinError(ibin)/max(0.001, thABCD_4.GetBinContent(ibin)))

  ra.GetYaxis().SetTitle("X/Direct")
  ra.SetMaximum(2)
  ra.SetMinimum(0)
  rah = ra.Clone("rah")
  rah.SetFillColor(0)
  rah.Draw("hist")
  ra.Draw("E2 same")
  #rABCD_8.Draw("P same")
  rABCD_8AC.Draw("P same")

  #rABCD_6X.Draw("P same")
  #rABCD_6Y.Draw("P same")
  rABCD_4.Draw("P same")
  #if doSig:
  #  rSig.SetFillStyle(0)
  #  rSig.Draw("hist same")

  c.SaveAs("%s.pdf"%tag)
  c.SaveAs("%s.png"%tag)
  tf = ROOT.TFile("%s.root"%tag,"RECREATE")
  tf.cd()
  tha.Write()
  thABCD_4.Write()
  thABCD_6Y.Write()
  thABCD_6X.Write()
  thABCD_8.Write()
  thABCD_8AC.Write()
  if doSig:
    for iss in range(len(doSig)): doSig[iss].Write()
  data_obs = thABCD_8AC.Clone("data_obs")
  data_obs.Write()
  return tha, thABCD_4, thABCD_6Y, thABCD_6X, thABCD_8

def checkClosure(fullhisto, dicvar1, dicvar2, sigs):
  cutvar1_1 = float(sys.argv[3])
  cutvar1_2 = float(sys.argv[4])
  cutvar2_1 = float(sys.argv[5])
  cutvar2_2 = float(sys.argv[6])
  #print(cutvar1_1, cutvar1_2, cutvar2_1, cutvar2_2)
  tha = fullhisto.Clone("tha")
  thb1= fullhisto.Clone("thb1")
  thb2= fullhisto.Clone("thb2")

  Var1_tight = []
  Var2_tight = []
  Var1_loose = []
  Var2_loose = []

  b1, b2, c1, c2, d1, d2, e1, e2 = 0, 0, 0, 0, 0, 0, 0, 0
  for ibinx in range(-1, fullhisto.GetNbinsX()+2):
    isVar1Tight = fullhisto.GetXaxis().GetBinLowEdge(ibinx)*dicvar1[-1] >= cutvar1_2*dicvar1[-1]
    isVar1Loose = fullhisto.GetXaxis().GetBinLowEdge(ibinx)*dicvar1[-1] >= cutvar1_1*dicvar1[-1]
    #print(ibinx)
    #print(fullhisto.GetXaxis().GetBinLowEdge(ibinx))
    #print(dicvar1[-1])
    #print(cutvar1_2, isVar1Tight)
    #print(cutvar1_1, isVar1Loose)
    #if ibinx >=25:
    #  meow
    if isVar1Tight:
        if ibinx not in Var1_tight:
          Var1_tight.append(ibinx)
    if isVar1Loose:
        if ibinx not in Var1_loose:
          Var1_loose.append(ibinx)
    for ibiny  in range(-1, fullhisto.GetNbinsY()+2):
      isVar2Tight = fullhisto.GetYaxis().GetBinLowEdge(ibiny)*dicvar2[-1] > cutvar2_2*dicvar2[-1]
      isVar2Loose = fullhisto.GetYaxis().GetBinLowEdge(ibiny)*dicvar2[-1] > cutvar2_1*dicvar2[-1]
      #print(ibiny)
      #print(fullhisto.GetYaxis().GetBinLowEdge(ibiny))
      #print(dicvar2[-1])
      #print(cutvar2_2, isVar2Tight)
      #print(cutvar2_1, isVar2Loose)
      #if ibiny >=50:
      #  meow
      if isVar2Tight:
          if ibiny not in Var2_tight:
            Var2_tight.append(ibiny)
      if isVar2Loose:
          if ibiny not in Var2_loose:
            Var2_loose.append(ibiny)   
      if isVar1Tight:
        if isVar2Tight:
          thb1.SetBinContent(ibinx, ibiny, 0)
          thb2.SetBinContent(ibinx, ibiny, 0)
        if isVar2Loose and not isVar2Tight:
          tha.SetBinContent(ibinx, ibiny, 0)
          tha.SetBinError(ibinx, ibiny, 0)
          thb2.SetBinContent(ibinx, ibiny, 0)
          thb2.SetBinError(ibinx, ibiny, 0)
          for iss in range(len(sigs)): sigs[iss].SetBinContent(ibinx, ibiny, 0)
        if not isVar2Loose:
          tha.SetBinContent(ibinx, ibiny, 0)
          tha.SetBinError(ibinx, ibiny, 0)
          thb1.SetBinContent(ibinx, ibiny, 0)
          thb1.SetBinError(ibinx, ibiny, 0)
          for iss in range(len(sigs)): sigs[iss].SetBinContent(ibinx, ibiny, 0)

      else:
        tha.SetBinContent(ibinx, ibiny, 0)
        tha.SetBinError(ibinx, ibiny, 0)
        thb1.SetBinContent(ibinx, ibiny, 0) 
        thb2.SetBinContent(ibinx, ibiny, 0)
        thb1.SetBinError(ibinx, ibiny, 0)
        thb2.SetBinError(ibinx, ibiny, 0)
        for iss in range(len(sigs)): sigs[iss].SetBinContent(ibinx, ibiny, 0)

      if isVar1Loose and (not isVar1Tight):
        if isVar2Tight:
          c1 += fullhisto.GetBinContent(ibinx, ibiny)
        if isVar2Loose and (not isVar2Tight):
          d1 += fullhisto.GetBinContent(ibinx, ibiny)
        if not isVar2Loose:
          e1 += fullhisto.GetBinContent(ibinx, ibiny)
      if not isVar1Loose:
        if isVar2Tight:
          c2 += fullhisto.GetBinContent(ibinx, ibiny)
        if isVar2Loose and (not isVar2Tight):
          d2 += fullhisto.GetBinContent(ibinx, ibiny)
        if not isVar2Loose:
          e2 += fullhisto.GetBinContent(ibinx, ibiny)

  #print(Var1_loose)
  #print(Var1_tight)
  #print(Var2_loose)
  #print(Var2_tight)
  
  tha = tha.ProjectionX()
  #print("Projection")
  #tha.Print("all")
  thb1 = thb1.ProjectionX()
  thb2 = thb2.ProjectionX()
  for iss in range(len(sigs)): sigs[iss] = sigs[iss].ProjectionX()

  customBins = [0, 14, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96, 100]
  nCustomBins = len(customBins) - 1

  customBinArray = ROOT.std.vector('double')(customBins)
  newHistogram = ROOT.TH1F("newHistogram", "Histogram with Custom Binning", nCustomBins, customBinArray.data())

  for i in range(1, tha.GetNbinsX() + 1):
    content = tha.GetBinContent(i)
    error = tha.GetBinError(i)
    binCenter = tha.GetBinCenter(i)

    newBin = newHistogram.FindBin(binCenter)
    

    currentContent = newHistogram.GetBinContent(newBin)
    newHistogram.SetBinContent(newBin, currentContent + content)

    currentError = newHistogram.GetBinError(newBin)
    newError = (currentError**2 + error**2)**0.5
    newHistogram.SetBinError(newBin, newError)

  
  tha = newHistogram

  customBinArray = ROOT.std.vector('double')(customBins)
  newHistogram = ROOT.TH1F("newHistogram", "Histogram with Custom Binning", nCustomBins, customBinArray.data())

  for i in range(1, thb1.GetNbinsX() + 1):
    content = thb1.GetBinContent(i)
    error = thb1.GetBinError(i)
    binCenter = thb1.GetBinCenter(i)

    newBin = newHistogram.FindBin(binCenter)
    
    currentContent = newHistogram.GetBinContent(newBin)
    newHistogram.SetBinContent(newBin, currentContent + content)
    
    currentError = newHistogram.GetBinError(newBin)
    newError = (currentError**2 + error**2)**0.5
    newHistogram.SetBinError(newBin, newError)

  
  thb1 = newHistogram

  customBinArray = ROOT.std.vector('double')(customBins)
  newHistogram = ROOT.TH1F("newHistogram", "Histogram with Custom Binning", nCustomBins, customBinArray.data())

  for i in range(1, thb2.GetNbinsX() + 1):
    content = thb2.GetBinContent(i)
    error = thb2.GetBinError(i)
    binCenter = thb2.GetBinCenter(i)

    newBin = newHistogram.FindBin(binCenter)

    currentContent = newHistogram.GetBinContent(newBin)
    newHistogram.SetBinContent(newBin, currentContent + content)

    currentError = newHistogram.GetBinError(newBin)
    newError = (currentError**2 + error**2)**0.5
    newHistogram.SetBinError(newBin, newError)

  
  thb2 = newHistogram
  
  #tha.Rebin(5)
  #thb1.Rebin(5)
  #thb2.Rebin(5)

  total_yields = tha.Integral() + thb1.Integral() + thb2.Integral() + c1 + c2 + d1 + d2 + e1 + e2
  flag = 0
  print('C2 D2 E2')
  if e2 > d2 or d2 > c2:
    print(c2, d2, e2)
    flag = 1
  print('C1 D1 E1')
  if e1 > d1 or d1 > c1:
    print(c1, d1, e1)
    flag = 1
  print('A B1 B2')
  if thb2.Integral() > thb1.Integral() or thb1.Integral() > tha.Integral():
    print(tha.Integral(), thb1.Integral(), thb2.Integral())
    flag = 1
  print('C2 C1 A')
  if tha.Integral() > c1 or c1 > c2:
    print(c2, c1, tha.Integral())
    flag = 1
  print('D2 D1 B1')
  if thb1.Integral() > d1 or d1 > d2:
    print(d2, d1, thb1.Integral())
    flag = 1
  print('E2 E1 B2')
  if thb2.Integral() > e1 or e1 > e2:
    print(e2, e1, thb2.Integral())
    flag = 1
  if flag == 0:
    print('C2 D2 E2')
    print(c2, d2, e2)
    print('C1 D1 E1')
    print(c1, d1, e1)
    print('A B1 B2')
    print(tha.Integral(), thb1.Integral(), thb2.Integral())
    print('C2 C1 A')
    print(c2, c1, tha.Integral())
    print('D2 D1 B1')
    print(d2, d1, thb1.Integral())
    print('E2 E1 B2')
    print(e2, e1, thb2.Integral())

  #print("Rebinned")
  #tha.Print("all")
  for iss in range(len(sigs)): sigs[iss].Rebin(5)

  vals = [thb1.Integral(), thb2.Integral(), c1, c2, d1, d2, e1,e2]
  errs = [i**0.5 for i in vals] 
  #print(vals, errs)
  doABCDEFGH(vals, errs, tha, thb1, thb2, sys.argv[7], doPlot=dicvar1, doSig=(sigs  if "SR" in sys.argv[1] else None))

 
var = {
#  "S_C" : ["leadclusterSpher_C", "S^{SUEP}", 100, 0, 1., 10, 1],
  "N_C" : ["leadcluster_ntracks", "N_{tracks}^{SUEP}", 100, 0, 100, 10, 1],
  "jet1pt":["leadjet_pt", "p_{T}^{jet1} [GeV]", 200, 0, 1000, 10, -1],
#  "S_pt": ["leadcluster_pt", "p_{T}^{SUEP} [GeV]", 200, 0, 1000, 10, 1],
#  "N" : ["ntracks", "N_{tracks}", 200, 0, 200, 10, 1],
#  "MET_pt": ["MET_pt", "p_{T}^{miss} [GeV]", 200, 0, 200, 10,-1],
}


inp = sys.argv[1] # "/eos/user/c/cericeci/www/SUEP/UL16APV/SR_2D/" 
for var1 in ["N_C"]:
  #if var1 != "N_C": continue
  for var2 in ["jet1pt"]:
    #if var2 != "jet1pt": continue
    #if var1 == var2: continue
    #print(inp + "/2D_%s_%s.root"%(var1, var2))
    if os.path.isfile(inp + "/2D_%s_%s.root"%(var1, var2)):
      #print("Run")
      tf = ROOT.TFile(inp + "/2D_%s_%s.root"%(var1, var2), "READ")
      #print(inp + "/2D_%s_%s.root"%(var1, var2), sys.argv[2] if "total" in sys.argv[2] else "2D_%s_%s_"%(var1, var2)+sys.argv[2])
      th = tf.Get(sys.argv[2]+";1" if "total" in sys.argv[2] else "2D_%s_%s_"%(var1, var2)+sys.argv[2]) #"2D_%s_%s_"%(var1, var2)+sys.argv[2] )
      tl = tf.GetListOfKeys()
      sigs = []
      #for k in tl:
      #  print(k.GetName())
      #  if "SUEP" in k.GetName(): sigs.append(tf.Get(k.GetName()))
      #print(sigs)
      #print("Correlation: %7s--%7s : %1.3f"%(var1, var2, th.GetCorrelationFactor()))
      checkClosure(th, var[var1], var[var2], sigs)
