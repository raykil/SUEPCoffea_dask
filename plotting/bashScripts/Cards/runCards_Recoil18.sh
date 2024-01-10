#!/bin/bash

python datacardMaker.py ZH/samples_withSF_nocuts_UL18.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Recoil30/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil30_18/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL18.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Recoil40/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil40_18/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL18.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Recoil50/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil50_18/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL18.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Recoil60/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil60_18/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region SR --doAll --floatB ;
wait