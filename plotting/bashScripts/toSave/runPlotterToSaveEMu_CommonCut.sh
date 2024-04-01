#!/bin/bash

#Default
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_dR_HighStats_EMu.py ZH/plots_forCardsEMu_dR_CommonCut.txt -l 59.9 --systFile ZH/systs_fullcorr_MC_EMuNoJec.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/EMu_18_CommonBounds_Fixed  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/EMu_18_Jobs_CommonBounds --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_dR_HighStats_EMu.py ZH/plots_forCardsEMu_dR_CommonCut.txt -l 41.6 --systFile ZH/systs_fullcorr_MC_EMuNoJec.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/EMu_17_CommonBounds_Fixed  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/EMu_17_Jobs_CommonBounds --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_dR_HighStats_EMu.py ZH/plots_forCardsEMu_dR_CommonCut.txt -l 16.4 --systFile ZH/systs_fullcorr_MC_EMuNoJec.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/EMu_16_CommonBounds_Fixed  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/EMu_16_Jobs_CommonBounds --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_dR_HighStats_EMu.py ZH/plots_forCardsEMu_dR_CommonCut.txt -l 19.9 --systFile ZH/systs_fullcorr_MC_EMuNoJec.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/EMu_16APV_CommonBounds_Fixed  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/EMu_16APV_Jobs_CommonBounds --plotAll --resubmit --queue workday ;
wait