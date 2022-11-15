import ROOT 
import numpy as np
import os

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(False)


inFiles = [ROOT.TFile("/eos/user/c/cericeci/SUEP_signals/skim_UL18/DYToLL_M50_Pt100To250/DYToLL_MLL50_Pt100To250_9.root", "READ")]#ROOT.TFile("/eos/user/j/jkil/SUEP/SUEPCoffea_dask/ZH18/total.root","READ")] #[ROOT.TFile("/eos/home-c/cericeci/SUEP_signals/UL18_withgeninfo/ZHleptonicpythia_generic_M125_MD2_T2_HT0.0_new_propergen/NANOAOD/" + f,"READ") for f in os.listdir("/eos/home-c/cericeci/SUEP_signals/UL18_withgeninfo/ZHleptonicpythia_generic_M125_MD2_T2_HT0.0_new_propergen/NANOAOD/")]
trees   =  [ inFile.Get("Events") for inFile in inFiles]
boostToH = False

h_tot    = ROOT.TH1F("tot","tot", 20,0,1)
h_totlab = ROOT.TH1F("totlab","totlab", 20,0,1)
h_dec    = ROOT.TH1F("dec","dec", 20,0,1)
h_declab = ROOT.TH1F("declab","declab", 20,0,1)

h_tracks = ROOT.TH1F("tracks","tracks", 20,0,1)
h_SUEPtracks = ROOT.TH1F("SUEPtracks","SUEPtracks", 20,0,1)
h_BACKtracks = ROOT.TH1F("BACKtracks","BACKtracks", 20,0,1)

h_trackslab = ROOT.TH1F("trackslab","trackslab", 20,0,1)
h_SUEPtrackslab = ROOT.TH1F("SUEPtrackslab","SUEPtrackslab", 20,0,1)
h_BACKtrackslab = ROOT.TH1F("BACKtrackslab","BACKtrackslab", 20,0,1)



def isChargedFromId(ev, idx, pdgid, id):
  charged    = [211, -211, 11, 13, 15, -11, -13, -15, 1,2,3,4,5,6,24, -1,-2,-3,-4,-5,-6, -24, 321, -321, 3222,-3222, 2212, -2212, 3112, -3112, 3312, -3312]
  notcharged = [21, 22, 23, 25, 12,14,16,-12,-14,-16,111, 130, 310,311, 2112, -2112, 3122, -3122, 3322, -3322]
  if pdgid in notcharged: return False
  elif pdgid in charged:
    while True:
      idx = ev.GenPart_genPartIdxMother[idx]
      if idx == -1: 
        return False
      else:
        if ev.GenPart_pdgId[idx] == id:
          return True
  else:
    print("Missing %i in lists"%pdgid)

def isFrom(ev, idx):
  if idx < 0: return -1
  decaychain = [ ev.GenPart_pdgId[idx] ]
  status     = [ ev.GenPart_status[idx] ]
  index      = [idx]
  while idx >= 0 and ev.GenPart_status[idx] != 4:
    print idx
    decaychain.append(ev.GenPart_pdgId[idx])
    status.append(ev.GenPart_status[idx])
    index.append(idx)
    idx = ev.GenPart_genPartIdxMother[idx]

  #print(index)
  #print(status)
  #print(decaychain)
  if 25 in decaychain: 
    return 25
  if 23 in decaychain:
    return 23
  if 63 in status:
    print("Underlying event!!")
    return 63 # Emission from UE
  if 61 in status:
    return 61 # Emission from other in primary interaction (i.e. ISR)

def optimize_Sphericity(momLab, momBoost, dR=1.5):
  bestEta = -1
  bestPhi = -1
  bestS   = -1
  bestTr  = 0
  for etaCenter in np.linspace(-6,6,120):
    for phiCenter in np.linspace(-3.14,3.14,62):
      toTest = []
      for iS in range(len(momLab)):
        if deltaR2(momLab[iS].Eta(),momLab[iS].Phi(), etaCenter, phiCenter) < dR*dR:
          toTest.append(momBoost[iS])
      newTr = len(toTest)
      if newTr > bestTr:
        bestTr  = newTr
        bestEta = etaCenter
        bestPhi = phiCenter
        bestS   = sphericity(toTest)
  return bestS, bestEta, bestPhi    

