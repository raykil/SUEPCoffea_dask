#!/bin/bash

# Default
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_dR.py ZH/plots_Kinematics.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_18_Kinematics --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_18_Kinematics --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_dR.py ZH/plots_Kinematics.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_17_Kinematics --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_17_Kinematics --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_dR.py ZH/plots_Kinematics.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_16_Kinematics --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16_Kinematics --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_dR.py ZH/plots_Kinematics.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_16APV_Kinematics --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16APV_Kinematics --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_RunII_dR.py ZH/plots_Kinematics.txt -l 137.8 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_{YEAR}_Kinematics --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_RunII_Kinematics --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_dR.py ZH/plots_Kinematics_A.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_18_Kinematics_A --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_18_Kinematics_A --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_dR.py ZH/plots_Kinematics_A.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_17_Kinematics_A --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_17_Kinematics_A --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_dR.py ZH/plots_Kinematics_A.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_16_Kinematics_A --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16_Kinematics_A --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_dR.py ZH/plots_Kinematics_A.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_16APV_Kinematics_A --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16APV_Kinematics_A --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_RunII_dR.py ZH/plots_Kinematics_A.txt -l 137.8 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_{YEAR}_Kinematics_A --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_RunII_Kinematics_A --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_dR.py ZH/plots_Kinematics_A_Nt30.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_18_Kinematics_A_Nt30 --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_18_Kinematics_A_Nt30 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_dR.py ZH/plots_Kinematics_A_Nt30.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_17_Kinematics_A_Nt30 --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_17_Kinematics_A_Nt30 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_dR.py ZH/plots_Kinematics_A_Nt30.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_16_Kinematics_A_Nt30 --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16_Kinematics_A_Nt30 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_dR.py ZH/plots_Kinematics_A_Nt30.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_16APV_Kinematics_A_Nt30 --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16APV_Kinematics_A_Nt30 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_RunII_dR.py ZH/plots_Kinematics_A_Nt30.txt -l 137.8 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_{YEAR}_Kinematics_A_Nt30 --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_RunII_Kinematics_A_Nt30 --plotAll --strict-order ;
wait