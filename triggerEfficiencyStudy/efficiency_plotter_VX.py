import os
import h5py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import math
import random
import sys
from multiprocessing import Pool
from contextlib import closing 
import time

isData = bool(int(sys.argv[1]))
year = int(sys.argv[2])

if isData:
    if year == 2015:
        direc = ["/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/analyzerOutput/2015/MET_B2", "/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/analyzerOutput/2015/MET_C", "/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/analyzerOutput/2015/MET_D", "/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/analyzerOutput/2015/MET_E", "/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/analyzerOutput/2015/MET_F"]
    if year == 2016:
        direc = ["/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/analyzerOutput/2016/MET_H", "/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/analyzerOutput/2016/MET_G", "/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/analyzerOutput/2016/MET_F"]
    if year == 2017:
        direc = ["/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/analyzerOutput/2017/MET_B", "/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/analyzerOutput/2017/MET_C", "/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/analyzerOutput/2017/MET_D", "/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/analyzerOutput/2017/MET_E", "/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/analyzerOutput/2017/MET_F"]
    if year == 2018:
        direc = ["/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/analyzerOutput/2018/MET_B", "/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/analyzerOutput/2018/MET_C", "/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/analyzerOutput/2018/MET_D", "/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/analyzerOutput/2018/MET_A"]
else:
    #direc = ["/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/analyzerOutput/"+str(year)+"/DYToLL_M50_Pt0To50", "/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/analyzerOutput/"+str(year)+"/DYToLL_M50_Pt50To100", "/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/analyzerOutput/"+str(year)+"/DYToLL_M50_Pt100To250", "/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/analyzerOutput/"+str(year)+"/DYToLL_M50", "/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/analyzerOutput/"+str(year)+"/DYToLL_M50_Pt250To400", "/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/analyzerOutput/"+str(year)+"/DY_lowmass", "/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/analyzerOutput/"+str(year)+"/DYToLL_M50_Pt650ToInf", "/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/analyzerOutput/"+str(year)+"/DYToLL_M50_Pt400To650"]
    direc = ["/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/analyzerOutput/"+str(year)+"/DY"]

df_elec = pd.DataFrame()
df_muon = pd.DataFrame()

def getcsvfromfile(fil):
    if os.path.getsize(fil) == 0:
        return -1 
    return pd.read_csv(fil, index_col = False)

for i in direc:
    dirs = os.listdir(i)
    print(i)
    elecfiles = [ i + '/' + f for f in filter(lambda x: x.endswith('_electrons.csv'),dirs)]
    mufiles = [ i + '/' + f for f in  filter(lambda x: x.endswith('_muons.csv'), dirs)]
    with closing(Pool(12)) as p:
        print("Now running " + str(len(elecfiles)) + " commands using: " + str(12) + " processes. Please wait")
        retlist1 = p.map_async(getcsvfromfile, elecfiles, 1)
        while not retlist1.ready():
                print("Runs left: {}".format(retlist1._number_left ))
                time.sleep(1)
        retlist1 = retlist1.get()
        p.close()
        p.join()
        p.terminate()

    print("Will now concatenate the electron results")
    for r in retlist1:
      if type(r) == type(-1): continue #Exception catching
      else:
        df_elec = pd.concat([df_elec, r], axis = 0)
        
    with closing(Pool(12)) as p:
        print("Now running " + str(len(mufiles)) + " commands using: " + str(12) + " processes. Please wait")
        retlist1 = p.map_async(getcsvfromfile, mufiles, 1)
        while not retlist1.ready():
                print("Runs left: {}".format(retlist1._number_left ))
                time.sleep(1)
        retlist1 = retlist1.get()
        p.close()
        p.join()
        p.terminate()

    print("Will now concatenate the muon results")
    for r in retlist1:
      if type(r) == type(-1): continue #Exception catching
      else:
        df_muon = pd.concat([df_muon, r], axis = 0)

pt_bins_muon = np.array([25.0, 40.0, 60.0, 90.0, 120.0, 160.0, 200.0])
pt_bins_muon_sub = np.array([10.0, 25.0, 40.0, 60.0, 90.0, 120.0, 160.0, 200.0])
eta_bins_muon = np.array([0.0, 0.9, 1.2, 2.1, 2.4])

#pt_bins_elec = np.array([25, 30, 35, 40, 45, 60, 120, 160, 200])
pt_bins_elec = np.array([25, 35, 45, 60, 120, 160, 200])
if year == 2015 or year == 2016:
    pt_bins_elec_forPOG = np.array([0., 30., 40., 50., 100., 200., 500.])
