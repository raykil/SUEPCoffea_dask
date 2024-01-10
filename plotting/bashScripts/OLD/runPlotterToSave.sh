#!/bin/bash

#Default
python plotter_vh.py ZH/samples_withSF_nocuts_UL18.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Default_18  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Default_18_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17.py ZH/plots_forCards.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Default_17  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Default_17_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16.py ZH/plots_forCards.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Default_16  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Default_16_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV.py ZH/plots_forCards.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Default_16APV  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Default_16APV_Jobs --plotAll --resubmit --queue workday
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
wait
#AkT
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

#ThinZMass
python plotter_vh.py ZH/samples_withSF_nocuts_UL18.py ZH/plots_forCards_ThinZMass.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/ThinZMass_18  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/ThinZMass_18_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17.py ZH/plots_forCards_ThinZMass.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/ThinZMass_17  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/ThinZMass_17_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16.py ZH/plots_forCards_ThinZMass.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/ThinZMass_16  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/ThinZMass_16_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV.py ZH/plots_forCards_ThinZMass.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/ThinZMass_16APV  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/ThinZMass_16APV_Jobs --plotAll --resubmit --queue workday
wait

#0 Jet Veto
python plotter_vh.py ZH/samples_withSF_nocuts_UL18.py ZH/plots_forCards_0JetVeto.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/0JetVeto_18  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/0JetVeto_18_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17.py ZH/plots_forCards_0JetVeto.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/0JetVeto_17  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/0JetVeto_17_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16.py ZH/plots_forCards_0JetVeto.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/0JetVeto_16  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/0JetVeto_16_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV.py ZH/plots_forCards_0JetVeto.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/0JetVeto_16APV  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/0JetVeto_16APV_Jobs --plotAll --resubmit --queue workday
wait

# Max 3 Jet
python plotter_vh.py ZH/samples_withSF_nocuts_UL18.py ZH/plots_forCards_Max3Jet.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Max3Jet_18  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Max3Jet_18_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17.py ZH/plots_forCards_Max3Jet.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Max3Jet_17  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Max3Jet_17_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16.py ZH/plots_forCards_Max3Jet.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Max3Jet_16  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Max3Jet_16_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV.py ZH/plots_forCards_Max3Jet.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Max3Jet_16APV  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Max3Jet_16APV_Jobs --plotAll --resubmit --queue workday
wait

# On-Shell B-jet
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_CR.py ZH/plots_forCards_OnShellBJet.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShellBJet_18  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShellBJet_18_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_CR.py ZH/plots_forCards_OnShellBJet.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShellBJet_17  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShellBJet_17_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_CR.py ZH/plots_forCards_OnShellBJet.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShellBJet_16  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShellBJet_16_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_CR.py ZH/plots_forCards_OnShellBJet.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShellBJet_16APV  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShellBJet_16APV_Jobs --plotAll --resubmit --queue workday
wait

#LJpT30
python plotter_vh.py ZH/samples_withSF_nocuts_UL18.py ZH/plots_forCards_LJpT30.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/LJpT30_18  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/LJpT30_18_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17.py ZH/plots_forCards_LJpT30.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/LJpT30_17  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/LJpT30_17_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16.py ZH/plots_forCards_LJpT30.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/LJpT30_16  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/LJpT30_16_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV.py ZH/plots_forCards_LJpT30.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/LJpT30_16APV  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Default_16APV_Jobs --plotAll --resubmit --queue workday
wait

#Bump Test
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_CR.py ZH/plots_forCards_NoCut.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/NoCut_18  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/NoCut_18_Jobs --plotAll --resubmit --queue workday
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_CR.py ZH/plots_forCards_OnlypT.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnlypT_18  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnlypT_18_Jobs --plotAll --resubmit --queue workday
wait



#Cambridge
#python plotter_vh.py ZH/samples_withSF_nocuts_UL18_Cam_p4.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Cambridge_p4  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Cambridge_p4_Jobs --plotAll --resubmit --queue workday --blind
#wait

#python plotter_vh.py ZH/samples_withSF_nocuts_UL18_Cam_p8.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Cambridge_p8  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Cambridge_p8_Jobs --plotAll --resubmit --queue workday --blind
#wait

#python plotter_vh.py ZH/samples_withSF_nocuts_UL18_Cam_1p2.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Cambridge_1p2  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Cambridge_1p2_Jobs --plotAll --resubmit --queue workday --blind
#wait

#python plotter_vh.py ZH/samples_withSF_nocuts_UL18_Cam.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Cambridge  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Cambridge_Jobs --plotAll --resubmit --queue workday --blind
#wait

#python plotter_vh.py ZH/samples_withSF_nocuts_UL18_Cam_2p0.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Cambridge_2p0  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Cambridge_2p0_Jobs --plotAll --resubmit --queue workday --blind
#wait

#python plotter_vh.py ZH/samples_withSF_nocuts_UL18_Cam_4p0.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/4p0  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/4p0_Jobs --plotAll --resubmit --queue workday
#wait
#NEW ID
#python plotter_vh.py ZH/samples_withSF_nocuts_UL18_NewID.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/NewID  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/NewID_Jobs --plotAll --resubmit --queue workday
#wait

#python plotter_vh.py ZH/samples_withSF_nocuts_UL18_NewID_CR.py ZH/plots_forCardsCRTT.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRTT_NewID  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRTT_NewID_Jobs --plotAll --resubmit --queue workday
#wait

#python plotter_vh.py ZH/samples_withSF_nocuts_UL18_NewID_CR.py ZH/plots_forCardsCRDY.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_NewID  --batchsize 100 --jobname  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_NewID_Jobs --plotAll --resubmit --queue workday
#wait