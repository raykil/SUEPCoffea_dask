"""
Plotter for boost properties. Boost are done in L, Z, T, C, S frames.
The objective is to reconstruct Higgs momentum.
Raymond Kil, 2022
"""

import pandas as pd
import ROOT
import os
import numpy as np

#ZH = [pd.HDFStore("../outputZHwithScale/"+f, 'r') for f in os.listdir("../outputZHwithScale/")]
ZH = [pd.HDFStore("../outputSimTracks/"+f, 'r') for f in os.listdir("../outputSimTracks/")]
#print(ZH[0]["onecluster"]["nOutBand0.5"])


Zboost_px = False
Zboost_py = False
Zboost_pz = False
Zboost_pt = False
outputZ = "/eos/user/j/jkil/www/Z-Frame_Property"

Tboost_px = False
Tboost_py = False
Tboost_pz = False
Tboost_pt = False
outputT = "/eos/user/j/jkil/www/T-Frame_Property"

Cboost_px = False
Cboost_py = False
Cboost_pz = False
Cboost_pt = False
outputC = "/eos/user/j/jkil/www/C-Frame_Property"

Sboost_px = False
Sboost_py = False
Sboost_pz = False
Sboost_pt = False
outputS = "/eos/user/j/jkil/www/S-Frame_Property"

scaledCboost_px = False
scaledCboost_py = False
scaledCboost_pz = False
scaledCboost_pt = False
outputScaledC = "/eos/user/j/jkil/www/scaledC-Frame_Property"

scaledSboost_px = False
scaledSboost_py = False
scaledSboost_pz = False
scaledSboost_pt = False
outputScaledS = "/eos/user/j/jkil/www/scaledS-Frame_Property"

genHpz_genHpt = False


###### Z BOOST ######
if Zboost_px:

    h_px = ROOT.TH2F("genHpx_vs_recZpx","genHpx vs recZpx",100,0,500,100,0,500)
    c_px = ROOT.TCanvas("c_px","", 800,600)

    for i in range(len(ZH)):
        Zpx = ZH[i]["onetrack"]["Z_px"]
        Hpx = ZH[i]["onetrack"]["genHpx"]
        for j in range(len(Zpx)):
            h_px.Fill(Zpx[j],Hpx[j])

    h_px.Draw()
    h_px.GetXaxis().SetTitle("px of recZ [GeV]")
    h_px.GetYaxis().SetTitle("px of genH [GeV]")
    c_px.SaveAs("%s/%s.pdf"%(outputZ,"genHpx_vs_recZpx"))
    c_px.SaveAs("%s/%s.png"%(outputZ,"genHpx_vs_recZpx"))

if Zboost_py:

    h_py = ROOT.TH2F("genHpy_vs_recZpy","genHpy vs recZpy",100,0,500,100,0,500)
    c_py = ROOT.TCanvas("c_py","", 800,600)

    for i in range(len(ZH)):
        Zpy = ZH[i]["onetrack"]["Z_py"]
        Hpy = ZH[i]["onetrack"]["genHpy"]
        for j in range(len(Zpy)):
            h_py.Fill(Zpy[j],Hpy[j])

    h_py.Draw()
    h_py.GetXaxis().SetTitle("py of recZ [GeV]")
    h_py.GetYaxis().SetTitle("py of genH [GeV]")
    c_py.SaveAs("%s/%s.pdf"%(outputZ,"genHpy_vs_recZpy"))
    c_py.SaveAs("%s/%s.png"%(outputZ,"genHpy_vs_recZpy"))

if Zboost_pz:

    h_pz = ROOT.TH2F("genHpz_vs_recZpz","genHpz vs recZpz",100,0,500,100,0,500)
    c_pz = ROOT.TCanvas("c_pz","", 800,600)

    for i in range(len(ZH)):
        Zpz = ZH[i]["onetrack"]["Z_pz"]
        Hpz = ZH[i]["onetrack"]["genHpz"]
        for j in range(len(Zpz)):
            h_pz.Fill(Zpz[j],Hpz[j])

    h_pz.Draw()
    h_pz.GetXaxis().SetTitle("pz of recZ [GeV]")
    h_pz.GetYaxis().SetTitle("pz of genH [GeV]")
    c_pz.SaveAs("%s/%s.pdf"%(outputZ,"genHpz_vs_recZpz"))
    c_pz.SaveAs("%s/%s.png"%(outputZ,"genHpz_vs_recZpz"))

