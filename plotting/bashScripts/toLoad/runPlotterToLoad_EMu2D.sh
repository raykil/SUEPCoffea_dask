#!/bin/bash

#CRTT
python plotter_vh.py ZH/samples_withSF_nocuts_UL18_dR_HighStats_EMu.py ZH/plots_forCards_EMu_2D_dR.py -l 59.9 --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/EMu_2D_18  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/EMu_2D_18 --addLines 20,0,20,1000 --addLines 10,0,10,1000 --addLines 0,100,100,100 --addLines 0,250,100,250 --addText A:60,20:0.05 --addText B1:60,120:0.05 --addText B2:60,270:0.05 --addText C1:12,20:0.05 --addText D1:12,120:0.05 --addText E1:12,270:0.05 --addText C2:3,20:0.05 --addText D2:3,120:0.05 --addText E2:3,270:0.05 ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL17_dR_HighStats_EMu.py ZH/plots_forCards_EMu_2D_dR.py -l 41.6 --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/EMu_2D_17  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/EMu_2D_17 --addLines 20,0,20,1000 --addLines 10,0,10,1000 --addLines 0,100,100,100 --addLines 0,250,100,250 --addText A:60,20:0.05 --addText B1:60,120:0.05 --addText B2:60,270:0.05 --addText C1:12,20:0.05 --addText D1:12,120:0.05 --addText E1:12,270:0.05 --addText C2:3,20:0.05 --addText D2:3,120:0.05 --addText E2:3,270:0.05 ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16_dR_HighStats_EMu.py ZH/plots_forCards_EMu_2D_dR.py -l 16.4 --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/EMu_2D_16  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/EMu_2D_16 --addLines 20,0,20,1000 --addLines 10,0,10,1000 --addLines 0,100,100,100 --addLines 0,250,100,250 --addText A:60,20:0.05 --addText B1:60,120:0.05 --addText B2:60,270:0.05 --addText C1:12,20:0.05 --addText D1:12,120:0.05 --addText E1:12,270:0.05 --addText C2:3,20:0.05 --addText D2:3,120:0.05 --addText E2:3,270:0.05 ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_UL16APV_dR_HighStats_EMu.py ZH/plots_forCards_EMu_2D_dR.py -l 19.9 --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/EMu_2D_16APV  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/EMu_2D_16APV --addLines 20,0,20,1000 --addLines 10,0,10,1000 --addLines 0,100,100,100 --addLines 0,250,100,250 --addText A:60,20:0.05 --addText B1:60,120:0.05 --addText B2:60,270:0.05 --addText C1:12,20:0.05 --addText D1:12,120:0.05 --addText E1:12,270:0.05 --addText C2:3,20:0.05 --addText D2:3,120:0.05 --addText E2:3,270:0.05 ;
wait

python plotter_vh.py ZH/samples_withSF_nocuts_RunII_EMu.py ZH/plots_forCards_EMu_2D_dR.py -l 137.8 --toLoad /eos/cms/store/group/phys_exotica/SUEPs/ZH_Histos/EMu_2D_{YEAR}  --plotdir /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/EMu_2D_RunII --addLines 20,0,20,1000 --addLines 10,0,10,1000 --addLines 0,100,100,100 --addLines 0,250,100,250 --addText A:60,20:0.05 --addText B1:60,120:0.05 --addText B2:60,270:0.05 --addText C1:12,20:0.05 --addText D1:12,120:0.05 --addText E1:12,270:0.05 --addText C2:3,20:0.05 --addText D2:3,120:0.05 --addText E2:3,270:0.05 ;
