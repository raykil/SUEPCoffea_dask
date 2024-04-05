#!/bin/bash

python datacardMaker_RunII.py ZH/samples_withSF_nocuts_RunII_dR_HighStats.py ZH/systs_fullcorr_RunII.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/ManualMC_Merged/RunII --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_RunII_CommonBounds_Fixed/leadclustertracks --var leadclustertracks --ABCD --year RunII --region SR --floatB --doAll --ManualMCStats ;

python datacardMaker_RunII.py ZH/samples_withSF_nocuts_RunII_dR_HighStats.py ZH/systs_fullcorr_RunII.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/Blind/ManualMC_Merged/RunII --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_RunII_CommonBounds_Fixed/leadclustertracks --var leadclustertracks --ABCD --year RunII --region SR --floatB --doAll --blind --ManualMCStats ;


python datacardMaker_RunII.py ZH/samples_withSF_nocuts_RunII_dR_HighStats.py ZH/systs_fullcorr_RunII.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/ManualMC_Merged/RunII --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_RunII_CommonBounds_Fixed/leadclustertracks --var leadclustertracks --ABCD --year RunII --region CRDY --floatB --doAll --ManualMCStats ;

python datacardMaker_RunII.py ZH/samples_withSF_nocuts_RunII_dR_HighStats.py ZH/systs_fullcorr_RunII.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/Blind/ManualMC_Merged/RunII --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_RunII_CommonBounds_Fixed/leadclustertracks --var leadclustertracks --ABCD --year RunII --region CRDY --floatB --doAll --blind --ManualMCStats ;


python datacardMaker_RunII.py ZH/samples_withSF_nocuts_RunII_dR_HighStats.py ZH/systs_fullcorr_RunII.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/ManualMC_Merged/RunII --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_RunII_CommonBounds_Fixed/leadclustertracks --var leadclustertracks --ABCD --year RunII --region CRTT --floatB --doAll --ManualMCStats ;

python datacardMaker_RunII.py ZH/samples_withSF_nocuts_RunII_dR_HighStats.py ZH/systs_fullcorr_RunII.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/Blind/ManualMC_Merged/RunII --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_RunII_CommonBounds_Fixed/leadclustertracks --var leadclustertracks --ABCD --year RunII --region CRTT --floatB --doAll --blind --ManualMCStats ;