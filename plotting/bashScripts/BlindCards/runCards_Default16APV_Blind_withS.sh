#!/bin/bash

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Blind/Default_S+B/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16APV/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region SR --thispoint SUEP_hadronic_mS125_mD3.00_T3.00 --floatB --blind_withS ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Blind/Default_S+B/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_16APV/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region CRDY --thispoint SUEP_hadronic_mS125_mD3.00_T3.00 --floatB --blind_withS ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Blind/Default_S+B/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_16APV/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region CRTT --thispoint SUEP_hadronic_mS125_mD3.00_T3.00 --floatB --blind_withS ;
wait