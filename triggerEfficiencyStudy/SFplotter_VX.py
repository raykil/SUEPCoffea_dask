import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

year = int(sys.argv[1])
plot = str(sys.argv[2])

dy_eff_elec = np.genfromtxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/'+str(year)+'/eff_e_DY_'+plot+'.csv',delimiter = ',')
MET_eff_elec = np.genfromtxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/'+str(year)+'/eff_e_MET_'+plot+'.csv',delimiter = ',')
dy_up_elec = np.genfromtxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/'+str(year)+'/up_e_DY_'+plot+'.csv',delimiter = ',')
MET_up_elec = np.genfromtxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/'+str(year)+'/up_e_MET_'+plot+'.csv',delimiter = ',')
dy_down_elec = np.genfromtxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/'+str(year)+'/down_e_DY_'+plot+'.csv',delimiter = ',')
MET_down_elec = np.genfromtxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/'+str(year)+'/down_e_MET_'+plot+'.csv',delimiter = ',')

dy_eff_muon = np.genfromtxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/'+str(year)+'/eff_m_DY_'+plot+'.csv',delimiter = ',')
MET_eff_muon = np.genfromtxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/'+str(year)+'/eff_m_MET_'+plot+'.csv',delimiter = ',')
dy_up_muon = np.genfromtxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/'+str(year)+'/up_m_DY_'+plot+'.csv',delimiter = ',')
MET_up_muon = np.genfromtxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/'+str(year)+'/up_m_MET_'+plot+'.csv',delimiter = ',')
dy_down_muon = np.genfromtxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/'+str(year)+'/down_m_DY_'+plot+'.csv',delimiter = ',')
MET_down_muon = np.genfromtxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/triggerEffs/'+str(year)+'/down_m_MET_'+plot+'.csv',delimiter = ',')


pt_bins_muon = np.array([25.0, 40.0, 60.0, 90.0, 120.0, 160.0, 200.0])
pt_bins_muon_sub = np.array([10.0, 25.0, 40.0, 60.0, 90.0, 120.0, 160.0, 200.0])
eta_bins_muon = np.array([0.0, 0.9, 1.2, 2.1, 2.4])

#pt_bins_elec = np.array([25, 30, 35, 40, 45, 60, 120, 160, 200])
pt_bins_elec = np.array([25, 35, 45, 60, 120, 160, 200])
pt_bins_elec_sub = np.array([10, 25, 60, 120, 160, 200])
#eta_bins_elec = np.array([-2.5, -1.566, -1.444, -.6, 0.0, .6, 1.444, 1.566, 2.5])
eta_bins_elec = np.array([-2.4, -2.0, -1.566, -1.4442, -0.8, 0, 0.8, 1.4442, 1.566, 2.0, 2.4])

if plot == 'Eta':
    if year == 2015 or year == 2016:
        pt_bins_elec = np.array([0., 30., 40., 50., 100., 200., 500.])
    else:
        pt_bins_elec = np.array([0., 33., 40., 50., 100., 200., 500.])

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

