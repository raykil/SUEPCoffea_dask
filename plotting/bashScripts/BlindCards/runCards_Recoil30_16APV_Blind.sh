#!/bin/bash

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Blind/Recoil30/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil30_16APV/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region SR --thispoint SUEP_hadronic_mS125_mD3.00_T3.00 --floatB --blind ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Blind/Recoil30/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil30_CRDY_16APV/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region CRDY --thispoint SUEP_hadronic_mS125_mD3.00_T3.00 --floatB --blind ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Blind/Recoil30/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil30_CRTT_16APV/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region CRTT --thispoint SUEP_hadronic_mS125_mD3.00_T3.00 --floatB --blind ;
wait