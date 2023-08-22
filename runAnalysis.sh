#!/bin/bash

python doAnalysis.py dataframes --output /eos/user/g/gdecastr/SUEPCoffea_dask/differentRadii_Updated/AkT_p4 -y 2018 --SR --analyzer ZH_simple_withsyst_AkT_p4 --submit
wait
python doAnalysis.py dataframes --output /eos/user/g/gdecastr/SUEPCoffea_dask/differentRadii_Updated/AkT_p8 -y 2018 --SR --analyzer ZH_simple_withsyst_AkT_p8 --submit
wait
python doAnalysis.py dataframes --output /eos/user/g/gdecastr/SUEPCoffea_dask/differentRadii_Updated/AkT_1p2 -y 2018 --SR --analyzer ZH_simple_withsyst_AkT_1p2 --submit
wait
python doAnalysis.py dataframes --output /eos/user/g/gdecastr/SUEPCoffea_dask/differentRadii_Updated/AkT_1p5 -y 2018 --SR --analyzer ZH_simple_withsyst_AkT_1p5 --submit
wait
python doAnalysis.py dataframes --output /eos/user/g/gdecastr/SUEPCoffea_dask/differentRadii_Updated/AkT_1p5_NewID -y 2018 --SR --analyzer ZH_simple_withsyst_AkT_1p5_NewID --submit
wait
python doAnalysis.py dataframes --output /eos/user/g/gdecastr/SUEPCoffea_dask/differentRadii_Updated/AkT_1p5_Light -y 2018 --SR --analyzer ZH_simple_withsyst_AkT_1p5_Light --submit
wait
python doAnalysis.py dataframes --output /eos/user/g/gdecastr/SUEPCoffea_dask/differentRadii_Updated/AkT_2p0 -y 2018 --SR --analyzer ZH_simple_withsyst_AkT_2p0 --submit
wait
python doAnalysis.py dataframes --output /eos/user/g/gdecastr/SUEPCoffea_dask/differentRadii_Updated/AkT_4p0 -y 2018 --SR --analyzer ZH_simple_withsyst_AkT_4p0 --submit
wait
python doAnalysis.py dataframes --output /eos/user/g/gdecastr/SUEPCoffea_dask/differentRadii_Updated/Cambridge_p4 -y 2018 --SR --analyzer ZH_simple_withsyst_Cambridge_p4 --submit
wait
python doAnalysis.py dataframes --output /eos/user/g/gdecastr/SUEPCoffea_dask/differentRadii_Updated/Cambridge_p8 -y 2018 --SR --analyzer ZH_simple_withsyst_Cambridge_p8 --submit
wait
python doAnalysis.py dataframes --output /eos/user/g/gdecastr/SUEPCoffea_dask/differentRadii_Updated/Cambridge_1p2 -y 2018 --SR --analyzer ZH_simple_withsyst_Cambridge_1p2 --submit
wait
python doAnalysis.py dataframes --output /eos/user/g/gdecastr/SUEPCoffea_dask/differentRadii_Updated/Cambridge_1p5 -y 2018 --SR --analyzer ZH_simple_withsyst_Cambridge_1p5 --submit
wait
python doAnalysis.py dataframes --output /eos/user/g/gdecastr/SUEPCoffea_dask/differentRadii_Updated/Cambridge_1p5_Light -y 2018 --SR --analyzer ZH_simple_withsyst_Cambridge_1p5_Light --submit
wait
python doAnalysis.py dataframes --output /eos/user/g/gdecastr/SUEPCoffea_dask/differentRadii_Updated/Cambridge_2p0 -y 2018 --SR --analyzer ZH_simple_withsyst_Cambridge_2p0 --submit
wait
python doAnalysis.py dataframes --output /eos/user/g/gdecastr/SUEPCoffea_dask/differentRadii_Updated/Cambridge_4p0 -y 2018 --SR --analyzer ZH_simple_withsyst_Cambridge_4p0 --submit