def sphericity(moms):
  spher = np.zeros((3,3))
  norm = 0
  for SUEP4 in moms:
    px, py, pz = SUEP4.Px(), SUEP4.Py(), SUEP4.Pz()
    spher[0,0] += px*px
    spher[0,1] += px*py
    spher[0,2] += px*pz
    spher[1,0] += py*px
    spher[1,1] += py*py
    spher[1,2] += py*pz
    spher[2,0] += pz*px
    spher[2,1] += pz*py
    spher[2,2] += pz*pz
    norm += SUEP4.P()*SUEP4.P()
  try:
    spher = spher/norm
    eigs = np.sort(np.linalg.eigvalsh(spher))
    return 1.5*eigs[0]+1.5*eigs[1]
  except:
    return 0
def deltaR2(eta1, phi1, eta2, phi2):
  deta = abs(eta1-eta2)
  dphi = (phi1-phi2)
  if dphi > 3.141592: dphi -= 2*3.141592
  if dphi < -3.141582: dphi += 2*3.141592
  return (deta*deta + dphi*dphi)

def deltaphi(phi1, phi2):
  dphi = (phi1-phi2)
  if dphi > 3.141592: dphi -= 2*3.141592
  if dphi < -3.141582: dphi += 2*3.141592
  return dphi

