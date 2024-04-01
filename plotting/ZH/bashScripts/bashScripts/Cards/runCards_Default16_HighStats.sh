#!/bin/bashwait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16_HighStats/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_16_HighStats/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region CRDY --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_16_HighStats/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region CRTT --doAll --floatB ;
wait