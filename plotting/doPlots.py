import pandas as pd
import ROOT
import os
import numpy as np

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(False)

DY = [pd.HDFStore("../outputDYwithScale/"+f, 'r') for f in os.listdir("../outputDYwithScale/")]
ZH = [pd.HDFStore("../outputZHwithScale/"+f, 'r') for f in os.listdir("../outputZHwithScale/")]

channel   = "onecluster"
normalize = True

# format for plots entry: "{plot title}": "["{var name in .hdf5 file}",{# of bins},{xmin},{xmax},"{xlabel}"]"

leptonProperty    = False
jetProperty       = False
trackMultiplicity = False
sphericityEvals   = False
scalarSphericityT = False
scalarSphericityC = False
scalarSphericityS = False
scaledScalarSpherC = False
scaledScalarSpherS = True

if leptonProperty:
  output = "/eos/user/j/jkil/www/"
  plots = {
    "Leading Lepton p_{T}": ["leadlep_pt", 50, 0, 200, "p_{T}^{l1} [GeV]"], 
    "Leading Lepton eta":["leadlep_eta", 50, -2.5, 2.5, "eta"],
    "Leading Lepton phi":["leadlep_phi",50,0,6.28,"phi"],
    "Leading Lepton mass":["leadlep_mass",50,0,0.01,"mass"],
    "SubLead Lepton p_{T}": ["subleadlep_pt", 50, 0, 200, "p_{T}^{l2} [GeV]"],
    "SubLead Lepton eta":["subleadlep_eta", 50, -2.5, 2.5, "eta"],
    "SubLead Lepton phi":["subleadlep_phi",50,0,6.28,"phi"],
    "Zpt":["Z_pt",50,0,200,"p_{t_{Z}} [GeV]"],
    "Zeta":["Z_eta",50,-2.5,2.5,"\eta_{Z}"],
    "Zphi":["Z_phi",50,-np.pi,np.pi,"\phi_{Z}"],
    "Zm":["Z_m",50,0,150,"m_{Z} [GeV]"]
  }

if jetProperty:
  output = "/eos/user/j/jkil/www/"
  plots = {
    "onejet p_{T}":["onejet_pt",50,0,150,"p_{T} [GeV]"],
    "onejet eta":["onejet_eta",50,-3.14,3.14,"eta"],
    "onejet phi":["onejet_phi",50,0,3.14,"phi"],

    "twojets1 p_{T}":["twojets1_pt",50,0,150,"p_{T} [GeV]"],
    "twojets1 eta":["twojets1_eta",50,-3.14,3.14,"eta"],
    "twojets1 phi":["twojets1_phi",50,0,3.14,"phi"],

    "twojets2 p_{T}":["twojets2_pt",50,0,150,"p_{T} [GeV]"],
    "twojets2 eta":["twojets2_eta",50,-3.14,3.14,"eta"],
    "twojets2 phi":["twojets2_phi",50,0,3.14,"phi"],

    "threejets1 p_{T}":["threejets1_pt",50,0,150,"p_{T} [GeV]"],
    "threejets1 eta":["threejets1_eta",50,-3.14,3.14,"eta"],
    "threejets1 phi":["threejets1_phi",50,0,3.14,"phi"],

    "threejets2 p_{T}":["threejets2_pt",50,0,150,"p_{T} [GeV]"],
    "threejets2 eta":["threejets2_eta",50,-3.14,3.14,"eta"],
    "threejets2 phi":["threejets2_phi",50,0,3.14,"phi"],

    "threejets3 p_{T}":["threejets3_pt",50,0,150,"p_{T} [GeV]"],
    "threejets3 eta":["threejets3_eta",50,-3.14,3.14,"eta"],
    "threejets3 phi":["threejets3_phi",50,0,3.14,"phi"]
  }

if trackMultiplicity:
  output = "/eos/user/j/jkil/www/"
  plots = {
    "NumTrk(3,3)":["Ntracks",50,0,100,"counts(pt = 3, fromPV = 3)"]
  }

