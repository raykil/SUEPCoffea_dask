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

#Z Masses
python plotter_vh.py ZH/samples_withSF_nocuts_RunII_CR.py ZH/plots_forCards_ZMassPm5.txt -l 137.8 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/ZMass_Pm5_RunII  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/ZMass_Pm5_RunII_Jobs  --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_RunII_CR.py ZH/plots_forCards_ZMassPm10.txt -l 137.8 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/ZMass_Pm10_RunII   --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/ZMass_Pm10_RunII_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_RunII_CR.py ZH/plots_forCards_ZMassPm32p5.txt -l 137.8 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/ZMass_Pm32p5_RunII   --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/ZMass_Pm32p5_RunII_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_RunII_CR.py ZH/plots_forCards_ZMassPm50.txt -l 137.8 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/ZMass_Pm50_RunII   --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/ZMass_Pm50_RunII_Jobs --plotAll --resubmit --queue workday ;
wait