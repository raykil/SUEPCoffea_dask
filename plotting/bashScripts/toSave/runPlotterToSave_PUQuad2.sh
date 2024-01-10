#!/bin/bash

#Default
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_PU.py ZH/plots_forCardsCRDY_PUQuad2.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/PUQuad2_CRDY_18  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/PUQuad2_CRDY_18_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_PU.py ZH/plots_forCardsCRDY_PUQuad2.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/PUQuad2_CRDY_17  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/PUQuad2_CRDY_17_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_PU.py ZH/plots_forCardsCRDY_PUQuad2.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/PUQuad2_CRDY_16  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/PUQuad2_CRDY_16_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_PU.py ZH/plots_forCardsCRDY_PUQuad2.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/PUQuad2_CRDY_16APV  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/PUQuad2_CRDY_16APV_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_PU.py ZH/plots_forCardsCRTT_PUQuad2.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/PUQuad2_CRTT_18  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/PUQuad2_CRTT_18_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_PU.py ZH/plots_forCardsCRTT_PUQuad2.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/PUQuad2_CRTT_17  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/PUQuad2_CRTT_17_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_PU.py ZH/plots_forCardsCRTT_PUQuad2.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/PUQuad2_CRTT_16  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/PUQuad2_CRTT_16_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_PU.py ZH/plots_forCardsCRTT_PUQuad2.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/PUQuad2_CRTT_16APV  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/PUQuad2_CRTT_16APV_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_PU.py ZH/plots_forCards_PUQuad2.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/PUQuad2_18  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/PUQuad2_18_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_PU.py ZH/plots_forCards_PUQuad2.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/PUQuad2_17  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/PUQuad2_17_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_PU.py ZH/plots_forCards_PUQuad2.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/PUQuad2_16  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/PUQuad2_16_Jobs --plotAll --resubmit --queue workday ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_PU.py ZH/plots_forCards_PUQuad2.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toSave /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/PUQuad2_16APV  --batchsize 100 --jobname  /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/PUQuad2_16APV_Jobs --plotAll --resubmit --queue workday ;
wait