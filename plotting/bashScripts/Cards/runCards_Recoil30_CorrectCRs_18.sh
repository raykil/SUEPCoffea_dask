#!/bin/bash

python datacardMaker.py ZH/samples_withSF_nocuts_UL18.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Recoil30_CorrectCRs_Replay/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil30_18/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL18.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Recoil30_CorrectCRs_Replay/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil30_CRDY_18/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region CRDY --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL18.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Recoil30_CorrectCRs_Replay/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil30_CRTT_18/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region CRTT --doAll --floatB ;
wait