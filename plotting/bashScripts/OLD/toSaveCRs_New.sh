#!/bin/bash

#CRDY mLL 1D
python plotter_vh.py ZH/samples_withSF_nocuts_RunII_CR.py ZH/plots_forCardsCRDY_LOW_mLL.txt -l 137.8 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_LOW_mLL_RunII  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_LOW_mLL_RunII_Jobs --plotAll --resubmit --queue workday ;
wait

#CRDY mLL 2D
python plotter_vh.py ZH/samples_withSF_nocuts_RunII_CR.py ZH/plots_forCardsCRDY_LOW_mLL_2D.py -l 137.8 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_LOW_mLL_RunII_2D  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_LOW_mLL_RunII_2D_Jobs --plotAll --resubmit --queue workday
wait

#Onshell BTag tight 1D
python plotter_vh.py ZH/samples_withSF_nocuts_RunII_CR.py ZH/plots_forCards_OnShellBTag_Tight.py -l 137.8 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShell_BTight_RunII --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShell_BTight_RunII_Jobs --plotAll --resubmit --queue workday
wait

#Onshell BTag tight 2D
python plotter_vh.py ZH/samples_withSF_nocuts_RunII_CR.py ZH/plots_OnShellBTagTight_2D.py -l 137.8 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShell_BTight_RunII_2D --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShell_BTight_RunII_2D_Jobs --plotAll --resubmit --queue workday
wait