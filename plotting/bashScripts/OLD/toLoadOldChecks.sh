#!/bin/bash

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_p4.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/p4  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/p4 --blind --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_p8.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/p8  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/p8 --blind --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_1p2.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/1p2  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/1p2 --blind --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_2p0.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/2p0  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/2p0 --blind --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_4p0.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/4p0  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/4p0 --blind --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_NewID.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/NewID  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/NewID --blind --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18.py ZH/plots_forCards.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisHistos/Default_18  --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/doAnalysisPlots/Default_18_Blind --blind --plotAll --strict-order ;
wait

