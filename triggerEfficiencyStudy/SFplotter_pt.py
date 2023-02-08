import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dy_eff_elec = np.genfromtxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/2016APV/eff_e_DY_pt.csv',delimiter = ',')
MET_eff_elec = np.genfromtxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/2016APV/eff_e_MET_pt.csv',delimiter = ',')
dy_up_elec = np.genfromtxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/2016APV/up_e_DY_pt.csv',delimiter = ',')
MET_up_elec = np.genfromtxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/2016APV/up_e_MET_pt.csv',delimiter = ',')
dy_down_elec = np.genfromtxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/2016APV/down_e_DY_pt.csv',delimiter = ',')
MET_down_elec = np.genfromtxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/2016APV/down_e_MET_pt.csv',delimiter = ',')

dy_eff_muon = np.genfromtxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/2016APV/eff_mu_DY_pt.csv',delimiter = ',')
MET_eff_muon = np.genfromtxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/2016APV/eff_mu_MET_pt.csv',delimiter = ',')
dy_up_muon = np.genfromtxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/2016APV/up_mu_DY_pt.csv',delimiter = ',')
MET_up_muon = np.genfromtxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/2016APV/up_mu_MET_pt.csv',delimiter = ',')
dy_down_muon = np.genfromtxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/2016APV/down_mu_DY_pt.csv',delimiter = ',')
MET_down_muon = np.genfromtxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/2016APV/down_mu_MET_pt.csv',delimiter = ',')

pt_bins_muons = np.array([25.0, 60.0, 120.0, 200.0])
pt_bins_muons_2 = np.array([25.0, 40.0, 60.0, 90.0, 120.0, 160.0, 200.0])
pt_bins_muons_sub = np.array([10.0, 25.0, 40.0, 60.0, 90.0, 120.0, 160.0, 200.0])

pt_bins_elec = np.array([25, 60, 120, 200])
pt_bins_elec_2 = np.array([25, 60, 120, 160, 200])
pt_bins_elec_sub = np.array([10, 25, 60, 120, 160, 200])


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
            temp_down.append((MET_eff_elec[i][j]/dy_eff_elec[i][j])*np.sqrt((dy_down_elec[i][j]/dy_eff_elec[i][j])**(2) + (MET_down_elec[i][j]/MET_eff_elec[i][j])**(2)))
    efficiencies_elec.append(temp_eff)
    up_elec.append(temp_up)
    down_elec.append(temp_down)

efficiencies_muon = []
up_muon = []
down_muon = []
for i in range(len(dy_eff_muon)):
    temp_eff = []
    temp_up = []
    temp_down = []
    for j in range(len(dy_eff_muon[0])):
        if(dy_eff_muon[i][j] == 0 or MET_eff_muon[i][j] == 0):
            temp_eff.append(0.0)
            temp_up.append(0.0)
            temp_down.append(0.0)
        else:
            temp_eff.append(MET_eff_muon[i][j]/dy_eff_muon[i][j])
            temp_up.append((MET_eff_muon[i][j]/dy_eff_muon[i][j])*np.sqrt((dy_up_muon[i][j]/dy_eff_muon[i][j])**(2) + (MET_up_muon[i][j]/MET_eff_muon[i][j])**(2)))
            temp_down.append((MET_eff_muon[i][j]/dy_eff_muon[i][j])*np.sqrt((dy_down_muon[i][j]/dy_eff_muon[i][j])**(2) + (MET_down_muon[i][j]/MET_eff_muon[i][j])**(2)))
    efficiencies_muon.append(temp_eff)
    up_muon.append(temp_up)
    down_muon.append(temp_down)

plt.clf()
plt.title('Electron SFs')
plt.xlabel('Subleading Electron pT')
plt.ylabel('Leading Electron pT')
plt.pcolormesh(pt_bins_elec_sub, pt_bins_elec_2, efficiencies_elec, cmap = 'jet', vmin = 0, vmax = 1.0)
plt.colorbar()
for i in range(len(pt_bins_elec_2)-1):
    for j in range(len(pt_bins_elec_sub)-1):
        plt.text((pt_bins_elec_sub[j]+pt_bins_elec_sub[j+1])/2,(pt_bins_elec_2[i]+pt_bins_elec_2[i+1])/2, str(round(efficiencies_elec[i][j],3))+r'$\pm$'+str(round((up_elec[i][j]+down_elec[i][j])/2,2)), color="w", ha="center", va="center", fontweight="bold", size = 4.5, rotation=45)
#plt.show()
plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/2016APV/SF_elec.pdf')
plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/2016APV/SF_elec.png', dpi = 2000)
#np.savetxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/2016APV/SF_val_elec.csv',np.flip(efficiencies_elec, axis = 0) , delimiter = ',')
#np.savetxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/2016APV/SF_up_elec.csv',np.flip(up_elec, axis = 0), delimiter = ',')
#np.savetxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/2016APV/SF_down_elec.csv',np.flip(up_elec, axis = 0), delimiter = ',')

plt.clf()
plt.title('Muon SFs')
plt.xlabel('Subleading Muon pT')
plt.ylabel('Leading Muon pT')
plt.pcolormesh(pt_bins_muons_sub, pt_bins_muons_2, efficiencies_muon, cmap = 'jet', vmin = 0, vmax = 1.0)
plt.colorbar()
for i in range(len(pt_bins_muons_2)-1):
    for j in range(len(pt_bins_muons_sub)-1):
        plt.text((pt_bins_muons_sub[j]+pt_bins_muons_sub[j+1])/2,(pt_bins_muons_2[i]+pt_bins_muons_2[i+1])/2, str(round(efficiencies_muon[i][j],3))+r'$\pm$'+str(round((up_muon[i][j]+down_muon[i][j])/2,2)), color="w", ha="center", va="center", fontweight="bold", size = 4.5, rotation=45)
#plt.show()
plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/2016APV/SF_muon.pdf')
plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/2016APV/SF_muon.png', dpi = 2000)
#np.savetxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/2016APV/SF_val_muon.csv',np.flip(efficiencies_muon, axis = 0) , delimiter = ',')
#np.savetxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/2016APV/SF_up_muon.csv',np.flip(up_muon, axis = 0), delimiter = ',')
#np.savetxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/2016APV/SF_down_muon.csv',np.flip(up_muon, axis = 0), delimiter = ',')

np.savetxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/2016APV/SF_e_pt.csv',np.array(efficiencies_elec).flatten('F'), delimiter = ',', fmt='%.14f')
np.savetxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/2016APV/SF_m_pt.csv',np.array(efficiencies_muon).flatten('F'), delimiter = ',', fmt='%.14f')
np.savetxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/2016APV/SF_e_up_pt.csv',np.array(up_elec).flatten('F'), delimiter = ',', fmt='%.14f')
np.savetxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/2016APV/SF_m_up_pt.csv',np.array(up_muon).flatten('F'), delimiter = ',', fmt='%.14f')
np.savetxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/2016APV/SF_e_down_pt.csv',np.array(down_elec).flatten('F'), delimiter = ',', fmt='%.14f')
np.savetxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/2016APV/SF_m_down_pt.csv',np.array(down_muon).flatten('F'), delimiter = ',', fmt='%.14f')
