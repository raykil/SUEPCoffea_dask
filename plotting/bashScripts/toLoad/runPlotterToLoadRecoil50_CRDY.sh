#!/bin/bash

#Default
python plotter_vh.py ZH/samples_withSF_nocuts_UL16.py ZH/plots_forCardsRecoil50_CRDY.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/Recoil50_CRDY_16  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil50_CRDY_16 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV.py ZH/plots_forCardsRecoil50_CRDY.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/Recoil50_CRDY_16APV  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil50_CRDY_16APV --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_RunII.py ZH/plots_forCardsRecoil50_CRDY.txt -l 137.8 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/Recoil50_CRDY_{YEAR}  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil50_CRDY_RunII --plotAll --strict-order ;
wait