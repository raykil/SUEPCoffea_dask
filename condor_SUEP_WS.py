import os
import json
import argparse

#Import coffea specific features
from coffea.processor import run_uproot_job, futures_executor


#Begin argparse
parser = argparse.ArgumentParser("")
parser.add_argument('--isMC', type=int, default=1, help="")
parser.add_argument('--jobNum', type=int, default=1, help="")
parser.add_argument('--era', type=str, default="2018", help="")
parser.add_argument('--doSyst', type=int, default=1, help="")
parser.add_argument('--infile', type=str, default=None, help="")
parser.add_argument('--dataset', type=str, default="X", help="")
parser.add_argument('--nevt', type=str, default=-1, help="")
parser.add_argument('--analyzer', type=str, default="GluGlu", help="")
parser.add_argument('--outputdir', type=str, default=None, help="")
parser.add_argument('--chunksize', type=int, default=500000, help="")
parser.add_argument('--test', type=bool, default=False, help="")
parser.add_argument('--isDY', action="store_true", default=False, help="Activate for the DY Zpt=0 fix for UL")
parser.add_argument('--SR', action="store_true", default=False, help="Activate to only save yields at SR level to save space")
options = parser.parse_args()

out_dir = options.outputdir if options.outputdir else os.getcwd()
print("isDY", options.isDY)
## Select analyzer
modules_era = []
if options.analyzer == "GluGlu":
  from workflows.SUEP_coffea import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=0,  syst_var='', sample=options.dataset, weight_syst='' , flag=False, output_location=out_dir))
elif options.analyzer == "ZH_simple":
  from workflows.SUEP_coffea_ZH_simple import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=0,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, doOF=False, isDY=options.isDY))
elif options.analyzer == "ZH_simple_DEBUGGING":
  from workflows.SUEP_coffea_ZH_simple_DEBUGGING import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=0,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, doOF=False, isDY=options.isDY))
elif options.analyzer == "ZH_RebuildSUEP":
  from workflows.SUEP_coffea_ZH_RebuildSUEP import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=0,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=True, output_location=out_dir, doOF=False, isDY=options.isDY))
elif options.analyzer == "ZH_ABCD":
  from workflows.SUEP_coffea_ZH_ABCD import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=0,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, doOF=False, isDY=options.isDY))
elif options.analyzer == "ZH_TalAndMaya":
  from workflows.SUEP_coffea_Tal_Maya import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=0,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=True, output_location=out_dir, doOF=False, isDY=False, doTracksGenMatching = True))
elif options.analyzer == "ZH_trigger_eff_UPDATED":
  from workflows.SUEP_coffea_ZH_trigger_eff_UPDATED import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=0,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, isDY=options.isDY))
elif options.analyzer == "ZH_simple_withsyst":
  from workflows.SUEP_coffea_ZH_simple import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=1,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, doOF=False, isDY=options.isDY))
elif options.analyzer == "ZH_simple_withsyst_AkT_2p0":
  from workflows.SUEP_coffea_ZH_simple_AkT_2p0 import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=1,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, doOF=False, isDY=options.isDY))
elif options.analyzer == "ZH_simple_withsyst_AkT_1p5":
  from workflows.SUEP_coffea_ZH_simple_AkT_1p5 import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=1,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, doOF=False, isDY=options.isDY))
elif options.analyzer == "ZH_simple_withsyst_AkT_4p0":
  from workflows.SUEP_coffea_ZH_simple_AkT_4p0 import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=1,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, doOF=False, isDY=options.isDY))
elif options.analyzer == "ZH_simple_withsyst_AkT_p4":
  from workflows.SUEP_coffea_ZH_simple_AkT_p4 import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=1,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, doOF=False, isDY=options.isDY))
elif options.analyzer == "ZH_simple_withsyst_AkT_1p5_NewID":
  from workflows.SUEP_coffea_ZH_simple_AkT_1p5_NewID import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=1,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, doOF=False, isDY=options.isDY))
elif options.analyzer == "ZH_simple_withsyst_AkT_1p5_Light":
  from workflows.SUEP_coffea_ZH_simple_AkT_1p5_Light import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=1,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, doOF=False, isDY=options.isDY))
elif options.analyzer == "ZH_simple_withsyst_AkT_1p2":
  from workflows.SUEP_coffea_ZH_simple_AkT_1p2 import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=1,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, doOF=False, isDY=options.isDY))
elif options.analyzer == "ZH_simple_withsyst_AkT_p8":
  from workflows.SUEP_coffea_ZH_simple_AkT_p8 import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=1,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, doOF=False, isDY=options.isDY))
elif options.analyzer == "ZH_simple_withsyst_Cambridge_2p0":
  from workflows.SUEP_coffea_ZH_simple_Cambridge_2p0 import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=1,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, doOF=False, isDY=options.isDY))
