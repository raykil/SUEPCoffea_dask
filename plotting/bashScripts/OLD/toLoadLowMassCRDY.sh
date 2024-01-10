#!/bin/bash

#OnshellB Tight 2D Unblind
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_CR.py ZH/plots_forCardsCRDY_LOW_mLL_2D.py -l 59.9 --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_LOW_mLL_18_2D  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRDY_LOW_mLL_18_2D ;
wait
python plotter_vh.py ZH/samples_withSF_nocuts_UL17_CR.py ZH/plots_forCardsCRDY_LOW_mLL_2D.py -l 41.6 --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_LOW_mLL_17_2D  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRDY_LOW_mLL_17_2D ;
wait
python plotter_vh.py ZH/samples_withSF_nocuts_UL16_CR.py ZH/plots_forCardsCRDY_LOW_mLL_2D.py -l 16.4 --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_LOW_mLL_16_2D  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRDY_LOW_mLL_16_2D ;
wait
python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_CR.py ZH/plots_forCardsCRDY_LOW_mLL_2D.py -l 19.9 --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_LOW_mLL_16APV_2D  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRDY_LOW_mLL_16APV_2D ;
wait
python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_CR_RunII.py ZH/plots_forCardsCRDY_LOW_mLL_2D.py -l 137.8 --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_LOW_mLL_{YEAR}_2D  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRDY_LOW_mLL_RunII_2D ;w