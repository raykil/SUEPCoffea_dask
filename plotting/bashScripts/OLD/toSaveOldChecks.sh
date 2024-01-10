#!/bin/bash

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_p4.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/p4  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/p4_Jobs --plotAll --resubmit --queue workday --blind
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_p8.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/p8  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/p8_Jobs --plotAll --resubmit --queue workday --blind
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_1p2.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/1p2  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/1p2_Jobs --plotAll --resubmit --queue workday --blind
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_2p0.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/2p0  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/2p0_Jobs --plotAll --resubmit --queue workday --blind
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_4p0.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/4p0  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/4p0_Jobs --plotAll --resubmit --queue workday --blind
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_NewID.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/NewID  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/NewID_Jobs --plotAll --resubmit --queue workday --blind
wait
