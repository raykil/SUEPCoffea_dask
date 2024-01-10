#!/bin/bash

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm5/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/ZMassPm5_16APV/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm10/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/ZMassPm10_16APV/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm15/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/ZMassPm15_16APV/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm50/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/ZMassPm50_16APV/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region SR --doAll --floatB ;
wait
