#!/bin/bash

# Default
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_dR_HighStats.py ZH/plots_forCardsSR_dR_CommonCut_Rebin.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_18_CommonBounds_Rebin  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_18_CommonBounds_Rebin  --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_dR_HighStats.py ZH/plots_forCardsSR_dR_CommonCut_Rebin.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_17_CommonBounds_Rebin  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_17_CommonBounds_Rebin  --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_dR_HighStats.py ZH/plots_forCardsSR_dR_CommonCut_Rebin.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_16_CommonBounds_Rebin  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16_CommonBounds_Rebin  --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_dR_HighStats.py ZH/plots_forCardsSR_dR_CommonCut_Rebin.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_16APV_CommonBounds_Rebin  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16APV_CommonBounds_Rebin  --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_RunII_dR_HighStats.py ZH/plots_forCardsSR_dR_CommonCut_Rebin.txt -l 137.8 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_{YEAR}_CommonBounds_Rebin  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_RunII_CommonBounds_Rebin  --plotAll --strict-order ;
wait