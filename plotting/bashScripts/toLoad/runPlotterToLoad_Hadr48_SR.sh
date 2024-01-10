#!/bin/bash

# Default
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_Hadronic_4_8.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/Histos/SR_18 --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_Hadr48_18 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_Hadronic_4_8.py ZH/plots_forCards.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/Histos/SR_17  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_Hadr48_17 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_Hadronic_4_8.py ZH/plots_forCards.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/Histos/SR_16  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_Hadr48_16 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_Hadronic_4_8.py ZH/plots_forCards.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/Histos/SR_16APV  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_Hadr48_16APV --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_RunII_Hadronic_4_8.py ZH/plots_forCards.txt -l 137.8 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/Histos/SR_{YEAR}  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_Hadr48_RunII --plotAll --strict-order ;
wait