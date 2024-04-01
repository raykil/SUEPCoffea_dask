#!/bin/bash

python datacardMaker.py ZH/samples_withSF_nocuts_UL18_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/Default/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_18_CommonBounds_Fixed/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region SR --floatB --doAll ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL17_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/Default/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_17_CommonBounds_Fixed/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region SR --floatB --doAll ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/Default/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16_CommonBounds_Fixed/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region SR --floatB --doAll ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/Default/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16APV_CommonBounds_Fixed/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region SR --floatB --doAll ;
wait
