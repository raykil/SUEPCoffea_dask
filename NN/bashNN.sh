#!/bin/bash
cd /eos/user/g/gdecastr/SUEPCoffea_dask
for i in {1..9}; do
    python condor_SUEP_WS.py --isMC=1 --era=2018 --analyzer=ZH_trackProps --infile=/eos/cms/store/user/cericeci/forGianfranco/ZHleptonicpythia_generic_M125_MD2_T2_HT0.0_new_propergen/NANOAOD/nanoaod_100"$i".root --outputdir=/eos/user/g/gdecastr/SUEPCoffea_dask/NN/HDF5s;
done
for i in {10..99}; do
    python condor_SUEP_WS.py --isMC=1 --era=2018 --analyzer=ZH_trackProps --infile=/eos/cms/store/user/cericeci/forGianfranco/ZHleptonicpythia_generic_M125_MD2_T2_HT0.0_new_propergen/NANOAOD/nanoaod_10"$i".root --outputdir=/eos/user/g/gdecastr/SUEPCoffea_dask/NN/HDF5s;
done
for i in {100..200}; do
    python condor_SUEP_WS.py --isMC=1 --era=2018 --analyzer=ZH_trackProps --infile=/eos/cms/store/user/cericeci/forGianfranco/ZHleptonicpythia_generic_M125_MD2_T2_HT0.0_new_propergen/NANOAOD/nanoaod_1"$i".root --outputdir=/eos/user/g/gdecastr/SUEPCoffea_dask/NN/HDF5s;
done