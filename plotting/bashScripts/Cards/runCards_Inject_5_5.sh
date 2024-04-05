#!/bin/bash
python datacardMaker.py ZH/samples_withSF_nocuts_UL17_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Blind/Inject_5_5/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_17_HighStats/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region SR --floatB --blind_withS --doAll ; 
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL17_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Blind/Inject_5_5/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_17_HighStats/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region CRDY --floatB --blind_withS --doAll ; 
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL17_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Blind/Inject_5_5/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_17_HighStats/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region CRTT --floatB --blind_withS --doAll ; 
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Blind/Inject_5_5/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16_HighStats/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region SR --floatB --blind_withS --doAll ; 
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Blind/Inject_5_5/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_16_HighStats/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region CRDY --floatB --blind_withS --doAll ; 
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Blind/Inject_5_5/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_16_HighStats/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region CRTT --floatB --blind_withS --doAll ; 
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Blind/Inject_5_5/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16APV_HighStats/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region SR --floatB --blind_withS --doAll ; 
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Blind/Inject_5_5/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_16APV_HighStats/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region CRDY --floatB --blind_withS --doAll ; 
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV_dR_HighStats.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/Blind/Inject_5_5/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_16APV_HighStats/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region CRTT --floatB --blind_withS --doAll ; 
wait


