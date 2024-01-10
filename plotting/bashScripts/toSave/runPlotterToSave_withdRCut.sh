#!/bin/bash

#Default
python plotter_vh.py ZH/samples_withSF_nocuts_UL18.py ZH/plots_forCardsCRDY_withDeltaR.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRDY_withdRCut_18  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRDY_withdRCut_18_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17.py ZH/plots_forCardsCRDY_withDeltaR.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRDY_withdRCut_17  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRDY_withdRCut_17_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16.py ZH/plots_forCardsCRDY_withDeltaR.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRDY_withdRCut_16  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRDY_withdRCut_16_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV.py ZH/plots_forCardsCRDY_withDeltaR.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRDY_withdRCut_16APV  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRDY_withdRCut_16APV_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18.py ZH/plots_forCardsCRTT_withDeltaR.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_withdRCut_18  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_withdRCut_18_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17.py ZH/plots_forCardsCRTT_withDeltaR.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_withdRCut_17 --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_withdRCut_17_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16.py ZH/plots_forCardsCRTT_withDeltaR.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_withdRCut_16 --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_withdRCut_16_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV.py ZH/plots_forCardsCRTT_withDeltaR.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_withdRCut_16APV  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/CRTT_withdRCut_16APV_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18.py ZH/plots_forCards_withDeltaR.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_withdRCut_18  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_withdRCut_18_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17.py ZH/plots_forCards_withDeltaR.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_withdRCut_17  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_withdRCut_17_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16.py ZH/plots_forCards_withDeltaR.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_withdRCut_16  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_withdRCut_16_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV.py ZH/plots_forCards_withDeltaR.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_withdRCut_16APV  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_withdRCut_16APV_Jobs --plotAll --resubmit --queue workday ;
wait