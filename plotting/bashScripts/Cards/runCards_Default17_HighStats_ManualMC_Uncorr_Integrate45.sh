#!/bin/bashwait

python datacardMaker_ManualMCStats.py ZH/samples_withSF_nocuts_UL17_dR_HighStats.py ZH/systs_uncorrClosure.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats_Integrate45_Uncorr_ManualMCStats/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_17_HighStats/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region SR --doAll --floatB --ManualMCStats --integrateBins 6 ;
wait

python datacardMaker_ManualMCStats.py ZH/samples_withSF_nocuts_UL17_dR_HighStats.py ZH/systs_uncorrClosure.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats_Integrate45_Uncorr_ManualMCStats/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_17_HighStats/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region CRDY --doAll --floatB --ManualMCStats --integrateBins 6 ;
wait

python datacardMaker_ManualMCStats.py ZH/samples_withSF_nocuts_UL17_dR_HighStats.py ZH/systs_uncorrClosure.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats_Integrate45_Uncorr_ManualMCStats/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_17_HighStats/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region CRTT --doAll --floatB --ManualMCStats --integrateBins 6 ;
wait