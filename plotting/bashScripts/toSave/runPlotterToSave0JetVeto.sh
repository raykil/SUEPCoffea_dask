#!/bin/bash

#Default
python plotter_vh.py ZH/samples_withSF_nocuts_UL18.py ZH/plots_forCards_0JetVeto.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/user/gdecastr/Histos/0JetVeto_18  --batchsize 100 --jobname  /eos/cms/store/user/gdecastr/Histos/0JetVeto_18_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17.py ZH/plots_forCards_0JetVeto.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/user/gdecastr/Histos/0JetVeto_17  --batchsize 100 --jobname  /eos/cms/store/user/gdecastr/Histos/0JetVeto_17_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16.py ZH/plots_forCards_0JetVeto.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/user/gdecastr/Histos/0JetVeto_16  --batchsize 100 --jobname  /eos/cms/store/user/gdecastr/Histos/0JetVeto_16_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV.py ZH/plots_forCards_0JetVeto.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/user/gdecastr/Histos/0JetVeto_16APV  --batchsize 100 --jobname  /eos/cms/store/user/gdecastr/Histos/0JetVeto_16APV_Jobs --plotAll --resubmit --queue workday ;
wait