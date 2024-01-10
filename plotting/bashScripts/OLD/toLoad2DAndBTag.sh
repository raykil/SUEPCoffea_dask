#!/bin/bash

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_CR.py ZH/plots_forCardsCRDY_LOW_mLL_2D.py -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_LOW_mLL_18_2D  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRDY_LOW_mLL_18_2D --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_CR.py ZH/plots_forCards_OnShellBTag.py -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShellB_Loose  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/OnShellB_Loose --blind --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_CR.py ZH/plots_forCards_OnShellBTag_Medium.py -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShellB_Medium  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/OnShellB_Medium --blind --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_CR.py ZH/plots_forCards_OnShellBTag_Tight.py -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShellB_Tight  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/OnShellB_Tight --blind --plotAll --strict-order ;
wait