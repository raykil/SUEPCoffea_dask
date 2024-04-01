#!/bin/bash

python datacardMaker_RunII.py ZH/samples_withSF_nocuts_RunII_dR_HighStats.py ZH/systs_fullcorr_RunII.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/ManualMC_Merged_Integrate45/RunII --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_RunII_CommonBounds_Fixed/leadclustertracks --var leadclustertracks --ABCD --year RunII --region SR --floatB --doAll --integrateBins 6 --ManualMCStats ;

python datacardMaker_RunII.py ZH/samples_withSF_nocuts_RunII_dR_HighStats.py ZH/systs_fullcorr_RunII.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/Blind/ManualMC_Merged_Integrate45/RunII --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_RunII_CommonBounds_Fixed/leadclustertracks --var leadclustertracks --ABCD --year RunII --region SR --floatB --doAll --blind --integrateBins 6 --ManualMCStats ;


python datacardMaker_RunII.py ZH/samples_withSF_nocuts_RunII_dR_HighStats.py ZH/systs_fullcorr_RunII.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/ManualMC_Merged_Integrate45/RunII --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_RunII_CommonBounds_Fixed/leadclustertracks --var leadclustertracks --ABCD --year RunII --region CRDY --floatB --doAll --integrateBins 6 --ManualMCStats ;

python datacardMaker_RunII.py ZH/samples_withSF_nocuts_RunII_dR_HighStats.py ZH/systs_fullcorr_RunII.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/Blind/ManualMC_Merged_Integrate45/RunII --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_RunII_CommonBounds_Fixed/leadclustertracks --var leadclustertracks --ABCD --year RunII --region CRDY --floatB --doAll --blind --integrateBins 6 --ManualMCStats ;


python datacardMaker_RunII.py ZH/samples_withSF_nocuts_RunII_dR_HighStats.py ZH/systs_fullcorr_RunII.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/ManualMC_Merged_Integrate45/RunII --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_RunII_CommonBounds_Fixed/leadclustertracks --var leadclustertracks --ABCD --year RunII --region CRTT --floatB --doAll --integrateBins 6 --ManualMCStats ;

python datacardMaker_RunII.py ZH/samples_withSF_nocuts_RunII_dR_HighStats.py ZH/systs_fullcorr_RunII.py /eos/user/g/gdecastr/SUEPCoffea_dask/Cards_CommonBounds_Fixed/Blind/ManualMC_Merged_Integrate45/RunII --rootfile /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_RunII_CommonBounds_Fixed/leadclustertracks --var leadclustertracks --ABCD --year RunII --region CRTT --floatB --doAll --blind --integrateBins 6 --ManualMCStats ;
