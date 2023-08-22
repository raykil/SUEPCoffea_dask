import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

filenames = os.listdir('/eos/user/g/gdecastr/SUEPCoffea_dask/RebuildingSUEP/csvs_Private')

Ak_files = [filename for filename in filenames if filename.endswith('kT.csv')]
Strip_files = [filename for filename in filenames if filename.endswith('Strip.csv')]
Higgs_files = [filename for filename in filenames if filename.endswith('GenHiggs.csv')]

# Extract the tags from the file names in each list
tags1 = set([filename.split('_')[3] for filename in Ak_files])
tags2 = set([filename.split('_')[3] for filename in Strip_files])
tags3 = set([filename.split('_')[3] for filename in Higgs_files])

# Find the intersection of the two sets of tags
common_tags = tags1.intersection(tags2, tags3)

# Keep only the files where the tag exists in both lists
Ak_files = [filename for filename in Ak_files if filename.split('_')[3] in common_tags]
Strip_files = [filename for filename in Strip_files if filename.split('_')[3] in common_tags]
Higgs_files = [filename for filename in Higgs_files if filename.split('_')[3] in common_tags]


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

##### Higgs
HiggsFrames = []
for file in Higgs_files:
    df = pd.read_csv('/eos/user/g/gdecastr/SUEPCoffea_dask/RebuildingSUEP/csvs_Private/' + file)
    HiggsFrames.append(df)

combined_Higgs = pd.concat(HiggsFrames, ignore_index=True)

combined_Ak = pd.concat([combined_Ak, combined_Higgs], axis = 1)
combined_Strip = pd.concat([combined_Strip, combined_Higgs], axis = 1)


temp_Ak = combined_Ak[(np.abs(combined_Ak['GenHiggsPx']) >= 100) | (np.abs(combined_Ak['GenHiggsPy']) >= 100)]
temp_Strip = combined_Strip[(np.abs(combined_Strip['GenHiggsPx']) >= 100) | (np.abs(combined_Strip['GenHiggsPy']) >= 100)]

temp_Ak_2 = combined_Ak[(np.abs(combined_Ak['GenHiggsPx']) < 100) & (np.abs(combined_Ak['GenHiggsPy']) < 100)]
temp_Strip_2 = combined_Strip[(np.abs(combined_Strip['GenHiggsPx']) < 100) & (np.abs(combined_Strip['GenHiggsPy']) < 100)]

'''
temp_Ak_2 = combined_Ak[np.abs(combined_Ak['GenHiggsPy']) >= 500]
temp_Ak_2 = temp_Ak_2[np.abs(temp_Ak_2['GenHiggsPz']) >= 500]
temp_Strip_2 = combined_Strip[np.abs(combined_Strip['GenHiggsPy']) >= 500]
temp_Strip_2 = temp_Strip_2[np.abs(temp_Strip_2['GenHiggsPz']) >= 500]
'''

