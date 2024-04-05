#!/bin/bash

#EMu
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_dR_HighStats_EMu.py ZH/plots_forCards_EMu_2D_dR.py -l 59.9 --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/EMu_2D_18  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/EMu_2D_18_Jobs --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_dR_HighStats_EMu.py ZH/plots_forCards_EMu_2D_dR.py -l 41.6 --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/EMu_2D_17  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/EMu_2D_17_Jobs --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_dR_HighStats_EMu.py ZH/plots_forCards_EMu_2D_dR.py -l 16.4 --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/EMu_2D_16  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/EMu_2D_16_Jobs --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_dR_HighStats_EMu.py ZH/plots_forCards_EMu_2D_dR.py -l 19.9 --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/EMu_2D_16APV  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/EMu_2D_16APV_Jobs --resubmit --queue workday ;
wait