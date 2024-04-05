#!/bin/bashwait

python datacardMaker.py ZH/samples_withSF_nocuts_UL18_dR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/DefaultAnalysis/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_18_All/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL18_dR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/DefaultAnalysis/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_18_All/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region CRDY --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL18_dR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/DefaultAnalysis/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_18_All/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region CRTT --doAll --floatB ;
wait