if sphericityEvals:
  output = "/eos/user/j/jkil/www/"
  plots = {
    "Eigenvalue #lambda_{1} (L)":["eval_L1",50,0,1,"1st Eigenvalue #lambda_{1} in Lab frame"],
    "Eigenvalue #lambda_{1} (S)":["eval_Z1",50,0,1,"1st Eigenvalue #lambda_{1} in -Z frame"],

    "Eigenvalue #lambda_{2} (L)":["eval_L2",50,0,1,"2nd Eigenvalue #lambda_{2} in Lab frame"],
    "Eigenvalue #lambda_{2} (S)":["eval_Z2",50,0,1,"2nd Eigenvalue #lambda_{2} in -Z frame"],

    "Eigenvalue #lambda_{3} (L)":["eval_L3",50,0,1,"3rd Eigenvalue #lambda_{3} in Lab frame"],
    "Eigenvalue #lambda_{3} (S)":["eval_Z3",50,0,1,"3rd Eigenvalue #lambda_{3} in -Z frame"]
  }

if scalarSphericityT:
  output = "/eos/user/j/jkil/www/ScalarSphericity_alltracks/"
  plots ={
    "Scalar Sphericity (L)":["ScalarSpher_L",50,0,1,"S^{tracks}_{scalar} (L)"],
    "Scalar Sphericity (Z)":["ScalarSpher_Z",50,0,1,"S^{tracks}_{scalar} (Z)"],
    "Scalar Sphericity (T)":["ScalarSpher_T",50,0,1,"S^{tracks}_{scalar} (T)"],
  }

if scalarSphericityC:
  output = "/eos/user/j/jkil/www/ScalarSphericity_leadcluster/"
  plots = {
    "Scalar Sphericity of Lead Cluster (L)": ["leadclusterScalarSpher_L",50,0,1,"S^{leadcluster}_{scalar} (L)"],
    "Scalar Sphericity of Lead Cluster (Z)": ["leadclusterScalarSpher_Z",50,0,1,"S^{leadcluster}_{scalar} (Z)"],
    "Scalar Sphericity of Lead Cluster (T)": ["leadclusterScalarSpher_T",50,0,1,"S^{leadcluster}_{scalar} (T)"],
    "Scalar Sphericity of Lead Cluster (C)": ["leadclusterScalarSpher_C",50,0,1,"S^{leadcluster}_{scalar} (C)"],
  }

