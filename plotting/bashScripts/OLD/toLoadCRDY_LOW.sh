#!/bin/bash

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_CR.py ZH/plots_forCardsCRDY_LOW.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_LOW_18  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRDY_LOW_18 --plotAll --strict-order ;

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_CR.py ZH/plots_forCardsCRDY_LOW.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_LOW_17  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRDY_LOW_17 --plotAll --strict-order ;

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_CR.py ZH/plots_forCardsCRDY_LOW.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_LOW_16  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRDY_LOW_16 --plotAll --strict-order ;

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_CR.py ZH/plots_forCardsCRDY_LOW.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_LOW_16APV  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRDY_LOW_16APV --plotAll --strict-order ;