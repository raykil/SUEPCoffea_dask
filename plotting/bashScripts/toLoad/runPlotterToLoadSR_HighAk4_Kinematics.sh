#!/bin/bash

# Default
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_dR.py ZH/plots_HighAk4_Kinematics.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_18_HighAk4_Kinematics --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_18_HighAk4_Kinematics --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_dR.py ZH/plots_HighAk4_Kinematics.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_17_HighAk4_Kinematics --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_17_HighAk4_Kinematics --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_dR.py ZH/plots_HighAk4_Kinematics.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_16_HighAk4_Kinematics --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16_HighAk4_Kinematics --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_dR.py ZH/plots_HighAk4_Kinematics.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_16APV_HighAk4_Kinematics --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16APV_HighAk4_Kinematics --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_RunII_dR.py ZH/plots_HighAk4_Kinematics.txt -l 137.8 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_{YEAR}_HighAk4_Kinematics --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_RunII_HighAk4_Kinematics --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_dR.py ZH/plots_HighAk4_Kinematics_A.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_18_HighAk4_Kinematics_A --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_18_HighAk4_Kinematics_A --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_dR.py ZH/plots_HighAk4_Kinematics_A.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_17_HighAk4_Kinematics_A --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_17_HighAk4_Kinematics_A --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_dR.py ZH/plots_HighAk4_Kinematics_A.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_16_HighAk4_Kinematics_A --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16_HighAk4_Kinematics_A --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_dR.py ZH/plots_HighAk4_Kinematics_A.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_16APV_HighAk4_Kinematics_A --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16APV_HighAk4_Kinematics_A --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_RunII_dR.py ZH/plots_HighAk4_Kinematics_A.txt -l 137.8 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_{YEAR}_HighAk4_Kinematics_A --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_RunII_HighAk4_Kinematics_A --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL18_dR.py ZH/plots_HighAk4_Kinematics_A_Nt30.txt -l 59.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_18_HighAk4_Kinematics_A_Nt30 --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_18_HighAk4_Kinematics_A_Nt30 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_dR.py ZH/plots_HighAk4_Kinematics_A_Nt30.txt -l 41.6 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_17_HighAk4_Kinematics_A_Nt30 --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_17_HighAk4_Kinematics_A_Nt30 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_dR.py ZH/plots_HighAk4_Kinematics_A_Nt30.txt -l 16.4 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_16_HighAk4_Kinematics_A_Nt30 --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16_HighAk4_Kinematics_A_Nt30 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_dR.py ZH/plots_HighAk4_Kinematics_A_Nt30.txt -l 19.9 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_16APV_HighAk4_Kinematics_A_Nt30 --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_16APV_HighAk4_Kinematics_A_Nt30 --plotAll --strict-order ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_RunII_dR.py ZH/plots_HighAk4_Kinematics_A_Nt30.txt -l 137.8 --systFile ZH/systs_fullcorr_MC.py --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/SR_{YEAR}_HighAk4_Kinematics_A_Nt30 --plotdir  /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/SR_RunII_HighAk4_Kinematics_A_Nt30 --plotAll --strict-order ;
wait