if scalarSphericityS:
  output = "/eos/user/j/jkil/www/ScalarSphericity_leadstrip/"
  plots = {
    "Scalar Sphericity of Lead Strip (EtaWidth = 0.1)(L)": ["leadstripScalarSpher_L"+"_dEta0.1",50,0,1,"S^{leadstrip}_{scalar} (L)"],
    "Scalar Sphericity of Lead Strip (EtaWidth = 0.1)(Z)": ["leadstripScalarSpher_Z"+"_dEta0.1",50,0,1,"S^{leadstrip}_{scalar} (Z)"],
    "Scalar Sphericity of Lead Strip (EtaWidth = 0.1)(T)": ["leadstripScalarSpher_T"+"_dEta0.1",50,0,1,"S^{leadstrip}_{scalar} (T)"],
    "Scalar Sphericity of Lead Strip (EtaWidth = 0.1)(S)": ["leadstripScalarSpher_S"+"_dEta0.1",50,0,1,"S^{leadstrip}_{scalar} (S)"],

    "Scalar Sphericity of Lead Strip (EtaWidth = 0.2)(L)": ["leadstripScalarSpher_L"+"_dEta0.2",50,0,1,"S^{leadstrip}_{scalar} (L)"],
    "Scalar Sphericity of Lead Strip (EtaWidth = 0.2)(Z)": ["leadstripScalarSpher_Z"+"_dEta0.2",50,0,1,"S^{leadstrip}_{scalar} (Z)"],
    "Scalar Sphericity of Lead Strip (EtaWidth = 0.2)(T)": ["leadstripScalarSpher_T"+"_dEta0.2",50,0,1,"S^{leadstrip}_{scalar} (T)"],
    "Scalar Sphericity of Lead Strip (EtaWidth = 0.2)(S)": ["leadstripScalarSpher_S"+"_dEta0.2",50,0,1,"S^{leadstrip}_{scalar} (S)"],

    "Scalar Sphericity of Lead Strip (EtaWidth = 0.3)(L)": ["leadstripScalarSpher_L"+"_dEta0.3",50,0,1,"S^{leadstrip}_{scalar} (L)"],
    "Scalar Sphericity of Lead Strip (EtaWidth = 0.3)(Z)": ["leadstripScalarSpher_Z"+"_dEta0.3",50,0,1,"S^{leadstrip}_{scalar} (Z)"],
    "Scalar Sphericity of Lead Strip (EtaWidth = 0.3)(T)": ["leadstripScalarSpher_T"+"_dEta0.3",50,0,1,"S^{leadstrip}_{scalar} (T)"],
    "Scalar Sphericity of Lead Strip (EtaWidth = 0.3)(S)": ["leadstripScalarSpher_S"+"_dEta0.3",50,0,1,"S^{leadstrip}_{scalar} (S)"],

    "Scalar Sphericity of Lead Strip (EtaWidth = 0.4)(L)": ["leadstripScalarSpher_L"+"_dEta0.4",50,0,1,"S^{leadstrip}_{scalar} (L)"],
    "Scalar Sphericity of Lead Strip (EtaWidth = 0.4)(Z)": ["leadstripScalarSpher_Z"+"_dEta0.4",50,0,1,"S^{leadstrip}_{scalar} (Z)"],
    "Scalar Sphericity of Lead Strip (EtaWidth = 0.4)(T)": ["leadstripScalarSpher_T"+"_dEta0.4",50,0,1,"S^{leadstrip}_{scalar} (T)"],
    "Scalar Sphericity of Lead Strip (EtaWidth = 0.4)(S)": ["leadstripScalarSpher_S"+"_dEta0.4",50,0,1,"S^{leadstrip}_{scalar} (S)"],

    "Scalar Sphericity of Lead Strip (EtaWidth = 0.5)(L)": ["leadstripScalarSpher_L"+"_dEta0.5",50,0,1,"S^{leadstrip}_{scalar} (L)"],
    "Scalar Sphericity of Lead Strip (EtaWidth = 0.5)(Z)": ["leadstripScalarSpher_Z"+"_dEta0.5",50,0,1,"S^{leadstrip}_{scalar} (Z)"],
    "Scalar Sphericity of Lead Strip (EtaWidth = 0.5)(T)": ["leadstripScalarSpher_T"+"_dEta0.5",50,0,1,"S^{leadstrip}_{scalar} (T)"],
    "Scalar Sphericity of Lead Strip (EtaWidth = 0.5)(S)": ["leadstripScalarSpher_S"+"_dEta0.5",50,0,1,"S^{leadstrip}_{scalar} (S)"],

    "Scalar Sphericity of Lead Strip (EtaWidth = 0.6)(L)": ["leadstripScalarSpher_L"+"_dEta0.6",50,0,1,"S^{leadstrip}_{scalar} (L)"],
    "Scalar Sphericity of Lead Strip (EtaWidth = 0.6)(Z)": ["leadstripScalarSpher_Z"+"_dEta0.6",50,0,1,"S^{leadstrip}_{scalar} (Z)"],
    "Scalar Sphericity of Lead Strip (EtaWidth = 0.6)(T)": ["leadstripScalarSpher_T"+"_dEta0.6",50,0,1,"S^{leadstrip}_{scalar} (T)"],
    "Scalar Sphericity of Lead Strip (EtaWidth = 0.6)(S)": ["leadstripScalarSpher_S"+"_dEta0.6",50,0,1,"S^{leadstrip}_{scalar} (S)"],

    "Scalar Sphericity of Lead Strip (EtaWidth = 0.7)(L)": ["leadstripScalarSpher_L"+"_dEta0.7",50,0,1,"S^{leadstrip}_{scalar} (L)"],
    "Scalar Sphericity of Lead Strip (EtaWidth = 0.7)(Z)": ["leadstripScalarSpher_Z"+"_dEta0.7",50,0,1,"S^{leadstrip}_{scalar} (Z)"],
    "Scalar Sphericity of Lead Strip (EtaWidth = 0.7)(T)": ["leadstripScalarSpher_T"+"_dEta0.7",50,0,1,"S^{leadstrip}_{scalar} (T)"],
    "Scalar Sphericity of Lead Strip (EtaWidth = 0.7)(S)": ["leadstripScalarSpher_S"+"_dEta0.7",50,0,1,"S^{leadstrip}_{scalar} (S)"],

    "Scalar Sphericity of Lead Strip (EtaWidth = 0.8)(L)": ["leadstripScalarSpher_L"+"_dEta0.8",50,0,1,"S^{leadstrip}_{scalar} (L)"],
    "Scalar Sphericity of Lead Strip (EtaWidth = 0.8)(Z)": ["leadstripScalarSpher_Z"+"_dEta0.8",50,0,1,"S^{leadstrip}_{scalar} (Z)"],
    "Scalar Sphericity of Lead Strip (EtaWidth = 0.8)(T)": ["leadstripScalarSpher_T"+"_dEta0.8",50,0,1,"S^{leadstrip}_{scalar} (T)"],
    "Scalar Sphericity of Lead Strip (EtaWidth = 0.8)(S)": ["leadstripScalarSpher_S"+"_dEta0.8",50,0,1,"S^{leadstrip}_{scalar} (S)"],

    "Scalar Sphericity of Lead Strip (EtaWidth = 0.9)(L)": ["leadstripScalarSpher_L"+"_dEta0.9",50,0,1,"S^{leadstrip}_{scalar} (L)"],
    "Scalar Sphericity of Lead Strip (EtaWidth = 0.9)(Z)": ["leadstripScalarSpher_Z"+"_dEta0.9",50,0,1,"S^{leadstrip}_{scalar} (Z)"],
    "Scalar Sphericity of Lead Strip (EtaWidth = 0.9)(T)": ["leadstripScalarSpher_T"+"_dEta0.9",50,0,1,"S^{leadstrip}_{scalar} (T)"],
    "Scalar Sphericity of Lead Strip (EtaWidth = 0.9)(S)": ["leadstripScalarSpher_S"+"_dEta0.9",50,0,1,"S^{leadstrip}_{scalar} (S)"],

    "Scalar Sphericity of Lead Strip (EtaWidth = 1.0)(L)": ["leadstripScalarSpher_L"+"_dEta1.0",50,0,1,"S^{leadstrip}_{scalar} (L)"],
    "Scalar Sphericity of Lead Strip (EtaWidth = 1.0)(Z)": ["leadstripScalarSpher_Z"+"_dEta1.0",50,0,1,"S^{leadstrip}_{scalar} (Z)"],
    "Scalar Sphericity of Lead Strip (EtaWidth = 1.0)(T)": ["leadstripScalarSpher_T"+"_dEta1.0",50,0,1,"S^{leadstrip}_{scalar} (T)"],
    "Scalar Sphericity of Lead Strip (EtaWidth = 1.0)(S)": ["leadstripScalarSpher_S"+"_dEta1.0",50,0,1,"S^{leadstrip}_{scalar} (S)"],
  }

