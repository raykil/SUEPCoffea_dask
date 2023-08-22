from correctionlib import CorrectionSet
import rich
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


ceval = CorrectionSet.from_file("C:/Users/slatt/Downloads/POGJsons/masterJSON_singleTrigger.json")


## 2018 Muons
ceval_muon18_POG = CorrectionSet.from_file("C:/Users/slatt/Downloads/POGJsons/muon_18.json")

pt_bins_muon_18 = [24,60,120,200]
pt_bins_muon_18_POG = [26.0,30.0,40.0,50.0,60.0,120.0,200.0]

muon_18_0_down = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf-down","Muon", 0.0, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf-down","Muon", 0.0, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf-down","Muon", 0.0, 199.9)]

muon_18_0 = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf","Muon", 0.0, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf","Muon", 0.0, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf","Muon", 0.0, 199.9)]
muon_18_0p9 = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf","Muon", 0.9, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf","Muon", 0.9, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf","Muon", 0.9, 199.9)]
muon_18_1p2 = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf","Muon", 1.2, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf","Muon", 1.2, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf","Muon", 1.2, 199.9)]
muon_18_2p1 = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf","Muon", 2.1, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf","Muon", 2.1, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf","Muon", 2.1, 199.9)]

muon_18_0_up = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf-up","Muon", 0.0, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf-up","Muon", 0.0, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf-up","Muon", 0.0, 199.9)]
muon_18_0p9_up = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf-up","Muon", 0.9, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf-up","Muon", 0.9, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf-up","Muon", 0.9, 199.9)]
muon_18_1p2_up = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf-up","Muon", 1.2, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf-up","Muon", 1.2, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf-up","Muon", 1.2, 199.9)]
muon_18_2p1_up = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf-up","Muon", 2.1, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf-up","Muon", 2.1, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf-up","Muon", 2.1, 199.9)]

muon_18_0_down = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf-down","Muon", 0.0, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf-down","Muon", 0.0, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf-down","Muon", 0.0, 199.9)]
muon_18_0p9_down = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf-down","Muon", 0.9, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf-down","Muon", 0.9, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf-down","Muon", 0.9, 199.9)]
muon_18_1p2_down = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf-down","Muon", 1.2, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf-down","Muon", 1.2, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf-down","Muon", 1.2, 199.9)]
muon_18_2p1_down = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf-down","Muon", 2.1, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf-down","Muon", 2.1, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2018',"sf-down","Muon", 2.1, 199.9)]