else:
    pt_bins_elec_forPOG = np.array([0., 33., 40., 50., 100., 200., 500.])

pt_bins_elec_sub = np.array([10, 25, 60, 120, 160, 200])
#eta_bins_elec = np.array([-2.5, -1.566, -1.444, -.6, 0.0, .6, 1.444, 1.566, 2.5])
eta_bins_elec = [-2.4, -2.0, -1.566, -1.4442, -0.8, 0, 0.8, 1.4442, 1.566, 2.0, 2.4]

def clopper_pearson(x, n, alpha=1-.682):
    b = scipy.stats.beta.ppf
    lo = b(alpha / 2, x, n - x + 1)
    hi = b(1 - alpha / 2, x + 1, n - x)
    div = float(x/n)
    return 0.0 if math.isnan(lo) else div-lo, 0.0 if math.isnan(hi) else hi-div

##################################################

# No Triggers Vs Single or Double Trigger in Eta ELECTRON
h1 = plt.hist2d(df_elec["LeadingPt"], df_elec["LeadingEta"], [pt_bins_elec_forPOG , eta_bins_elec])
h2 = plt.hist2d(df_elec[df_elec['SingleElecTrig'] > 0]["LeadingPt"], df_elec[df_elec['SingleElecTrig'] > 0]["LeadingEta"], [pt_bins_elec_forPOG , eta_bins_elec])

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

efficiencies_elec = np.asarray(efficiencies_elec)
up_elec = np.asarray(up_elec)
down_elec = np.asarray(down_elec)

# Plotting Single or Double Trigger in Eta / Everything 
plt.clf()
if isData:
    if year == 2015:
        plt.title(r'Electron Trigger Eff - 15.613 $fb^{-1}$')
    if year == 2016:
        plt.title(r'Electron Trigger Eff - 14.480 $fb^{-1}$')
    if year == 2017:
        plt.title(r'Electron Trigger Eff - 41.433 $fb^{-1}$')   
    if year == 2018:
        plt.title(r'Electron Trigger Eff - 48.353 $fb^{-1}$')
else:
    plt.title(r'Electron Trigger Eff')

plt.xlabel(r'Leading Electron $|\eta|$')
plt.ylabel('Leading Electron pT')
plt.pcolormesh(eta_bins_elec, pt_bins_elec_forPOG , efficiencies_elec, cmap = 'jet', vmin = 0, vmax = 1.0)
plt.colorbar()
for i in range(len(pt_bins_elec_forPOG )-1):
    for j in range(len(eta_bins_elec)-1):
        plt.text((eta_bins_elec[j]+eta_bins_elec[j+1])/2,(pt_bins_elec_forPOG [i]+pt_bins_elec_forPOG [i+1])/2, str(round(efficiencies_elec[i][j],3))+r'$\pm$'+str(round((up_elec[i][j]+down_elec[i][j])/2,2)), color="white", ha="center", va="center", fontweight="bold", size = 4.5, rotation=45)

if isData:
    plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/'+str(year)+'/MET_e_Eta.pdf')
else:
    plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/'+str(year)+'/DY_e_Eta.pdf')

#plt.show()

if isData:
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/eff_e_MET_Eta.csv", efficiencies_elec, delimiter=",")
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/up_e_MET_Eta.csv", up_elec, delimiter=",")
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/down_e_MET_Eta.csv", down_elec, delimiter=",")
else:
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/eff_e_DY_Eta.csv", efficiencies_elec, delimiter=",")
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/up_e_DY_Eta.csv", up_elec, delimiter=",")
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/down_e_DY_Eta.csv", down_elec, delimiter=",")

##################################################

# No Triggers Vs Single or Double Trigger in pT ELECTRON
h1 = plt.hist2d(df_elec["LeadingPt"], np.abs(df_elec["SubleadingPt"]), [pt_bins_elec, pt_bins_elec_sub])
h2 = plt.hist2d(df_elec[(df_elec['SingleElecTrig'] + df_elec['DoubleElecTrig']) > 0]["LeadingPt"], df_elec[(df_elec['SingleElecTrig'] + df_elec['DoubleElecTrig']) > 0]["SubleadingPt"], [pt_bins_elec, pt_bins_elec_sub])

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

efficiencies_elec = np.asarray(efficiencies_elec)
up_elec = np.asarray(up_elec)
down_elec = np.asarray(down_elec)

