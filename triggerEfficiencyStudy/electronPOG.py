import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ROOT
import sys

year = int(sys.argv[1])

dy_eff_elec = np.genfromtxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/'+str(year)+'/eff_e_DY_Eta.csv',delimiter = ',')
MET_eff_elec = np.genfromtxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/'+str(year)+'/eff_e_MET_Eta.csv',delimiter = ',')
dy_up_elec = np.genfromtxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/'+str(year)+'/up_e_DY_Eta.csv',delimiter = ',')
MET_up_elec = np.genfromtxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/'+str(year)+'/up_e_MET_Eta.csv',delimiter = ',')
dy_down_elec = np.genfromtxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/'+str(year)+'/down_e_DY_Eta.csv',delimiter = ',')
MET_down_elec = np.genfromtxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/'+str(year)+'/down_e_MET_Eta.csv',delimiter = ',')

if year == 2015 or year == 2016:
    pt_bins_elec = np.array([0., 30., 40., 50., 100., 200., 500.])
else:
    np.array([0., 33., 40., 50., 100., 200., 500.])

#eta_bins_elec = np.array([-2.5, -1.566, -1.444, -.6, 0.0, .6, 1.444, 1.566, 2.5])
eta_bins_elec = [-2.4, -2.0, -1.566, -1.4442, -0.8, 0, 0.8, 1.4442, 1.566, 2.0, 2.4]

efficiencies_elec = []
up_elec = []
down_elec = []
for i in range(len(dy_eff_elec)):
    temp_eff = []
    temp_up = []
    temp_down = []
    for j in range(len(dy_eff_elec[0])):
        if(dy_eff_elec[i][j] == 0 or MET_eff_elec[i][j] == 0):
            temp_eff.append(0.0)
            temp_up.append(0.0)
            temp_down.append(0.0)
        else:
            temp_eff.append(MET_eff_elec[i][j]/dy_eff_elec[i][j])
            temp_up.append((MET_eff_elec[i][j]/dy_eff_elec[i][j])*np.sqrt((dy_up_elec[i][j]/dy_eff_elec[i][j])**(2) + (MET_up_elec[i][j]/MET_eff_elec[i][j])**(2)))
            if ((MET_eff_elec[i][j]/dy_eff_elec[i][j])*np.sqrt((dy_down_elec[i][j]/dy_eff_elec[i][j])**(2) + (MET_down_elec[i][j]/MET_eff_elec[i][j])**(2)) > 0.8):
                temp_down.append(0)
            else:
                temp_down.append((MET_eff_elec[i][j]/dy_eff_elec[i][j])*np.sqrt((dy_down_elec[i][j]/dy_eff_elec[i][j])**(2) + (MET_down_elec[i][j]/MET_eff_elec[i][j])**(2)))
    efficiencies_elec.append(temp_eff)
    up_elec.append(temp_up)
    down_elec.append(temp_down)

e_SF = np.array(efficiencies_elec).flatten('F')
e_up = np.array(up_elec).flatten('F')
e_down = np.array(down_elec).flatten('F')

colors =  ['r','g','b','c','m', 'y', 'k']
for i in range(5):
    if i == 2:
        continue
    j = (3.5 - i)/2
    plt.errorbar([35-j, 45-j, 75-j, 150-j, 350-j], e_SF[i*6 + 1:i*6 + 6],  yerr = (e_down[i*6 + 1:i*6 + 6], e_up[i*6 + 1:i*6 + 6]), xerr = ([5-j, 5-j, 25-j, 50-j, 150-j], [5+j, 5+j, 25+j, 50+j, 150+j]), fmt = 'o', label = str(eta_bins_elec[i])+r'$<\eta$<'+str(eta_bins_elec[i+1]), color = colors[i])

if year == 2015 or year == 2016:
    f = ROOT.TFile("Riccardo_egammaTriggerEfficiency_2016_20200422.root")
elif year == 2017:
    f = ROOT.TFile("Riccardo_egammaTriggerEfficiency_2017_20200422.root")
else:
    f = ROOT.TFile("Riccardo_egammaTriggerEfficiency_2018_20200422.root")

bin_35, bin_45, bin_75, bin_150, bin_350 = [], [], [], [], []

graph = f.Get("grSF1D_1")
for i in range(graph.GetN()):
    bin_35.append((graph.GetErrorX(i), graph.GetErrorY(i), graph.GetPointX(i), graph.GetPointY(i)))

bin_35 = sorted(bin_35, key = lambda x: x[2])

graph = f.Get("grSF1D_2")
for i in range(graph.GetN()):
    bin_45.append((graph.GetErrorX(i), graph.GetErrorY(i), graph.GetPointX(i), graph.GetPointY(i)))

bin_45 = sorted(bin_45, key = lambda x: x[2])