muon_18_0_POG = [ceval_muon18_POG['NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(0.0, 39.0,'nominal'),ceval_muon18_POG['NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(0.0, 49.0,'nominal'),ceval_muon18_POG['NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(0.0, 59.0,'nominal'),ceval_muon18_POG['NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 0.0, 119.0,'nominal'),ceval_muon18_POG['NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 0.0, 199.9,'nominal')]
muon_18_0p9_POG = [ceval_muon18_POG['NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(0.9, 39.0,'nominal'),ceval_muon18_POG['NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(0.9, 49.0,'nominal'),ceval_muon18_POG['NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 0.9, 59.0,'nominal'),ceval_muon18_POG['NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 0.9, 119.0,'nominal'),ceval_muon18_POG['NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 0.9, 199.9,'nominal')]
muon_18_1p2_POG = [ceval_muon18_POG['NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(1.9, 39.0,'nominal'),ceval_muon18_POG['NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(1.2, 49.0,'nominal'),ceval_muon18_POG['NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 1.2, 59.0,'nominal'),ceval_muon18_POG['NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 1.2, 119.0,'nominal'),ceval_muon18_POG['NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 1.2, 199.9,'nominal')]
muon_18_2p1_POG = [ceval_muon18_POG['NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(2.1, 39.0,'nominal'),ceval_muon18_POG['NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(2.1, 49.0,'nominal'),ceval_muon18_POG['NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 2.1, 59.0,'nominal'),ceval_muon18_POG['NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 2.1, 119.0,'nominal'),ceval_muon18_POG['NUM_IsoMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 2.1, 199.9,'nominal')]

colors =  ['r',None,'g','b','c','m', None, 'y', 'k']
plt.errorbar([84/2, 180/2, 320/2], muon_18_0, label = r'$0<|\eta|<0.9$', color = colors[0],  yerr = (muon_18_0_down, muon_18_0_up), fmt = 'o')
plt.errorbar([35, 45, 55, 180/2, 320/2], muon_18_0_POG, label = r'$0<|\eta|<0.9$ - POG', color = colors[0], marker = '^', fmt = 'o')
plt.errorbar([84/2, 180/2, 320/2], muon_18_0p9, label = r'$0.9<|\eta|<1.2$', color = colors[2],  yerr = (muon_18_0p9_down, muon_18_0p9_up), fmt = 'o')
plt.errorbar([35, 45, 55, 180/2, 320/2], muon_18_0p9_POG, label = r'$0.9<|\eta|<1.2$ - POG', color = colors[2], marker = '^', fmt = 'o')
plt.errorbar([84/2, 180/2, 320/2], muon_18_1p2, label = r'$1.2<|\eta|<2.1$', color = colors[4],  yerr = (muon_18_1p2_down, muon_18_1p2_up), fmt = 'o')
plt.errorbar([35, 45, 55, 180/2, 320/2], muon_18_1p2_POG, label = r'$1.2<|\eta|<2.1$ - POG', color = colors[4], marker = '^', fmt = 'o')
plt.errorbar([84/2, 180/2, 320/2], muon_18_2p1, label = r'$2.1<|\eta|<2.4$', color = colors[7],  yerr = (muon_18_2p1_down, muon_18_2p1_up), fmt = 'o')
plt.errorbar([35, 45, 55, 180/2, 320/2], muon_18_2p1_POG, label = r'$2.1<|\eta|<2.4$ - POG', color = colors[7], marker = '^', fmt = 'o')
plt.legend(loc =(.6,.5),prop={'size': 6})
plt.xlabel('Center of pT Bin')
plt.ylabel('Scale Factor')
plt.title('Muon 2018 POG Comparison')
#plt.show()
print(list(ceval.keys()))
plt.savefig('2018POGComparison_m.png', dpi = 2000)
plt.clf()


## 2017 Muons
ceval_muon17_POG = CorrectionSet.from_file("C:/Users/slatt/Downloads/POGJsons/muon_17.json")

pt_bins_muon_17 = [27,60,120,200]
pt_bins_muon_17_POG = [29.0,30.0,40.0,50.0,60.0,120.0,200.0]

muon_17_0_down = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf-down","Muon", 0.0, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf-down","Muon", 0.0, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf-down","Muon", 0.0, 199.9)]

muon_17_0 = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf","Muon", 0.0, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf","Muon", 0.0, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf","Muon", 0.0, 199.9)]
muon_17_0p9 = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf","Muon", 0.9, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf","Muon", 0.9, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf","Muon", 0.9, 199.9)]
muon_17_1p2 = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf","Muon", 1.2, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf","Muon", 1.2, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf","Muon", 1.2, 199.9)]
muon_17_2p1 = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf","Muon", 2.1, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf","Muon", 2.1, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf","Muon", 2.1, 199.9)]

muon_17_0_up = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf-up","Muon", 0.0, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf-up","Muon", 0.0, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf-up","Muon", 0.0, 199.9)]
muon_17_0p9_up = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf-up","Muon", 0.9, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf-up","Muon", 0.9, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf-up","Muon", 0.9, 199.9)]
muon_17_1p2_up = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf-up","Muon", 1.2, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf-up","Muon", 1.2, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf-up","Muon", 1.2, 199.9)]
muon_17_2p1_up = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf-up","Muon", 2.1, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf-up","Muon", 2.1, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf-up","Muon", 2.1, 199.9)]

muon_17_0_down = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf-down","Muon", 0.0, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf-down","Muon", 0.0, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf-down","Muon", 0.0, 199.9)]
muon_17_0p9_down = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf-down","Muon", 0.9, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf-down","Muon", 0.9, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf-down","Muon", 0.9, 199.9)]
muon_17_1p2_down = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf-down","Muon", 1.2, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf-down","Muon", 1.2, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf-down","Muon", 1.2, 199.9)]
muon_17_2p1_down = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf-down","Muon", 2.1, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf-down","Muon", 2.1, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2017',"sf-down","Muon", 2.1, 199.9)]

muon_17_0_POG = [ceval_muon17_POG['NUM_IsoMu27_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(0.0, 39.0,'nominal'),ceval_muon17_POG['NUM_IsoMu27_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(0.0, 49.0,'nominal'),ceval_muon17_POG['NUM_IsoMu27_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(0.0, 59.0,'nominal'),ceval_muon17_POG['NUM_IsoMu27_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 0.0, 119.0,'nominal'),ceval_muon17_POG['NUM_IsoMu27_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 0.0, 199.9,'nominal')]
muon_17_0p9_POG = [ceval_muon17_POG['NUM_IsoMu27_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(0.9, 39.0,'nominal'),ceval_muon17_POG['NUM_IsoMu27_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(0.9, 49.0,'nominal'),ceval_muon17_POG['NUM_IsoMu27_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 0.9, 59.0,'nominal'),ceval_muon17_POG['NUM_IsoMu27_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 0.9, 119.0,'nominal'),ceval_muon17_POG['NUM_IsoMu27_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 0.9, 199.9,'nominal')]
muon_17_1p2_POG = [ceval_muon17_POG['NUM_IsoMu27_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(1.9, 39.0,'nominal'),ceval_muon17_POG['NUM_IsoMu27_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(1.2, 49.0,'nominal'),ceval_muon17_POG['NUM_IsoMu27_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 1.2, 59.0,'nominal'),ceval_muon17_POG['NUM_IsoMu27_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 1.2, 119.0,'nominal'),ceval_muon17_POG['NUM_IsoMu27_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 1.2, 199.9,'nominal')]
muon_17_2p1_POG = [ceval_muon17_POG['NUM_IsoMu27_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(2.1, 39.0,'nominal'),ceval_muon17_POG['NUM_IsoMu27_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(2.1, 49.0,'nominal'),ceval_muon17_POG['NUM_IsoMu27_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 2.1, 59.0,'nominal'),ceval_muon17_POG['NUM_IsoMu27_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 2.1, 119.0,'nominal'),ceval_muon17_POG['NUM_IsoMu27_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 2.1, 199.9,'nominal')]

plt.errorbar([87/2, 180/2, 320/2], muon_17_0, label = r'$0<|\eta|<0.9$', color = colors[0],  yerr = (muon_17_0_down, muon_17_0_up), fmt = 'o')
plt.errorbar([35, 45, 55, 180/2, 320/2], muon_17_0_POG, label = r'$0<|\eta|<0.9$ - POG', color = colors[0], marker = '^', fmt = 'o')
plt.errorbar([87/2, 180/2, 320/2], muon_17_0p9, label = r'$0.9<|\eta|<1.2$', color = colors[2],  yerr = (muon_17_0p9_down, muon_17_0p9_up), fmt = 'o')
plt.errorbar([35, 45, 55, 180/2, 320/2], muon_17_0p9_POG, label = r'$0.9<|\eta|<1.2$ - POG', color = colors[2], marker = '^', fmt = 'o')
plt.errorbar([87/2, 180/2, 320/2], muon_17_1p2, label = r'$1.2<|\eta|<2.1$', color = colors[4],  yerr = (muon_17_1p2_down, muon_17_1p2_up), fmt = 'o')
plt.errorbar([35, 45, 55, 180/2, 320/2], muon_17_1p2_POG, label = r'$1.2<|\eta|<2.1$ - POG', color = colors[4], marker = '^', fmt = 'o')
plt.errorbar([87/2, 180/2, 320/2], muon_17_2p1, label = r'$2.1<|\eta|<2.4$', color = colors[7],  yerr = (muon_17_2p1_down, muon_17_2p1_up), fmt = 'o')
plt.errorbar([35, 45, 55, 180/2, 320/2], muon_17_2p1_POG, label = r'$2.1<|\eta|<2.4$ - POG', color = colors[7], marker = '^', fmt = 'o')
plt.legend(loc =(.6,.5),prop={'size': 6})
plt.xlabel('Center of pT Bin')
plt.ylabel('Scale Factor')
plt.title('Muon 2017 POG Comparison')
#plt.show()
print(list(ceval.keys()))
plt.savefig('2017POGComparison_m.png', dpi = 2000)
plt.clf()


## 2016 Muons
ceval_muon16_POG = CorrectionSet.from_file("C:/Users/slatt/Downloads/POGJsons/muon_16.json")

pt_bins_muon_16 = [24,60,120,200]
pt_bins_muon_16_POG = [26.0,30.0,40.0,50.0,60.0,120.0,200.0]

muon_16_0_down = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf-down","Muon", 0.0, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf-down","Muon", 0.0, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf-down","Muon", 0.0, 199.9)]

muon_16_0 = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf","Muon", 0.0, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf","Muon", 0.0, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf","Muon", 0.0, 199.9)]
muon_16_0p9 = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf","Muon", 0.9, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf","Muon", 0.9, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf","Muon", 0.9, 199.9)]
muon_16_1p2 = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf","Muon", 1.2, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf","Muon", 1.2, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf","Muon", 1.2, 199.9)]
muon_16_2p1 = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf","Muon", 2.1, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf","Muon", 2.1, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf","Muon", 2.1, 199.9)]

muon_16_0_up = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf-up","Muon", 0.0, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf-up","Muon", 0.0, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf-up","Muon", 0.0, 199.9)]
muon_16_0p9_up = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf-up","Muon", 0.9, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf-up","Muon", 0.9, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf-up","Muon", 0.9, 199.9)]
muon_16_1p2_up = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf-up","Muon", 1.2, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf-up","Muon", 1.2, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf-up","Muon", 1.2, 199.9)]
muon_16_2p1_up = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf-up","Muon", 2.1, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf-up","Muon", 2.1, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf-up","Muon", 2.1, 199.9)]

muon_16_0_down = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf-down","Muon", 0.0, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf-down","Muon", 0.0, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf-down","Muon", 0.0, 199.9)]
muon_16_0p9_down = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf-down","Muon", 0.9, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf-down","Muon", 0.9, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf-down","Muon", 0.9, 199.9)]
muon_16_1p2_down = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf-down","Muon", 1.2, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf-down","Muon", 1.2, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf-down","Muon", 1.2, 199.9)]
muon_16_2p1_down = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf-down","Muon", 2.1, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf-down","Muon", 2.1, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016',"sf-down","Muon", 2.1, 199.9)]


muon_16_0_POG = [ceval_muon16_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(0.0, 39.0,'nominal'),ceval_muon16_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(0.0, 49.0,'nominal'),ceval_muon16_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(0.0, 59.0,'nominal'),ceval_muon16_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 0.0, 119.0,'nominal'),ceval_muon16_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 0.0, 199.9,'nominal')]
muon_16_0p9_POG = [ceval_muon16_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(0.9, 39.0,'nominal'),ceval_muon16_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(0.9, 49.0,'nominal'),ceval_muon16_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 0.9, 59.0,'nominal'),ceval_muon16_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 0.9, 119.0,'nominal'),ceval_muon16_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 0.9, 199.9,'nominal')]
muon_16_1p2_POG = [ceval_muon16_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(1.9, 39.0,'nominal'),ceval_muon16_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(1.2, 49.0,'nominal'),ceval_muon16_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 1.2, 59.0,'nominal'),ceval_muon16_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 1.2, 119.0,'nominal'),ceval_muon16_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 1.2, 199.9,'nominal')]
muon_16_2p1_POG = [ceval_muon16_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(2.1, 39.0,'nominal'),ceval_muon16_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(2.1, 49.0,'nominal'),ceval_muon16_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 2.1, 59.0,'nominal'),ceval_muon16_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 2.1, 119.0,'nominal'),ceval_muon16_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 2.1, 199.9,'nominal')]

plt.errorbar([84/2, 180/2, 320/2], muon_16_0, label = r'$0<|\eta|<0.9$', color = colors[0], fmt = 'o',  yerr = (muon_16_0_down, muon_16_0_up))
plt.errorbar([35, 45, 55, 180/2, 320/2], muon_16_0_POG, label = r'$0<|\eta|<0.9$ - POG', color = colors[0], marker = '^', fmt = 'o')
plt.errorbar([84/2, 180/2, 320/2], muon_16_0p9, label = r'$0.9<|\eta|<1.2$', color = colors[2], fmt = 'o',  yerr = (muon_16_0p9_down, muon_16_0p9_up))
plt.errorbar([35, 45, 55, 180/2, 320/2], muon_16_0p9_POG, label = r'$0.9<|\eta|<1.2$ - POG', color = colors[2], marker = '^', fmt = 'o')
plt.errorbar([84/2, 180/2, 320/2], muon_16_1p2, label = r'$1.2<|\eta|<2.1$', color = colors[4], fmt = 'o',  yerr = (muon_16_1p2_down, muon_16_1p2_up))
plt.errorbar([35, 45, 55, 180/2, 320/2], muon_16_1p2_POG, label = r'$1.2<|\eta|<2.1$ - POG', color = colors[4], marker = '^', fmt = 'o')
plt.errorbar([84/2, 180/2, 320/2], muon_16_2p1, label = r'$2.1<|\eta|<2.4$', color = colors[7], fmt = 'o',  yerr = (muon_16_2p1_down, muon_16_2p1_up))
plt.errorbar([35, 45, 55, 180/2, 320/2], muon_16_2p1_POG, label = r'$2.1<|\eta|<2.4$ - POG', color = colors[7], marker = '^', fmt = 'o')
plt.legend(loc =(.6,.5),prop={'size': 6})
plt.xlabel('Center of pT Bin')
plt.ylabel('Scale Factor')
plt.title('Muon 2016 POG Comparison')
#plt.show()
print(list(ceval.keys()))
plt.savefig('2016POGComparison_m.png', dpi = 2000)
plt.clf()


## 2016APV Muons
ceval_muon16APV_POG = CorrectionSet.from_file("C:/Users/slatt/Downloads/POGJsons/muon_16APV.json")

pt_bins_muon_16APV = [24,60,120,200]
pt_bins_muon_16APV_POG = [26.0,30.0,40.0,50.0,60.0,120.0,200.0]

muon_16APV_0_down = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf-down","Muon", 0.0, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf-down","Muon", 0.0, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf-down","Muon", 0.0, 199.9)]

muon_16APV_0 = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf","Muon", 0.0, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf","Muon", 0.0, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf","Muon", 0.0, 199.9)]
muon_16APV_0p9 = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf","Muon", 0.9, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf","Muon", 0.9, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf","Muon", 0.9, 199.9)]
muon_16APV_1p2 = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf","Muon", 1.2, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf","Muon", 1.2, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf","Muon", 1.2, 199.9)]
muon_16APV_2p1 = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf","Muon", 2.1, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf","Muon", 2.1, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf","Muon", 2.1, 199.9)]

muon_16APV_0_up = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf-up","Muon", 0.0, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf-up","Muon", 0.0, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf-up","Muon", 0.0, 199.9)]
muon_16APV_0p9_up = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf-up","Muon", 0.9, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf-up","Muon", 0.9, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf-up","Muon", 0.9, 199.9)]
muon_16APV_1p2_up = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf-up","Muon", 1.2, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf-up","Muon", 1.2, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf-up","Muon", 1.2, 199.9)]
muon_16APV_2p1_up = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf-up","Muon", 2.1, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf-up","Muon", 2.1, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf-up","Muon", 2.1, 199.9)]

muon_16APV_0_down = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf-down","Muon", 0.0, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf-down","Muon", 0.0, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf-down","Muon", 0.0, 199.9)]
muon_16APV_0p9_down = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf-down","Muon", 0.9, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf-down","Muon", 0.9, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf-down","Muon", 0.9, 199.9)]
muon_16APV_1p2_down = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf-down","Muon", 1.2, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf-down","Muon", 1.2, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf-down","Muon", 1.2, 199.9)]
muon_16APV_2p1_down = [ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf-down","Muon", 2.1, 59.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf-down","Muon", 2.1, 119.0),ceval['UL-PtEta-Trigger-SFs'].evaluate('2016APV',"sf-down","Muon", 2.1, 199.9)]

muon_16APV_0_POG = [ceval_muon16APV_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(0.0, 39.0,'nominal'),ceval_muon16APV_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(0.0, 49.0,'nominal'),ceval_muon16APV_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(0.0, 59.0,'nominal'),ceval_muon16APV_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 0.0, 119.0,'nominal'),ceval_muon16APV_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 0.0, 199.9,'nominal')]
muon_16APV_0p9_POG = [ceval_muon16APV_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(0.9, 39.0,'nominal'),ceval_muon16APV_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(0.9, 49.0,'nominal'),ceval_muon16APV_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 0.9, 59.0,'nominal'),ceval_muon16APV_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 0.9, 119.0,'nominal'),ceval_muon16APV_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 0.9, 199.9,'nominal')]
muon_16APV_1p2_POG = [ceval_muon16APV_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(1.9, 39.0,'nominal'),ceval_muon16APV_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(1.2, 49.0,'nominal'),ceval_muon16APV_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 1.2, 59.0,'nominal'),ceval_muon16APV_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 1.2, 119.0,'nominal'),ceval_muon16APV_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 1.2, 199.9,'nominal')]
muon_16APV_2p1_POG = [ceval_muon16APV_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(2.1, 39.0,'nominal'),ceval_muon16APV_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate(2.1, 49.0,'nominal'),ceval_muon16APV_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 2.1, 59.0,'nominal'),ceval_muon16APV_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 2.1, 119.0,'nominal'),ceval_muon16APV_POG['NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdMedium_and_PFIsoMedium'].evaluate( 2.1, 199.9,'nominal')]

plt.errorbar([84/2, 180/2, 320/2], muon_16APV_0, label = r'$0<|\eta|<0.9$', color = colors[0], fmt = 'o',  yerr = (muon_16_0_down, muon_16_0_up))
plt.errorbar([35, 45, 55, 180/2, 320/2], muon_16APV_0_POG, label = r'$0<|\eta|<0.9$ - POG', color = colors[0], marker = '^', fmt = 'o')
plt.errorbar([84/2, 180/2, 320/2], muon_16APV_0p9, label = r'$0.9<|\eta|<1.2$', color = colors[2], fmt = 'o',  yerr = (muon_16APV_0p9_down, muon_16APV_0p9_up))
plt.errorbar([35, 45, 55, 180/2, 320/2], muon_16APV_0p9_POG, label = r'$0.9<|\eta|<1.2$ - POG', color = colors[2], marker = '^', fmt = 'o')
plt.errorbar([84/2, 180/2, 320/2], muon_16APV_1p2, label = r'$1.2<|\eta|<2.1$', color = colors[4], fmt = 'o',  yerr = (muon_16APV_1p2_down, muon_16APV_1p2_up))
plt.errorbar([35, 45, 55, 180/2, 320/2], muon_16APV_1p2_POG, label = r'$1.2<|\eta|<2.1$ - POG', color = colors[4], marker = '^', fmt = 'o')
plt.errorbar([84/2, 180/2, 320/2], muon_16APV_2p1, label = r'$2.1<|\eta|<2.4$', color = colors[7], fmt = 'o',  yerr = (muon_16APV_2p1_down, muon_16APV_2p1_up))
plt.errorbar([35, 45, 55, 180/2, 320/2], muon_16APV_2p1_POG, label = r'$2.1<|\eta|<2.4$ - POG', color = colors[7], marker = '^', fmt = 'o')
plt.legend(loc =(.6,.5),prop={'size': 6})
plt.xlabel('Center of pT Bin')
plt.ylabel('Scale Factor')
plt.title('Muon 2016APV POG Comparison')
#plt.show()
print(list(ceval.keys()))
plt.savefig('2016APVPOGComparison_m.png', dpi = 2000)
plt.clf()