if Zboost_pt:

    h_pt = ROOT.TH2F("genHpt_vs_recZpt","genHpt vs recZpt",100,0,500,100,0,500)
    c_pt = ROOT.TCanvas("c_pt","", 800,600)

    for i in range(len(ZH)):
        Zpt = ZH[i]["onetrack"]["Z_pt"]
        Hpt = ZH[i]["onetrack"]["genHpt"]
        for j in range(len(Zpt)):
            h_pt.Fill(Zpt[j],Hpt[j])
    
    #f = ROOT.TF1("f","[0]*x",0,500)
    #h_pt.Fit("f") # Draws the best fit curve to the plot.

    correlation = h_pt.GetCorrelationFactor()
    print(correlation,"correlation factor")

    h_pt.Draw()
    h_pt.GetXaxis().SetTitle("pt of recZ [GeV]")
    h_pt.GetYaxis().SetTitle("pt of genH [GeV]")
    c_pt.SaveAs("%s/%s.pdf"%(outputZ,"genHpt_vs_recZpt"))
    c_pt.SaveAs("%s/%s.png"%(outputZ,"genHpt_vs_recZpt"))


###### T BOOST ######
if Tboost_px:

    h_px = ROOT.TH2F("genHpx_vs_TboostPx","generated Hpx vs TboostPx",100,-300,300,100,-300,300)
    c_px = ROOT.TCanvas("c_px", "", 800,600)

    for i in range(len(ZH)):
        Tboost_px = ZH[i]["onecluster"]["boostT_px"]
        Hpx = ZH[i]["onecluster"]["genHpx"]
        for j in range(len(Tboost_px)):
            h_px.Fill(Tboost_px[j],Hpx[j])

    h_px.Draw()
    h_px.GetXaxis().SetTitle("px of Tboost [GeV]")
    h_px.GetYaxis().SetTitle("px of H [GeV]")
    c_px.SaveAs("%s/%s.pdf"%(outputT,"genHpx_vs_TboostPx"))
    c_px.SaveAs("%s/%s.png"%(outputT,"genHpx_vs_TboostPx"))

if Tboost_py:

    h_py = ROOT.TH2F("genHpy_vs_Tboostpy","generated Hpy vs Tboostpy",100,-300,300,100,-300,300)
    c_py = ROOT.TCanvas("c_py", "", 800,600)

    for i in range(len(ZH)):
        Tboost_py = ZH[i]["onecluster"]["boostT_py"]
        Hpy = ZH[i]["onecluster"]["genHpy"]
        for j in range(len(Tboost_py)):
            h_py.Fill(Tboost_py[j],Hpy[j])

    h_py.Draw()
    h_py.GetXaxis().SetTitle("py of Tboost [GeV]")
    h_py.GetYaxis().SetTitle("py of H [GeV]")
    c_py.SaveAs("%s/%s.pdf"%(outputT,"genHpy_vs_Tboostpy"))
    c_py.SaveAs("%s/%s.png"%(outputT,"genHpy_vs_Tboostpy"))

if Tboost_pz:

    h_pz = ROOT.TH2F("genHpz_vs_Tboostpz","generated Hpz vs Tboostpz",100,-300,300,-300,0,300)
    c_pz = ROOT.TCanvas("c_pz", "", 800,600)

    for i in range(len(ZH)):
        Tboost_pz = ZH[i]["onetrack"]["boostT_pz"]
        Hpz = ZH[i]["onetrack"]["genHpz"]
        for j in range(len(Tboost_pz)):
            h_pz.Fill(Tboost_pz[j],Hpz[j])

    correlation = h_pz.GetCorrelationFactor()
    print(correlation,"correlation factor")

    h_pz.Draw()
    h_pz.GetXaxis().SetTitle("pz of Tboost [GeV]")
    h_pz.GetYaxis().SetTitle("pz of H [GeV]")
    c_pz.SaveAs("%s/%s.pdf"%(outputT,"genHpz_vs_Tboostpz"))
    c_pz.SaveAs("%s/%s.png"%(outputT,"genHpz_vs_Tboostpz"))

