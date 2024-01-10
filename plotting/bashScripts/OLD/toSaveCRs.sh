#!/bin/bash

#TTBar CR
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_CR.py ZH/plots_forCardsCRTT.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRTT_18  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRTT_18_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_CR.py ZH/plots_forCardsCRTT.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRTT_17  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRTT_17_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_CR.py ZH/plots_forCardsCRTT.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRTT_16  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRTT_16_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_CR.py ZH/plots_forCardsCRTT.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRTT_16APV  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRTT_16APV_Jobs --plotAll --resubmit --queue workday
wait
#DY CR
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_CR.py ZH/plots_forCardsCRDY.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_18  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_18_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_CR.py ZH/plots_forCardsCRDY.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_17  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_17_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_CR.py ZH/plots_forCardsCRDY.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_16  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_16_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_CR.py ZH/plots_forCardsCRDY.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_16APV  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_16APV_Jobs --plotAll --resubmit --queue workday
wait
