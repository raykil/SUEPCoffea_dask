#!/bin/bash

#Default
python plotter_vh.py ZH/samples_withSF_nocuts_UL18.py ZH/plots_forCards_SUEPpT50_2D.py -l 59.9 --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SUEPpT50_2D_18  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SUEPpT50_2D_18 ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17.py ZH/plots_forCards_SUEPpT50_2D.py -l 41.6 --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SUEPpT50_2D_17  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SUEPpT50_2D_17 ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16.py ZH/plots_forCards_SUEPpT50_2D.py -l 16.4 --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SUEPpT50_2D_16  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SUEPpT50_2D_16 ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV.py ZH/plots_forCards_SUEPpT50_2D.py -l 19.9 --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SUEPpT50_2D_16APV  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SUEPpT50_2D_16APV ;
wait