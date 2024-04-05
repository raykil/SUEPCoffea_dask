#!/bin/bashwait

python datacardMaker_ManualMCStats.py ZH/samples_withSF_nocuts_UL16APV_dR_HighStats.py ZH/systs_uncorrClosure.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats_ManualMC_Uncorr/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16APV_HighStats/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region SR --doAll --floatB --ManualMCStats ;
wait

python datacardMaker_ManualMCStats.py ZH/samples_withSF_nocuts_UL16APV_dR_HighStats.py ZH/systs_uncorrClosure.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats_ManualMC_Uncorr/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_16APV_HighStats/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region CRDY --doAll --floatB --ManualMCStats ;
wait

python datacardMaker_ManualMCStats.py ZH/samples_withSF_nocuts_UL16APV_dR_HighStats.py ZH/systs_uncorrClosure.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats_ManualMC_Uncorr/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_16APV_HighStats/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region CRTT --doAll --floatB --ManualMCStats ;
wait