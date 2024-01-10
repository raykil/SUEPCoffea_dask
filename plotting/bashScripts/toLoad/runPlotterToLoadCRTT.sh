#!/bin/bash

# Default
python plotter_vh.py ZH/samples_withSF_nocuts_UL18.py ZH/plots_forCardsCRTT.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/Histos/CRTT_18  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_18 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17.py ZH/plots_forCardsCRTT.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/Histos/CRTT_17  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_17 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16.py ZH/plots_forCardsCRTT.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/Histos/CRTT_16  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_16 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV.py ZH/plots_forCardsCRTT.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/Histos/CRTT_16APV  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_16APV --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_RunII.py ZH/plots_forCardsCRTT.txt -l 137.8 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/Histos/CRTT_{YEAR}  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_RunII --plotAll --strict-order ;
wait