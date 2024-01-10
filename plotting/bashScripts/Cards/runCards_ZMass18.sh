#!/bin/bash

python datacardMaker.py ZH/samples_withSF_nocuts_UL18.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm5/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/ZMassPm5_18/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL18.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm10/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/ZMassPm10_18/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL18.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm15/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/ZMassPm15_18/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL18.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm50/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/ZMassPm50_18/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region SR --doAll --floatB ;
wait