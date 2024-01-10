#!/bin/bash

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_CR.py ZH/plots_forCardsCRDY_LOW_mLL.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_LOW_mLL_18  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRDY_LOW_mLL_18_BLIND --plotAll --strict-order --blind ;

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_CR.py ZH/plots_forCardsCRDY_LOW_mLL.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_LOW_mLL_17  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRDY_LOW_mLL_17_BLIND --plotAll --strict-order --blind ;

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_CR.py ZH/plots_forCardsCRDY_LOW_mLL.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_LOW_mLL_16  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRDY_LOW_mLL_16_BLIND --plotAll --strict-order --blind ;

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_CR.py ZH/plots_forCardsCRDY_LOW_mLL.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_LOW_mLL_16APV  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRDY_LOW_mLL_16APV_BLIND --plotAll --strict-order --blind ;

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_CR.py ZH/plots_forCardsCRDY_LOW_mLL.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_LOW_mLL_16APV  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRDY_LOW_mLL_16APV --plotAll --strict-order ;