if Tboost_pt:

    h_pt = ROOT.TH2F("genHpt_vs_Tboostpt","generated Hpt vs Tboostpt",100,-300,300,-300,0,300)
    c_pt = ROOT.TCanvas("c_pt", "", 800,600)

    for i in range(len(ZH)):
        Tboost_pt = ZH[i]["onetrack"]["boostT_pt"]
        Hpt = ZH[i]["onetrack"]["genHpt"]
        for j in range(len(Tboost_pt)):
            h_pt.Fill(Tboost_pt[j],Hpt[j])

    h_pt.Draw()
    h_pt.GetXaxis().SetTitle("pt of Tboost [GeV]")
    h_pt.GetYaxis().SetTitle("pt of H [GeV]")
    c_pt.SaveAs("%s/%s.pdf"%(outputT,"genHpt_vs_Tboostpt"))
    c_pt.SaveAs("%s/%s.png"%(outputT,"genHpt_vs_Tboostpt"))


###### C BOOST ######
if Cboost_px:

    h_px = ROOT.TH2F("genHpx_vs_CboostPx","generated Hpx vs CboostPx",100,-500,500,100,-500,500)
    c_px = ROOT.TCanvas("c_px", "", 800,600)

    for i in range(len(ZH)):
        Cboost_px = ZH[i]["onecluster"]["boostC_px"]
        Hpx = ZH[i]["onecluster"]["genHpx"]
        for j in range(len(Cboost_px)):
            h_px.Fill(Cboost_px[j],Hpx[j])

    correlation = h_px.GetCorrelationFactor()
    t = ROOT.TLatex()

    h_px.Draw("colz")
    t.SetTextAlign(10)
    t.DrawLatex(-450,-450,"r = {0:.4f}".format(correlation))
    h_px.GetXaxis().SetTitle("p_{x} of Cboost [GeV]")
    h_px.GetYaxis().SetTitle("p_{x} of genH [GeV]")
    c_px.SaveAs("%s/%s.pdf"%(outputC,"genHpx_vs_CboostPx"))
    c_px.SaveAs("%s/%s.png"%(outputC,"genHpx_vs_CboostPx"))

if Cboost_py:

    h_py = ROOT.TH2F("genHpy_vs_Cboostpy","generated Hpy vs Cboostpy",100,-500,500,100,-500,500)
    c_py = ROOT.TCanvas("c_py", "", 800,600)

    for i in range(len(ZH)):
        Cboost_py = ZH[i]["onecluster"]["boostC_py"]
        Hpy = ZH[i]["onecluster"]["genHpy"]
        for j in range(len(Cboost_py)):
            h_py.Fill(Cboost_py[j],Hpy[j])

    correlation = h_py.GetCorrelationFactor()
    t = ROOT.TLatex()

    h_py.Draw("colz")
    t.SetTextAlign(10)
    t.DrawLatex(-450,-450,"r = {0:.4f}".format(correlation))
    h_py.GetXaxis().SetTitle("p_{y} of Cboost [GeV]")
    h_py.GetYaxis().SetTitle("p_{y} of genH [GeV]")
    c_py.SaveAs("%s/%s.pdf"%(outputC,"genHpy_vs_Cboostpy"))
    c_py.SaveAs("%s/%s.png"%(outputC,"genHpy_vs_Cboostpy"))

if Cboost_pz:

    h_pz = ROOT.TH2F("genHpz_vs_CboostPz", "generated Hpz vs CboostPz",100,-500,500,100,-500,500)
    c_pz = ROOT.TCanvas("c_pz", "", 800,600)

    for i in range(len(ZH)):
        Cboost_pz = ZH[i]["onecluster"]["boostC_pz"]
        Hpz = ZH[i]["onecluster"]["genHpz"]
        for j in range(len(Cboost_pz)):
            h_pz.Fill(Cboost_pz[j],Hpz[j])

    correlation = h_pz.GetCorrelationFactor()
    t1 = ROOT.TLatex()

    h_pz.Fit("pol1")
    h_pz.Draw("colz")
    t1.DrawLatex(-450,400,"r = {0:.4f}".format(correlation))
    h_pz.GetXaxis().SetTitle("p_{z} of Cboost [GeV]")
    h_pz.GetYaxis().SetTitle("p_{z} of genH [GeV]")
    c_pz.SaveAs("%s/%s.pdf"%(outputC,"genHpz_vs_CboostPz"))
    c_pz.SaveAs("%s/%s.png"%(outputC,"genHpz_vs_CboostPz"))
    
