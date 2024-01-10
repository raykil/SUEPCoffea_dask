#!/bin/bash

#Default
python plotter_vh.py ZH/samples_withSF_nocuts_UL18.py ZH/plots_forCards_OnShellBTag_Tight.py -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/user/gdecastr/Histos/OnShellBTight_18  --batchsize 100 --jobname  /eos/cms/store/user/gdecastr/Histos/OnShellBTight_18_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17.py ZH/plots_forCards_OnShellBTag_Tight.py -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/user/gdecastr/Histos/OnShellBTight_17  --batchsize 100 --jobname  /eos/cms/store/user/gdecastr/Histos/OnShellBTight_17_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16.py ZH/plots_forCards_OnShellBTag_Tight.py -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/user/gdecastr/Histos/OnShellBTight_16  --batchsize 100 --jobname  /eos/cms/store/user/gdecastr/Histos/OnShellBTight_16_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV.py ZH/plots_forCards_OnShellBTag_Tight.py -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/user/gdecastr/Histos/OnShellBTight_16APV  --batchsize 100 --jobname  /eos/cms/store/user/gdecastr/Histos/OnShellBTight_16APV_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18.py ZH/plots_OnShellBTagTight_2D.py -l 59.9 --toSave /eos/cms/store/user/gdecastr/Histos/OnShellBTight_2D_18  --batchsize 100 --jobname  /eos/cms/store/user/gdecastr/Histos/OnShellBTight_2D_18_Jobs --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17.py ZH/plots_OnShellBTagTight_2D.py -l 41.6 --toSave /eos/cms/store/user/gdecastr/Histos/OnShellBTight_2D_17  --batchsize 100 --jobname  /eos/cms/store/user/gdecastr/Histos/OnShellBTight_2D_17_Jobs --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16.py ZH/plots_OnShellBTagTight_2D.py -l 16.4 --toSave /eos/cms/store/user/gdecastr/Histos/OnShellBTight_2D_16  --batchsize 100 --jobname  /eos/cms/store/user/gdecastr/Histos/OnShellBTight_2D_16_Jobs --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV.py ZH/plots_OnShellBTagTight_2D.py -l 19.9 --toSave /eos/cms/store/user/gdecastr/Histos/OnShellBTight_2D_16APV  --batchsize 100 --jobname  /eos/cms/store/user/gdecastr/Histos/OnShellBTight_2D_16APV_Jobs --resubmit --queue workday ;
wait