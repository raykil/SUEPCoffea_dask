import os
import h5py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import math
import random

#direc = ['C:/Users/slatt/Downloads/test/']
#direc = ['/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2017/MET_E','/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2017/MET_B','/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2017/MET_D','/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2017/MET_C','/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2017/MET_F']
#direc = ['/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2016APV/MET_E','/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2016APV/MET_B2','/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2016APV/MET_D','/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2016APV/MET_C','/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2016APV/MET_F']
#direc = ['/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2016/MET_F','/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2016/MET_G','/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2016/MET_H']
#direc = ['/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2018/MET_A', '/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2018/MET_D', '/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2018/MET_B', '/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2018/MET_C']

direc = ['/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2018/DY_lowmass', '/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2018/DYToLL_M50_Pt0To50', '/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2018/DYToLL_M50_Pt100To250', '/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2018/DYToLL_M50_Pt250To400', '/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2018/DYToLL_M50_Pt400To650', '/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2018/DYToLL_M50']
#direc = ['/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2017/DY_lowmass', '/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2017/DYToLL_M50_Pt0To50', '/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2017/DYToLL_M50_Pt100To250', '/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2017/DYToLL_M50_Pt250To400', '/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2017/DYToLL_M50_Pt400To650', '/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2017/DYToLL_M50']
#direc = ['/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2016/DY_lowmass', '/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2016/DYToLL_M50_Pt0To50', '/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2016/DYToLL_M50_Pt100To250', '/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2016/DYToLL_M50_Pt250To400', '/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2016/DYToLL_M50_Pt400To650', '/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2016/DYToLL_M50']
#direc = ['/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2016APV/DY_lowmass', '/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2016APV/DYToLL_M50_Pt0To50', '/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2016APV/DYToLL_M50_Pt100To250', '/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2016APV/DYToLL_M50_Pt250To400', '/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2016APV/DYToLL_M50_Pt400To650', '/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/allTriggerData/2016APV/DYToLL_M50']

 # the working directory (where your files are stored)
#direc = ['/eos/user/g/gdecastr/SUEPCoffea_dask/DY_lowmass_16', '/eos/user/g/gdecastr/SUEPCoffea_dask/DY_50t100_16', '/eos/user/g/gdecastr/SUEPCoffea_dask/DY_100t250_16', '/eos/user/g/gdecastr/SUEPCoffea_dask/DY_250t400_16']
#direc = [ '/eos/user/g/gdecastr/SUEPCoffea_dask/DY_lowmass_16APV', '/eos/user/g/gdecastr/SUEPCoffea_dask/DY_50t100_16APV', '/eos/user/g/gdecastr/SUEPCoffea_dask/DY_100t250_16APV', '/eos/user/g/gdecastr/SUEPCoffea_dask/DY_250t400_16APV']
#direc = ['/eos/user/g/gdecastr/SUEPCoffea_dask/DY_lowmass_18','/eos/user/g/gdecastr/SUEPCoffea_dask/DY_50t100_18', '/eos/user/g/gdecastr/SUEPCoffea_dask/DY_100t250_18', '/eos/user/g/gdecastr/SUEPCoffea_dask/DY_250t400_18']
#direc = ['/eos/user/g/gdecastr/SUEPCoffea_dask/testWorkflow']


electrons_leadpt = np.array([])
electrons_eta = np.array([])
electrons_phi = np.array([])
electrons_subleadpt = np.array([])

muons_leadpt = np.array([])
muons_subleadpt = np.array([])
muons_eta = np.array([])
muons_phi = np.array([])

ctrl_muons_leadpt = np.array([])
ctrl_muons_subleadpt = np.array([])
ctrl_muons_eta = np.array([])
ctrl_muons_phi = np.array([])
ctrl_electrons_leadpt = np.array([])
ctrl_electrons_subleadpt = np.array([])
ctrl_electrons_eta = np.array([])
ctrl_electrons_phi = np.array([])

