#!/bin/bash

python datacardMaker.py ZH/samples_withSF_nocuts_UL18_dR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm5/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_18_ZMassPm5/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region SR --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL18_dR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm5/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_18_ZMassPm5/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region CRDY --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL18_dR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm5/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_18_ZMassPm5/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region CRTT --floatB ;
wait