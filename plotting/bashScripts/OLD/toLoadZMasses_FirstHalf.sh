#!/bin/bash--toLoad

# Z Mass pm 50
python plotter_vh.py ZH/samples_withSF_nocuts_RunII_CR.py ZH/plots_forCards_ZMassPm50.txt -l 137.8 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/ZMassPm50_{YEAR}  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/ZMassPm50_RunII --plotAll --strict-order ;
wait

# Z Mass pm 32p5
python plotter_vh.py ZH/samples_withSF_nocuts_RunII_CR.py ZH/plots_forCards_ZMassPm32p5.txt -l 137.8 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/ZMassPm32p5_{YEAR}  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/ZMassPm32p5_RunII --plotAll --strict-order ;
wait