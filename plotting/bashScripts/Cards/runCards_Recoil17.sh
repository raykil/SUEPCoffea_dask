#!/bin/bash

python datacardMaker.py ZH/samples_withSF_nocuts_UL17.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Recoil30/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil30_17/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL17.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Recoil40/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil40_17/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL17.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Recoil50/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil50_17/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL17.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Recoil60/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil60_17/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region SR --doAll --floatB ;
wait