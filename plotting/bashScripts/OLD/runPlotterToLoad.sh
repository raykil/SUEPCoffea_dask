#!/bin/bash

#Default
python plotter_vh.py ZH/samples_withSF_nocuts_UL18.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Default_18  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/Default_18 --plotAll --strict-order ;


python plotter_vh.py ZH/samples_withSF_nocuts_UL17.py ZH/plots_forCards.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Default_17  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/Default_17 --plotAll --strict-order ;


python plotter_vh.py ZH/samples_withSF_nocuts_UL16.py ZH/plots_forCards.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Default_16  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/Default_16 --plotAll --strict-order ;


python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV.py ZH/plots_forCards.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Default_16APV  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/Default_16APV --plotAll --strict-order ;

#TTBar CR
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_CR.py ZH/plots_forCardsCRTT.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRTT_18  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRTT_18 --plotAll --strict-order ;


python plotter_vh.py ZH/samples_withSF_nocuts_UL17_CR.py ZH/plots_forCardsCRTT.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRTT_17  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRTT_17 --plotAll --strict-order ;


python plotter_vh.py ZH/samples_withSF_nocuts_UL16_CR.py ZH/plots_forCardsCRTT.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRTT_16  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRTT_16 --plotAll --strict-order ;


python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_CR.py ZH/plots_forCardsCRTT.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRTT_16APV  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRTT_16APV --plotAll --strict-order ;

#DY CR
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_CR.py ZH/plots_forCardsCRDY.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_18  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRDY_18 --plotAll --strict-order ;


python plotter_vh.py ZH/samples_withSF_nocuts_UL17_CR.py ZH/plots_forCardsCRDY.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_17  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRDY_17 --plotAll --strict-order ;


python plotter_vh.py ZH/samples_withSF_nocuts_UL16_CR.py ZH/plots_forCardsCRDY.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_16  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRDY_16 --plotAll --strict-order ;


python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_CR.py ZH/plots_forCardsCRDY.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_16APV  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRDY_16APV --plotAll --strict-order ;

#AkT
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_p4.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/p4  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/p4 --plotAll --strict-order 

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_p8.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/p8  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/p8 --plotAll --strict-order 

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_1p2.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/1p2  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/1p2 --plotAll --strict-order 

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_2p0.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/2p0  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/2p0 --plotAll --strict-order 

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_4p0.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/4p0  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/4p0 --plotAll --strict-order 

#Cambridge
#python plotter_vh.py ZH/samples_withSF_nocuts_UL18_Cam_p4.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Cambridge_p4  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/Cambridge_p4 --plotAll --strict-order 
#

#python plotter_vh.py ZH/samples_withSF_nocuts_UL18_Cam_p8.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Cambridge_p8  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/Cambridge_p8 --plotAll --strict-order 
#

#python plotter_vh.py ZH/samples_withSF_nocuts_UL18_Cam_1p2.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Cambridge_1p2  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/Cambridge_1p2 --plotAll --strict-order 
#

#python plotter_vh.py ZH/samples_withSF_nocuts_UL18_Cam.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Cambridge  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/Cambridge --plotAll --strict-order 
#

#python plotter_vh.py ZH/samples_withSF_nocuts_UL18_Cam_2p0.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Cambridge_2p0  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/Cambridge_2p0 --plotAll --strict-order 
#

#python plotter_vh.py ZH/samples_withSF_nocuts_UL18_Cam_4p0.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/4p0  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/4p0 --plotAll --strict-order ;
#
#NEW ID
#python plotter_vh.py ZH/samples_withSF_nocuts_UL18_NewID.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/NewID  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/NewID --plotAll --strict-order ;
#

#python plotter_vh.py ZH/samples_withSF_nocuts_UL18_NewID_CR.py ZH/plots_forCardsCRTT.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRTT_NewID  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRTT_NewID --plotAll --strict-order ;
#

#python plotter_vh.py ZH/samples_withSF_nocuts_UL18_NewID_CR.py ZH/plots_forCardsCRDY.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/CRDY_NewID  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/CRDY_NewID --plotAll --strict-order ;
#

