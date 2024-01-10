#!/bin/bash

#TTBar CR
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_CR.py ZH/plots_forCardsCRDY_LOW.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_LOW_18  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_LOW_18_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_CR.py ZH/plots_forCardsCRDY_LOW.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_LOW_16APV  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_LOW_16APV_Jobs --plotAll --resubmit --queue workday
wait