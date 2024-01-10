#!/bin/bash

python datacardMaker.py ZH/samples_withSF_nocuts_UL18_p4.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisCards_p4/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/p4/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region SR --doAll --floatB --blind ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL18_p8.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisCards_p8/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/p8/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region SR --doAll --floatB --blind ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL18_1p2.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisCards_1p2/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/1p2/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region SR --doAll --floatB --blind ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL18_2p0.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisCards_2p0/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/2p0/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region SR --doAll --floatB --blind ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL18_4p0.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisCards_4p0/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/4p0/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region SR --doAll --floatB --blind ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL18_NewID.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisCards_NewID/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/NewID/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region SR --doAll --floatB --blind ;
wait

python datacardMaker.py ZH/samples_withSF_nocuts_UL18.py ZH/systs_fullcorr.py /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisCards_Default/2018 --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/Default_18_Blind/leadclustertracks --var leadclustertracks --ABCD --year 2018 --region SR --doAll --floatB --blind ;
wait