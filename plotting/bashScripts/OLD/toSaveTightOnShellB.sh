#!/bin/bash

#CRDY mLL 2D
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_CR.py ZH/plots_OnShellBTagTight_2D.py -l 59.9  --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShell_BTight_18_2D  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShell_BTight_18_2D_Jobs --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_CR.py ZH/plots_OnShellBTagTight_2D.py -l 41.6  --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShell_BTight_17_2D --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShell_BTight_17_2D_Jobs  --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_CR.py ZH/plots_OnShellBTagTight_2D.py -l 16.4  --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShell_BTight_16_2D  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShell_BTight_16_2D_Jobs --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_CR.py ZH/plots_OnShellBTagTight_2D.py -l 19.9  --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShell_BTight_16APV_2D  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShell_BTight_16APV_2D_Jobs --resubmit --queue workday
wait