graph = f.Get("grSF1D_3")
for i in range(graph.GetN()):
    bin_75.append((graph.GetErrorX(i), graph.GetErrorY(i), graph.GetPointX(i), graph.GetPointY(i)))

bin_75 = sorted(bin_75, key = lambda x: x[2])

graph = f.Get("grSF1D_4")
for i in range(graph.GetN()):
    bin_150.append((graph.GetErrorX(i), graph.GetErrorY(i), graph.GetPointX(i), graph.GetPointY(i)))

bin_150 = sorted(bin_150, key = lambda x: x[2])

graph = f.Get("grSF1D_5")
for i in range(graph.GetN()):
    bin_350.append((graph.GetErrorX(i), graph.GetErrorY(i), graph.GetPointX(i), graph.GetPointY(i)))

bin_350 = sorted(bin_350, key = lambda x: x[2])

eta_bins_elec = [-2.4, -2.0, -1.566, -1.4442, -0.8, 0, 0.8, 1.4442, 1.566, 2.0, 2.4]
colors =  ['r','g','b','c','m', 'y', 'k']
for i in range(5):
    temp_eta = []
    if i == 2:
        continue
    for b in [bin_35, bin_45, bin_75, bin_150, bin_350]:
        temp_eta.append(b[i])
    j = (3.5 - i)/2
    plt.errorbar([35-j, 45-j, 75-j, 150-j, 350-j], [x[3] for x in temp_eta],  yerr = ([x[1] for x in temp_eta], [x[1] for x in temp_eta]), xerr = ([5-j, 5-j, 25-j, 50-j, 150-j], [5+j, 5+j, 25+j, 50+j, 150+j]), fmt = '^', label = "POG " + str(eta_bins_elec[i])+r'$<\eta$<'+str(eta_bins_elec[i+1]), color = colors[i])
plt.xlabel(r'Center of $p_T$ Bin')
plt.ylabel('Scale Factor')
plt.legend(loc =(.5,.8),prop={'size': 6}, ncol = 2)
if year == 2015:
    plt.title('Single Electron Tight 2016APV Comparison')
    plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/EGamma/2016APV_e.png', dpi = 2000)
if year == 2016:
    plt.title('Single Electron Tight 2016 Comparison')
    plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/EGamma/2016_e.png', dpi = 2000)
if year == 2017:
    plt.title('Single Electron Tight 2017 Comparison')
    plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/EGamma/2017_e.png', dpi = 2000)
if year == 2018:
    plt.title('Single Electron Tight 2018 Comparison')
    plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/EGamma/2018_e.png', dpi = 2000)
plt.clf()

for i in range(5, 10):
    if i == 7:
        continue
    j = (3.5 - i)/2
    plt.errorbar([35-j, 45-j, 75-j, 150-j, 350-j], e_SF[i*6 + 1:i*6 + 6],  yerr = (e_down[i*6 + 1:i*6 + 6], e_up[i*6 + 1:i*6 + 6]), xerr = ([5-j, 5-j, 25-j, 50-j, 150-j], [5+j, 5+j, 25+j, 50+j, 150+j]), fmt = 'o', label = str(eta_bins_elec[i])+r'$<\eta$<'+str(eta_bins_elec[i+1]), color = colors[i-5])

for i in range(5,10):
    temp_eta = []
    if i == 7:
        continue
    for b in [bin_35, bin_45, bin_75, bin_150, bin_350]:
        temp_eta.append(b[i])
    j = (3.5 - i)/2
    plt.errorbar([35-j, 45-j, 75-j, 150-j, 350-j], [x[3] for x in temp_eta],  yerr = ([x[1] for x in temp_eta], [x[1] for x in temp_eta]), xerr = ([5-j, 5-j, 25-j, 50-j, 150-j], [5+j, 5+j, 25+j, 50+j, 150+j]), fmt = '^', label = "POG " + str(eta_bins_elec[i])+r'$<\eta$<'+str(eta_bins_elec[i+1]), color = colors[i-5])
plt.xlabel(r'Center of $p_T$ Bin')
plt.ylabel('Scale Factor')
plt.legend(loc =(.5,.8),prop={'size': 6}, ncol = 2)
if year == 2015:
    plt.title('Single Electron Tight 2016APV Comparison')
    plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/EGamma/2016APV_e_2.png', dpi = 2000)
if year == 2016:
    plt.title('Single Electron Tight 2016 Comparison')
    plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/EGamma/2016_e_2.png', dpi = 2000)
if year == 2017:
    plt.title('Single Electron Tight 2017 Comparison')
    plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/EGamma/2017_e_2.png', dpi = 2000)
if year == 2018:
    plt.title('Single Electron Tight 2018 Comparison')
    plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/EGamma/2018_e_2.png', dpi = 2000)
plt.clf()