elif options.analyzer == "ZH_simple_withsyst_Cambridge_4p0":
  from workflows.SUEP_coffea_ZH_simple_Cambridge_4p0 import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=1,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, doOF=False, isDY=options.isDY))
elif options.analyzer == "ZH_simple_withsyst_Cambridge_p4":
  from workflows.SUEP_coffea_ZH_simple_Cambridge_p4 import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=1,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, doOF=False, isDY=options.isDY))
elif options.analyzer == "ZH_simple_withsyst_Cambridge_1p5":
  from workflows.SUEP_coffea_ZH_simple_Cambridge_1p5 import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=1,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, doOF=False, isDY=options.isDY))
elif options.analyzer == "ZH_simple_withsyst_Cambridge_1p5_Light":
  from workflows.SUEP_coffea_ZH_simple_Cambridge_1p5_Light import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=1,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, doOF=False, isDY=options.isDY))
elif options.analyzer == "ZH_simple_withsyst_Cambridge_1p2":
  from workflows.SUEP_coffea_ZH_simple_Cambridge_1p2 import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=1,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, doOF=False, isDY=options.isDY))
elif options.analyzer == "ZH_simple_withsyst_Cambridge_p8":
  from workflows.SUEP_coffea_ZH_simple_Cambridge_p8 import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=1,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, doOF=False, isDY=options.isDY))
elif options.analyzer == "ZH_simple_withsyst_kT_2p0":
  from workflows.SUEP_coffea_ZH_simple_kT_2p0 import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=1,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, doOF=False, isDY=options.isDY))
elif options.analyzer == "ZH_simple_withsyst_kT_1p5":
  from workflows.SUEP_coffea_ZH_simple_kT_1p5 import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=1,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, doOF=False, isDY=options.isDY))
elif options.analyzer == "ZH_simple_withsyst_kT_1p2":
  from workflows.SUEP_coffea_ZH_simple_kT_1p2 import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=1,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, doOF=False, isDY=options.isDY))
elif options.analyzer == "ZH_simple_withsyst_kT_p8":
  from workflows.SUEP_coffea_ZH_simple_kT_p8 import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=1,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, doOF=False, isDY=options.isDY))
elif options.analyzer == "ZH_simple_fortests":
  from workflows.SUEP_coffea_ZH_simple_fortests import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=0,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, doOF=False, isDY=options.isDY))
elif options.analyzer == "ZH_simple_OF":
  from workflows.SUEP_coffea_ZH_simple import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=0,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, doOF=True))
elif options.analyzer == "ZH_trackID":
  from workflows.SUEP_coffea_ZH_trackID import * 
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=0,  syst_var='', sample=options.dataset, weight_syst='' , flag=False, output_location=out_dir))
elif options.analyzer == "ZH_trackProps":
  from workflows.SUEP_coffea_ZH_trackProps import * 
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=0,  syst_var='', sample=options.dataset, weight_syst='' , flag=False, output_location=out_dir))
elif options.analyzer == "ZH_gen":
  from workflows.SUEP_coffea_ZH_onlygenZpt import * 
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=0,  syst_var='', sample=options.dataset, weight_syst='' , flag=False, output_location=out_dir, doOF=False, isDY=options.isDY))
elif options.analyzer == "ZH_leptonID":
  from workflows.SUEP_coffea_ZH_leptonID import * 
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=0,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, doOF=True, isDY = options.isDY))
elif options.analyzer == "ZH_btagEff":
  from workflows.SUEP_coffea_ZH_bTagEff import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=0,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, doOF=True, isDY = options.isDY))
elif options.analyzer == "MuonID":
  from workflows.SUEP_coffea_ZH_checkMuonID import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=1,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, doOF=False, isDY=options.isDY))
elif options.analyzer == "ntracksplit":
  from workflows.SUEP_coffea_ZH_simple_ntracksplit import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=1,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, doOF=False, isDY=options.isDY))
elif options.analyzer == "checkJetID":
  from workflows.SUEP_coffea_ZH_checkJetID import *
  modules_era.append(SUEP_cluster(isMC=options.isMC, era=int(options.era), do_syst=1,  syst_var='', sample=options.dataset, weight_syst='' , SRonly=options.SR, output_location=out_dir, doOF=False, isDY=options.isDY))

for instance in modules_era:
    output = run_uproot_job(
        {instance.sample: [options.infile]},
        treename='Events',
        processor_instance=instance,
        executor=futures_executor,
        executor_args={'workers': 1,
                       'schema': processor.NanoAODSchema,
                       'xrootdtimeout': 10,
        },
        chunksize = 100 if options.test else options.chunksize,
        maxchunks = 1 if options.test else None,
    )
