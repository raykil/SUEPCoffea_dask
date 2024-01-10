#!/bin/bash

python datacardMaker.py ZH/samples_withSF_nocuts_UL17.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/LowMassCRDY/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDYLowMass_17/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region SR --thispoint SUEP_hadronic_mS125_mD3.00_T3.00 --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL18.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/LowMassCRDY/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDYLowMass_18/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region SR --thispoint SUEP_hadronic_mS125_mD3.00_T3.00 --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/LowMassCRDY/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDYLowMass_16/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region SR --thispoint SUEP_hadronic_mS125_mD3.00_T3.00 --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/LowMassCRDY/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDYLowMass_16APV/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region SR --thispoint SUEP_hadronic_mS125_mD3.00_T3.00 --floatB ;
wait
