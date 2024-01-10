#!/bin/bash

python datacardMaker.py ZH/samples_withSF_nocuts_UL16.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/LowSUEP/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_withdRCut_LowSUEP_16/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/LowSUEP/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_withdRCut_LowSUEP_16/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region CRDY --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/LowSUEP/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_withdRCut_LowSUEP_16/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region CRTT --doAll --floatB ;
wait