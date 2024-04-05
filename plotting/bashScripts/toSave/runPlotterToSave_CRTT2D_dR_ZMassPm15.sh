#!/bin/bash

#CRTT
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_dR_HighStats.py ZH/plots_forCards_CRTT_2D_dR_ZMassPm15.py -l 59.9 --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_2D_18_ZMassPm15  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_2D_18_ZMassPm15_Jobs --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_dR_HighStats.py ZH/plots_forCards_CRTT_2D_dR_ZMassPm15.py -l 41.6 --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_2D_17_ZMassPm15  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_2D_17_ZMassPm15_Jobs --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_dR_HighStats.py ZH/plots_forCards_CRTT_2D_dR_ZMassPm15.py -l 16.4 --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_2D_16_ZMassPm15  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_2D_16_ZMassPm15_Jobs --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_dR_HighStats.py ZH/plots_forCards_CRTT_2D_dR_ZMassPm15.py -l 19.9 --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_2D_16APV_ZMassPm15  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_2D_16APV_ZMassPm15_Jobs --resubmit --queue workday ;
wait