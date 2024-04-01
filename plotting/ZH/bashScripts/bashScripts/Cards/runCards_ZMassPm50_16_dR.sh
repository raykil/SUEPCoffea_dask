#!/bin/bash

python datacardMaker.py ZH/samples_withSF_nocuts_UL16_dR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm50/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16_ZMassPm50/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region SR --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16_dR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm50/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_16_ZMassPm50/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region CRDY --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16_dR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm50/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_16_ZMassPm50/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region CRTT --floatB ;
wait