#!/bin/bash

python datacardMaker.py ZH/samples_withSF_nocuts_UL17_dR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm50/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_17_ZMassPm50/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region SR --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL17_dR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm50/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_17_ZMassPm50/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region CRDY --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL17_dR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm50/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_17_ZMassPm50/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region CRTT --floatB ;
wait