#!/bin/bash

#CRTT
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_dR.py ZH/plots_forCards_CRTT_2D_dR_ZMassPm50.py -l 59.9 --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_2D_18_ZMassPm50  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_2D_18_ZMassPm50 ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_dR.py ZH/plots_forCards_CRTT_2D_dR_ZMassPm50.py -l 41.6 --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_2D_17_ZMassPm50  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_2D_17_ZMassPm50 ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_dR.py ZH/plots_forCards_CRTT_2D_dR_ZMassPm50.py -l 16.4 --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_2D_16_ZMassPm50  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_2D_16_ZMassPm50 ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_dR.py ZH/plots_forCards_CRTT_2D_dR_ZMassPm50.py -l 19.9 --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_2D_16APV_ZMassPm50  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_2D_16APV_ZMassPm50 ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_RunII_dR.py ZH/plots_forCards_CRTT_2D_dR_ZMassPm50.py -l 137.8 --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_2D_{YEAR}_ZMassPm50  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRTT_2D_RunII_ZMassPm50 ;