if Cboost_pt:

    h_pt = ROOT.TH2F("genHpt_vs_Cboostpt","generated Hpt vs Cboostpt",100,0,500,100,0,500)
    c_pt = ROOT.TCanvas("c_pt", "", 800,600)

    for i in range(len(ZH)):
        Cboost_pt = ZH[i]["onecluster"]["boostC_pt"]
        Hpt = ZH[i]["onecluster"]["genHpt"]
        for j in range(len(Cboost_pt)):
            h_pt.Fill(Cboost_pt[j],Hpt[j])

    correlation = h_pt.GetCorrelationFactor()
    t = ROOT.TLatex()

    h_pt.Fit("pol1")
    h_pt.Draw("colz")
    t.SetTextAlign(10)
    t.DrawLatex(50,450,"r = {0:.4f}".format(correlation))
    h_pt.GetXaxis().SetTitle("p_{T} of Cboost [GeV]")
    h_pt.GetYaxis().SetTitle("p_{T} of genH [GeV]")
    c_pt.SaveAs("%s/%s.pdf"%(outputC,"genHpt_vs_Cboostpt"))
    c_pt.SaveAs("%s/%s.png"%(outputC,"genHpt_vs_Cboostpt"))


###### S BOOST ######
if Sboost_px:

    h_px = ROOT.TH2F("genHpx_vs_SboostPx","generated Hpx vs SboostPx",100,-500,500,100,-500,500)
    c_px = ROOT.TCanvas("c_px", "", 800,600)

    for i in range(len(ZH)):
        Sboost_px = ZH[i]["onecluster"]["boostS_px"]
        Hpx = ZH[i]["onecluster"]["genHpx"]
        for j in range(len(Sboost_px)):
            h_px.Fill(Sboost_px[j],Hpx[j])

    correlation = h_px.GetCorrelationFactor()
    t = ROOT.TLatex()

    h_px.Draw("colz")
    t.SetTextAlign(10)
    t.DrawLatex(-450,-450,"r = {0:.4f}".format(correlation))
    h_px.GetXaxis().SetTitle("p_{x} of Sboost [GeV]")
    h_px.GetYaxis().SetTitle("p_{x} of H [GeV]")
    c_px.SaveAs("%s/%s.pdf"%(outputS,"genHpx_vs_SboostPx"))
    c_px.SaveAs("%s/%s.png"%(outputS,"genHpx_vs_SboostPx"))

if Sboost_py:

    h_py = ROOT.TH2F("genHpy_vs_SboostPy","generated Hpy vs SboostPy",100,-500,500,100,-500,500)
    c_py = ROOT.TCanvas("c_py", "", 800,600)

    for i in range(len(ZH)):
        Sboost_py = ZH[i]["onecluster"]["boostS_py"]
        Hpy = ZH[i]["onecluster"]["genHpy"]
        for j in range(len(Sboost_py)):
            h_py.Fill(Sboost_py[j],Hpy[j])

    correlation = h_py.GetCorrelationFactor()
    t = ROOT.TLatex()

    h_py.Draw("colz")
    t.SetTextAlign(10)
    t.DrawLatex(-450,-450,"r = {0:.4f}".format(correlation))
    h_py.GetXaxis().SetTitle("p_{y} of Sboost [GeV]")
    h_py.GetYaxis().SetTitle("p_{y} of H [GeV]")
    c_py.SaveAs("%s/%s.pdf"%(outputS,"genHpy_vs_SboostPy"))
    c_py.SaveAs("%s/%s.png"%(outputS,"genHpy_vs_SboostPy"))

