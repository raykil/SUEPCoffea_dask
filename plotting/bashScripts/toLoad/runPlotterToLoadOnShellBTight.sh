#!/bin/bash

# Default
python plotter_vh.py ZH/samples_withSF_nocuts_UL18.py ZH/plots_forCards_OnShellBTag_Tight.py -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/user/gdecastr/Histos/OnShellBTight_18  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/OnShellBTight_18 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17.py ZH/plots_forCards_OnShellBTag_Tight.py -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/user/gdecastr/Histos/OnShellBTight_17  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/OnShellBTight_17 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16.py ZH/plots_forCards_OnShellBTag_Tight.py -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/user/gdecastr/Histos/OnShellBTight_16  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/OnShellBTight_16 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV.py ZH/plots_forCards_OnShellBTag_Tight.py -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/user/gdecastr/Histos/OnShellBTight_16APV  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/OnShellBTight_16APV --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_RunII.py ZH/plots_forCards_OnShellBTag_Tight.py -l 137.8 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/user/gdecastr/Histos/OnShellBTight_{YEAR}  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/OnShellBTight_RunII --plotAll --strict-order ;
wait
#2D
python plotter_vh.py ZH/samples_withSF_nocuts_UL18.py ZH/plots_OnShellBTagTight_2D.py -l 59.9 --toLoad /eos/cms/store/user/gdecastr/Histos/OnShellBTight_2D_18  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/OnShellBTight_2D_18 ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17.py ZH/plots_OnShellBTagTight_2D.py -l 41.6 --toLoad /eos/cms/store/user/gdecastr/Histos/OnShellBTight_2D_17  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/OnShellBTight_2D_17 ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16.py ZH/plots_OnShellBTagTight_2D.py -l 16.4 --toLoad /eos/cms/store/user/gdecastr/Histos/OnShellBTight_2D_16  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/OnShellBTight_2D_16 ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV.py ZH/plots_OnShellBTagTight_2D.py -l 19.9 --toLoad /eos/cms/store/user/gdecastr/Histos/OnShellBTight_2D_16APV  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/OnShellBTight_2D_16APV ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_RunII.py ZH/plots_OnShellBTagTight_2D.py -l 137.8 --toLoad /eos/cms/store/user/gdecastr/Histos/OnShellBTight_2D_{YEAR}  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/OnShellBTight_2D_RunII ;
wait