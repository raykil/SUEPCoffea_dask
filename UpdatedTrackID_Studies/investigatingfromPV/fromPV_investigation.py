import matplotlib.pyplot as plt
import h5py
import numpy as np
import pandas as pd


#Loading Data

master_f = pd.HDFStore("/eos/user/g/gdecastr/SUEPCoffea_dask/trackID/investigatingfromPV/UL18_trackInfo_fromPV0_withPU/out_115006_116_1.hdf5","r")['onecluster']
print('Loaded')
master_f = master_f.explode(['tracks_d0', 'tracks_d0Err', 'tracks_dz', 'tracks_dzErr', 'tracks_fromPV'])
print('Exploded')
master_f = master_f[(master_f['tracks_dzErr'] >= 0) & (master_f['tracks_dzErr'] < 100)]
master_f = master_f[(master_f['tracks_d0Err'] >= 0) & (master_f['tracks_d0Err'] < 100)]
fromPV1 = master_f[master_f['tracks_fromPV'] == 1]
fromPV2 = master_f[master_f['tracks_fromPV'] == 2]
print('Sorted')

fromPV1_0t20 = fromPV1[fromPV1['injected_PU'] <= 20]
fromPV1_20t40 = fromPV1[(fromPV1['injected_PU'] > 20) & (fromPV1['injected_PU'] <= 40)]
fromPV1_40t60 = fromPV1[(fromPV1['injected_PU'] > 40) & (fromPV1['injected_PU'] <= 60)]
fromPV1_60 = fromPV1[fromPV1['injected_PU'] > 60]

fromPV2_0t20 = fromPV2[fromPV2['injected_PU'] <= 20]
fromPV2_20t40 = fromPV2[(fromPV2['injected_PU'] > 20) & (fromPV2['injected_PU'] <= 40)]
fromPV2_40t60 = fromPV2[(fromPV2['injected_PU'] > 40) & (fromPV2['injected_PU'] <= 60)]
fromPV2_60 = fromPV2[fromPV2['injected_PU'] > 60]

plt.hist(fromPV1_0t20['tracks_d0'], histtype=u'step', label = 'fromPV1 - 0 <= PU <= 20', log = True, bins = np.linspace(-15, 15, 30), density = True)
plt.hist(fromPV1_20t40['tracks_d0'], histtype=u'step', label = 'fromPV1 - 20 < PU <= 40', log = True, bins = np.linspace(-15, 15, 30), density = True)
plt.hist(fromPV1_40t60['tracks_d0'], histtype=u'step', label = 'fromPV1 - 40 < PU <= 60', log = True, bins = np.linspace(-15, 15, 30), density = True)
plt.hist(fromPV1_60['tracks_d0'], histtype=u'step', label = 'fromPV1 - PU > 60', log = True, bins = np.linspace(-15, 15, 30), density = True)
plt.xlabel('d0')
plt.ylabel('Log Frequency')
plt.legend(fontsize = '6')
plt.title('Distribution of d0 in Nominal Signal Point - fromPV = 1')
plt.savefig('d0_fromPV1.png')
plt.clf()

plt.hist(fromPV2_0t20['tracks_d0'], histtype=u'step', label = 'fromPV2 - 0 <= PU <= 20', log = True, bins = np.linspace(-15, 15, 30), density = True)
plt.hist(fromPV2_20t40['tracks_d0'], histtype=u'step', label = 'fromPV2 - 20 < PU <= 40', log = True, bins = np.linspace(-15, 15, 30), density = True)
plt.hist(fromPV2_40t60['tracks_d0'], histtype=u'step', label = 'fromPV2 - 40 < PU <= 60', log = True, bins = np.linspace(-15, 15, 30), density = True)
plt.hist(fromPV2_60['tracks_d0'], histtype=u'step', label = 'fromPV2 - PU > 60', log = True, bins = np.linspace(-15, 15, 30), density = True)
plt.xlabel('d0')
plt.ylabel('Log Frequency')
plt.legend(fontsize = '6')
plt.title('Distribution of d0 in Nominal Signal Point - fromPV = 2')
plt.savefig('d0_fromPV2.png')
plt.clf()