if Sboost_pz:

    h_pz = ROOT.TH2F("genHpz_vs_SboostPz","generated Hpz vs SboostPz",100,-500,500,100,-500,500)
    c_pz = ROOT.TCanvas("c_pz", "", 800,600)

    for i in range(len(ZH)):
        Sboost_pz = ZH[i]["onecluster"]["boostS_pz"]
        Hpz = ZH[i]["onecluster"]["genHpz"]
        for j in range(len(Sboost_pz)):
            h_pz.Fill(Sboost_pz[j],Hpz[j])

    correlation = h_pz.GetCorrelationFactor()
    t = ROOT.TLatex()

    h_pz.Fit("pol1")
    h_pz.Draw("colz")
    t.DrawLatex(-450,400,"r = {0:.4f}".format(correlation))
    h_pz.GetXaxis().SetTitle("p_{z} of Sboost [GeV]")
    h_pz.GetYaxis().SetTitle("p_{z} of H [GeV]")
    c_pz.SaveAs("%s/%s.pdf"%(outputS,"genHpz_vs_SboostPz"))
    c_pz.SaveAs("%s/%s.png"%(outputS,"genHpz_vs_SboostPz"))

if Sboost_pt:

    h_pt = ROOT.TH2F("genHpt_vs_SboostPt","generated Hpt vs SboostPt",100,0,500,100,0,500)
    c_pt = ROOT.TCanvas("c_pt", "", 800,600)

    for i in range(len(ZH)):
        Sboost_pt = ZH[i]["onecluster"]["boostS_pt"]
        Hpt = ZH[i]["onecluster"]["genHpt"]
        for j in range(len(Sboost_pt)):
            h_pt.Fill(Sboost_pt[j],Hpt[j])

    correlation = h_pt.GetCorrelationFactor()
    t = ROOT.TLatex()

    h_pt.Fit("pol1")
    h_pt.Draw("colz")
    t.DrawLatex(50,430,"r = {0:.4f}".format(correlation))
    h_pt.GetXaxis().SetTitle("p_{T} of Sboost [GeV]")
    h_pt.GetYaxis().SetTitle("p_{T} of genH [GeV]")
    c_pt.SaveAs("%s/%s.pdf"%(outputS,"genHpt_vs_SboostPt"))
    c_pt.SaveAs("%s/%s.png"%(outputS,"genHpt_vs_SboostPt"))


###### Scaled C BOOST ######
if scaledCboost_px:

    h_px = ROOT.TH2F("genHpx_vs_scaledCboostPx","generated Hpx vs scaledCboostPx",100,-500,500,100,-500,500)
    c_px = ROOT.TCanvas("c_px", "", 800,600)

    for i in range(len(ZH)):
        Cboost_px = ZH[i]["onecluster"]["scaledBoostC_px"]
        Hpx = ZH[i]["onecluster"]["genHpx"]
        for j in range(len(Cboost_px)):
            h_px.Fill(Cboost_px[j],Hpx[j])

    correlation = h_px.GetCorrelationFactor()
    t = ROOT.TLatex()

    h_px.Draw("colz")
    t.SetTextAlign(10)
    t.DrawLatex(-450,-450,"r = {0:.4f}".format(correlation))
    h_px.GetXaxis().SetTitle("p_{x} of scaledCboost [GeV]")
    h_px.GetYaxis().SetTitle("p_{x} of genH [GeV]")
    c_px.SaveAs("%s/%s.pdf"%(outputScaledC,"genHpx_vs_scaledCboostPx"))
    c_px.SaveAs("%s/%s.png"%(outputScaledC,"genHpx_vs_scaledCboostPx"))

