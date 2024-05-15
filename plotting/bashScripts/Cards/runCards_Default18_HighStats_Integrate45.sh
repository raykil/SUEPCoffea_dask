#!/bin/bashwait

python datacardMaker_IntegrateBins.py ZH/samples_withSF_nocuts_UL18_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats_Integrate45/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_18_HighStats/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region SR --doAll --floatB --integrateBins 6 ;
wait

python datacardMaker_IntegrateBins.py ZH/samples_withSF_nocuts_UL18_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats_Integrate45/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_18_HighStats/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region CRDY --doAll --floatB --integrateBins 6 ;
wait

python datacardMaker_IntegrateBins.py ZH/samples_withSF_nocuts_UL18_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats_Integrate45/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_18_HighStats/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region CRTT --doAll --floatB --integrateBins 6 ;
wait