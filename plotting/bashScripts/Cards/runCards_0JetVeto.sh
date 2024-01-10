#!/bin/bash

python datacardMaker.py ZH/samples_withSF_nocuts_UL17.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/0JetVeto/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/0JetVeto_17/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL18.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/0JetVeto/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/0JetVeto_18/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/0JetVeto/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/0JetVeto_16/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/0JetVeto/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/0JetVeto_16APV/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region SR --doAll --floatB ;
wait
