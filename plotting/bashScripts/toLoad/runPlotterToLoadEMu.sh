#!/bin/bash

# Default
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_dR_HighStats_EMu.py ZH/plots_forCardsEMu_dR.txt -l 59.9 --systFile ZH/systs_fullcorr_MC_EMuNoJec.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/EMu_18  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/EMu_18 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_dR_HighStats_EMu.py ZH/plots_forCardsEMu_dR.txt -l 41.6 --systFile ZH/systs_fullcorr_MC_EMuNoJec.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/EMu_17  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/EMu_17 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_dR_HighStats_EMu.py ZH/plots_forCardsEMu_dR.txt -l 16.4 --systFile ZH/systs_fullcorr_MC_EMuNoJec.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/EMu_16  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/EMu_16 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_dR_HighStats_EMu.py ZH/plots_forCardsEMu_dR.txt -l 19.9 --systFile ZH/systs_fullcorr_MC_EMuNoJec.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/EMu_16APV  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/EMu_16APV --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_RunII_dR_HighStats_EMu.py ZH/plots_forCardsEMu_dR.txt -l 137.8 --systFile ZH/systs_fullcorr_MC_EMuNoJec.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/EMu_{YEAR}  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/EMu_RunII --plotAll --strict-order ;
wait