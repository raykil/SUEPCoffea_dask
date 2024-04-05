#!/bin/bash

# Default
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_dR.py ZH/plots_forCards_withDeltaR.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_18  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_18_All --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_dR.py ZH/plots_forCards_withDeltaR.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_17  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_17_All --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_dR.py ZH/plots_forCards_withDeltaR.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_16  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16_All --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_dR.py ZH/plots_forCards_withDeltaR.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_16APV  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16APV_All --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_RunII_dR.py ZH/plots_forCards_withDeltaR.txt -l 137.8 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_{YEAR}  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_RunII_All --plotAll --strict-order ;
wait