nTotalEvs = 0
for tree in trees:
 if nTotalEvs >= 1000: continue
 for iev, ev in enumerate(tree):
  print(iev)
  if nTotalEvs >= 1000: continue
  nTotalEvs += 1
  c = ROOT.TCanvas("c","c",800,600)
  th2 = ROOT.TH2F("etaphihits","etaphihits", 50, -8, 8, 50, -3.14, 3.14)
  th2.GetXaxis().SetTitle("#eta")
  th2.GetYaxis().SetTitle("#phi")
  th2.SetTitle("Hit positions")
  meanEta = 0
  meanCosPhi = 0
  meanSinPhi = 0

  nSUEP   = 0
  Zpt     = 0
  Hpt     = 0
  lepEta  = []
  lepPhi  = []
  Hp4     = ROOT.TLorentzVector()
  boost   = ROOT.TVector3()
  norm = 0
  labs    = []
  boosted = []
  labsdec    = []
  boosteddec = []

  pfcands = []
  pfcandsp4 = []
  pfcandsp4lab = []
  pfcandsSUEP   = []
  pfcandsSUEPp4lab = []
  pfcandsSUEPp4boost = []

  pfcandsBACK   = []
  pfcandsBACKp4lab = []
  pfcandsBACKp4boost = []

  for igen, idx in enumerate(ev.GenPart_pdgId):
    if idx == 23 and ev.GenPart_status[igen] == 62:
      Zpt = ev.GenPart_pt[igen]
      Zeta = ev.GenPart_eta[igen]
      Zphi = ev.GenPart_phi[igen]
       
    if idx == 25 and ev.GenPart_status[igen] == 62:
      Hpt  = ev.GenPart_pt[igen]
      Heta = ev.GenPart_eta[igen]
      Hphi = ev.GenPart_phi[igen]
      Hp4.SetPtEtaPhiM(Hpt, Heta, Hphi, 125)
      boost = -Hp4.BoostVector()
    if (abs(idx) == 11 or abs(idx)==13 or abs(idx)==15) and ev.GenPart_status[igen] == 1 and ev.GenPart_pt[igen] >= 10:
      lepEta.append( ev.GenPart_eta[igen])
      lepPhi.append( ev.GenPart_phi[igen])


  for iPF, pt in enumerate(ev.PFCands_pt):
    if (ev.PFCands_fromPV[iPF] >= 2 and ev.PFCands_trkPt[iPF] >= 1 and abs(ev.PFCands_trkEta[iPF]) <= 2.5 and abs(ev.PFCands_dz[iPF])<10 and abs(ev.PFCands_dzErr[iPF]) < 0.05):
      #print("add pf")
      pfcands.append(ROOT.TMarker(ev.PFCands_eta[iPF], ev.PFCands_phi[iPF], ROOT.kCircle))
      #print(ev.PFCands_eta[iPF], ev.PFCands_phi[iPF])
      pfcands[-1].SetMarkerSize(1)
      ppff = ROOT.TLorentzVector()
      ppfflab =  ROOT.TLorentzVector()
      ppfflab.SetPtEtaPhiM( ev.PFCands_pt[iPF], ev.PFCands_eta[iPF], ev.PFCands_phi[iPF], ev.PFCands_mass[iPF])
      ppff.SetPtEtaPhiM( ev.PFCands_pt[iPF], ev.PFCands_eta[iPF], ev.PFCands_phi[iPF], ev.PFCands_mass[iPF])
      ppff.Boost(boost)
      pfcandsp4.append(ppff)
      pfcandsp4lab.append(ppfflab)

      matched    = -1
      parentCode = 0
      minDR2  = 0.4
      """for itrack, trackgen in enumerate(ev.SimTracks_igenPart):
        if deltaR2(ev.PFCands_eta[iPF], ev.PFCands_phi[iPF], ev.SimTracks_eta[itrack], ev.SimTracks_phi[itrack]) < minDR2:
          minDR2  = deltaR2(ev.PFCands_eta[iPF], ev.PFCands_phi[iPF], ev.SimTracks_eta[itrack], ev.SimTracks_phi[itrack])
          matched = trackgen
      if matched >= 0: parentCode = isFrom(ev, matched)"""

      for itrack, trackgen in enumerate(ev.GenPart_pdgId):
        if deltaR2(ev.PFCands_eta[iPF], ev.PFCands_phi[iPF], ev.GenPart_eta[itrack], ev.GenPart_phi[itrack]) < minDR2:
          minDR2  = deltaR2(ev.PFCands_eta[iPF], ev.PFCands_phi[iPF], ev.GenPart_eta[itrack], ev.GenPart_phi[itrack])
          matched = itrack
      if matched >= 0: parentCode = isFrom(ev, matched)

      if parentCode == 25: pfcands[-1].SetMarkerColor(ROOT.kGreen)
      elif parentCode == 23: pfcands[-1].SetMarkerColor(ROOT.kOrange)
      elif parentCode == 63: pfcands[-1].SetMarkerColor(ROOT.kRed)#ROOT.kBlue)
      elif parentCode == 61: pfcands[-1].SetMarkerColor(ROOT.kRed)#Black)
      elif matched < 0:      pfcands[-1].SetMarkerColor(ROOT.kRed)
      else: pfcands[-1].SetMarkerColor(ROOT.kRed)#Cyan)

      #print("track, matched %i, isFrom %i"%(matched,isFrom(ev, matched)))
      if not(parentCode == 25):
        #pfcandsBACK.append(ROOT.TMarker(ev.PFCands_eta[iPF], ev.PFCands_phi[iPF], ROOT.kCircle))
        #pfcandsBACK[-1].SetMarkerColor(ROOT.kRed)
        #pfcandsBACK[-1].SetMarkerSize(1)
        pfcandsBACKp4lab.append(ppfflab)
        pfcandsBACKp4boost.append(ppff)

      else:
        #pfcandsSUEP.append(ROOT.TMarker(ev.PFCands_eta[iPF], ev.PFCands_phi[iPF], ROOT.kCircle))
        #pfcandsSUEP[-1].SetMarkerColor(ROOT.kGreen)
        #pfcandsSUEP[-1].SetMarkerSize(1)
        pfcandsSUEPp4lab.append(ppfflab)
        pfcandsSUEPp4boost.append(ppff)


  for igen, idx in enumerate(ev.GenPart_pdgId):
    if idx == 999999 and ev.GenPart_status[igen] == 2:
        SUEP4 = ROOT.TLorentzVector()
        SUEP4.SetPtEtaPhiM( ev.GenPart_pt[igen], ev.GenPart_eta[igen], ev.GenPart_phi[igen], ev.GenPart_mass[igen] )
        SUEP4boosted = ROOT.TLorentzVector()
        SUEP4boosted.SetPtEtaPhiM( ev.GenPart_pt[igen], ev.GenPart_eta[igen], ev.GenPart_phi[igen], ev.GenPart_mass[igen]) 
        SUEP4boosted.Boost(boost)
        labs.append(SUEP4)
        boosted.append(SUEP4boosted)
        nSUEP += 1
    elif ev.GenPart_status[igen] == 1:
      if isChargedFromId(ev, igen, idx, 999998):
        SUEP4dec = ROOT.TLorentzVector()
        SUEP4dec.SetPtEtaPhiM( ev.GenPart_pt[igen], ev.GenPart_eta[igen], ev.GenPart_phi[igen], ev.GenPart_mass[igen] )
        SUEP4boosteddec = ROOT.TLorentzVector()
        SUEP4boosteddec.SetPtEtaPhiM( ev.GenPart_pt[igen], ev.GenPart_eta[igen], ev.GenPart_phi[igen], ev.GenPart_mass[igen])
        SUEP4boosteddec.Boost(boost)
        labsdec.append(SUEP4dec)
        boosteddec.append(SUEP4boosteddec)
        #th2.Fill(ev.GenPart_eta[igen], ev.GenPart_phi[igen])
      

  spher, meanEta, meanPhi = optimize_Sphericity(pfcandsp4lab, pfcandsp4, 1.5)
  #spher10, meanEta10, meanPhi10 = optimize_Sphericity(pfcandsp4, pfcandsp4, 1.0)
  #spher4, meanEta4, meanPhi4 = optimize_Sphericity(pfcandsp4, pfcandsp4, 0.4)
  labsphericity   = sphericity(labs)
  totalsphericity = sphericity(boosted)
  labdecsphericity   = sphericity(labsdec)
  totaldecsphericity = sphericity(boosteddec)

  tracksphericity = sphericity(pfcandsp4)
  trackSUEPsphericity = sphericity(pfcandsSUEPp4boost)
  trackBACKsphericity = sphericity(pfcandsBACKp4boost)
  tracksphericitylab = sphericity(pfcandsp4lab)
  trackSUEPsphericitylab = sphericity(pfcandsSUEPp4lab)
  trackBACKsphericitylab = sphericity(pfcandsBACKp4lab)


  h_tot.Fill(totalsphericity)
  h_totlab.Fill(labsphericity)
  h_dec.Fill(totaldecsphericity)
  h_declab.Fill(labdecsphericity)

  h_tracks.Fill(tracksphericity)
  h_trackslab.Fill(tracksphericitylab)

  h_BACKtracks.Fill(trackBACKsphericity)
  h_BACKtrackslab.Fill(trackBACKsphericitylab)
  h_SUEPtracks.Fill(trackSUEPsphericity)
  h_SUEPtrackslab.Fill(trackSUEPsphericitylab)

  ak15 = ROOT.TEllipse(meanEta, meanPhi, 1.5)
  ak15.SetFillColor(ROOT.kNone)
  ak15.SetFillStyle(0)
  ak15.SetLineColor(ROOT.kBlue)

  #ak10 = ROOT.TEllipse(meanEta10, meanPhi10, 1.0)
  #ak10.SetFillColor(ROOT.kNone)
  #ak10.SetFillStyle(0)
  #ak10.SetLineColor(ROOT.kBlue)

  #ak4 = ROOT.TEllipse(meanEta4, meanPhi4, 0.4)
  #ak4.SetFillColor(ROOT.kNone)
  #ak4.SetFillStyle(0)
  #ak4.SetLineColor(ROOT.kGreen)

  Ztext = ROOT.TLatex(3.0,2.2, "p_{T}^{Z} = %.1f GeV"%Zpt)
  Htext = ROOT.TLatex(3.0,2.8, "p_{T}^{H} = %.1f GeV"%Hpt)
  Stottext = ROOT.TLatex(3.0,1.6, "S_{#phi} = %.3f"%totalsphericity)
  Stottextlab = ROOT.TLatex(-8.0,1.6, "S_{#phi}^{Lab} = %.3f"%labsphericity)
  Stottextdec = ROOT.TLatex(3.0,1.0, "S_{A}  = %.3f"%totaldecsphericity)
  Stottextlabdec = ROOT.TLatex(-8.0,1.0, "S_{A}^{Lab} = %.3f"%labdecsphericity)


  Stracktext = ROOT.TLatex(3.0,0.4, "S_{Tracks} = %.3f"%tracksphericity)
  StrackSUEPtext = ROOT.TLatex(3.0,-0.2, "S_{Tracks}^{SUEP} = %.3f"%trackSUEPsphericity)
  StrackBACKtext = ROOT.TLatex(3.0,-0.8, "S_{Tracks}^{BACK} = %.3f"%trackBACKsphericity)
  StrackSUEPtext.SetTextColor(ROOT.kGreen)
  StrackBACKtext.SetTextColor(ROOT.kRed)

  Stracktextlab = ROOT.TLatex(-8.0,0.4, "S_{Tracks}^{Lab} = %.3f"%tracksphericitylab)
  StrackSUEPtextlab = ROOT.TLatex(-8.0,-0.2, "S_{Tracks}^{SUEP, Lab} = %.3f"%trackSUEPsphericitylab)
  StrackBACKtextlab = ROOT.TLatex(-8.0,-0.8, "S_{Tracks}^{BACK, Lab} = %.3f"%trackBACKsphericitylab)
  StrackSUEPtextlab.SetTextColor(ROOT.kGreen)
  StrackBACKtextlab.SetTextColor(ROOT.kRed)


  """Zmark = ROOT.TMarker(Zeta, Zphi, 5)
  Hmark = ROOT.TMarker(Heta, Hphi, 5)
  Ztext.SetTextColor(ROOT.kOrange)
  Zmark.SetMarkerColor(ROOT.kOrange)
  Htext.SetTextColor(ROOT.kBlue)
  Hmark.SetMarkerColor(ROOT.kBlue)
  Hmark.SetMarkerSize(3)
  Zmark.SetMarkerSize(3)"""

  Stext = ROOT.TLatex(-8.0,2.8, "AK_{15} Jet")
  Stextjet = ROOT.TLatex(-8.0,2.2, "S_{Jet} = %.3f"%spher)

  Stext.SetTextColor(ROOT.kBlue)
  Stextjet.SetTextColor(ROOT.kBlue)

  #Stext10 = ROOT.TLatex(-8.0,-0.1, "S_{AK10} = %.3f"%spher10)
  #Stext10.SetTextColor(ROOT.kBlue)

  #Stext4 = ROOT.TLatex(-8.0,-0.8, "S_{AK4} = %.3f"%spher4)
  #Stext4.SetTextColor(ROOT.kGreen)
  
  lepCircles = []
  for ilep in range(len(lepEta)):
    lepCircles.append(ROOT.TEllipse(lepEta[ilep], lepPhi[ilep], 0.4))
    lepCircles[-1].SetFillColor(ROOT.kNone)
    lepCircles[-1].SetLineColor(ROOT.kBlack)
    lepCircles[-1].SetFillStyle(0)
  lepCircles.append(ROOT.TEllipse(5.8, -2.45, 0.4))
  lepCircles[-1].SetFillColor(ROOT.kNone)
  lepCircles[-1].SetLineColor(ROOT.kBlack)
  lepCircles[-1].SetFillStyle(0)
  akEllipse = ROOT.TEllipse(-4.5,2.35, 0.4)
  akEllipse.SetFillColor(ROOT.kNone)
  akEllipse.SetLineColor(ROOT.kBlue)
  akEllipse.SetFillStyle(0)
  
  if len(lepEta) > 0:
    leptext = ROOT.TLatex(3.0,-2.6, "Lepton")

  th2.Draw("colz")
  ak15.Draw("same")
  #ak10.Draw("same")
  #ak4.Draw("same")
  Ztext.Draw("same")
  Htext.Draw("same")
  #Hmark.Draw("same")
  #Zmark.Draw("same")
  Stottext.Draw("same")
  Stottextlab.Draw("same")
  Stottextdec.Draw("same")
  Stottextlabdec.Draw("same")

  Stracktext.Draw("same")
  StrackSUEPtext.Draw("same")
  StrackBACKtext.Draw("same")
  Stracktextlab.Draw("same")
  StrackSUEPtextlab.Draw("same")
  StrackBACKtextlab.Draw("same")
  akEllipse.Draw("same")
  Stext.Draw("same")
  Stextjet.Draw("same")
  #Stext10.Draw("same")
  #Stext4.Draw("same")
  if len(lepEta)> 0:
    leptext.Draw("same")
    for ilepcirc in  lepCircles:
      ilepcirc.Draw("same")

  for pf in pfcands:
    pf.Draw("same")
  for pf in pfcandsBACK:
    pf.Draw("same")
  for pf in pfcandsSUEP:
    pf.Draw("same")
  
  tag = "%i_%i_%i"%(ev.run, ev.luminosityBlock, ev.event)
  c.SaveAs("/eos/user/c/cericeci/www/SUEP/etaphiplots_forRaymond/DY_evdec_%s%s.pdf"%(tag, "boosted" if boostToH else ""))
  c.SaveAs("/eos/user/c/cericeci/www/SUEP/etaphiplots_forRaymond/DY_evdec_%s%s.png"%(tag, "boosted" if boostToH else ""))
  #if iev > 10: break


  h_tot.Fill(totalsphericity)
  h_totlab.Fill(labsphericity)
  h_dec.Fill(totaldecsphericity)
  h_declab.Fill(labdecsphericity)

  h_tracks.Fill(tracksphericity)
  h_trackslab.Fill(tracksphericitylab)

  h_BACKtracks.Fill(trackBACKsphericity)
  h_BACKtrackslab.Fill(trackBACKsphericitylab)
  h_SUEPtracks.Fill(trackSUEPsphericity)
  h_SUEPtrackslab.Fill(trackSUEPsphericitylab)


