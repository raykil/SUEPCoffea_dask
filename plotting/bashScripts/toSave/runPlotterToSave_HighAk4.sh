#!/bin/bash

#Default
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_dR.py ZH/plots_forCards_withDeltaR_HighAk4.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_18_HighAk4  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_18_Jobs_HighAk4 --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_dR.py ZH/plots_forCards_withDeltaR_HighAk4.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_17_HighAk4  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_17_Jobs_HighAk4 --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_dR.py ZH/plots_forCards_withDeltaR_HighAk4.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_16_HighAk4  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_16_Jobs_HighAk4 --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_dR.py ZH/plots_forCards_withDeltaR_HighAk4.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_16APV_HighAk4  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_16APV_Jobs_HighAk4 --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_dR.py ZH/plots_forCards_withDeltaR_CRTT_HighAk4.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_18_HighAk4  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_18_Jobs_HighAk4 --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_dR.py ZH/plots_forCards_withDeltaR_CRTT_HighAk4.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_17_HighAk4  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_17_Jobs_HighAk4 --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_dR.py ZH/plots_forCards_withDeltaR_CRTT_HighAk4.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_16_HighAk4  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_16_Jobs_HighAk4 --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_dR.py ZH/plots_forCards_withDeltaR_CRTT_HighAk4.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_16APV_HighAk4  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_16APV_Jobs_HighAk4 --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_dR.py ZH/plots_forCards_withDeltaR_CRDY_HighAk4.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRDY_18_HighAk4  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRDY_18_Jobs_HighAk4 --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_dR.py ZH/plots_forCards_withDeltaR_CRDY_HighAk4.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRDY_17_HighAk4  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRDY_17_Jobs_HighAk4 --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_dR.py ZH/plots_forCards_withDeltaR_CRDY_HighAk4.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRDY_16_HighAk4  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRDY_16_Jobs_HighAk4 --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_dR.py ZH/plots_forCards_withDeltaR_CRDY_HighAk4.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRDY_16APV_HighAk4  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRDY_16APV_Jobs_HighAk4 --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_dR.py ZH/plots_forCards_Default_2D_dR_HighAk4.py -l 59.9 --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/Default_2D_18_HighAk4  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/Default_2D_18_Jobs_HighAk4 --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_dR.py ZH/plots_forCards_Default_2D_dR_HighAk4.py -l 41.6 --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/Default_2D_17_HighAk4  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/Default_2D_17_Jobs_HighAk4 --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_dR.py ZH/plots_forCards_Default_2D_dR_HighAk4.py -l 16.4 --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/Default_2D_16_HighAk4  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/Default_2D_16_Jobs_HighAk4 --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_dR.py ZH/plots_forCards_Default_2D_dR_HighAk4.py -l 19.9 --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/Default_2D_16APV_HighAk4  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/Default_2D_16APV_Jobs_HighAk4 --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_dR.py ZH/plots_forCards_CRTT_2D_dR_HighAk4.py -l 59.9 --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_2D_18_HighAk4  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_2D_18_Jobs_HighAk4 --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_dR.py ZH/plots_forCards_CRTT_2D_dR_HighAk4.py -l 41.6 --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_2D_17_HighAk4  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_2D_17_Jobs_HighAk4 --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_dR.py ZH/plots_forCards_CRTT_2D_dR_HighAk4.py -l 16.4 --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_2D_16_HighAk4  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_2D_16_Jobs_HighAk4 --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_dR.py ZH/plots_forCards_CRTT_2D_dR_HighAk4.py -l 19.9 --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_2D_16APV_HighAk4  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_2D_16APV_Jobs_HighAk4 --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_dR.py ZH/plots_forCards_CRDY_2D_dR_HighAk4.py -l 59.9 --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRDY_2D_18_HighAk4  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRDY_2D_18_Jobs_HighAk4 --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_dR.py ZH/plots_forCards_CRDY_2D_dR_HighAk4.py -l 41.6 --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRDY_2D_17_HighAk4  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRDY_2D_17_Jobs_HighAk4 --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_dR.py ZH/plots_forCards_CRDY_2D_dR_HighAk4.py -l 16.4 --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRDY_2D_16_HighAk4  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRDY_2D_16_Jobs_HighAk4 --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_dR.py ZH/plots_forCards_CRDY_2D_dR_HighAk4.py -l 19.9 --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRDY_2D_16APV_HighAk4  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRDY_2D_16APV_Jobs_HighAk4 --resubmit --queue workday ;
wait