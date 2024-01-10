#!/bin/bash

# Default
python plotter_vh.py ZH/samples_withSF_nocuts_UL18.py ZH/plots_forCardsRecoil60.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/user/gdecastr/Histos/Recoil60_18  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil60_18 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17.py ZH/plots_forCardsRecoil60.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/user/gdecastr/Histos/Recoil60_17  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil60_17 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16.py ZH/plots_forCardsRecoil60.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/user/gdecastr/Histos/Recoil60_16  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil60_16 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV.py ZH/plots_forCardsRecoil60.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/user/gdecastr/Histos/Recoil60_16APV  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil60_16APV --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_RunII.py ZH/plots_forCardsRecoil60.txt -l 137.8 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/user/gdecastr/Histos/Recoil60_{YEAR}  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Recoil60_RunII --plotAll --strict-order ;
wait