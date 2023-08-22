import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


temps = np.around(np.linspace(.3, 7.3, 10)[1:], decimals = 2)

LC_ntracks, LC_ntracks_4, LC_ntracks_8 = [], [], []
LJ_pt, LJ_pt_4, LJ_pt_8  = [], [], []
Nevents, Nevents_4, Nevents_8 = [], [], []

for i in range(1,10):
    file = pd.read_hdf('mD2/Batch'+str(i)+'/out_1_1_1001.hdf5')
    LC_ntracks.append(file["leadcluster_ntracks"])
    LJ_pt.append(file["leadjet_pt"])
    Nevents.append(len(file["leadjet_pt"]))

for i in range(1,10):
    file = pd.read_hdf('mD4/Batch'+str(i)+'/out_1_1_1001.hdf5')
    LC_ntracks_4.append(file["leadcluster_ntracks"])
    LJ_pt_4.append(file["leadjet_pt"])
    Nevents_4.append(len(file["leadjet_pt"]))

for i in range(1,10):
    file = pd.read_hdf('mD8/Batch'+str(i)+'/out_1_1_1001.hdf5')
    LC_ntracks_8.append(file["leadcluster_ntracks"])
    LJ_pt_8.append(file["leadjet_pt"])
    Nevents_8.append(len(file["leadjet_pt"]))

cumulativeArrays, cumulativeArrays_4, cumulativeArrays_8 = [], [], []
xbins = [0,10,20,25,30,35,40,45,50,55,60]
ybins = [0, 100, 250, 1000]

for i in range(9):
    h = plt.hist2d(LC_ntracks[i], LJ_pt[i], bins = (100, 100), range=np.array([(0, 100), (0, 1000)]))
    plt.colorbar(h[3])
    plt.xlim(0,100)
    plt.ylim(0,1000)
    plt.text(60, 800, 'NEvents in SR: ' + str(Nevents[i]), color = 'w')
    plt.axhline(y=100,linewidth=2, linestyle = '--', color = 'w')
    plt.axhline(y=250,linewidth=2, linestyle = '--', color = 'w')
    plt.axvline(x=20,linewidth=2, linestyle = '--', color = 'w')
    plt.axvline(x=10,linewidth=2, linestyle = '--', color = 'w')
    plt.xlabel(r'Lead Cluster $N^{SUEP}_{Tracks}$')
    plt.ylabel(r'Lead Ak4 Jet $p_T$')
    plt.title(r"Generic (30k) $m_D = 2\;GeV\;T_D = $"+str(temps[i])+r"$\;GeV$ (SR)")
    plt.savefig("ABCD/temp"+str(temps[i])+".png")

    plt.clf()

    h = plt.hist2d(LC_ntracks[i], LJ_pt[i], bins = (xbins, ybins))

    plt.clf()

    cumulativeArrays.append(h[0])
    
    h = plt.hist2d(LC_ntracks_4[i], LJ_pt_4[i], bins = (xbins, ybins))

    plt.clf()

    cumulativeArrays_4.append(h[0])
    
    h = plt.hist2d(LC_ntracks_8[i], LJ_pt_8[i], bins = (xbins, ybins))

    plt.clf()

    cumulativeArrays_8.append(h[0])

Sidebands = [['C2', 'D2', 'E2'], ['C1', 'D1', 'E1'], ['A', 'B1', 'B2']]

def plotter(data, data_4, data_8, xbin, ybin):
    data = np.stack(data).astype(None)
    selectedData, selectedData_4, selectedData_8  = [], [], []
    for i in data:
        selectedData.append(i[xbin][ybin])
    for i in data_4:
        selectedData_4.append(i[xbin][ybin])
    for i in data_8:
        selectedData_8.append(i[xbin][ybin])
    plt.plot(temps, selectedData, label = r'$m_D = 2$')
    plt.plot(temps, selectedData_4, label = r'$m_D = 4$')
    plt.plot(temps, selectedData_8, label = r'$m_D = 8$')
    plt.ylabel('Counts')
    plt.xlabel(r'$T_D$')
    plt.title(r'1D Projection of $T_D$ - AK4 $p_T\in[$'+str(ybins[ybin])+','+str(ybins[ybin+1])+r'$]$ - $N^{SUEP}_{Tracks}\in[$'+str(xbins[xbin])+','+str(xbins[xbin+1])+r'$]$ ('+Sidebands[xbin][ybin]+')')
    plt.legend()
    plt.savefig('plots/TDProjection_'+Sidebands[xbin][ybin]+'.png')
    plt.clf()

for i in range(len(Sidebands)):
    for j in range(len(Sidebands[i])):
        plotter(cumulativeArrays, cumulativeArrays_4, cumulativeArrays_8, i, j)