count = 0
for i in direc:
    dirs = os.listdir(i)
    print(i)
    for idir in dirs: # this will iterate over the files in your working directory
        print(idir)
        if os.path.getsize(direc[count]+'/'+idir) == 0:
            continue
        if idir.endswith('_electrons.csv'):
            df = pd.read_csv(direc[count]+'/'+idir)
            electrons_leadpt = np.concatenate((electrons_leadpt,df['electron_leadpt'].tolist()), axis = None)
            electrons_subleadpt = np.concatenate((electrons_subleadpt,df['electron_subleadpt'].tolist()), axis = None)
            electrons_eta = np.concatenate((electrons_eta,df['electron_leadeta'].tolist()), axis = None)
            #electrons_phi = np.concatenate((electrons_phi,df['electron_leadphi'].tolist()), axis = None)
        if idir.endswith('_electrons_control.csv'):
            df = pd.read_csv(direc[count]+'/'+idir)
            ctrl_electrons_leadpt = np.concatenate((ctrl_electrons_leadpt,df['electrons_control_lead'].tolist()), axis = None)
            ctrl_electrons_subleadpt = np.concatenate((ctrl_electrons_subleadpt,df['electrons_control_sublead'].tolist()), axis = None)
            ctrl_electrons_eta = np.concatenate((ctrl_electrons_eta,df['electronsControl_leadeta'].tolist()), axis = None)
            #ctrl_electrons_phi = np.concatenate((ctrl_electrons_phi,df['electronsControl_leadphi'].tolist()), axis = None)
        if idir.endswith('_muons.csv'):
            df = pd.read_csv(direc[count]+'/'+idir)
            muons_leadpt = np.concatenate((muons_leadpt,df['muon_leadpt'].tolist()), axis = None)
            muons_subleadpt = np.concatenate((muons_subleadpt,df['muon_subleadpt'].tolist()), axis = None)
            muons_eta = np.concatenate((muons_eta,df['muon_leadeta'].tolist()), axis = None)
            #muons_phi = np.concatenate((muons_phi,df['muon_leadphi'].tolist()), axis = None)
        if idir.endswith('_muons_control.csv'):
            df = pd.read_csv(direc[count]+'/'+idir)
            ctrl_muons_leadpt = np.concatenate((ctrl_muons_leadpt,df['muon_control_lead'].tolist()), axis = None)
            ctrl_muons_subleadpt = np.concatenate((ctrl_muons_subleadpt,df['muon_control_sublead'].tolist()), axis = None)
            ctrl_muons_eta = np.concatenate((ctrl_muons_eta,df['muon_control_leadeta'].tolist()), axis = None)
            #ctrl_muons_phi = np.concatenate((ctrl_muons_phi,df['muon_control_leadphi'].tolist()), axis = None)
    count = count + 1

pt_bins_muons = np.array([25.0, 60.0, 120.0, 200.0])
pt_bins_muons_2 = np.array([25.0, 40.0, 60.0, 90.0, 120.0, 160.0, 200.0])
pt_bins_muons_sub = np.array([10.0, 25.0, 40.0, 60.0, 90.0, 120.0, 160.0, 200.0])
eta_bins_muons = np.array([0.0, 0.9, 1.2, 2.1, 2.4])

pt_bins_elec = np.array([25, 60, 120, 200])
pt_bins_elec_2 = np.array([25, 60, 120, 160, 200])
pt_bins_elec_sub = np.array([10, 25, 60, 120, 160, 200])
#eta_bins_elec = np.array([-2.5, -1.566, -1.444, 0.0, 1.444, 1.566, 2.5])
eta_bins_elec = np.array([0.0, .6, 1.444, 1.566, 2.5])
eta_bins_elec_2 = np.array([-2.5, -1.566, -1.444, -.6, 0.0, .6, 1.444, 1.566, 2.5])

def clopper_pearson(x, n, alpha=1-.682):
    b = scipy.stats.beta.ppf
    lo = b(alpha / 2, x, n - x + 1)
    hi = b(1 - alpha / 2, x + 1, n - x)
    div = float(x/n)
    return 0.0 if math.isnan(lo) else div-lo, 0.0 if math.isnan(hi) else hi-div
    return [div-lo, hi-div]

h1 = plt.hist2d(ctrl_electrons_leadpt, np.abs(ctrl_electrons_eta), [pt_bins_elec, eta_bins_elec])
h2 = plt.hist2d(electrons_leadpt, np.abs(electrons_eta), [pt_bins_elec, eta_bins_elec])

efficiencies_elec = []
up_elec = []
down_elec = []
idx_x = 0
idx_y = 0
for i in h2[0]:
    temp_eff = []
    temp_up = []
    temp_down = []
    idx_y = 0
    for j in i:
        if h1[0][idx_x][idx_y] == 0:
            temp_eff.append(0)
            temp_up.append(0)
            temp_down.append(0)
        else:
            temp_var = h1[0][idx_x][idx_y]
            temp_eff.append(j/temp_var)
            uncertainties = clopper_pearson(j,temp_var)
            temp_down.append(uncertainties[0])
            temp_up.append(uncertainties[1])
        idx_y = idx_y + 1
    efficiencies_elec.append(temp_eff)
    up_elec.append(temp_up)
    down_elec.append(temp_down)
    idx_x = idx_x +1