plt.hist(fromPV1_0t20['tracks_d0Err'], histtype=u'step', label = 'fromPV1 - 0 <= PU <= 20', log = True, bins = np.linspace(0, 10, 10), density = True)
plt.hist(fromPV1_20t40['tracks_d0Err'], histtype=u'step', label = 'fromPV1 - 20 < PU <= 40', log = True, bins = np.linspace(0, 10, 10), density = True)
plt.hist(fromPV1_40t60['tracks_d0Err'], histtype=u'step', label = 'fromPV1 - 40 < PU <= 60', log = True, bins = np.linspace(0, 10, 10), density = True)
plt.hist(fromPV1_60['tracks_d0Err'], histtype=u'step', label = 'fromPV1 - PU > 60', log = True, bins = np.linspace(0, 10, 10), density = True)
plt.xlabel('d0Err')
plt.ylabel('Log Frequency')
plt.legend(fontsize = '6')
plt.title('Distribution of d0Err in Nominal Signal Point - fromPV = 1')
plt.savefig('d0Err_fromPV1.png')
plt.clf()

plt.hist(fromPV2_0t20['tracks_d0Err'], histtype=u'step', label = 'fromPV2 - 0 <= PU <= 20', log = True, bins = np.linspace(0, 10, 10), density = True)
plt.hist(fromPV2_20t40['tracks_d0Err'], histtype=u'step', label = 'fromPV2 - 20 < PU <= 40', log = True, bins = np.linspace(0, 10, 10), density = True)
plt.hist(fromPV2_40t60['tracks_d0Err'], histtype=u'step', label = 'fromPV2 - 40 < PU <= 60', log = True, bins = np.linspace(0, 10, 10), density = True)
plt.hist(fromPV2_60['tracks_d0Err'], histtype=u'step', label = 'fromPV2 - PU > 60', log = True, bins = np.linspace(0, 10, 10), density = True)
plt.xlabel('d0Err')
plt.ylabel('Log Frequency')
plt.legend(fontsize = '6')
plt.title('Distribution of d0Err in Nominal Signal Point - fromPV = 2')
plt.savefig('d0Err_fromPV2.png')
plt.clf()

plt.xscale('log')
plt.hist(fromPV1_0t20['tracks_d0']/fromPV1_0t20['tracks_d0Err'], histtype=u'step', label = 'fromPV1 - 0 <= PU <= 20', log = True, bins = np.logspace(-3, 3, 10), density = True)
plt.hist(fromPV1_20t40['tracks_d0']/fromPV1_20t40['tracks_d0Err'], histtype=u'step', label = 'fromPV1 - 20 < PU <= 40', log = True, bins = np.logspace(-3, 3, 10), density = True)
plt.hist(fromPV1_40t60['tracks_d0']/fromPV1_40t60['tracks_d0Err'], histtype=u'step', label = 'fromPV1 - 40 < PU <= 60', log = True, bins = np.logspace(-3, 3, 10), density = True)
plt.hist(fromPV1_60['tracks_d0']/fromPV1_60['tracks_d0Err'], histtype=u'step', label = 'fromPV1 - PU > 60', log = True, bins = np.logspace(-3, 3, 10), density = True)
plt.xlabel('d0/doErr')
plt.ylabel('Log Frequency')
plt.legend(fontsize = '6')
plt.title('Distribution of d0Sig in Nominal Signal Point - fromPV = 1')
plt.savefig('d0Sig_fromPV1.png')
plt.clf()

