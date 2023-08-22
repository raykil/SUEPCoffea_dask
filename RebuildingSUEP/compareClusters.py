import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

filenames = os.listdir('/eos/user/g/gdecastr/SUEPCoffea_dask/RebuildingSUEP/csvs_Private')

kT_files = [filename for filename in filenames if filename.endswith('kT.csv')]
Ak_files = [filename for filename in filenames if filename.endswith('Ak.csv')]
Strip_files = [filename for filename in filenames if filename.endswith('Strip.csv')]
Cam_files = [filename for filename in filenames if filename.endswith('Cambridge.csv')]


##### kT
kTFrames = []
for file in kT_files:
    df = pd.read_csv('/eos/user/g/gdecastr/SUEPCoffea_dask/RebuildingSUEP/csvs_Private/' + file)
    kTFrames.append(df)

combined_kT = pd.concat(kTFrames, ignore_index=True)

##### Cambridge
CamFrames = []
for file in Cam_files:
    df = pd.read_csv('/eos/user/g/gdecastr/SUEPCoffea_dask/RebuildingSUEP/csvs_Private/' + file)
    CamFrames.append(df)

combined_Cam = pd.concat(CamFrames, ignore_index=True)

##### AkT
AkFrames = []
for file in Ak_files:
    df = pd.read_csv('/eos/user/g/gdecastr/SUEPCoffea_dask/RebuildingSUEP/csvs_Private/' + file)
    AkFrames.append(df)

combined_Ak = pd.concat(AkFrames, ignore_index=True)

##### Strips
StripFrames = []
for file in Strip_files:
    df = pd.read_csv('/eos/user/g/gdecastr/SUEPCoffea_dask/RebuildingSUEP/csvs_Private/' + file)
    StripFrames.append(df)

combined_Strip = pd.concat(StripFrames, ignore_index=True)