h1 = plt.hist2d(ctrl_electrons_leadpt, ctrl_electrons_eta, [pt_bins_elec, eta_bins_elec_2])
h2 = plt.hist2d(electrons_leadpt, electrons_eta, [pt_bins_elec, eta_bins_elec_2])

efficiencies_elec_2 = []
up_elec_2 = []
down_elec_2 = []
idx_x = 0
idx_y = 0
for i in h2[0]:
    temp_eff = []
    temp_up = []
    temp_down = []
    idx_y = 0
    for j in i:
        if h1[0][idx_x][idx_y] == 0:
            temp_eff.append(0)
            temp_up.append(0)
            temp_down.append(0)
        else:
            temp_var = h1[0][idx_x][idx_y]
            temp_eff.append(j/temp_var)
            uncertainties = clopper_pearson(j,temp_var)
            temp_down.append(uncertainties[0])
            temp_up.append(uncertainties[1])
        idx_y = idx_y + 1
    efficiencies_elec_2.append(temp_eff)
    up_elec_2.append(temp_up)
    down_elec_2.append(temp_down)
    idx_x = idx_x +1

h1 = plt.hist2d(ctrl_electrons_leadpt, ctrl_electrons_subleadpt, [pt_bins_elec_2, pt_bins_elec_sub])
h2 = plt.hist2d(electrons_leadpt, electrons_subleadpt, [pt_bins_elec_2, pt_bins_elec_sub])

efficiencies_elec_pt = []
up_elec_pt = []
down_elec_pt = []
idx_x = 0
idx_y = 0
for i in h2[0]:
    temp_eff = []
    temp_up = []
    temp_down = []
    idx_y = 0
    for j in i:
        if h1[0][idx_x][idx_y] == 0:
            temp_eff.append(0)
            temp_up.append(0)
            temp_down.append(0)
        else:
            temp_var = h1[0][idx_x][idx_y]
            temp_eff.append(j/temp_var)
            uncertainties = clopper_pearson(j,temp_var)
            temp_down.append(uncertainties[0])
            temp_up.append(uncertainties[1])
        idx_y = idx_y + 1
    efficiencies_elec_pt.append(temp_eff)
    up_elec_pt.append(temp_up)
    down_elec_pt.append(temp_down)
    idx_x = idx_x +1

h1 = plt.hist2d(ctrl_muons_leadpt, np.abs(ctrl_muons_eta), [pt_bins_muons, eta_bins_muons])
h2 = plt.hist2d(muons_leadpt, np.abs(muons_eta), [pt_bins_muons, eta_bins_muons])

efficiencies_muon = []
up_muon = []
down_muon = []
idx_x = 0
idx_y = 0
for i in h2[0]:
    temp_eff = []
    temp_up = []
    temp_down = []
    idx_y = 0
    for j in i:
        if h1[0][idx_x][idx_y] == 0:
            temp_eff.append(0)
            temp_up.append(0)
            temp_down.append(0)
        else:
            temp_var = h1[0][idx_x][idx_y]
            temp_eff.append(j/temp_var)
            uncertainties = clopper_pearson(j,temp_var)
            temp_down.append(uncertainties[0])
            temp_up.append(uncertainties[1])
        idx_y = idx_y + 1
    efficiencies_muon.append(temp_eff)
    up_muon.append(temp_up)
    down_muon.append(temp_down)
    idx_x = idx_x +1

h1 = plt.hist2d(ctrl_muons_leadpt, ctrl_muons_subleadpt, [pt_bins_muons_2, pt_bins_muons_sub])
h2 = plt.hist2d(muons_leadpt, muons_subleadpt, [pt_bins_muons_2, pt_bins_muons_sub])

efficiencies_muon_pt = []
up_muon_pt = []
down_muon_pt = []
idx_x = 0
idx_y = 0
for i in h2[0]:
    temp_eff = []
    temp_up = []
    temp_down = []
    idx_y = 0
    for j in i:
        if h1[0][idx_x][idx_y] == 0:
            temp_eff.append(0)
            temp_up.append(0)
            temp_down.append(0)
        else:
            temp_var = h1[0][idx_x][idx_y]
            temp_eff.append(j/temp_var)
            uncertainties = clopper_pearson(j,temp_var)
            temp_down.append(uncertainties[0])
            temp_up.append(uncertainties[1])
        idx_y = idx_y + 1
    efficiencies_muon_pt.append(temp_eff)
    up_muon_pt.append(temp_up)
    down_muon_pt.append(temp_down)
    idx_x = idx_x +1