if scaledScalarSpherC:
  output = "/eos/user/j/jkil/www/ScaledScalarSpher_leadcluster"
  plots = {
    "LeadC ScalarSpher(C,scaled,m=125)": ["scaledLeadclusterScalarSpher_C",50,0,1,"S^{leadcluster}_{scalar} (C, scaled)"],
    "LeadC ScalarSpher(T,scaled,m=125)": ["scaledLeadclusterScalarSpher_T",50,0,1,"S^{leadcluster}_{scalar} (T, scaled)"],
  }

if scaledScalarSpherS:
  output = "/eos/user/j/jkil/www/ScaledScalarSpher_leadstrip"
  plots = {
    "LeadS ScalarSpher(Etaw=0.6,T,scaled,m=125)": ["scaledLeadstripScalarSpher_T"+"_dEta0.6",50,0,1,"S^{leadstrip}_{scalar} (T, scaled)"],
    "LeadS ScalarSpher(Etaw=0.7,T,scaled,m=125)": ["scaledLeadstripScalarSpher_T"+"_dEta0.7",50,0,1,"S^{leadstrip}_{scalar} (T, scaled)"],
    "LeadS ScalarSpher(Etaw=0.8,T,scaled,m=125)": ["scaledLeadstripScalarSpher_T"+"_dEta0.8",50,0,1,"S^{leadstrip}_{scalar} (T, scaled)"],

    "LeadS ScalarSpher(Etaw=0.6,S,scaled,m=125)": ["scaledLeadstripScalarSpher_S"+"_dEta0.6",50,0,1,"S^{leadstrip}_{scalar} (S, scaled)"],
    "LeadS ScalarSpher(Etaw=0.7,S,scaled,m=125)": ["scaledLeadstripScalarSpher_S"+"_dEta0.7",50,0,1,"S^{leadstrip}_{scalar} (S, scaled)"],
    "LeadS ScalarSpher(Etaw=0.8,S,scaled,m=125)": ["scaledLeadstripScalarSpher_S"+"_dEta0.8",50,0,1,"S^{leadstrip}_{scalar} (S, scaled)"],
  }


