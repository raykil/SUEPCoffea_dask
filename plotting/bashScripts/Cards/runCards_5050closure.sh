#!/bin/bash

python datacardMaker.py ZH/samples_withSF_nocuts_UL18_dR.py ZH/systs_5050corr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/5050Closure/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_18_All/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL18_dR.py ZH/systs_5050corr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/5050Closure/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_18_All/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region CRDY --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL18_dR.py ZH/systs_5050corr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/5050Closure/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_18_All/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region CRTT --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL17_dR.py ZH/systs_5050corr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/5050Closure/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_17_All/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL17_dR.py ZH/systs_5050corr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/5050Closure/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_17_All/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region CRDY --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL17_dR.py ZH/systs_5050corr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/5050Closure/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_17_All/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region CRTT --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16_dR.py ZH/systs_5050corr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/5050Closure/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16_All/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16_dR.py ZH/systs_5050corr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/5050Closure/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_16_All/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region CRDY --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16_dR.py ZH/systs_5050corr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/5050Closure/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_16_All/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region CRTT --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV_dR.py ZH/systs_5050corr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/5050Closure/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16APV_All/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV_dR.py ZH/systs_5050corr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/5050Closure/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_16APV_All/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region CRDY --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV_dR.py ZH/systs_5050corr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/5050Closure/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_16APV_All/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region CRTT --doAll --floatB ;
wait