#plt.hist(combined_Ak['kT20DeltaR2'], bins = np.linspace(0,1,30), label = r'kT $r = 2.0$ Inclusive', histtype='step', density = True)
plt.hist(temp_Ak['kT20DeltaR2'], bins = np.linspace(0,1,30), label = r'kT $r = 2.0$ Strong Trans Boost', histtype='step', density = True)
plt.hist(temp_Ak_2['kT20DeltaR2'], bins = np.linspace(0,1,30), label = r'kT $r = 2.0$ Weak Trans Boost', histtype='step', density = True)
#plt.hist(combined_Strip['Strip20DeltaR2'], bins = np.linspace(0,1,30), label = r'Strip $\Delta\eta = 2.0$ Inclusive', histtype='step', density = True)
plt.hist(temp_Strip['Strip20DeltaR2'], bins = np.linspace(0,1,30), label = r'Strip $\Delta\eta = 2.0$ Strong Trans Boost', histtype='step', density = True)
plt.hist(temp_Strip_2['Strip20DeltaR2'], bins = np.linspace(0,1,30), label = r'Strip $\Delta\eta = 2.0$ Weak Trans Boost', histtype='step', density = True)
plt.text(.2, 10.0, r"kT $r = 2.0$ Strong Trans Boost:$\;\mu$ = " + str(round(temp_Ak['kT20DeltaR2'].mean(),2)) + r', $M = $' + str(round(temp_Ak['kT20DeltaR2'].median(),2)) + r'$, \sigma$ = ' + str(round(temp_Ak['kT20DeltaR2'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(temp_Ak['kT20DeltaR2'].mean()/temp_Ak['kT20DeltaR2'].std(),2)), size = 7)
plt.text(.2, 9.0, r"kT $r = 2.0$ Weak Trans Boost:$\;\mu$ = " + str(round(temp_Ak_2['kT20DeltaR2'].mean(),2)) + r', $M = $' + str(round(temp_Ak_2['kT20DeltaR2'].median(),2)) + r'$, \sigma$ = ' + str(round(temp_Ak_2['kT20DeltaR2'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(temp_Ak_2['kT20DeltaR2'].mean()/temp_Ak_2['kT20DeltaR2'].std(),2)), size = 7)
plt.text(.2, 8.0, r"Strip $\Delta\eta = 2.0$ Strong Trans Boost:$\;\mu$ = " + str(round(temp_Strip['Strip20DeltaR2'].mean(),2)) + r', $M = $' + str(round(temp_Strip['Strip20DeltaR2'].median(),2)) + r'$, \sigma$ = ' + str(round(temp_Strip['Strip20DeltaR2'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(temp_Strip['Strip20DeltaR2'].mean()/temp_Strip['Strip20DeltaR2'].std(),2)), size = 7)
plt.text(.2, 7.0, r"Strip $\Delta\eta = 2.0$ Weak Trans Boost:$\;\mu$ = " + str(round(temp_Strip_2['Strip20DeltaR2'].mean(),2)) + r', $M = $' + str(round(temp_Strip_2['Strip20DeltaR2'].median(),2)) + r'$, \sigma$ = ' + str(round(temp_Strip_2['Strip20DeltaR2'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(temp_Strip_2['Strip20DeltaR2'].mean()/temp_Strip_2['Strip20DeltaR2'].std(),2)), size = 7)
plt.title(r'$dR^2$ between Cluster and Gen Higgs for Different Boosts')
plt.xlabel(r'$dR^2$')
plt.ylabel('Frequency')
plt.xlim(0,1)
plt.legend()
plt.savefig('/eos/user/g/gdecastr/www/JetAlgorithms_Boosting/dR2_trans.png')

plt.clf()

#plt.hist(combined_Ak['kT20BetaRes'], bins = np.linspace(-.5,1,30), label = r'kT $r = 2.0$ Inclusive', histtype='step', density = True)
plt.hist(temp_Ak['kT20BetaRes'], bins = np.linspace(-.5,1,30), label = r'kT $r = 2.0$ Strong Trans Boost', histtype='step', density = True)
plt.hist(temp_Ak_2['kT20BetaRes'], bins = np.linspace(-.5,1,30), label = r'kT $r = 2.0$ Weak Trans Boost', histtype='step', density = True)
#plt.hist(combined_Strip['Strip20BetaRes'], bins = np.linspace(-.5,1,30), label = r'Strip $\Delta\eta = 2.0$ Inclusive', histtype='step', density = True)
plt.hist(temp_Strip['Strip20BetaRes'], bins = np.linspace(-.5,1,30), label = r'Strip $\Delta\eta = 2.0$ Strong Trans Boost', histtype='step', density = True)
plt.hist(temp_Strip_2['Strip20BetaRes'], bins = np.linspace(-.5,1,30), label = r'Strip $\Delta\eta = 2.0$ Weak Trans Boost', histtype='step', density = True)
plt.text(.1, 6, r"kT $r = 2.0$ Strong Trans Boost:$\;\mu$ = " + str(round(temp_Ak['kT20BetaRes'].mean(),2)) + r', $M = $' + str(round(temp_Ak['kT20BetaRes'].median(),2)) + r'$, \sigma$ = ' + str(round(temp_Ak['kT20BetaRes'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(temp_Ak['kT20BetaRes'].mean()/temp_Ak['kT20BetaRes'].std(),2)), size = 6)
plt.text(.1, 6.5, r"kT $r = 2.0$ Weak Trans Boost:$\;\mu$ = " + str(round(temp_Ak_2['kT20BetaRes'].mean(),2)) + r', $M = $' + str(round(temp_Ak_2['kT20BetaRes'].median(),2)) + r'$, \sigma$ = ' + str(round(temp_Ak_2['kT20BetaRes'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(temp_Ak_2['kT20BetaRes'].mean()/temp_Ak_2['kT20BetaRes'].std(),2)), size = 6)
plt.text(.1, 5, r"Strip $\Delta\eta = 2.0$ Strong Trans Boost:$\;\mu$ = " + str(round(temp_Strip['Strip20BetaRes'].mean(),2)) + r', $M = $' + str(round(temp_Strip['Strip20BetaRes'].median(),2)) + r'$, \sigma$ = ' + str(round(temp_Strip['Strip20BetaRes'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(temp_Strip['Strip20BetaRes'].mean()/temp_Strip['Strip20BetaRes'].std(),2)), size = 6)
plt.text(.1, 5.5, r"Strip $\Delta\eta = 2.0$ Weak Trans Boost:$\;\mu$ = " + str(round(temp_Strip_2['Strip20BetaRes'].mean(),2)) + r', $M = $' + str(round(temp_Strip_2['Strip20BetaRes'].median(),2)) + r'$, \sigma$ = ' + str(round(temp_Strip_2['Strip20BetaRes'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(temp_Strip_2['Strip20BetaRes'].mean()/temp_Strip_2['Strip20BetaRes'].std(),2)), size = 6)
plt.title(r'$\beta$ resolution between Cluster and Gen Higgs')
plt.xlabel(r'$\frac{\beta_{Ak} - \beta_{Gen}}{\beta_{Gen}}$')
plt.ylabel('Frequency')
plt.legend()
plt.xlim(-.5,1)
plt.savefig('/eos/user/g/gdecastr/www/JetAlgorithms_Boosting/BetaRes_trans.png')

plt.clf()

#plt.hist(combined_Ak['LeadingkT20Purity'], bins = np.linspace(0,1,30), label = r'kT $r = 2.0$ Inclusive', histtype='step', density = True)
plt.hist(temp_Ak['LeadingkT20Purity'], bins = np.linspace(0,1,30), label = r'kT $r = 2.0$ Strong Trans Boost', histtype='step', density = True)
plt.hist(temp_Ak_2['LeadingkT20Purity'], bins = np.linspace(0,1,30), label = r'kT $r = 2.0$ Weak Trans Boost', histtype='step', density = True)
#plt.hist(combined_Strip['Strip20Purity'], bins = np.linspace(0,1,30), label = r'Strip $\Delta\eta = 2.0$ Inclusive', histtype='step', density = True)
plt.hist(temp_Strip['Strip20Purity'], bins = np.linspace(0,1,30), label = r'Strip $\Delta\eta = 2.0$ Strong Trans Boost', histtype='step', density = True)
plt.hist(temp_Strip_2['Strip20Purity'], bins = np.linspace(0,1,30), label = r'Strip $\Delta\eta = 2.0$ Weak Trans Boost', histtype='step', density = True)
plt.text(.0, 4., r"kT $r = 2.0$ Strong Trans Boost:$\;\mu$ = " + str(round(temp_Ak['LeadingkT20Purity'].mean(),2)) + r', $M = $' + str(round(temp_Ak['LeadingkT20Purity'].median(),2)) + r'$, \sigma$ = ' + str(round(temp_Ak['LeadingkT20Purity'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(temp_Ak['LeadingkT20Purity'].mean()/temp_Ak['LeadingkT20Purity'].std(),2)), size = 7)
plt.text(.0, 3.5, r"kT $r = 2.0$ Weak Trans Boost:$\;\mu$ = " + str(round(temp_Ak_2['LeadingkT20Purity'].mean(),2)) + r', $M = $' + str(round(temp_Ak_2['LeadingkT20Purity'].median(),2)) + r'$, \sigma$ = ' + str(round(temp_Ak_2['LeadingkT20Purity'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(temp_Ak_2['LeadingkT20Purity'].mean()/temp_Ak_2['LeadingkT20Purity'].std(),2)), size = 7)
plt.text(.0, 3., r"Strip $\Delta\eta = 2.0$ Strong Trans Boost:$\;\mu$ = " + str(round(temp_Strip['Strip20Purity'].mean(),2)) + r', $M = $' + str(round(temp_Strip['Strip20Purity'].median(),2)) + r'$, \sigma$ = ' + str(round(temp_Strip['Strip20Purity'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(temp_Strip['Strip20Purity'].mean()/temp_Strip['Strip20Purity'].std(),2)), size = 7)
plt.text(.0, 2.5, r"Strip $\Delta\eta = 2.0$ Weak Trans Boost:$\;\mu$ = " + str(round(temp_Strip_2['Strip20Purity'].mean(),2)) + r', $M = $' + str(round(temp_Strip_2['Strip20Purity'].median(),2)) + r'$, \sigma$ = ' + str(round(temp_Strip_2['Strip20Purity'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(temp_Strip_2['Strip20Purity'].mean()/temp_Strip_2['Strip20Purity'].std(),2)), size = 7)
plt.title(r'Purity')
plt.xlabel(r'Purity')
plt.ylabel('Frequency')
plt.legend(loc = 'upper center')
plt.xlim(0,1)
plt.savefig('/eos/user/g/gdecastr/www/JetAlgorithms_Boosting/Purity_trans.png')

plt.clf()

#plt.hist(combined_Ak['LeadingkT20Eff'], bins = np.linspace(0,1,30), label = r'kT $r = 2.0$ Inclusive', histtype='step', density = True)
plt.hist(temp_Ak['LeadingkT20Eff'], bins = np.linspace(0,1,30), label = r'kT $r = 2.0$ Strong Trans Boost', histtype='step', density = True)
plt.hist(temp_Ak_2['LeadingkT20Eff'], bins = np.linspace(0,1,30), label = r'kT $r = 2.0$ Weak Trans Boost', histtype='step', density = True)
#plt.hist(combined_Strip['Strip20Eff'], bins = np.linspace(0,1,30), label = r'Strip $\Delta\eta = 2.0$ Inclusive', histtype='step', density = True)
plt.hist(temp_Strip['Strip20Eff'], bins = np.linspace(0,1,30), label = r'Strip $\Delta\eta = 2.0$ Strong Trans Boost', histtype='step', density = True)
plt.hist(temp_Strip_2['Strip20Eff'], bins = np.linspace(0,1,30), label = r'Strip $\Delta\eta = 2.0$ Weak Trans Boost', histtype='step', density = True)
plt.text(.2, 17.0, r"kT $r = 2.0$ Strong Trans Boost:$\;\mu$ = " + str(round(temp_Ak['LeadingkT20Eff'].mean(),2)) + r', $M = $' + str(round(temp_Ak['LeadingkT20Eff'].median(),2)) + r'$, \sigma$ = ' + str(round(temp_Ak['LeadingkT20Eff'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(temp_Ak['LeadingkT20Eff'].mean()/temp_Ak['LeadingkT20Eff'].std(),2)), size = 7)
plt.text(.2, 15.0, r"kT $r = 2.0$ Weak Trans Boost:$\;\mu$ = " + str(round(temp_Ak_2['LeadingkT20Eff'].mean(),2)) + r', $M = $' + str(round(temp_Ak_2['LeadingkT20Eff'].median(),2)) + r'$, \sigma$ = ' + str(round(temp_Ak_2['LeadingkT20Eff'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(temp_Ak_2['LeadingkT20Eff'].mean()/temp_Ak_2['LeadingkT20Eff'].std(),2)), size = 7)
plt.text(.2, 13.0, r"Strip $\Delta\eta = 2.0$ Strong Trans Boost:$\;\mu$ = " + str(round(temp_Strip['Strip20Eff'].mean(),2)) + r', $M = $' + str(round(temp_Strip['Strip20Eff'].median(),2)) + r'$, \sigma$ = ' + str(round(temp_Strip['Strip20Eff'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(temp_Strip['Strip20Eff'].mean()/temp_Strip['Strip20Eff'].std(),2)), size = 7)
plt.text(.2, 11.0, r"Strip $\Delta\eta = 2.0$ Weak Trans Boost:$\;\mu$ = " + str(round(temp_Strip_2['Strip20Eff'].mean(),2)) + r', $M = $' + str(round(temp_Strip_2['Strip20Eff'].median(),2)) + r'$, \sigma$ = ' + str(round(temp_Strip_2['Strip20Eff'].std(),2)) + r', $\frac{\mu}{\sigma} = $' + str(round(temp_Strip_2['Strip20Eff'].mean()/temp_Strip_2['Strip20Eff'].std(),2)), size = 7)
plt.title(r'Efficiency')
plt.xlabel(r'Efficiency')
plt.ylabel('Frequency')
plt.xlim(0,1)
plt.legend(loc = 'upper center')
plt.savefig('/eos/user/g/gdecastr/www/JetAlgorithms_Boosting/Eff_trans.png')

plt.clf()