for p in plots:
  h1 = ROOT.TH1F(plots[p][0], plots[p][0], plots[p][1], plots[p][2], plots[p][3])
  h2 = h1.Clone(h1.GetName()+ "_2")

  sumwB = 0
  for d in DY:
    #print d.get_storer("vars").attrs.metadata
    sumwB += d.get_storer(channel).attrs.metadata["gensumweight"]
    weightsDY = d[channel]["genweight"]
    for idx, val in enumerate(d[channel][plots[p][0]]):
      h1.Fill(np.real(val),weightsDY[idx])

  sumwS = 0
  for d in ZH:
    if idx%1000 == 0: print (idx)
    #print d.get_storer("vars").attrs.metadata
    sumwS += d.get_storer(channel).attrs.metadata["gensumweight"]
    weightsZS = d[channel]["genweight"]
    for idx, val in enumerate(d[channel][plots[p][0]]):
      h2.Fill(val, weightsZS[idx])

  theColors = {"1":ROOT.kBlue, "2":ROOT.kRed}
  c = ROOT.TCanvas("c","c", 800,600)
  p1 = ROOT.TPad("mainpad", "mainpad", 0, 0.30, 1, 1)
  p1.SetBottomMargin(0.025)
  p1.SetTopMargin(0.08)
  p1.SetLeftMargin(0.12)
  p1.Draw()
  p1.SetLogy(True)
  p2 = ROOT.TPad("ratiopad", "ratiopad", 0, 0, 1, 0.30)
  p2.SetTopMargin(0.01)
  p2.SetBottomMargin(0.45)
  p2.SetLeftMargin(0.12)
  p2.SetFillStyle(0)
  p2.Draw()

  p1.cd()

  h1.SetTitle("")
  if normalize:
    h1.GetYaxis().SetTitle("Normalized events")
    h1.Scale(1./h1.Integral())
    h2.Scale(1./h2.Integral())
    h1.SetMaximum(1.1)
    h1.SetMinimum(0.001)

  else: # Scale to 137 fb^{-1}, a lot of hard coding we need to fix
    xsecDY   = 7181000*0.0336*2
    xsecSUEP = 870 * 0.0336 * 2 # ZH*Br(Z->ll)*2 accounting for el/mu
    lumi     = 137.0
    h1.Scale(lumi*xsecDY/sumwB)
    h2.Scale(lumi*xsecSUEP/sumwS)
    maxY = max(h1.GetMaximum(), h2.GetMaximum())
    minY = max(min(h2.GetMinimum(), h2.GetMinimum()),1)
    h1.SetMaximum(maxY)
    h1.SetMinimum(minY)

  h1.SetLineColor(theColors["1"])
  h2.SetLineColor(theColors["2"])
  h1.Draw()
  h2.Draw("same")
  tl = ROOT.TLegend(0.6,0.7,0.9,0.9)
  tl.AddEntry(h1, "DY", "l")
  tl.AddEntry(h2, "ZS, m_{S} = 125 GeV", "l")
  tl.Draw("same")

  p2.cd()
  ratioOff = h1.Clone(h1.GetName().replace("h","r"))
  ratioCus = h2.Clone(h2.GetName().replace("h","r"))
  ratioOff.Divide(h1)
  ratioOff.GetYaxis().SetTitle("Events/DY Events")
  ratioOff.SetTitleSize(0.05)
  ratioCus.Divide(h1)
  ratioCus.SetLineColor(theColors["2"])
  ratioOff.SetMaximum(2.)
  ratioOff.SetMinimum(0.)
  ratioOff.GetXaxis().SetTitle(plots[p][4])
  ratioOff.GetXaxis().SetTitleSize(0.18)
  ratioOff.GetXaxis().SetTitleOffset(1.)
  ratioOff.GetXaxis().SetLabelSize(0.15)
  ratioOff.Draw()
  ratioCus.Draw("same")
  c.SaveAs("%s/%s.pdf"%(output,p))
  c.SaveAs("%s/%s.png"%(output,p))

