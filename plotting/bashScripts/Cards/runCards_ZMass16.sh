#!/bin/bash

python datacardMaker.py ZH/samples_withSF_nocuts_UL16.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm5/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/ZMassPm5_16/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm10/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/ZMassPm10_16/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm15/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/ZMassPm15_16/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm50/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/ZMassPm50_16/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region SR --doAll --floatB ;
wait