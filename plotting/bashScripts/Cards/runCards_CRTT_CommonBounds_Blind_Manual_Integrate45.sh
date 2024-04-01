#!/bin/bash

python datacardMaker_ManualMCStats.py ZH/samples_withSF_nocuts_UL18_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/Blind/ManualMC_Integrate45/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_18_CommonBounds_Fixed/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region CRTT --floatB --doAll --ManualMCStats --blind --integrateBins 6 ;
wait

python datacardMaker_ManualMCStats.py ZH/samples_withSF_nocuts_UL17_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/Blind/ManualMC_Integrate45/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_17_CommonBounds_Fixed/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region CRTT --floatB --doAll --ManualMCStats --blind --integrateBins 6 ;
wait

python datacardMaker_ManualMCStats.py ZH/samples_withSF_nocuts_UL16_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/Blind/ManualMC_Integrate45/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_16_CommonBounds_Fixed/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region CRTT --floatB --doAll --ManualMCStats --blind --integrateBins 6 ;
wait

python datacardMaker_ManualMCStats.py ZH/samples_withSF_nocuts_UL16APV_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/Blind/ManualMC_Integrate45/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_16APV_CommonBounds_Fixed/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region CRTT --floatB --doAll --ManualMCStats --blind --integrateBins 6 ;
wait