if scaledCboost_py:

    h_py = ROOT.TH2F("genHpy_vs_scaledCboostpy","generated Hpy vs scaledCboostpy",100,-500,500,100,-500,500)
    c_py = ROOT.TCanvas("c_py", "", 800,600)

    for i in range(len(ZH)):
        Cboost_py = ZH[i]["onecluster"]["scaledBoostC_py"]
        Hpy = ZH[i]["onecluster"]["genHpy"]
        for j in range(len(Cboost_py)):
            h_py.Fill(Cboost_py[j],Hpy[j])

    correlation = h_py.GetCorrelationFactor()
    t = ROOT.TLatex()

    h_py.Draw("colz")
    t.SetTextAlign(10)
    t.DrawLatex(-450,-450,"r = {0:.4f}".format(correlation))
    h_py.GetXaxis().SetTitle("p_{y} of scaledCboost [GeV]")
    h_py.GetYaxis().SetTitle("p_{y} of genH [GeV]")
    c_py.SaveAs("%s/%s.pdf"%(outputScaledC,"genHpy_vs_scaledCboostpy"))
    c_py.SaveAs("%s/%s.png"%(outputScaledC,"genHpy_vs_scaledCboostpy"))

if scaledCboost_pz:

    sFactor = 1
    h_pz = ROOT.TH2F("genHpz_vs_scaledCboostPz", "generated Hpz vs scaledCboostPz",100,-500,500,100,-500,500)
    c_pz = ROOT.TCanvas("c_pz", "", 800,600)

    for i in range(len(ZH)):
        Cboost_pz = ZH[i]["onecluster"]["scaledBoostC_pz"]
        Hpz = ZH[i]["onecluster"]["genHpz"]
        for j in range(len(Cboost_pz)):
            #h_pz.Fill(Cboost_pz[j],Hpz[j])
            h_pz.Fill((sFactor)*Cboost_pz[j],Hpz[j])

    correlation = h_pz.GetCorrelationFactor()
    t1 = ROOT.TLatex()

    h_pz.Fit("pol1")
    h_pz.Draw("colz")
    t1.DrawLatex(-450,400,"r = {0:.4f}".format(correlation))
    h_pz.GetXaxis().SetTitle("p_{z} of scaledCboost [GeV]")
    h_pz.GetYaxis().SetTitle("p_{z} of genH [GeV]")
    c_pz.SaveAs("%s/%s.pdf"%(outputScaledC,"genHpz_vs_scaledCboostPz"))
    c_pz.SaveAs("%s/%s.png"%(outputScaledC,"genHpz_vs_scaledCboostPz"))
    
if scaledCboost_pt:

    sFactor = 1
    h_pt = ROOT.TH2F("genHpt_vs_scaledCboostpt","generated Hpt vs scaledCboostpt",100,0,500,100,0,500)
    c_pt = ROOT.TCanvas("c_pt", "", 800,600)

    for i in range(len(ZH)):
        Cboost_pt = ZH[i]["onecluster"]["scaledBoostC_pt"]
        Hpt = ZH[i]["onecluster"]["genHpt"]
        for j in range(len(Cboost_pt)):
            h_pt.Fill((sFactor)*Cboost_pt[j],Hpt[j])

    correlation = h_pt.GetCorrelationFactor()
    t = ROOT.TLatex()

    h_pt.Fit("pol1")
    h_pt.Draw("colz")
    t.SetTextAlign(10)
    t.DrawLatex(50,450,"r = {0:.4f}".format(correlation))
    h_pt.GetXaxis().SetTitle("p_{T} of Cboost [GeV]")
    h_pt.GetYaxis().SetTitle("p_{T} of genH [GeV]")
    c_pt.SaveAs("%s/%s.pdf"%(outputScaledC,"genHpt_vs_scaledCboostpt"))
    c_pt.SaveAs("%s/%s.png"%(outputScaledC,"genHpt_vs_scaledCboostpt"))


###### Scaled S BOOST ######
if scaledSboost_px:

    h_px = ROOT.TH2F("genHpx_vs_scaledSboostPx","generated Hpx vs scaledSboostPx",100,-500,500,100,-500,500)
    c_px = ROOT.TCanvas("c_px", "", 800,600)

    for i in range(len(ZH)):
        Sboost_px = ZH[i]["onecluster"]["scaledBoostS_px"]
        Hpx = ZH[i]["onecluster"]["genHpx"]
        for j in range(len(Sboost_px)):
            h_px.Fill(Sboost_px[j],Hpx[j])

    correlation = h_px.GetCorrelationFactor()
    t = ROOT.TLatex()

    h_px.Draw("colz")
    t.SetTextAlign(10)
    t.DrawLatex(-450,-450,"r = {0:.4f}".format(correlation))
    h_px.GetXaxis().SetTitle("p_{x} of scaledSboost [GeV]")
    h_px.GetYaxis().SetTitle("p_{x} of H [GeV]")
    c_px.SaveAs("%s/%s.pdf"%(outputScaledS,"genHpx_vs_scaledSboostPx"))
    c_px.SaveAs("%s/%s.png"%(outputScaledS,"genHpx_vs_scaledSboostPx"))

