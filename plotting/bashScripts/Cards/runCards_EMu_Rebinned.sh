#!/bin/bashwait

python datacardMaker_EMu.py ZH/samples_withSF_nocuts_UL18_dR_HighStats_EMu.py ZH/systs_fullcorr_EMu.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Rebinned/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/EMu_18_Rebinned/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region EMu --doAll --floatB ;
wait

python datacardMaker_EMu.py ZH/samples_withSF_nocuts_UL17_dR_HighStats_EMu.py ZH/systs_fullcorr_EMu.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Rebinned/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/EMu_17_Rebinned/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region EMu --doAll --floatB ;
wait

python datacardMaker_EMu.py ZH/samples_withSF_nocuts_UL16_dR_HighStats_EMu.py ZH/systs_fullcorr_EMu.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Rebinned/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/EMu_16_Rebinned/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region EMu --doAll --floatB ;
wait

python datacardMaker_EMu.py ZH/samples_withSF_nocuts_UL16APV_dR_HighStats_EMu.py ZH/systs_fullcorr_EMu.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Rebinned/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/EMu_16APV_Rebinned/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region EMu --doAll --floatB ;
wait