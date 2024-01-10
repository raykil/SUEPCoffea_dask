#!/bin/bash

# Default
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_PU.py ZH/plots_forCardsCRTT_highPU.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/highPU_CRTT_18  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/highPU_CRTT_18 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_PU.py ZH/plots_forCardsCRTT_highPU.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/highPU_CRTT_17  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/highPU_CRTT_17 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_PU.py ZH/plots_forCardsCRTT_highPU.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/highPU_CRTT_16  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/highPU_CRTT_16 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_PU.py ZH/plots_forCardsCRTT_highPU.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/highPU_CRTT_16APV  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/highPU_CRTT_16APV --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_RunII_PU.py ZH/plots_forCardsCRTT_highPU.txt -l 137.8 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/highPU_CRTT_{YEAR}  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/highPU_CRTT_RunII --plotAll --strict-order ;
wait