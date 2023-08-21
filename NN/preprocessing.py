import pandas as pd
import h5py
import numpy as np
import sys
from multiprocessing import Pool
from contextlib import closing 
import os
import time
import csv

direc = '/eos/user/g/gdecastr/SUEPCoffea_dask/NN/HDF5s_Private/'

eta_bins = np.linspace(-2.5, 2.5, 20)
phi_bins = np.linspace(-np.pi, np.pi, 20)


def threaded(path):
    output = []

    df = pd.HDFStore(path, "r")['twoleptons']
    for i in range(len(df)):
        if -999 not in df['tracks_eta'][i]:
             padding_index = len(df['tracks_eta'][i])
        else:   
            padding_index = df['tracks_eta'][i].index(-999) #Find where padding begins
        eta_idx = np.digitize(df['tracks_eta'][i][:padding_index], eta_bins) #Get Eta Grid Indices
        phi_idx = np.digitize(df['tracks_phi'][i][:padding_index], phi_bins) #Get Phi Grid Indices

        projectedbins = [((phi_idx[entry]-1)*len(phi_bins) + eta_idx[entry]-1) for entry in range(len(df['tracks_phi'][i][:padding_index]))] #Convert eta/phi bin indices into 1D

        tempDF = pd.DataFrame({'pt': df['tracks_pt'][i][:padding_index],
            'bin': projectedbins,
            'fromSUEP': df['tracks_fromSUEP'][i][:padding_index]})
        tempDF = tempDF.sort_values(by = 'bin')

        output_pixels = []
        output_flag = []

        for j in range(len(eta_bins)*len(phi_bins)):
            output_pixels.append(tempDF[tempDF['bin'] == j].pt.sum())
            if len(tempDF[tempDF['bin'] == j]) == 0:
                output_flag.append(0)
            else:
                var = tempDF[tempDF['bin'] == j].fromSUEP.sum() / len(tempDF[tempDF['bin'] == j])
                if var >= .75:
                    output_flag.append(1.0)
                else:
                    output_flag.append(0.0)

        output.append(np.concatenate([output_pixels, output_flag]))
    return np.array(output)

def list_full_paths(directory):
    return [os.path.join(directory, file) for file in os.listdir(directory)]

with closing(Pool(10)) as p:
    sys.stdout.write("Now running {} commands using: {} processes. Please wait\n".format(len(list_full_paths(direc)), 12))
    sys.stdout.flush()
    retlist1 = p.map_async(threaded, list_full_paths(direc), 1)
    while not retlist1.ready():
        sys.stdout.write("Runs left: {}\n".format(retlist1._number_left))
        sys.stdout.flush()
        time.sleep(1)
    retlist1 = retlist1.get()
    p.close()
    p.join()
    p.terminate()

processedData = [elem for twod in retlist1 for elem in twod]

with open("processedData_Private_20x20.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(processedData)