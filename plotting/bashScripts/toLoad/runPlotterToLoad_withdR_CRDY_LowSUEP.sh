#!/bin/bash

# Default
python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV.py ZH/plots_forCardsCRDY_withDeltaR_LowSUEP.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRDY_withdRCut_LowSUEP_16APV  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_withdRCut_LowSUEP_16APV --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_RunII.py ZH/plots_forCardsCRDY_withDeltaR_LowSUEP.txt -l 137.8 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRDY_withdRCut_LowSUEP_{YEAR}  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/CRDY_withdRCut_LowSUEP_RunII --plotAll --strict-order ;
wait