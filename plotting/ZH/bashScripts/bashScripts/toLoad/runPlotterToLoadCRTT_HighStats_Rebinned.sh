#!/bin/bash

# Default
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_dR_HighStats.py ZH/plots_forCards_withDeltaR_CRTT_Rebinned.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_18_Rebinned  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_18_Rebinned --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_dR_HighStats.py ZH/plots_forCards_withDeltaR_CRTT_Rebinned.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_17_Rebinned  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_17_Rebinned --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_dR_HighStats.py ZH/plots_forCards_withDeltaR_CRTT_Rebinned.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_16_Rebinned  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_16_Rebinned --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_dR_HighStats.py ZH/plots_forCards_withDeltaR_CRTT_Rebinned.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_16APV_Rebinned  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_16APV_Rebinned --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_RunII_dR_HighStats.py ZH/plots_forCards_withDeltaR_CRTT_Rebinned.txt -l 137.8 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_{YEAR}_Rebinned  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_RunII_Rebinned --plotAll --strict-order ;
wait