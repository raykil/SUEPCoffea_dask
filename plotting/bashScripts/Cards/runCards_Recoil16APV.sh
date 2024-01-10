#!/bin/bash

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Recoil30/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil30_16APV/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Recoil40/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil40_16APV/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Recoil50/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil50_16APV/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Recoil60/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil60_16APV/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region SR --doAll --floatB ;
wait
