#!/bin/bash

python datacardMaker_IntegrateBins.py ZH/samples_withSF_nocuts_UL18_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/CRDY_ABCDVeto/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_18_CommonBounds_Fixed/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region CRDY --floatB --doAll --integrateBins 5 ;
wait

python datacardMaker_IntegrateBins.py ZH/samples_withSF_nocuts_UL17_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/CRDY_ABCDVeto/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_17_CommonBounds_Fixed/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region CRDY --floatB --doAll --integrateBins 5 ;
wait

python datacardMaker_IntegrateBins.py ZH/samples_withSF_nocuts_UL16_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/CRDY_ABCDVeto/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_16_CommonBounds_Fixed/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region CRDY --floatB --doAll --integrateBins 6 ;
wait

python datacardMaker_IntegrateBins.py ZH/samples_withSF_nocuts_UL16APV_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/CRDY_ABCDVeto/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_16APV_CommonBounds_Fixed/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region CRDY --floatB --doAll --integrateBins 6 ;
wait