#ThinZMass
python plotter_vh.py ZH/samples_withSF_nocuts_UL18.py ZH/plots_forCards_ThinZMass.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/ThinZMass_18  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/ThinZMass_18 --plotAll --strict-order ;


python plotter_vh.py ZH/samples_withSF_nocuts_UL17.py ZH/plots_forCards_ThinZMass.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/ThinZMass_17  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/ThinZMass_17 --plotAll --strict-order ;


python plotter_vh.py ZH/samples_withSF_nocuts_UL16.py ZH/plots_forCards_ThinZMass.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/ThinZMass_16  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/ThinZMass_16 --plotAll --strict-order ;


python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV.py ZH/plots_forCards_ThinZMass.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/ThinZMass_16APV  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/ThinZMass_16APV --plotAll --strict-order ;


#0 Jet Veto
python plotter_vh.py ZH/samples_withSF_nocuts_UL18.py ZH/plots_forCards_0JetVeto.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/0JetVeto_18  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/0JetVeto_18 --plotAll --strict-order ;


python plotter_vh.py ZH/samples_withSF_nocuts_UL17.py ZH/plots_forCards_0JetVeto.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/0JetVeto_17  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/0JetVeto_17 --plotAll --strict-order ;


python plotter_vh.py ZH/samples_withSF_nocuts_UL16.py ZH/plots_forCards_0JetVeto.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/0JetVeto_16  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/0JetVeto_16 --plotAll --strict-order ;


python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV.py ZH/plots_forCards_0JetVeto.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/0JetVeto_16APV  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/0JetVeto_16APV --plotAll --strict-order ;


# Max 3 Jet
python plotter_vh.py ZH/samples_withSF_nocuts_UL18.py ZH/plots_forCards_Max3Jet.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Max3Jet_18  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/Max3Jet_18 --plotAll --strict-order ;


python plotter_vh.py ZH/samples_withSF_nocuts_UL17.py ZH/plots_forCards_Max3Jet.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Max3Jet_17  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/Max3Jet_17 --plotAll --strict-order ;


python plotter_vh.py ZH/samples_withSF_nocuts_UL16.py ZH/plots_forCards_Max3Jet.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Max3Jet_16  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/Max3Jet_16 --plotAll --strict-order ;


python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV.py ZH/plots_forCards_Max3Jet.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Max3Jet_16APV  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/Max3Jet_16APV --plotAll --strict-order ;


# On-Shell B-jet
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_CR.py ZH/plots_forCards_OnShellBJet.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShellBJet_18  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/OnShellBJet_18 --plotAll --strict-order ;


python plotter_vh.py ZH/samples_withSF_nocuts_UL17_CR.py ZH/plots_forCards_OnShellBJet.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShellBJet_17  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/OnShellBJet_17 --plotAll --strict-order ;


python plotter_vh.py ZH/samples_withSF_nocuts_UL16_CR.py ZH/plots_forCards_OnShellBJet.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShellBJet_16  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/OnShellBJet_16 --plotAll --strict-order ;


python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_CR.py ZH/plots_forCards_OnShellBJet.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnShellBJet_16APV  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/OnShellBJet_16APV --plotAll --strict-order ;

#LJpT30
python plotter_vh.py ZH/samples_withSF_nocuts_UL18.py ZH/plots_forCards_LJpT30.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/LJpT30_18  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/LJpT30_18 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17.py ZH/plots_forCards_LJpT30.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/LJpT30_17  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/LJpT30_17 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16.py ZH/plots_forCards_LJpT30.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/LJpT30_16  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/LJpT30_16 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV.py ZH/plots_forCards_LJpT30.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/LJpT30_16APV --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/Default_16APV --plotAll --strict-order ;
wait

#Bump Test
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_CR.py ZH/plots_forCards_NoCut.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/NoCut_18  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/NoCut_18 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_CR.py ZH/plots_forCards_OnlypT.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/OnlypT_18  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/OnlypT_18 --plotAll --strict-order ;
wait