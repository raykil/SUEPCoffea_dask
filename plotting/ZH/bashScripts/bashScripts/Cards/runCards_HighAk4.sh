#!/bin/bash

python datacardMaker.py ZH/samples_withSF_nocuts_UL18_dR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighAk4/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_18_HighAk4/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region SR --doAll --floatB  ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL18_dR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighAk4/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_18_HighAk4/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region CRDY --doAll --floatB  ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL18_dR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighAk4/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_18_HighAk4/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region CRTT --doAll --floatB  ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL17_dR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighAk4/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_17_HighAk4/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region SR --doAll --floatB  ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL17_dR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighAk4/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_17_HighAk4/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region CRDY --doAll --floatB  ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL17_dR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighAk4/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_17_HighAk4/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region CRTT --doAll --floatB  ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16_dR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighAk4/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16_HighAk4/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region SR --doAll --floatB  ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16_dR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighAk4/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_16_HighAk4/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region CRDY --doAll --floatB  ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16_dR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighAk4/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_16_HighAk4/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region CRTT --doAll --floatB  ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV_dR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighAk4/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16APV_HighAk4/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region SR --doAll --floatB  ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV_dR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighAk4/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_16APV_HighAk4/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region CRDY --doAll --floatB  ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV_dR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighAk4/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_16APV_HighAk4/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region CRTT --doAll --floatB  ;
wait


