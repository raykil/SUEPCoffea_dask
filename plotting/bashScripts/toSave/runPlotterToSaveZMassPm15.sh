#!/bin/bash

#Default
python plotter_vh.py ZH/samples_withSF_nocuts_UL18.py ZH/plots_forCards_ZMassPm15.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/user/gdecastr/Histos/ZMassPm15_18  --batchsize 100 --jobname  /eos/cms/store/user/gdecastr/Histos/ZMassPm15_18_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17.py ZH/plots_forCards_ZMassPm15.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/user/gdecastr/Histos/ZMassPm15_17  --batchsize 100 --jobname  /eos/cms/store/user/gdecastr/Histos/ZMassPm15_17_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16.py ZH/plots_forCards_ZMassPm15.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/user/gdecastr/Histos/ZMassPm15_16  --batchsize 100 --jobname  /eos/cms/store/user/gdecastr/Histos/ZMassPm15_16_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV.py ZH/plots_forCards_ZMassPm15.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/user/gdecastr/Histos/ZMassPm15_16APV  --batchsize 100 --jobname  /eos/cms/store/user/gdecastr/Histos/ZMassPm15_16APV_Jobs --plotAll --resubmit --queue workday ;
wait