plt.xscale('log')
plt.hist(fromPV2_0t20['tracks_d0']/fromPV2_0t20['tracks_d0Err'], histtype=u'step', label = 'fromPV2 - 0 <= PU <= 20', log = True, bins = np.logspace(-3, 3, 10), density = True)
plt.hist(fromPV2_20t40['tracks_d0']/fromPV2_20t40['tracks_d0Err'], histtype=u'step', label = 'fromPV2 - 20 < PU <= 40', log = True, bins = np.logspace(-3, 3, 10), density = True)
plt.hist(fromPV2_40t60['tracks_d0']/fromPV2_40t60['tracks_d0Err'], histtype=u'step', label = 'fromPV2 - 40 < PU <= 60', log = True, bins = np.logspace(-3, 3, 10), density = True)
plt.hist(fromPV2_60['tracks_d0']/fromPV2_60['tracks_d0Err'], histtype=u'step', label = 'fromPV2 - PU > 60', log = True, bins = np.logspace(-3, 3, 10), density = True)
plt.xlabel('d0/doErr')
plt.ylabel('Log Frequency')
plt.legend(fontsize = '6')
plt.title('Distribution of d0Sig in Nominal Signal Point - fromPV = 2')
plt.savefig('d0Sig_fromPV2.png')
plt.clf()

plt.hist(fromPV1_0t20['tracks_dz'], histtype=u'step', label = 'fromPV1 - 0 <= PU <= 20', log = True, bins = np.linspace(-15, 15, 30), density = True)
plt.hist(fromPV1_20t40['tracks_dz'], histtype=u'step', label = 'fromPV1 - 20 < PU <= 40', log = True, bins = np.linspace(-15, 15, 30), density = True)
plt.hist(fromPV1_40t60['tracks_dz'], histtype=u'step', label = 'fromPV1 - 40 < PU <= 60', log = True, bins = np.linspace(-15, 15, 30), density = True)
plt.hist(fromPV1_60['tracks_dz'], histtype=u'step', label = 'fromPV1 - PU > 60', log = True, bins = np.linspace(-15, 15, 30), density = True)
plt.xlabel('dz')
plt.ylabel('Log Frequency')
plt.legend(fontsize = '6')
plt.title('Distribution of dz in Nominal Signal Point - fromPV = 1')
plt.savefig('dz_fromPV1.png')
plt.clf()

plt.hist(fromPV2_0t20['tracks_dz'], histtype=u'step', label = 'fromPV2 - 0 <= PU <= 20', log = True, bins = np.linspace(-15, 15, 30), density = True)
plt.hist(fromPV2_20t40['tracks_dz'], histtype=u'step', label = 'fromPV2 - 20 < PU <= 40', log = True, bins = np.linspace(-15, 15, 30), density = True)
plt.hist(fromPV2_40t60['tracks_dz'], histtype=u'step', label = 'fromPV2 - 40 < PU <= 60', log = True, bins = np.linspace(-15, 15, 30), density = True)
plt.hist(fromPV2_60['tracks_dz'], histtype=u'step', label = 'fromPV2 - PU > 60', log = True, bins = np.linspace(-15, 15, 30), density = True)
plt.xlabel('dz')
plt.ylabel('Log Frequency')
plt.legend(fontsize = '6')
plt.title('Distribution of dz in Nominal Signal Point - fromPV = 2')
plt.savefig('dz_fromPV2.png')
plt.clf()


plt.hist(fromPV1_0t20['tracks_dzErr'], histtype=u'step', label = 'fromPV1 - 0 <= PU <= 20', log = True, bins = np.linspace(0, 10, 10), density = True)
plt.hist(fromPV1_20t40['tracks_dzErr'], histtype=u'step', label = 'fromPV1 - 20 < PU <= 40', log = True, bins = np.linspace(0, 10, 10), density = True)
plt.hist(fromPV1_40t60['tracks_dzErr'], histtype=u'step', label = 'fromPV1 - 40 < PU <= 60', log = True, bins = np.linspace(0, 10, 10), density = True)
plt.hist(fromPV1_60['tracks_dzErr'], histtype=u'step', label = 'fromPV1 - PU > 60', log = True, bins = np.linspace(0, 10, 10), density = True)
plt.xlabel('dzErr')
plt.ylabel('Log Frequency')
plt.legend(fontsize = '6')
plt.title('Distribution of dzErr in Nominal Signal Point - fromPV = 1')
plt.savefig('dzErr_fromPV1.png')
plt.clf()


