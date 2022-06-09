"""
Plotter for boost properties. Boost are done in L, Z, T, C frames.
The objective is to reconstruct Higgs momentum.
Raymond Kil, 2022
"""

import pandas as pd
import ROOT
import os
import numpy as np

ZH = [pd.HDFStore("../outputZH/"+f, 'r') for f in os.listdir("../outputZH/")]

Zboost_px = True
Zboost_py = True
Zboost_pz = True
Zboost_pt = True
outputZ = "/eos/user/j/jkil/www/Z-Frame_Property"

Tboost_px = True
Tboost_py = True
Tboost_pz = True
Tboost_pt = True
outputT = "/eos/user/j/jkil/www/T-Frame_Property"

Cboost_px = True
Cboost_py = True
Cboost_pz = True
Cboost_pt = True
outputC = "/eos/user/j/jkil/www/C-Frame_Property"


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

    h_px = ROOT.TH2F("genHpx_vs_TboostPx","generated Hpx vs TboostPx",100,-300,300,-300,0,300)
    c_px = ROOT.TCanvas("c_px", "", 800,600)

    for i in range(len(ZH)):
        Tboost_px = ZH[i]["onetrack"]["boostT_px"]
        Hpx = ZH[i]["onetrack"]["genHpx"]
        for j in range(len(Tboost_px)):
            h_px.Fill(Tboost_px[j],Hpx[j])

    h_px.Draw()
    h_px.GetXaxis().SetTitle("px of Tboost [GeV]")
    h_px.GetYaxis().SetTitle("px of H [GeV]")
    c_px.SaveAs("%s/%s.pdf"%(outputT,"genHpx_vs_TboostPx"))
    c_px.SaveAs("%s/%s.png"%(outputT,"genHpx_vs_TboostPx"))

if Tboost_py:

    h_py = ROOT.TH2F("genHpy_vs_Tboostpy","generated Hpy vs Tboostpy",100,-300,300,-300,0,300)
    c_py = ROOT.TCanvas("c_py", "", 800,600)

    for i in range(len(ZH)):
        Tboost_py = ZH[i]["onetrack"]["boostT_py"]
        Hpy = ZH[i]["onetrack"]["genHpy"]
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

    h_px = ROOT.TH2F("genHpx_vs_CboostPx","generated Hpx vs CboostPx",100,-300,300,100,-300,300)
    c_px = ROOT.TCanvas("c_px", "", 800,600)

    for i in range(len(ZH)):
        Cboost_px = ZH[i]["onecluster"]["boostC_px"]
        Hpx = ZH[i]["onecluster"]["genHpx"]
        for j in range(len(Cboost_px)):
            h_px.Fill(Cboost_px[j],Hpx[j])

    h_px.Draw()
    h_px.GetXaxis().SetTitle("px of Cboost [GeV]")
    h_px.GetYaxis().SetTitle("px of genH [GeV]")
    c_px.SaveAs("%s/%s.pdf"%(outputC,"genHpx_vs_CboostPx"))
    c_px.SaveAs("%s/%s.png"%(outputC,"genHpx_vs_CboostPx"))

if Cboost_py:

    h_py = ROOT.TH2F("genHpy_vs_Cboostpy","generated Hpy vs Cboostpy",100,-300,300,100,-300,300)
    c_py = ROOT.TCanvas("c_py", "", 800,600)

    for i in range(len(ZH)):
        Cboost_py = ZH[i]["onecluster"]["boostC_py"]
        Hpy = ZH[i]["onecluster"]["genHpy"]
        for j in range(len(Cboost_py)):
            h_py.Fill(Cboost_py[j],Hpy[j])

    h_py.Draw()
    h_py.GetXaxis().SetTitle("py of Cboost [GeV]")
    h_py.GetYaxis().SetTitle("py of genH [GeV]")
    c_py.SaveAs("%s/%s.pdf"%(outputC,"genHpy_vs_Cboostpy"))
    c_py.SaveAs("%s/%s.png"%(outputC,"genHpy_vs_Cboostpy"))

if Cboost_pz:

    h_pz = ROOT.TH2F("genHpz_vs_Cboostpz","generated Hpz vs Cboostpz (scaleFactor = 2.23)",100,-300,300,100,-300,300)
    c_pz = ROOT.TCanvas("c_pz", "", 800,600)

    for i in range(len(ZH)):
        Cboost_pz = ZH[i]["onecluster"]["boostC_pz"]
        Hpz = ZH[i]["onecluster"]["genHpz"]
        for j in range(len(Cboost_pz)):
            h_pz.Fill(2.23*Cboost_pz[j],Hpz[j]) # Scaling by 2.23 gives greatest correlation factor

    correlation = h_pz.GetCorrelationFactor()
    print(correlation,"correlation factor")

    h_pz.Draw()
    h_pz.GetXaxis().SetTitle("pz of Cboost [GeV]")
    h_pz.GetYaxis().SetTitle("pz of genH [GeV]")
    c_pz.SaveAs("%s/%s.pdf"%(outputC,"genHpz_vs_Cboostpz (scaleFactor = 2.23)"))
    c_pz.SaveAs("%s/%s.png"%(outputC,"genHpz_vs_Cboostpz (scaleFactor = 2.23)"))
    
if Cboost_pt:

    h_pt = ROOT.TH2F("genHpt_vs_Cboostpt","generated Hpt vs Cboostpt",100,-300,300,100,-300,300)
    c_pt = ROOT.TCanvas("c_pt", "", 800,600)

    for i in range(len(ZH)):
        Cboost_pt = ZH[i]["onecluster"]["boostC_pt"]
        Hpt = ZH[i]["onecluster"]["genHpt"]
        for j in range(len(Cboost_pt)):
            h_pt.Fill(Cboost_pt[j],Hpt[j])

    h_pt.Draw()
    h_pt.GetXaxis().SetTitle("pt of Cboost [GeV]")
    h_pt.GetYaxis().SetTitle("pt of genH [GeV]")
    c_pt.SaveAs("%s/%s.pdf"%(outputC,"genHpt_vs_Cboostpt"))
    c_pt.SaveAs("%s/%s.png"%(outputC,"genHpt_vs_Cboostpt"))