#!/bin/bash

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV_dR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm5/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16APV_ZMassPm5/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region SR --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV_dR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm5/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_16APV_ZMassPm5/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region CRDY --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV_dR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm5/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_16APV_ZMassPm5/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region CRTT --floatB ;
wait