plt.hist(fromPV2_0t20['tracks_dzErr'], histtype=u'step', label = 'fromPV2 - 0 <= PU <= 20', log = True, bins = np.linspace(0, 10, 10), density = True)
plt.hist(fromPV2_20t40['tracks_dzErr'], histtype=u'step', label = 'fromPV2 - 20 < PU <= 40', log = True, bins = np.linspace(0, 10, 10), density = True)
plt.hist(fromPV2_40t60['tracks_dzErr'], histtype=u'step', label = 'fromPV2 - 40 < PU <= 60', log = True, bins = np.linspace(0, 10, 10), density = True)
plt.hist(fromPV2_60['tracks_dzErr'], histtype=u'step', label = 'fromPV2 - PU > 60', log = True, bins = np.linspace(0, 10, 10), density = True)
plt.xlabel('dzErr')
plt.ylabel('Log Frequency')
plt.legend(fontsize = '6')
plt.title('Distribution of dzErr in Nominal Signal Point - fromPV = 2')
plt.savefig('dzErr_fromPV2.png')
plt.clf()

plt.xscale('log')
plt.hist(fromPV1_0t20['tracks_dz']/fromPV1_0t20['tracks_dzErr'], histtype=u'step', label = 'fromPV1 - 0 <= PU <= 20', log = True, bins = np.logspace(-3, 3, 10), density = True)
plt.hist(fromPV1_20t40['tracks_dz']/fromPV1_20t40['tracks_dzErr'], histtype=u'step', label = 'fromPV1 - 20 < PU <= 40', log = True, bins = np.logspace(-3, 3, 10), density = True)
plt.hist(fromPV1_40t60['tracks_dz']/fromPV1_40t60['tracks_dzErr'], histtype=u'step', label = 'fromPV1 - 40 < PU <= 60', log = True, bins = np.logspace(-3, 3, 10), density = True)
plt.hist(fromPV1_60['tracks_dz']/fromPV1_60['tracks_dzErr'], histtype=u'step', label = 'fromPV1 - PU > 60', log = True, bins = np.logspace(-3, 3, 10), density = True)
plt.xlabel('dz/dzErr')
plt.ylabel('Log Frequency')
plt.legend(fontsize = '6')
plt.title('Distribution of dzSig in Nominal Signal Point - fromPV = 1')
plt.savefig('dzSig_fromPV1.png')
plt.clf()

plt.xscale('log')
plt.hist(fromPV2_0t20['tracks_dz']/fromPV2_0t20['tracks_dzErr'], histtype=u'step', label = 'fromPV2 - 0 <= PU <= 20', log = True, bins = np.logspace(-3, 3, 10), density = True)
plt.hist(fromPV2_20t40['tracks_dz']/fromPV2_20t40['tracks_dzErr'], histtype=u'step', label = 'fromPV2 - 20 < PU <= 40', log = True, bins = np.logspace(-3, 3, 10), density = True)
plt.hist(fromPV2_40t60['tracks_dz']/fromPV2_40t60['tracks_dzErr'], histtype=u'step', label = 'fromPV2 - 40 < PU <= 60', log = True, bins = np.logspace(-3, 3, 10), density = True)
plt.hist(fromPV2_60['tracks_dz']/fromPV2_60['tracks_dzErr'], histtype=u'step', label = 'fromPV2 - PU > 60', log = True, bins = np.logspace(-3, 3, 10), density = True)
plt.xlabel('dz/dzErr')
plt.ylabel('Log Frequency')
plt.legend(fontsize = '6')
plt.title('Distribution of dzSig in Nominal Signal Point - fromPV = 2')
plt.savefig('dzSig_fromPV2.png')
plt.clf()

