#!/bin/bash

#DY CR

python plotter_vh.py ZH/samples_withSF_nocuts_UL18.py ZH/plots_forCardsCRDY.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/Histos/CRDY_18  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/Histos/CRDY_18_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17.py ZH/plots_forCardsCRDY.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/Histos/CRDY_17  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/Histos/CRDY_17_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16.py ZH/plots_forCardsCRDY.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/Histos/CRDY_16  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/Histos/CRDY_16_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV.py ZH/plots_forCardsCRDY.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/Histos/CRDY_16APV  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/Histos/CRDY_16APV_Jobs --plotAll --resubmit --queue workday
wait