efficiencies_muon = np.asarray(efficiencies_muon)
up_muon = np.asarray(up_muon)
down_muon = np.asarray(down_muon)

efficiencies_muon_pt = np.asarray(efficiencies_muon_pt)
up_muon_pt = np.asarray(up_muon_pt)
down_muon_pt = np.asarray(down_muon_pt)

efficiencies_elec = np.asarray(efficiencies_elec)
up_elec = np.asarray(up_elec)
down_elec = np.asarray(down_elec)

efficiencies_elec_2 = np.asarray(efficiencies_elec_2)
up_elec_2 = np.asarray(up_elec_2)
down_elec_2 = np.asarray(down_elec_2)

efficiencies_elec_pt = np.asarray(efficiencies_elec_pt)
up_elec_pt = np.asarray(up_elec_pt)
down_elec_pt = np.asarray(down_elec_pt)

np.savetxt("finalResults/triggerEffs/2018/eff_mu_DY.csv", efficiencies_muon, delimiter=",")
np.savetxt("finalResults/triggerEffs/2018/up_mu_DY.csv", up_muon, delimiter=",")
np.savetxt("finalResults/triggerEffs/2018/down_mu_DY.csv", down_muon, delimiter=",")

np.savetxt("finalResults/triggerEffs/2018/eff_mu_DY_pt.csv", efficiencies_muon_pt, delimiter=",")
np.savetxt("finalResults/triggerEffs/2018/up_mu_DY_pt.csv", up_muon_pt, delimiter=",")
np.savetxt("finalResults/triggerEffs/2018/down_mu_DY_pt.csv", down_muon_pt, delimiter=",")

np.savetxt("finalResults/triggerEffs/2018/eff_e_DY.csv", efficiencies_elec, delimiter=",")
np.savetxt("finalResults/triggerEffs/2018/up_e_DY.csv", up_elec, delimiter=",")
np.savetxt("finalResults/triggerEffs/2018/down_e_DY.csv", down_elec, delimiter=",")

np.savetxt("finalResults/triggerEffs/2018/eff_e_DY_2.csv", efficiencies_elec_2, delimiter=",")
np.savetxt("finalResults/triggerEffs/2018/up_e_DY_2.csv", up_elec_2, delimiter=",")
np.savetxt("finalResults/triggerEffs/2018/down_e_DY_2.csv", down_elec_2, delimiter=",")

np.savetxt("finalResults/triggerEffs/2018/eff_e_DY_pt.csv", efficiencies_elec_pt, delimiter=",")
np.savetxt("finalResults/triggerEffs/2018/up_e_DY_pt.csv", up_elec_pt, delimiter=",")
np.savetxt("finalResults/triggerEffs/2018/down_e_DY_pt.csv", down_elec_pt, delimiter=",")


plt.clf()
#plt.title(r'Electron Trigger Eff - 48.353 $fb^{-1}$')
plt.title(r'Electron Trigger Eff')
plt.xlabel(r'Leading Electron $|\eta|$')
plt.ylabel('Leading Electron pT')
plt.pcolormesh(eta_bins_elec, pt_bins_elec, efficiencies_elec, cmap = 'jet', vmin = 0, vmax = 1.0)
plt.colorbar()
for i in range(len(pt_bins_elec)-1):
    for j in range(len(eta_bins_elec)-1):
        plt.text((eta_bins_elec[j]+eta_bins_elec[j+1])/2,(pt_bins_elec[i]+pt_bins_elec[i+1])/2, str(round(efficiencies_elec[i][j],3))+r'$\pm$'+str(round((up_elec[i][j]+down_elec[i][j])/2,2)), color="w", ha="center", va="center", fontweight="bold", size = 3, rotation=45)
plt.savefig('finalResults/triggerEffs/2018/DY_elec.pdf')
plt.savefig('finalResults/triggerEffs/2018/DY_elec.png', dpi = 2000)
#plt.show()

