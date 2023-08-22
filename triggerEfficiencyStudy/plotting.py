import ROOT
import matplotlib.pyplot as plt
f = ROOT.TFile("Riccardo_egammaTriggerEfficiency_2016_20200422.root")
bin_35, bin_45, bin_75, bin_150, bin_350 = [], [], [], [], []

graph = f.Get("grSF1D_1")
for i in range(graph.GetN()):
    bin_35.append((graph.GetErrorX(i), graph.GetErrorY(i), graph.GetPointX(i), graph.GetPointY(i)))
    print(graph.GetErrorX(i))    
    print(graph.GetErrorY(i))
    print(graph.GetPointX(i))
    print(graph.GetPointY(i))
    print()
bin_35 = sorted(bin_35, key = lambda x: x[2])

graph = f.Get("grSF1D_2")
for i in range(graph.GetN()):
    bin_45.append((graph.GetErrorX(i), graph.GetErrorY(i), graph.GetPointX(i), graph.GetPointY(i)))
    print(graph.GetErrorX(i))    
    print(graph.GetErrorY(i))
    print(graph.GetPointX(i))
    print(graph.GetPointY(i))
    print()
bin_45 = sorted(bin_45, key = lambda x: x[2])

graph = f.Get("grSF1D_3")
for i in range(graph.GetN()):
    bin_75.append((graph.GetErrorX(i), graph.GetErrorY(i), graph.GetPointX(i), graph.GetPointY(i)))
    print(graph.GetErrorX(i))    
    print(graph.GetErrorY(i))
    print(graph.GetPointX(i))
    print(graph.GetPointY(i))
    print()
bin_75 = sorted(bin_75, key = lambda x: x[2])

graph = f.Get("grSF1D_4")
for i in range(graph.GetN()):
    bin_150.append((graph.GetErrorX(i), graph.GetErrorY(i), graph.GetPointX(i), graph.GetPointY(i)))
    print(graph.GetErrorX(i))    
    print(graph.GetErrorY(i))
    print(graph.GetPointX(i))
    print(graph.GetPointY(i))
    print()
bin_150 = sorted(bin_150, key = lambda x: x[2])

graph = f.Get("grSF1D_5")
for i in range(graph.GetN()):
    bin_350.append((graph.GetErrorX(i), graph.GetErrorY(i), graph.GetPointX(i), graph.GetPointY(i)))
    print(graph.GetErrorX(i))    
    print(graph.GetErrorY(i))
    print(graph.GetPointX(i))
    print(graph.GetPointY(i))
    print()
bin_350 = sorted(bin_350, key = lambda x: x[2])

eta_bins_elec = [-2.4, -2.0, -1.566, -1.4442, -0.8, 0, 0.8, 1.4442, 1.566, 2.0, 2.4]
colors =  ['r','g','b','c','m', 'y', 'k']
for i in range(5):
    temp_eta = []
    for b in [bin_35, bin_45, bin_75, bin_150]:
        temp_eta.append(b[i])
    j = (3.5 - i)/2
    plt.errorbar([35-j, 45-j, 75-j, 150-j], [x[3] for x in temp_eta],  yerr = ([x[1] for x in temp_eta], [x[1] for x in temp_eta]), xerr = ([5-j, 5-j, 25-j, 50-j], [5+j, 5+j, 25+j, 50+j]), fmt = 'o', label = str(eta_bins_elec[i])+r'$<\eta$<'+str(eta_bins_elec[i+1]), color = colors[i])
plt.xlabel(r'Center of $p_T$ Bin')
plt.ylabel('Scale Factor')
plt.title('Single Electron Tight 2016APV Comparison')
plt.legend(loc =(.5,.8),prop={'size': 6}, ncol = 2)
plt.ylim(.5,1.5)
plt.savefig('/eos/user/g/gdecastr/SUEPCoffea_dask/triggerEfficiencyStudy/finalResults/EGamma/2016APV_e_2.png', dpi = 2000)
plt.clf()

