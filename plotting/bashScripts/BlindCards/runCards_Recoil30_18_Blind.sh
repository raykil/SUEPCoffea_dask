#!/bin/bash

python datacardMaker.py ZH/samples_withSF_nocuts_UL18.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Blind/Recoil30/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil30_18/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region SR --thispoint SUEP_hadronic_mS125_mD3.00_T3.00 --floatB --blind ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL18.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Blind/Recoil30/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil30_CRDY_18/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region CRDY --thispoint SUEP_hadronic_mS125_mD3.00_T3.00 --floatB --blind ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL18.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Blind/Recoil30/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil30_CRTT_18/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region CRTT --thispoint SUEP_hadronic_mS125_mD3.00_T3.00 --floatB --blind ;
wait