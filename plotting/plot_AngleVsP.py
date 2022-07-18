"""
    Plotting (max difference of) eta against z momentum of Higgs, 
    and (max difference of) phi against transverse momentum of Higgs.
    Objective is to determine the optimal strip size for an event.
    Raymond Kil, 2022
"""

#from this import d
from tkinter import Y
import pandas as pd
import ROOT
import os
import numpy as np

output = "/eos/user/j/jkil/www/S-Frame_Property"
ZH = [pd.HDFStore("../outputSimTracks/"+f, 'r') for f in os.listdir("../outputSimTracks/")]

# Command for accessing the hdf5 files
# print(ZH[0]["onetrack"]["genHpz"], "genHpz")
# print(ZH[0]["onetrack"]["ntracks"], "ntracks")

EtaPz = True
EtaPt = False
PhiPz = False
PhiPt = False

genHpzgenHpt = False

if EtaPz:
    #delta Eta vs pz
    h = ROOT.TH2F("deltaEta_vs_Hpz","#Delta#eta vs p_{z} of H",30,0,1500,100,0,4)
    c = ROOT.TCanvas("c", "", 800,600)
    
    for i in range(len(ZH)):
        deltaEta = ZH[i]["onetrack"]["boostS_deltaEta"]
        Hpz = ZH[i]["onetrack"]["genHpz"]
        for j in range(len(deltaEta)):
            h.Fill(Hpz[j],deltaEta[j])

    h.Fit("pol1")

    h.Draw("colz")
    h.Draw("CANDLE SAME")
    h.GetXaxis().SetTitle("p_{z} of genH [GeV]")
    h.GetYaxis().SetTitle("#Delta#eta")
    h.SetMarkerStyle(7)
    c.SaveAs("%s/%s.pdf"%(output,"deltaEta_vs_Hpz"))
    c.SaveAs("%s/%s.png"%(output,"deltaEta_vs_Hpz"))

if EtaPt:
    #delta Eta vs pt
    h = ROOT.TH2F("deltaEta_vs_Hptt","#Delta#eta vs p_{t} of H",30,0,1500,100,0,4)
    c = ROOT.TCanvas("c", "", 800,600)
    
    for i in range(len(ZH)):
        deltaEta = ZH[i]["onetrack"]["boostS_deltaEta"]
        Hpt = ZH[i]["onetrack"]["genHpt"]
        for j in range(len(deltaEta)):
            h.Fill(Hpt[j],deltaEta[j])

    h.Draw("colz")
    h.Draw("CANDLE SAME")
    h.GetXaxis().SetTitle("p_{t} of genH [GeV]")
    h.GetYaxis().SetTitle("#Delta#eta")
    h.SetMarkerStyle(7)
    c.SaveAs("%s/%s.pdf"%(output,"deltaEta_vs_Hpt"))
    c.SaveAs("%s/%s.png"%(output,"deltaEta_vs_Hpt"))

if PhiPz:
    #delta Phi vs pz
    h = ROOT.TH2F("deltaPhi_vs_Hpz","#Delta#phi vs p_{z} of H",30,0,1500,100,0,4)
    c = ROOT.TCanvas("c", "", 800,600)
    
    for i in range(len(ZH)):
        deltaPhi = ZH[i]["onetrack"]["boostS_deltaPhi"]
        Hpz = ZH[i]["onetrack"]["genHpz"]
        for j in range(len(deltaPhi)):
            h.Fill(Hpz[j],deltaPhi[j])

    h.Draw("colz")
    h.Draw("CANDLE SAME")
    h.GetXaxis().SetTitle("p_{z} of genH [GeV]")
    h.GetYaxis().SetTitle("#Delta#phi")
    h.SetMarkerStyle(7)
    c.SaveAs("%s/%s.pdf"%(output,"deltaPhi_vs_Hpz"))
    c.SaveAs("%s/%s.png"%(output,"deltaPhi_vs_Hpz"))

if PhiPt:
    #delta Phi vs pt
    h = ROOT.TH2F("deltaPhi_vs_Hpt","#Delta#phi vs p_{t} of H",30,0,1500,100,0,4)
    c = ROOT.TCanvas("c", "", 800,600)
    
    for i in range(len(ZH)):
        deltaPhi = ZH[i]["onetrack"]["boostS_deltaPhi"]
        Hpt = ZH[i]["onetrack"]["genHpt"]
        for j in range(len(deltaPhi)):
            h.Fill(Hpt[j],deltaPhi[j])

    h.Draw("colz")
    h.Draw("CANDLE SAME")
    h.GetXaxis().SetTitle("p_{t} of genH [GeV]")
    h.GetYaxis().SetTitle("#Delta#phi")
    h.SetMarkerStyle(7)
    c.SaveAs("%s/%s.pdf"%(output,"deltaPhi_vs_Hpt"))
    c.SaveAs("%s/%s.png"%(output,"deltaPhi_vs_Hpt"))


if genHpzgenHpt:
    #pz vs pt of Higgs. Purpose is to see if high pt implies low pz
    h = ROOT.TH2F("genHpz_vs_genHpt","p_{z} vs p_{t} of H",100,0,600,100,-300,300)
    c = ROOT.TCanvas("c", "", 800,600)
    
    for i in range(len(ZH)):
        x = ZH[i]["onetrack"]["genHpt"]
        y = ZH[i]["onetrack"]["genHpz"]
        for j in range(len(y)):
            h.Fill(x[j],y[j])

    #h.Draw("colz")
    #h.Draw("CANDLE SAME")
    h.Draw()
    h.GetXaxis().SetTitle("p_{t} of genH [GeV]")
    h.GetYaxis().SetTitle("p_{z} of genH [GeV]")
    h.SetMarkerStyle(7)
    c.SaveAs("%s/%s.pdf"%(output,"genHpz_vs_genHpt"))
    c.SaveAs("%s/%s.png"%(output,"genHpz_vs_genHpt"))