plt.clf()
#plt.title(r'Electron Trigger Eff - 48.353 $fb^{-1}$')
plt.title(r'Electron Trigger Eff')
plt.xlabel(r'Leading Electron $\eta$')
plt.ylabel('Leading Electron pT')
plt.pcolormesh(eta_bins_elec_2, pt_bins_elec, efficiencies_elec_2, cmap = 'jet', vmin = 0, vmax = 1.0)
plt.colorbar()
for i in range(len(pt_bins_elec)-1):
    for j in range(len(eta_bins_elec_2)-1):
        plt.text((eta_bins_elec_2[j]+eta_bins_elec_2[j+1])/2,(pt_bins_elec[i]+pt_bins_elec[i+1])/2, str(round(efficiencies_elec_2[i][j],3))+r'$\pm$'+str(round((up_elec_2[i][j]+down_elec_2[i][j])/2,2)), color="w", ha="center", va="center", fontweight="bold", size = 3, rotation=45)
plt.savefig('finalResults/triggerEffs/2018/DY_elec_2.pdf')
plt.savefig('finalResults/triggerEffs/2018/DY_elec_2.png', dpi = 2000)
#plt.show()

plt.clf()
#plt.title(r'Electron Trigger Eff - 48.353 $fb^{-1}$')
plt.title(r'Electron Trigger Eff')
plt.xlabel(r'Subleading Electron pT')
plt.ylabel('Leading Electron pT')
plt.pcolormesh(pt_bins_elec_sub, pt_bins_elec_2, efficiencies_elec_pt, cmap = 'jet', vmin = 0, vmax = 1.0)
plt.colorbar()
for i in range(len(pt_bins_elec_2)-1):
    for j in range(len(pt_bins_elec_sub)-1):
        plt.text((pt_bins_elec_sub[j]+pt_bins_elec_sub[j+1])/2,(pt_bins_elec_2[i]+pt_bins_elec_2[i+1])/2, str(round(efficiencies_elec_pt[i][j],3))+r'$\pm$'+str(round((up_elec_pt[i][j]+down_elec_pt[i][j])/2,2)), color="w", ha="center", va="center", fontweight="bold", size = 4, rotation=45)
plt.savefig('finalResults/triggerEffs/2018/DY_elec_pt.pdf')
plt.savefig('finalResults/triggerEffs/2018/DY_elec_pt.png', dpi = 2000)
#plt.show()

plt.clf()
#plt.title(r'Muon Trigger Eff - 48.353 $fb^{-1}$')
plt.title(r'Muon Trigger Eff')
plt.xlabel(r'Leading Muon $\eta$')
plt.ylabel('Leading Muon pT')
plt.pcolormesh(eta_bins_muons, pt_bins_muons, efficiencies_muon, cmap = 'jet', vmin = 0, vmax = 1.0)
plt.colorbar()
for i in range(len(pt_bins_muons)-1):
    for j in range(len(eta_bins_muons)-1):
        plt.text((eta_bins_muons[j]+eta_bins_muons[j+1])/2,(pt_bins_muons[i]+pt_bins_muons[i+1])/2, str(round(efficiencies_muon[i][j],3))+r'$\pm$'+str(round((up_muon[i][j]+down_muon[i][j])/2,2)), color="w", ha="center", va="center", fontweight="bold", size = 3, rotation=45)
plt.savefig('finalResults/triggerEffs/2018/DY_muon.pdf')
plt.savefig('finalResults/triggerEffs/2018/DY_muon.png', dpi = 2000)
#plt.show()

plt.clf()
#plt.title(r'Muon Trigger Eff - 48.353 $fb^{-1}$')
plt.title(r'Muon Trigger Eff')
plt.xlabel('Subleading Muon pT')
plt.ylabel('Leading Muon pT')
plt.pcolormesh(pt_bins_muons_sub, pt_bins_muons_2, efficiencies_muon_pt, cmap = 'jet', vmin = 0, vmax = 1.0)
plt.colorbar()
for i in range(len(pt_bins_muons_2)-1):
    for j in range(len(pt_bins_muons_sub)-1):
        plt.text((pt_bins_muons_sub[j]+pt_bins_muons_sub[j+1])/2,(pt_bins_muons_2[i]+pt_bins_muons_2[i+1])/2, str(round(efficiencies_muon_pt[i][j],3))+r'$\pm$'+str(round((up_muon_pt[i][j]+down_muon_pt[i][j])/2,2)), color="w", ha="center", va="center", fontweight="bold", size = 2.5, rotation=45)
plt.savefig('finalResults/triggerEffs/2018/DY_muon_pt.pdf')
plt.savefig('finalResults/triggerEffs/2018/DY_muon_pt.png', dpi = 2000)
#plt.show()
