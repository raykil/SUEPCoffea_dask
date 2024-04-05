#!/bin/bashwait

python datacardMaker_ManualMCStats.py ZH/samples_withSF_nocuts_UL18_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds/CRDY_Rebinned_Manual/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_18_CommonBounds_Rebin/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region CRDY --doAll --floatB --ManualMCStats ;
wait

python datacardMaker_ManualMCStats.py ZH/samples_withSF_nocuts_UL17_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds/CRDY_Rebinned_Manual/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_17_CommonBounds_Rebin/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region CRDY --doAll --floatB --ManualMCStats ;
wait

python datacardMaker_ManualMCStats.py ZH/samples_withSF_nocuts_UL16_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds/CRDY_Rebinned_Manual/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_16_CommonBounds_Rebin/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region CRDY --doAll --floatB --ManualMCStats ;
wait

python datacardMaker_ManualMCStats.py ZH/samples_withSF_nocuts_UL16APV_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds/CRDY_Rebinned_Manual/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_16APV_CommonBounds_Rebin/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region CRDY --doAll --floatB --ManualMCStats ;
wait