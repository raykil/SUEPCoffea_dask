#!/bin/bash

#Default
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_dR.py ZH/plots_forCards_Default_2D_dR_ZMassPm5.py -l 59.9 --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/Default_2D_18_ZMassPm5  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Default_2D_18_ZMassPm5 ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_dR.py ZH/plots_forCards_Default_2D_dR_ZMassPm5.py -l 41.6 --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/Default_2D_17_ZMassPm5  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Default_2D_17_ZMassPm5 ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_dR.py ZH/plots_forCards_Default_2D_dR_ZMassPm5.py -l 16.4 --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/Default_2D_16_ZMassPm5  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Default_2D_16_ZMassPm5 ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_dR.py ZH/plots_forCards_Default_2D_dR_ZMassPm5.py -l 19.9 --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/Default_2D_16APV_ZMassPm5  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Default_2D_16APV_ZMassPm5 ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_RunII_dR.py ZH/plots_forCards_Default_2D_dR_ZMassPm5.py -l 137.8 --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/Default_2D_{YEAR}_ZMassPm5  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/Default_2D_RunII_ZMassPm5 ;
