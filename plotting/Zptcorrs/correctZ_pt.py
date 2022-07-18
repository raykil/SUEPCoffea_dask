import ROOT
import json
import array

ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetPaintTextFormat("1.2f")
inputs = ROOT.TFile("/eos/user/c/cericeci/www/SUEP/stack_Zptsideband_2D/2D_Zpt_Zeta.root", "READ")
back = inputs.Get("total_background;12")
data = inputs.Get("2D_Zpt_Zeta_data")

ptbins  = array.array('d',[-5,1.,5,10,15,25,35,50,60,80,100,125,150,175,200,300,400])
etabins = array.array('d',[-5,-4,-3,-2,-1,0,1,2,3,4,5])
print(ptbins, etabins)
Zpt_d  = ROOT.TH2D('Zpt_d', 'Zpt_d', 16, ptbins, 10, etabins)
Zpt_b  = ROOT.TH2D('Zpt_b', 'Zpt_b', 16, ptbins, 10, etabins)

#Zpt_SF  = ROOT.TH2D('Zpt_SF', 'Zpt_SF', len(ptbins), ptbins, len(etabins), etabins)

for i in range(0, back.GetNbinsX()+1):
  for j in range(0, back.GetNbinsY()+1):
    bx = Zpt_d.GetXaxis().FindBin(back.GetXaxis().GetBinCenter(i))
    by = Zpt_d.GetYaxis().FindBin(back.GetYaxis().GetBinCenter(j))
    Zpt_d.SetBinContent(bx, by, Zpt_d.GetBinContent(bx, by)+ data.GetBinContent(i,j))
    Zpt_b.SetBinContent(bx, by, Zpt_b.GetBinContent(bx, by)+ back.GetBinContent(i,j))

c = ROOT.TCanvas("c","c", 800,600)
c.SetLogx(True)
Zpt_SF = Zpt_d.Clone("Zpt_SF")
Zpt_SF.Divide(Zpt_b)
Zpt_SF.SetMaximum(1.5)
Zpt_SF.SetMinimum(0.5)
Zpt_SF.SetTitle("Zpt_SF")
Zpt_SF.Draw("colztext")
c.SaveAs("/eos/user/c/cericeci/www/Zpt_corr.pdf")
out = ROOT.TFile("Zpt_corr.root","RECREATE")
out.cd()
Zpt_SF.Write()
Zpt_d.Write()
Zpt_b.Write()

