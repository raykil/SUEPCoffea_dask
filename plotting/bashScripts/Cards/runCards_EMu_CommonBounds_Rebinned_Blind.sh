#!/bin/bashwait

python datacardMaker_EMu.py ZH/samples_withSF_nocuts_UL18_dR_HighStats_EMu.py ZH/systs_fullcorr_EMu.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds/Blind/EMu_Rebinned/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/EMu_18_CommonBounds_Rebin/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region EMu --doAll --floatB --blind ;
wait

python datacardMaker_EMu.py ZH/samples_withSF_nocuts_UL17_dR_HighStats_EMu.py ZH/systs_fullcorr_EMu.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds/Blind/EMu_Rebinned/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/EMu_17_CommonBounds_Rebin/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region EMu --doAll --floatB --blind ;
wait

python datacardMaker_EMu.py ZH/samples_withSF_nocuts_UL16_dR_HighStats_EMu.py ZH/systs_fullcorr_EMu.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds/Blind/EMu_Rebinned/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/EMu_16_CommonBounds_Rebin/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region EMu --doAll --floatB --blind ;
wait

python datacardMaker_EMu.py ZH/samples_withSF_nocuts_UL16APV_dR_HighStats_EMu.py ZH/systs_fullcorr_EMu.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds/Blind/EMu_Rebinned/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/EMu_16APV_CommonBounds_Rebin/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region EMu --doAll --floatB --blind ;
wait