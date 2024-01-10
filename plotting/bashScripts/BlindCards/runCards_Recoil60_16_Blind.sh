#!/bin/bash

python datacardMaker.py ZH/samples_withSF_nocuts_UL16.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Blind/Recoil60/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil60_16/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region SR --thispoint SUEP_hadronic_mS125_mD3.00_T3.00 --floatB --blind ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Blind/Recoil60/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil60_CRDY_16/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region CRDY --thispoint SUEP_hadronic_mS125_mD3.00_T3.00 --floatB --blind ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Blind/Recoil60/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil60_CRTT_16/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region CRTT --thispoint SUEP_hadronic_mS125_mD3.00_T3.00 --floatB --blind ;
wait