c = ROOT.TCanvas("c","c",800,600)
c.SetLogY(True)
tl = ROOT.TLegend(0.2,0.6,0.9,0.9)
h_tot.GetXaxis().SetTitle("Sphericity")
h_tot.SetLineColor(1)
h_dec.SetLineColor(2)
h_tracks.SetLineColor(3)
h_SUEPtracks.SetLineColor(4)
h_BACKtracks.SetLineColor(5)

h_totlab.SetLineColor(1)
h_declab.SetLineColor(2)
h_trackslab.SetLineColor(3)
h_SUEPtrackslab.SetLineColor(4)
h_BACKtrackslab.SetLineColor(5)

h_totlab.SetLineStyle(3)
h_declab.SetLineStyle(3)
h_trackslab.SetLineStyle(3)
h_SUEPtrackslab.SetLineStyle(3)
h_BACKtrackslab.SetLineStyle(3)


tl.AddEntry(h_tot, "#Phi, S frame","l")
tl.AddEntry(h_dec, "A, S frame","l")
tl.AddEntry(h_tracks, "Tracks, S frame","l")
tl.AddEntry(h_SUEPtracks, "SUEP Tracks, S frame","l")
tl.AddEntry(h_BACKtracks, "Back Tracks, S frame","l")
tl.AddEntry(h_totlab, "#Phi, Lab frame","l")
tl.AddEntry(h_declab, "A, Lab frame","l")
tl.AddEntry(h_trackslab, "Tracks, Lab frame","l")
tl.AddEntry(h_SUEPtrackslab, "SUEP Tracks, Lab frame","l")
tl.AddEntry(h_BACKtrackslab, "Back Tracks, Lab frame","l")


h_tot.SetMaximum(2000)
h_tot.SetMinimum(0.5)
h_tot.Draw("hist")
h_dec.Draw("hist same")
h_tracks.Draw("hist same")
h_SUEPtracks.Draw("hist same")
h_BACKtracks.Draw("hist same")
h_totlab.Draw("hist same")
h_declab.Draw("hist same")
h_trackslab.Draw("hist same")
h_SUEPtrackslab.Draw("hist same")
h_BACKtrackslab.Draw("hist same")

tl.Draw("same")

c.SaveAs("/eos/user/c/cericeci/www/SUEP/etaphiplots_forRaymond/DY_summary_dec.pdf")
c.SaveAs("/eos/user/c/cericeci/www/SUEP/etaphiplots_forRaymond/DY_summary_dec.png")
