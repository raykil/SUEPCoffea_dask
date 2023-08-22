import matplotlib.pyplot as plt
import h5py
import numpy as np
import pandas as pd
import os

#Loading Data

master_f = pd.DataFrame()

direc = '/eos/user/g/gdecastr/SUEPCoffea_dask/trackID/GenVsRecoClusters'
files = os.listdir(direc)
for file in files:
    print(file)
    if file.endswith('.csv'):
       df = pd.read_csv(direc+'/'+file)
       master_f = pd.concat([master_f, df], ignore_index=True)
labels = list(master_f.columns.values)

for i in labels:
    temp_f = master_f[np.abs(master_f[i]) < 20]
    mean = str(round(temp_f[i].mean(), 3))
    std = str(round(temp_f[i].std(), 3))
    '''
    plt.hist(temp_f[i], histtype=u'step', bins = np.linspace(-3,3,40))
    plt.xlabel('(Reco - Gen)/Gen')
    plt.ylabel('Frequency')
    plt.title('Comparing Reconstructed Cluster and Gen-Level Higgs - ' + i)
    plt.text(1.5, 2000, 'Mean: ' + mean)
    plt.text(1.5, 1800, 'Std: ' + std)
    plt.savefig('GenVsRecoClusters_' + i + '.png', dpi = 1000)
    plt.clf()
    '''
    plt.hist(temp_f[i], histtype=u'step', bins = np.linspace(-20,20,30), log = True)
    plt.xlabel('(Reco - Gen)/Gen')
    plt.ylabel('Frequency')
    plt.title('Comparing Reconstructed Cluster and Gen-Level Higgs - ' + i)
    plt.text(5, 5000, 'Mean: ' + mean)
    plt.text(5, 1000, 'Std: ' + std)
    plt.savefig('GenVsRecoClusters_' + i + '_logy.png', dpi = 1000)
    plt.clf()
