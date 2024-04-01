#!/bin/bashwait

python datacardMaker_ManualMCStats.py ZH/samples_withSF_nocuts_UL18_dR_HighStats.py ZH/systs_uncorrClosure.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats_Integrate45_Uncorr_ManualMCStats/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_18_HighStats/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region SR --doAll --floatB --ManualMCStats --integrateBins 6 ;
wait

python datacardMaker_ManualMCStats.py ZH/samples_withSF_nocuts_UL18_dR_HighStats.py ZH/systs_uncorrClosure.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats_Integrate45_Uncorr_ManualMCStats/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_18_HighStats/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region CRDY --doAll --floatB --ManualMCStats --integrateBins 6 ;
wait

python datacardMaker_ManualMCStats.py ZH/samples_withSF_nocuts_UL18_dR_HighStats.py ZH/systs_uncorrClosure.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats_Integrate45_Uncorr_ManualMCStats/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_18_HighStats/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region CRTT --doAll --floatB --ManualMCStats --integrateBins 6 ;
wait