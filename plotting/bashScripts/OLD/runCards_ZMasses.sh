#!/bin/bash

# pm 10
python datacardMaker.py ZH/samples_withSF_nocuts_UL18_CR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm10/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/ZMassPm10_18/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL17_CR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm10/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/ZMassPm10_17/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16_CR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm10/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/ZMassPm10_16/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV_CR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm10/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/ZMassPm10_16APV/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region SR --doAll --floatB ;
wait


# pm 50
python datacardMaker.py ZH/samples_withSF_nocuts_UL18_CR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm50/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/ZMassPm50_18/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL17_CR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm50/2017 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/ZMassPm50_17/leadclustertracks --var leadclustertracks --ABCD --year 2017 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16_CR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm50/2016 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/ZMassPm50_16/leadclustertracks --var leadclustertracks --ABCD --year 2016 --region SR --doAll --floatB ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL16APV_CR.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards/ZMassPm50/2016APV --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/ZMassPm50_16APV/leadclustertracks --var leadclustertracks --ABCD --year 2016APV --region SR --doAll --floatB ;
wait