# Plotting Single or Double Trigger in pT / Everything
plt.clf()
if isData:
    if year == 2015:
        plt.title(r'Electron Trigger Eff - 15.613 $fb^{-1}$')
    if year == 2016:
        plt.title(r'Electron Trigger Eff - 14.480 $fb^{-1}$')
    if year == 2017:
        plt.title(r'Electron Trigger Eff - 41.433 $fb^{-1}$')   
    if year == 2018:
        plt.title(r'Electron Trigger Eff - 48.353 $fb^{-1}$')
else:
    plt.title(r'Electron Trigger Eff')

plt.xlabel(r'Subleading Electron pT')
plt.ylabel('Leading Electron pT')
plt.pcolormesh(pt_bins_elec_sub, pt_bins_elec, efficiencies_elec, cmap = 'jet', vmin = 0, vmax = 1.0)
plt.colorbar()
for i in range(len(pt_bins_elec)-1):
    for j in range(len(pt_bins_elec_sub)-1):
        plt.text((pt_bins_elec_sub[j]+pt_bins_elec_sub[j+1])/2,(pt_bins_elec[i]+pt_bins_elec[i+1])/2, str(round(efficiencies_elec[i][j],3))+r'$\pm$'+str(round((up_elec[i][j]+down_elec[i][j])/2,2)), color="white", ha="center", va="center", fontweight="bold", size = 4.5, rotation=45)

if isData:
    plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/'+str(year)+'/MET_e_Pt.pdf')
else:
    plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/'+str(year)+'/DY_e_Pt.pdf')

#plt.show()

if isData:
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/eff_e_MET_Pt.csv", efficiencies_elec, delimiter=",")
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/up_e_MET_Pt.csv", up_elec, delimiter=",")
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/down_e_MET_Pt.csv", down_elec, delimiter=",")
else:
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/eff_e_DY_Pt.csv", efficiencies_elec, delimiter=",")
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/up_e_DY_Pt.csv", up_elec, delimiter=",")
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/down_e_DY_Pt.csv", down_elec, delimiter=",")

##################################################

# MET Triggers Vs Single or Double Trigger in pT ELECTRON
df_elec_MET = df_elec[(df_elec['METTrig_a'] + df_elec['METTrig_b']) > 0]
h1 = plt.hist2d(df_elec_MET["LeadingPt"], np.abs(df_elec_MET["SubleadingPt"]), [pt_bins_elec, pt_bins_elec_sub])
h2 = plt.hist2d(df_elec_MET[(df_elec_MET['SingleElecTrig'] + df_elec_MET['DoubleElecTrig']) > 0]["LeadingPt"], df_elec_MET[(df_elec_MET['SingleElecTrig'] + df_elec_MET['DoubleElecTrig']) > 0]["SubleadingPt"], [pt_bins_elec, pt_bins_elec_sub])

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

efficiencies_elec = np.asarray(efficiencies_elec)
up_elec = np.asarray(up_elec)
down_elec = np.asarray(down_elec)

# Plotting Single or Double Trigger in pT / Everything
plt.clf()
if isData:
    if year == 2015:
        plt.title(r'Electron Trigger Eff (METTrig applied) - 15.613 $fb^{-1}$')
    if year == 2016:
        plt.title(r'Electron Trigger Eff (METTrig applied) - 14.480 $fb^{-1}$')
    if year == 2017:
        plt.title(r'Electron Trigger Eff (METTrig applied) - 41.433 $fb^{-1}$')   
    if year == 2018:
        plt.title(r'Electron Trigger Eff (METTrig applied) - 48.353 $fb^{-1}$')
else:
    plt.title(r'Electron Trigger Eff (METTrig applied)')

plt.xlabel(r'Subleading Electron pT')
plt.ylabel('Leading Electron pT')
plt.pcolormesh(pt_bins_elec_sub, pt_bins_elec, efficiencies_elec, cmap = 'jet', vmin = 0, vmax = 1.0)
plt.colorbar()
for i in range(len(pt_bins_elec)-1):
    for j in range(len(pt_bins_elec_sub)-1):
        plt.text((pt_bins_elec_sub[j]+pt_bins_elec_sub[j+1])/2,(pt_bins_elec[i]+pt_bins_elec[i+1])/2, str(round(efficiencies_elec[i][j],3))+r'$\pm$'+str(round((up_elec[i][j]+down_elec[i][j])/2,2)), color="white", ha="center", va="center", fontweight="bold", size = 4.5, rotation=45)

if isData:
    plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/'+str(year)+'/MET_e_METTrig.pdf')
else:
    plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/'+str(year)+'/DY_e_METTrig.pdf')

#plt.show()

