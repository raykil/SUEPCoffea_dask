#!/bin/bash

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/DefaultAnalysis/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16APV/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/DefaultAnalysis/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_16APV/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region CRDY --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/DefaultAnalysis/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_16APV/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region CRTT --doAll --floatB ;
wait