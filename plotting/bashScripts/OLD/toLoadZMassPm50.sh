#!/bin/bash--toLoad

# Z Mass pm 50
python plotter_vh.py ZH/samples_withSF_nocuts_UL18.py ZH/plots_forCards_ZMassPm50.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/ZMassPm50_18  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/ZMassPm50_18 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17.py ZH/plots_forCards_ZMassPm50.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/ZMassPm50_17  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/ZMassPm50_17 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16.py ZH/plots_forCards_ZMassPm50.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/ZMassPm50_16  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/ZMassPm50_16 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV.py ZH/plots_forCards_ZMassPm50.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/ZMassPm50_16APV  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/ZMassPm50_16APV --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_RunII.py ZH/plots_forCards_ZMassPm50.txt -l 137.8 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/ZMassPm50_{YEAR}  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/ZMassPm50_RunII --plotAll --strict-order ;
wait