plt.hist(combined_Ak['Ak20BetaRes'], bins = np.linspace(-.5,1,30), label = r'Ak $r = 2.0$', histtype='step', density = True)
plt.hist(combined_Cam['cambridge20BetaRes'], bins = np.linspace(-.5,1,30), label = r'Cambridge $r = 2.0$', histtype='step', density = True)
plt.hist(combined_Strip['Strip20BetaRes'], bins = np.linspace(-.5,1,30), label = r'Strip $\Delta\eta = 2.0$', density = True, histtype='step')
plt.hist(combined_kT['kT20BetaRes'], bins = np.linspace(-.5,1,30), label = r'kT $r = 2.0$', histtype='step', density = True)
plt.text(.2, 4.0, r"$r = 2.0:\;\mu$ = " + str(round(combined_Ak['Ak20BetaRes'].mean(),2)) + r', $M = $' + str(round(combined_Ak['Ak20BetaRes'].median(),2)) + r'$, \sigma$ = ' + str(round(combined_Ak['Ak20BetaRes'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(combined_Ak['Ak20BetaRes'].mean()/combined_Ak['Ak20BetaRes'].std(),2)), size = 8)
plt.text(.2, 3.75, r"$r = 2.0:\;\mu$ = " + str(round(combined_Cam['cambridge20BetaRes'].mean(),2)) + r', $M = $' + str(round(combined_Cam['cambridge20BetaRes'].median(),2)) + r'$, \sigma$ = ' + str(round(combined_Cam['cambridge20BetaRes'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(combined_Cam['cambridge20BetaRes'].mean()/combined_Cam['cambridge20BetaRes'].std(),2)), size = 8)
plt.text(.2, 3.5, r"Strip $\Delta\eta = 1.5:\;\mu$ = " + str(round(combined_Strip['Strip20BetaRes'].mean(),2)) + r', $M = $' + str(round(combined_Strip['Strip20BetaRes'].median(),2)) + r'$, \sigma$ = ' + str(round(combined_Strip['Strip20BetaRes'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(combined_Strip['Strip20BetaRes'].mean()/combined_Strip['Strip20BetaRes'].std(),2)), size = 8)
plt.text(.2, 3.25, r"$r = 2.0:\;\mu$ = " + str(round(combined_kT['kT20BetaRes'].mean(),2)) + r', $M = $' + str(round(combined_kT['kT20BetaRes'].median(),2)) + r'$, \sigma$ = ' + str(round(combined_kT['kT20BetaRes'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(combined_kT['kT20BetaRes'].mean()/combined_kT['kT20BetaRes'].std(),2)), size = 8)
plt.title(r'$\beta$ resolution between Cluster and Gen Higgs for Various Algorithms')
plt.xlabel(r'$\frac{\beta_{Ak} - \beta_{Gen}}{\beta_{Gen}}$')
plt.ylabel('Frequency')
plt.legend()
plt.xlim(-.5,1)
plt.savefig('/eos/user/g/gdecastr/www/JetAlgorithms_Comparison_Private/BetaRes.png')

plt.clf()

plt.hist(combined_Ak['LeadingAk20Eff'], bins = np.linspace(0,1,30), label = r'Ak $r = 2.0$', histtype='step', density = True)
plt.hist(combined_Cam['Leadingcambridge20Eff'], bins = np.linspace(0,1,30), label = r'Cambridge $r = 2.0$', histtype='step', density = True)
plt.hist(combined_Strip['Strip20Eff'], bins = np.linspace(0,1,30), label = r'Strip $\Delta\eta = 2.0$', density = True, histtype='step')
plt.hist(combined_kT['LeadingkT20Eff'], bins = np.linspace(0,1,30), label = r'kT $r = 2.0$', histtype='step', density = True)
plt.text(.2, 10.0, r"$r = 2.0:\;\mu$ = " + str(round(combined_Cam['Leadingcambridge20Eff'].mean(),2)) + r', $M = $' + str(round(combined_Cam['Leadingcambridge20Eff'].median(),2)) + r'$, \sigma$ = ' + str(round(combined_Cam['Leadingcambridge20Eff'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(combined_Cam['Leadingcambridge20Eff'].mean()/combined_Cam['Leadingcambridge20Eff'].std(),2)), size = 8)
plt.text(.2, 9.0, r"$r = 2.0:\;\mu$ = " + str(round(combined_Ak['LeadingAk20Eff'].mean(),2)) + r', $M = $' + str(round(combined_Ak['LeadingAk20Eff'].median(),2)) + r'$, \sigma$ = ' + str(round(combined_Ak['LeadingAk20Eff'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(combined_Ak['LeadingAk20Eff'].mean()/combined_Ak['LeadingAk20Eff'].std(),2)), size = 8)
plt.text(.2, 8.0, r"Strip $\Delta\eta = 1.5:\;\mu$ = " + str(round(combined_Strip['Strip20Eff'].mean(),2)) + r', $M = $' + str(round(combined_Strip['Strip20Eff'].median(),2)) + r'$, \sigma$ = ' + str(round(combined_Strip['Strip20Eff'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(combined_Strip['Strip20Eff'].mean()/combined_Strip['Strip20Eff'].std(),2)), size = 8)
plt.text(.2, 7.0, r"$r = 2.0:\;\mu$ = " + str(round(combined_kT['LeadingkT20Eff'].mean(),2)) + r', $M = $' + str(round(combined_kT['LeadingkT20Eff'].median(),2)) + r'$, \sigma$ = ' + str(round(combined_kT['LeadingkT20Eff'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(combined_kT['LeadingkT20Eff'].mean()/combined_kT['LeadingkT20Eff'].std(),2)), size = 8)
plt.title(r'Efficiency for Various Algorithms')
plt.xlabel(r'Efficiency')
plt.ylabel('Frequency')
plt.xlim(0,1)
plt.legend(loc = 'upper center')
plt.savefig('/eos/user/g/gdecastr/www/JetAlgorithms_Comparison_Private/Eff.png')

plt.clf()

plt.hist(combined_Ak['LeadingAk20Purity'], bins = np.linspace(0,1,30), label = r'Ak $r = 2.0$', histtype='step', density = True)
plt.hist(combined_Cam['Leadingcambridge20Purity'], bins = np.linspace(0,1,30), label = r'Cambridge $r = 2.0$', histtype='step', density = True)
plt.hist(combined_Strip['Strip20Purity'], bins = np.linspace(0,1,30), label = r'Strip $\Delta\eta = 2.0$', density = True, histtype='step')
plt.hist(combined_kT['LeadingkT20Purity'], bins = np.linspace(0,1,30), label = r'kT $r = 2.0$', histtype='step', density = True)
plt.text(.2, 4.5, r"$r = 2.0:\;\mu$ = " + str(round(combined_Ak['LeadingAk20Purity'].mean(),2)) + r', $M = $' + str(round(combined_Ak['LeadingAk20Purity'].median(),2)) + r'$, \sigma$ = ' + str(round(combined_Ak['LeadingAk20Purity'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(combined_Ak['LeadingAk20Purity'].mean()/combined_Ak['LeadingAk20Purity'].std(),2)), size = 8)
plt.text(.2, 4, r"$r = 2.0:\;\mu$ = " + str(round(combined_Cam['Leadingcambridge20Purity'].mean(),2)) + r', $M = $' + str(round(combined_Cam['Leadingcambridge20Purity'].median(),2)) + r'$, \sigma$ = ' + str(round(combined_Cam['Leadingcambridge20Purity'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(combined_Cam['Leadingcambridge20Purity'].mean()/combined_Cam['Leadingcambridge20Purity'].std(),2)), size = 8)
plt.text(.2, 3.5, r"Strip $\Delta\eta = 1.5:\;\mu$ = " + str(round(combined_Strip['Strip20Purity'].mean(),2)) + r', $M = $' + str(round(combined_Strip['Strip20Purity'].median(),2)) + r'$, \sigma$ = ' + str(round(combined_Strip['Strip20Purity'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(combined_Strip['Strip20Purity'].mean()/combined_Strip['Strip20Purity'].std(),2)), size = 8)
plt.text(.2, 3.0, r"$r = 2.0:\;\mu$ = " + str(round(combined_kT['LeadingkT20Purity'].mean(),2)) + r', $M = $' + str(round(combined_kT['LeadingkT20Purity'].median(),2)) + r'$, \sigma$ = ' + str(round(combined_kT['LeadingkT20Purity'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(combined_kT['LeadingkT20Purity'].mean()/combined_kT['LeadingkT20Purity'].std(),2)), size = 8)
plt.title(r'Purity for Various Algorithms')
plt.xlabel(r'Purity')
plt.ylabel('Frequency')
plt.legend(loc = 'upper center')
plt.xlim(0,1)
plt.savefig('/eos/user/g/gdecastr/www/JetAlgorithms_Comparison_Private/Purity.png')

plt.clf()

plt.hist(combined_Ak['Ak20DeltaR2'], bins = np.linspace(0,1,30), label = r'Ak $r = 2.0$', histtype='step', density = True)
plt.hist(combined_Cam['cambridge20DeltaR2'], bins = np.linspace(0,1,30), label = r'Cambridge $r = 2.0$', histtype='step', density = True)
plt.hist(combined_Strip['Strip20DeltaR2'], bins = np.linspace(0,1,30), label = r'Strip $\Delta\eta = 2.0$', density = True, histtype='step')
plt.hist(combined_kT['kT20DeltaR2'], bins = np.linspace(0,1,30), label = r'kT $r = 2.0$', histtype='step', density = True)
plt.text(.3, 4.5, r"$r = 2.0:\;\mu$ = " + str(round(combined_Ak['Ak20DeltaR2'].mean(),2)) + r', $M = $' + str(round(combined_Ak['Ak20DeltaR2'].median(),2)) + r'$, \sigma$ = ' + str(round(combined_Ak['Ak20DeltaR2'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(combined_Ak['Ak20DeltaR2'].mean()/combined_Ak['Ak20DeltaR2'].std(),2)), size = 8)
plt.text(.3, 4.0, r"$r = 2.0:\;\mu$ = " + str(round(combined_Cam['cambridge20DeltaR2'].mean(),2)) + r', $M = $' + str(round(combined_Cam['cambridge20DeltaR2'].median(),2)) + r'$, \sigma$ = ' + str(round(combined_Cam['cambridge20DeltaR2'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(combined_Cam['cambridge20DeltaR2'].mean()/combined_Cam['cambridge20DeltaR2'].std(),2)), size = 8)
plt.text(.3, 3.5, r"Strip $\Delta\eta = 1.5:\;\mu$ = " + str(round(combined_Strip['Strip20DeltaR2'].mean(),2)) + r', $M = $' + str(round(combined_Strip['Strip20DeltaR2'].median(),2)) + r'$, \sigma$ = ' + str(round(combined_Strip['Strip20DeltaR2'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(combined_Strip['Strip20DeltaR2'].mean()/combined_Strip['Strip20DeltaR2'].std(),2)), size = 8)
plt.text(.3, 3.0, r"$r = 2.0:\;\mu$ = " + str(round(combined_kT['kT20DeltaR2'].mean(),2)) + r', $M = $' + str(round(combined_kT['kT20DeltaR2'].median(),2)) + r'$, \sigma$ = ' + str(round(combined_kT['kT20DeltaR2'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(combined_kT['kT20DeltaR2'].mean()/combined_kT['kT20DeltaR2'].std(),2)), size = 8)
plt.title(r'$dR^2$ between Cluster and Gen Higgs for Various Algorithms')
plt.xlabel(r'$dR^2$')
plt.ylabel('Frequency')
plt.xlim(0,1)
plt.legend()
plt.savefig('/eos/user/g/gdecastr/www/JetAlgorithms_Comparison_Private/AkdR2.png')

plt.clf()
