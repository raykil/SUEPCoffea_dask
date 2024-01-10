#!/bin/bash

#Default
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_PU.py ZH/plots_forCardsCRDY_lowPU.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/lowPU_CRDY_18  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/lowPU_CRDY_18_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_PU.py ZH/plots_forCardsCRDY_lowPU.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/lowPU_CRDY_17  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/lowPU_CRDY_17_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_PU.py ZH/plots_forCardsCRDY_lowPU.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/lowPU_CRDY_16  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/lowPU_CRDY_16_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_PU.py ZH/plots_forCardsCRDY_lowPU.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/lowPU_CRDY_16APV  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/lowPU_CRDY_16APV_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_PU.py ZH/plots_forCardsCRTT_lowPU.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/lowPU_CRTT_18  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/lowPU_CRTT_18_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_PU.py ZH/plots_forCardsCRTT_lowPU.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/lowPU_CRTT_17  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/lowPU_CRTT_17_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_PU.py ZH/plots_forCardsCRTT_lowPU.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/lowPU_CRTT_16  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/lowPU_CRTT_16_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_PU.py ZH/plots_forCardsCRTT_lowPU.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/lowPU_CRTT_16APV  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/lowPU_CRTT_16APV_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_PU.py ZH/plots_forCards_lowPU.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/lowPU_18  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/lowPU_18_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_PU.py ZH/plots_forCards_lowPU.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/lowPU_17  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/lowPU_17_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_PU.py ZH/plots_forCards_lowPU.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/lowPU_16  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/lowPU_16_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_PU.py ZH/plots_forCards_lowPU.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/lowPU_16APV  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/lowPU_16APV_Jobs --plotAll --resubmit --queue workday ;
wait