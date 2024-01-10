#!/bin/bash

#Default
python plotter_vh.py ZH/samples_withSF_nocuts_UL18.py ZH/plots_dRBreakdown_DY.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/dR_CRDY_18  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/dR_CRDY_18_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17.py ZH/plots_dRBreakdown_DY.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/dR_CRDY_17  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/dR_CRDY_17_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16.py ZH/plots_dRBreakdown_DY.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/dR_CRDY_16  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/dR_CRDY_16_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV.py ZH/plots_dRBreakdown_DY.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/dR_CRDY_16APV  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/dR_CRDY_16APV_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18.py ZH/plots_dRBreakdown_TT.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/dR_CRTT_18  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/dR_CRTT_18_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17.py ZH/plots_dRBreakdown_TT.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/dR_CRTT_17  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/dR_CRTT_17_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16.py ZH/plots_dRBreakdown_TT.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/dR_CRTT_16  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/dR_CRTT_16_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV.py ZH/plots_dRBreakdown_TT.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/dR_CRTT_16APV  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/dR_CRTT_16APV_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18.py ZH/plots_dRBreakdown_SR.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/dR_SR_18  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/dR_SR_18_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17.py ZH/plots_dRBreakdown_SR.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/dR_SR_17  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/dR_SR_17_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16.py ZH/plots_dRBreakdown_SR.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/dR_SR_16  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/dR_SR_16_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV.py ZH/plots_dRBreakdown_SR.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/dR_SR_16APV  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/dR_SR_16APV_Jobs --plotAll --resubmit --queue workday ;
wait