if plot == 'Pt' or plot == 'METTrig':
    plt.clf()
    if plot == 'METTrig':
        plt.title('Electron SFs (METTrig Applied)')
    else:
        plt.title('Electron SFs')
    plt.xlabel('Subleading Electron pT')
    plt.ylabel('Leading Electron pT')
    plt.pcolormesh(pt_bins_elec_sub, pt_bins_elec, efficiencies_elec, cmap = 'jet', vmin = 0, vmax = 1.0)
    plt.colorbar()
    for i in range(len(pt_bins_elec)-1):
        for j in range(len(pt_bins_elec_sub)-1):
            plt.text((pt_bins_elec_sub[j]+pt_bins_elec_sub[j+1])/2,(pt_bins_elec[i]+pt_bins_elec[i+1])/2, str(round(efficiencies_elec[i][j],3))+r'$\pm$'+str(round((up_elec[i][j]+down_elec[i][j])/2,2)), color="white", ha="center", va="center", fontweight="bold", size = 4.5, rotation=45)
    #plt.show()
    plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/'+str(year)+'/SF_e_'+plot+'.pdf')

    np.savetxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/'+str(year)+'/SF_e_'+plot+'.csv',np.array(efficiencies_elec).flatten('F'), delimiter = ',', fmt='%.14f')
    np.savetxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/'+str(year)+'/SF_e_up_'+plot+'.csv',np.array(up_elec).flatten('F'), delimiter = ',', fmt='%.14f')
    np.savetxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/'+str(year)+'/SF_e_down_'+plot+'.csv',np.array(down_elec).flatten('F'), delimiter = ',', fmt='%.14f')

    plt.clf()
    plt.title('Muon SFs')
    plt.xlabel('Subleading Muon pT')
    plt.ylabel('Leading Muon pT')
    print(pt_bins_muon_sub)
    print(pt_bins_muon)
    print(efficiencies_muon)
    plt.pcolormesh(pt_bins_muon_sub, pt_bins_muon, efficiencies_muon, cmap = 'jet', vmin = 0, vmax = 1.0)
    plt.colorbar()
    for i in range(len(pt_bins_muon)-1):
        for j in range(len(pt_bins_muon_sub)-1):
            plt.text((pt_bins_muon_sub[j]+pt_bins_muon_sub[j+1])/2,(pt_bins_muon[i]+pt_bins_muon[i+1])/2, str(round(efficiencies_muon[i][j],3))+r'$\pm$'+str(round((up_muon[i][j]+down_muon[i][j])/2,2)), color="white", ha="center", va="center", fontweight="bold", size = 4.5, rotation=45)
    #plt.show()
    plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/'+str(year)+'/SF_m_'+plot+'.pdf')

    np.savetxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/'+str(year)+'/SF_m_'+plot+'.csv',np.array(efficiencies_muon).flatten('F'), delimiter = ',', fmt='%.14f')
    np.savetxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/'+str(year)+'/SF_m_up_'+plot+'.csv',np.array(up_muon).flatten('F'), delimiter = ',', fmt='%.14f')
    np.savetxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/'+str(year)+'/SF_m_down_'+plot+'.csv',np.array(down_muon).flatten('F'), delimiter = ',', fmt='%.14f')

if plot == 'Eta':
    plt.clf()
    plt.title('Electron SFs')
    plt.xlabel(r'Leading Electron $\eta$')
    plt.ylabel('Leading Electron pT')
    for i in efficiencies_elec:
        print(i)
    plt.pcolormesh(eta_bins_elec, pt_bins_elec, efficiencies_elec, cmap = 'jet', vmin = 0, vmax = 1.0)
    plt.colorbar()
    for i in range(len(pt_bins_elec)-1):
        for j in range(len(eta_bins_elec)-1):
            plt.text((eta_bins_elec[j]+eta_bins_elec[j+1])/2,(pt_bins_elec[i]+pt_bins_elec[i+1])/2, str(round(efficiencies_elec[i][j],3))+r'$\pm$'+str(round((up_elec[i][j]+down_elec[i][j])/2,2)), color="white", ha="center", va="center", fontweight="bold", size = 4.5, rotation=45)
    #plt.show()
    plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/'+str(year)+'/SF_e_'+plot+'.pdf')

    np.savetxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/'+str(year)+'/SF_e_'+plot+'.csv',np.array(efficiencies_elec).flatten('F'), delimiter = ',', fmt='%.14f')
    np.savetxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/'+str(year)+'/SF_e_up_'+plot+'.csv',np.array(up_elec).flatten('F'), delimiter = ',', fmt='%.14f')
    np.savetxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/'+str(year)+'/SF_e_down_'+plot+'.csv',np.array(down_elec).flatten('F'), delimiter = ',', fmt='%.14f')

    plt.clf()
    plt.title('Muon SFs')
    plt.xlabel('Subleading Muon pT')
    plt.ylabel('Leading Muon pT')
    plt.pcolormesh(eta_bins_muon, pt_bins_muon, efficiencies_muon, cmap = 'jet', vmin = 0, vmax = 1.0)
    plt.colorbar()
    for i in range(len(pt_bins_muon)-1):
        for j in range(len(eta_bins_muon)-1):
            plt.text((eta_bins_muon[j]+eta_bins_muon[j+1])/2,(pt_bins_muon[i]+pt_bins_muon[i+1])/2, str(round(efficiencies_muon[i][j],3))+r'$\pm$'+str(round((up_muon[i][j]+down_muon[i][j])/2,2)), color="white", ha="center", va="center", fontweight="bold", size = 4.5, rotation=45)
    #plt.show()
    plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/'+str(year)+'/SF_m_'+plot+'.pdf')

    np.savetxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/'+str(year)+'/SF_m_'+plot+'.csv',np.array(efficiencies_muon).flatten('F'), delimiter = ',', fmt='%.14f')
    np.savetxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/'+str(year)+'/SF_m_up_'+plot+'.csv',np.array(up_muon).flatten('F'), delimiter = ',', fmt='%.14f')
    np.savetxt('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/SFs/'+str(year)+'/SF_m_down_'+plot+'.csv',np.array(down_muon).flatten('F'), delimiter = ',', fmt='%.14f')