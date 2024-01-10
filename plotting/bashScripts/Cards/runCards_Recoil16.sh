#!/bin/bash

python datacardMaker.py ZH/samples_withSF_nocuts_UL16.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Recoil30/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil30_16/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Recoil40/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil40_16/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Recoil50/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil50_16/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Recoil60/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil60_16/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region SR --doAll --floatB ;
wait