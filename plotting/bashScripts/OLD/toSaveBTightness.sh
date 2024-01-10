#!/bin/bash

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_CR.py ZH/plots_forCards_OnShellBTag.py -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShellB_Loose  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShellB_Loose_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_CR.py ZH/plots_forCards_OnShellBTag_Medium.py -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShellB_Medium  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShellB_Medium_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_CR.py ZH/plots_forCards_OnShellBTag_Tight.py -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShellB_Tight  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShellB_Tight_Jobs --plotAll --resubmit --queue workday
wait