if scaledSboost_py:

    h_py = ROOT.TH2F("genHpy_vs_scaledSboostPy","generated Hpy vs scaledSboostPy",100,-500,500,100,-500,500)
    c_py = ROOT.TCanvas("c_py", "", 800,600)

    for i in range(len(ZH)):
        Sboost_py = ZH[i]["onecluster"]["scaledBoostS_py"]
        Hpy = ZH[i]["onecluster"]["genHpy"]
        for j in range(len(Sboost_py)):
            h_py.Fill(Sboost_py[j],Hpy[j])

    correlation = h_py.GetCorrelationFactor()
    t = ROOT.TLatex()

    h_py.Draw("colz")
    t.SetTextAlign(10)
    t.DrawLatex(-450,-450,"r = {0:.4f}".format(correlation))
    h_py.GetXaxis().SetTitle("p_{y} of scaledSboost [GeV]")
    h_py.GetYaxis().SetTitle("p_{y} of H [GeV]")
    c_py.SaveAs("%s/%s.pdf"%(outputScaledS,"genHpy_vs_scaledSboostPy"))
    c_py.SaveAs("%s/%s.png"%(outputScaledS,"genHpy_vs_scaledSboostPy"))

if scaledSboost_pz:

    h_pz = ROOT.TH2F("genHpz_vs_scaledSboostPz","generated Hpz vs scaledSboostPz",100,-500,500,100,-500,500)
    c_pz = ROOT.TCanvas("c_pz", "", 800,600)

    for i in range(len(ZH)):
        Sboost_pz = ZH[i]["onecluster"]["scaledBoostS_pz"]
        Hpz = ZH[i]["onecluster"]["genHpz"]
        for j in range(len(Sboost_pz)):
            h_pz.Fill(Sboost_pz[j],Hpz[j])

    correlation = h_pz.GetCorrelationFactor()
    t = ROOT.TLatex()

    h_pz.Fit("pol1")
    h_pz.Draw("colz")
    t.DrawLatex(-450,400,"r = {0:.4f}".format(correlation))
    h_pz.GetXaxis().SetTitle("p_{z} of scaledSboost [GeV]")
    h_pz.GetYaxis().SetTitle("p_{z} of H [GeV]")
    c_pz.SaveAs("%s/%s.pdf"%(outputScaledS,"genHpz_vs_scaledSboostPz"))
    c_pz.SaveAs("%s/%s.png"%(outputScaledS,"genHpz_vs_scaledSboostPz"))

if scaledSboost_pt:

    h_pt = ROOT.TH2F("genHpt_vs_scaledSboostPt","generated Hpt vs scaledSboostPt",100,0,500,100,0,500)
    c_pt = ROOT.TCanvas("c_pt", "", 800,600)

    for i in range(len(ZH)):
        Sboost_pt = ZH[i]["onecluster"]["scaledBoostS_pt"]
        Hpt = ZH[i]["onecluster"]["genHpt"]
        for j in range(len(Sboost_pt)):
            h_pt.Fill(Sboost_pt[j],Hpt[j])

    correlation = h_pt.GetCorrelationFactor()
    t = ROOT.TLatex()

    h_pt.Fit("pol1")
    h_pt.Draw("colz")
    t.DrawLatex(50,430,"r = {0:.4f}".format(correlation))
    h_pt.GetXaxis().SetTitle("p_{T} of scaledSboost [GeV]")
    h_pt.GetYaxis().SetTitle("p_{T} of genH [GeV]")
    c_pt.SaveAs("%s/%s.pdf"%(outputScaledS,"genHpt_vs_scaledSboostPt"))
    c_pt.SaveAs("%s/%s.png"%(outputScaledS,"genHpt_vs_scaledSboostPt"))