if isData:
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/eff_e_MET_METTrig.csv", efficiencies_elec, delimiter=",")
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/up_e_MET_METTrig.csv", up_elec, delimiter=",")
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/down_e_MET_METTrig.csv", down_elec, delimiter=",")
else:
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/eff_e_DY_METTrig.csv", efficiencies_elec, delimiter=",")
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/up_e_DY_METTrig.csv", up_elec, delimiter=",")
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/down_e_DY_METTrig.csv", down_elec, delimiter=",")

##################################################

# No Triggers Vs Single or Double Trigger in Eta MUON
h1 = plt.hist2d(df_muon["LeadingPt"], df_muon["LeadingEta"], [pt_bins_muon, eta_bins_muon])
h2 = plt.hist2d(df_muon[df_muon['SingleMuonTrig'] > 0]["LeadingPt"], df_muon[df_muon['SingleMuonTrig'] > 0]["LeadingEta"], [pt_bins_muon, eta_bins_muon])

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

efficiencies_muon = np.asarray(efficiencies_muon)
up_muon = np.asarray(up_muon)
down_muon = np.asarray(down_muon)

# Plotting Single or Double Trigger in Eta / Everything
plt.clf()
if isData:
    if year == 2015:
        plt.title(r'Muon Trigger Eff - 15.613 $fb^{-1}$')
    if year == 2016:
        plt.title(r'Muon Trigger Eff - 14.480 $fb^{-1}$')
    if year == 2017:
        plt.title(r'Muon Trigger Eff - 41.433 $fb^{-1}$')   
    if year == 2018:
        plt.title(r'Muon Trigger Eff - 48.353 $fb^{-1}$')
else:
    plt.title(r'Muon Trigger Eff')

plt.xlabel(r'Leading Muon $|\eta|$')
plt.ylabel('Leading Muon pT')
plt.pcolormesh(eta_bins_muon, pt_bins_muon, efficiencies_muon, cmap = 'jet', vmin = 0, vmax = 1.0)
plt.colorbar()
for i in range(len(pt_bins_muon)-1):
    for j in range(len(eta_bins_muon)-1):
        plt.text((eta_bins_muon[j]+eta_bins_muon[j+1])/2,(pt_bins_muon[i]+pt_bins_muon[i+1])/2, str(round(efficiencies_muon[i][j],3))+r'$\pm$'+str(round((up_muon[i][j]+down_muon[i][j])/2,2)), color="white", ha="center", va="center", fontweight="bold", size = 4.5, rotation=45)

if isData:
    plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/'+str(year)+'/MET_m_Eta.pdf')
else:
    plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/'+str(year)+'/DY_m_Eta.pdf')

#plt.show()

if isData:
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/eff_m_MET_Eta.csv", efficiencies_muon, delimiter=",")
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/up_m_MET_Eta.csv", up_muon, delimiter=",")
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/down_m_MET_Eta.csv", down_muon, delimiter=",")
else:
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/eff_m_DY_Eta.csv", efficiencies_muon, delimiter=",")
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/up_m_DY_Eta.csv", up_muon, delimiter=",")
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/down_m_DY_Eta.csv", down_muon, delimiter=",")

##################################################

# No Triggers Vs Single or Double Trigger in pT MUON
h1 = plt.hist2d(df_muon["LeadingPt"], np.abs(df_muon["SubleadingPt"]), [pt_bins_muon, pt_bins_muon_sub])
h2 = plt.hist2d(df_muon[(df_muon['SingleMuonTrig'] + df_muon['DoubleMuonTrig']) > 0]["LeadingPt"], df_muon[(df_muon['SingleMuonTrig'] + df_muon['DoubleMuonTrig']) > 0]["SubleadingPt"], [pt_bins_muon, pt_bins_muon_sub])

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

efficiencies_muon = np.asarray(efficiencies_muon)
up_muon = np.asarray(up_muon)
down_muon = np.asarray(down_muon)

# Plotting Single or Double Trigger in pT / Everything
plt.clf()
if isData:
    if year == 2015:
        plt.title(r'Muon Trigger Eff - 15.613 $fb^{-1}$')
    if year == 2016:
        plt.title(r'Muon Trigger Eff - 14.480 $fb^{-1}$')
    if year == 2017:
        plt.title(r'Muon Trigger Eff - 41.433 $fb^{-1}$')   
    if year == 2018:
        plt.title(r'Muon Trigger Eff - 48.353 $fb^{-1}$')
else:
    plt.title(r'Muon Trigger Eff')

