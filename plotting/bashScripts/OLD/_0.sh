#!/bin/bash
source /afs/cern.ch/cms/cmsset_default.sh
cd /eos/user/g/gdecastr/SUEPCoffea_dask/CMSSW_10_6_29/src/
cmsenv
cd /eos/home-g/gdecastr/SUEPCoffea_dask/plotting
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_CR.py ZH/plots_forCardsCRDY_LOW_mLL.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_LOW_mLL_18 --batchsize 100 --jobname /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_LOW_mLL_18_Jobs --plotAll --resubmit  --sample data --files /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHDF5s/NoSR_18/data//out_2514178354_1619_321457.hdf5