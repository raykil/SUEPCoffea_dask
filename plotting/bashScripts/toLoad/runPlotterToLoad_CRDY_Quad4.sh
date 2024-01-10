#!/bin/bash

# Default
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_PU.py ZH/plots_forCardsCRDY_PUQuad4.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/PUQuad4_CRDY_18  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/PUQuad4_CRDY_18 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_PU.py ZH/plots_forCardsCRDY_PUQuad4.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/PUQuad4_CRDY_17  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/PUQuad4_CRDY_17 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_PU.py ZH/plots_forCardsCRDY_PUQuad4.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/PUQuad4_CRDY_16  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/PUQuad4_CRDY_16 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_PU.py ZH/plots_forCardsCRDY_PUQuad4.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/PUQuad4_CRDY_16APV  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/PUQuad4_CRDY_16APV --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_RunII_PU.py ZH/plots_forCardsCRDY_PUQuad4.txt -l 137.8 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/PUQuad4_CRDY_{YEAR}  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/PUQuad4_CRDY_RunII --plotAll --strict-order ;
wait