plt.xlabel(r'Subleading Muon pT')
plt.ylabel('Leading Muon pT')
plt.pcolormesh(pt_bins_muon_sub, pt_bins_muon, efficiencies_muon, cmap = 'jet', vmin = 0, vmax = 1.0)
plt.colorbar()
for i in range(len(pt_bins_muon)-1):
    for j in range(len(pt_bins_muon_sub)-1):
        plt.text((pt_bins_muon_sub[j]+pt_bins_muon_sub[j+1])/2,(pt_bins_muon[i]+pt_bins_muon[i+1])/2, str(round(efficiencies_muon[i][j],3))+r'$\pm$'+str(round((up_muon[i][j]+down_muon[i][j])/2,2)), color="white", ha="center", va="center", fontweight="bold", size = 4.5, rotation=45)

if isData:
    plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/'+str(year)+'/MET_m_Pt.pdf')
else:
    plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/'+str(year)+'/DY_m_Pt.pdf')

#plt.show()

if isData:
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/eff_m_MET_Pt.csv", efficiencies_muon, delimiter=",")
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/up_m_MET_Pt.csv", up_muon, delimiter=",")
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/down_m_MET_Pt.csv", down_muon, delimiter=",")
else:
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/eff_m_DY_Pt.csv", efficiencies_muon, delimiter=",")
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/up_m_DY_Pt.csv", up_muon, delimiter=",")
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/down_m_DY_Pt.csv", down_muon, delimiter=",")

##################################################

# MET Triggers Vs Single or Double Trigger in pT Muon
df_muon_MET = df_muon[(df_muon['METTrig_a'] + df_muon['METTrig_b']) > 0]
h1 = plt.hist2d(df_muon_MET["LeadingPt"], np.abs(df_muon_MET["SubleadingPt"]), [pt_bins_muon, pt_bins_muon_sub])
h2 = plt.hist2d(df_muon_MET[(df_muon_MET['SingleMuonTrig'] + df_muon_MET['DoubleMuonTrig']) > 0]["LeadingPt"], df_muon_MET[(df_muon_MET['SingleMuonTrig'] + df_muon_MET['DoubleMuonTrig']) > 0]["SubleadingPt"], [pt_bins_muon, pt_bins_muon_sub])

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

efficiencies_muon = np.asarray(efficiencies_muon)
up_muon = np.asarray(up_muon)
down_muon = np.asarray(down_muon)

# Plotting Single or Double Trigger in pT / Everything
plt.clf()
if isData:
    if year == 2015:
        plt.title(r'Muon Trigger Eff (METTrig applied) - 15.613 $fb^{-1}$')
    if year == 2016:
        plt.title(r'Muon Trigger Eff (METTrig applied) - 14.480 $fb^{-1}$')
    if year == 2017:
        plt.title(r'Muon Trigger Eff (METTrig applied) - 41.433 $fb^{-1}$')   
    if year == 2018:
        plt.title(r'Muon Trigger Eff (METTrig applied) - 48.353 $fb^{-1}$')
else:
    plt.title(r'Muon Trigger Eff (METTrig applied)')

plt.xlabel(r'Subleading Muon pT')
plt.ylabel('Leading Muon pT')
plt.pcolormesh(pt_bins_muon_sub, pt_bins_muon, efficiencies_muon, cmap = 'jet', vmin = 0, vmax = 1.0)
plt.colorbar()
for i in range(len(pt_bins_muon)-1):
    for j in range(len(pt_bins_muon_sub)-1):
        plt.text((pt_bins_muon_sub[j]+pt_bins_muon_sub[j+1])/2,(pt_bins_muon[i]+pt_bins_muon[i+1])/2, str(round(efficiencies_muon[i][j],3))+r'$\pm$'+str(round((up_muon[i][j]+down_muon[i][j])/2,2)), color="white", ha="center", va="center", fontweight="bold", size = 4.5, rotation=45)

if isData:
    plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/'+str(year)+'/MET_m_METTrig.pdf')
else:
    plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/'+str(year)+'/DY_m_METTrig.pdf')

#plt.show()

if isData:
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/eff_m_MET_METTrig.csv", efficiencies_muon, delimiter=",")
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/up_m_MET_METTrig.csv", up_muon, delimiter=",")
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/down_m_MET_METTrig.csv", down_muon, delimiter=",")
else:
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/eff_m_DY_METTrig.csv", efficiencies_muon, delimiter=",")
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/up_m_DY_METTrig.csv", up_muon, delimiter=",")
    np.savetxt("/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/"+str(year)+"/down_m_DY_METTrig.csv", down_muon, delimiter=",")

##################################################
