#!/bin/bash

python datacardMaker.py ZH/samples_withSF_nocuts_UL16.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Blind/Default_S+B_Scale5/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region SR --thispoint SUEP_hadronic_mS125_mD3.00_T3.00 --floatB --blind_withS ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Blind/Default_S+B_Scale5/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_16/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region CRDY --thispoint SUEP_hadronic_mS125_mD3.00_T3.00 --floatB --blind_withS ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Blind/Default_S+B_Scale5/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_16/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region CRTT --thispoint SUEP_hadronic_mS125_mD3.00_T3.00 --floatB --blind_withS ;
wait