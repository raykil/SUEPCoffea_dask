#!/bin/bash

python datacardMaker.py ZH/samples_withSF_nocuts_UL17_CR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/CRDY/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRDY_17_v2/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region CRDY --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL17_CR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/CRTT/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRTT_17_v2/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region CRTT --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL18_CR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/CRDY/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRDY_18_v2/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region CRDY --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL18_CR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/CRTT/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRTT_18_v2/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region CRTT --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16_CR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/CRDY/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRDY_16_v2/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region CRDY --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16_CR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/CRTT/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRTT_16_v2/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region CRTT --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV_CR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/CRDY/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRDY_16APV_v2/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region CRDY --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV_CR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/CRTT/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRTT_16APV_v2/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region CRTT --doAll --floatB ;
wait