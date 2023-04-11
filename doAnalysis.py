from optparse import OptionParser
import os
import json 
import re

print("Running analysis parsing helper...")
parser = OptionParser(usage="%prog [all OR dataframes OR plots OR cards OR ABCDtests OR ZptCorrections] [options] [--detailed will get you a rundown of what you are running]")
parser.add_option("-y","--year", dest="year", type="string", default="2018", help="Year")
parser.add_option("-s","--samples", dest="samples", action="append", type="string", default=[], help="Only run these samples (accepts regexp matching)")
parser.add_option("-d","--detailed", dest="detailed", default=False, action="store_true", help="Print some more details on what is going on")
parser.add_option("-o","--output", dest="output", type="string", default=os.getcwd(), help="Where to put the output of what you are running")
parser.add_option("-q","--queue", dest="queue", type="string", default="workday", help="Which condor queue to use, the default is workday (8h)")
parser.add_option("-i","--interval", dest="interval", type="int", default=100, help="When submitting jobs, each one runs this many samples")
parser.add_option("--SR", dest="SR", action="store_true", help="If activated, the analyzer only saves yields up to SR to save space")
parser.add_option("--submit", dest="submit", action="store_true", help="If activated, do submission of jobs on top of printing the commands")
parser.add_option("--unblind", dest="unblind", action="store_true", help="Unless you activate this, data won't appear")
parser.add_option("--plotfile", dest="plotfile", type="string", default="ZH/plots_SR.py", help="File detailing the plots to do in the plotter")
parser.add_option("--samplefile", dest="samplefile", type="string", default="ZH/samples_withSF_nocut_UL18.py", help="File detailing the samples to use in the plotter")
parser.add_option("--systfile", dest="systfile", type="string", default="ZH/systs_fullcorr_MC.py", help="File detailing the uncertainties to use in the datacards")
parser.add_option("--tag", dest="tag", type="string", default="", help="Add this extra tag to separate the plotting step from others")
parser.add_option("--var", dest="var", type="string", default="leadclusterspher", help="Make cards based on the shape of this variable")
parser.add_option("--leptonID", dest="leptonID", action="store_true", default=False, help="Activate lepton ID optimization commands")
parser.add_option("--muonID", dest="muonID", action="store_true", default=False, help="To check Muon IP cuts")
parser.add_option("--jetID", dest="jetID", action="store_true", default=False, help="To check relaxed jet ID cuts")
parser.add_option("--PU", dest="PU", action="store_true", default=False, help="To check PU splitting")
parser.add_option("--btagEff", dest="btagEff", action="store_true", default=False, help="Activate bTag Efficiency commands")
(options, args) = parser.parse_args()

doWhat = args[0]
if not(os.path.exists(options.output)):
    os.system("mkdir %s"%(options.output))

era = str(options.year) # The analyzer just takes the year
if "APV" in era: era = "2015" # Convention so it is less annoying for conversion of types

theLumis = {"2015": 19.9,"2016": 16.4, "2017":41.5, "2018":59.9} 

if doWhat == "all" or doWhat == "dataframes":
  if options.detailed:
    print("\x1b[0;31;40m The first analysis step is producing dataframes with reduced event content. By default this will use the SUEP_ZH_simple.py analyzer")
    print("  - The following commands will generate a folder per sample on --output=%s containing the reduced .hdf5 files"%(options.output))
    print("  - The default behaviour is to run all of the samples for the given year (--year option), this can be modified with the -s argument")
    print("  - The default behaviour is not to run data. This can be modified with --unblind")
    print("  - By default commands will be given for batch submission as this should not be run locally. Which queue can be regulated with the -q option")
    print("  - On lxplus, monitoring of the jobs can be done with the condor_q command\x1b[0m")
  print("-------------------------------------------")
  analyzer = "ZH_simple_withsyst"
  if options.leptonID: 
    analyzer = "ZH_leptonID"
    if options.plotfile == "ZH/plots_mZ.py": # If default, change to leptonID one
      options.plotfile = "ZH/plots_leptonID.py" 
  if options.jetID:
    analyzer = "checkJetID"
  if options.btagEff:
    analyzer = "ZH_btagEff"
    doWhat = "dataframes"
    print("\x1b[0;31;40m Reminder: B tagging effiency dataframe production step is suggested to run only for TT and DY samples (--samples argument) \x1b[0m")
  if options.muonID:
    analyzer = "MuonID"
  if options.PU:
    analyzer = "ntracksplit"
  print("[DATAFRAMES] creation step...")
  samples = open(os.getcwd() +  "/data/samples_%s.json"%options.year)
  samplesjson = json.loads(samples.read())
  for sample in samplesjson:
    if type(samplesjson[sample]["path"]) != type( [1,2]): #Convert into list
      samplesjson[sample]["path"] = [samplesjson[sample]["path"]]
    if (samplesjson[sample]["isData"] > 0) and not(options.unblind): continue
    if len(options.samples) == 0:
      for samplepath in samplesjson[sample]["path"]:
        print("python submitJobs.py -1 %s %s/%s/ %s 1 %s %s %i %i %s %s %s"%(samplepath, options.output, sample, options.queue, analyzer, era, samplesjson[sample]["isData"], options.interval, "1" if options.SR else "0", "" if samplesjson[sample]["filter"] == 0 else samplesjson[sample]["filter"], "1" if samplesjson[sample]["isDYinclusive"] == 1 else ""))
        if options.submit: os.system("python submitJobs.py -1 %s %s/%s/ %s 1 %s %s %i %i %s %s %s"%(samplepath, options.output, sample, options.queue, analyzer, era, samplesjson[sample]["isData"], options.interval, "1" if options.SR else "0", "" if samplesjson[sample]["filter"] == 0 else samplesjson[sample]["filter"], "1" if samplesjson[sample]["isDYinclusive"] == 1 else ""))
    else:
      for filt in options.samples:
        if re.match(filt, sample):
          for samplepath in samplesjson[sample]["path"]:
            print("python submitJobs.py -1 %s %s/%s/ %s 1 %s %s %i %i %s %s %s"%(samplepath, options.output, sample, options.queue, analyzer, era, samplesjson[sample]["isData"], options.interval, "1" if options.SR else "0", "" if samplesjson[sample]["filter"] == 0 else samplesjson[sample]["filter"], "1" if samplesjson[sample]["isDYinclusive"] == 1 else ""))
            if options.submit: os.system("python submitJobs.py -1 %s %s/%s/ %s 1 %s %s %i %i %s %s %s"%(samplepath, options.output, sample, options.queue, analyzer, era, samplesjson[sample]["isData"], options.interval, "1" if options.SR else "0", "" if samplesjson[sample]["filter"] == 0 else samplesjson[sample]["filter"], "1" if samplesjson[sample]["isDYinclusive"] == 1 else ""))
  print("-------------------------------------------")
  print("-------------------------------------------")
  print("-------------------------------------------")
  if options.btagEff:
    print("\x1b[0;31;40m After the dataframes are run, collect efficiencies with \x1b[0m")
    print("python workflows/utils/getBTagEff.py %s %s"%(options.output, options.output + "/effs"))
if doWhat == "all" or doWhat == "plots":
  if options.detailed:
    print("\x1b[0;31;40m The next analysis step is producing histograms from the produced dataframes this is done in two steps with the plotter_vh.py script")
    print(" - Two configuration files are needed: --samplefile=%s for providing the dataframes to read and --plotfile=%s for providing the variables to plot. Remember to update your configuration files to read the samples you produced on the last step!!"%(options.samplefile, options.plotfile))
    print(" - Then the plotter proceeds in two steps: first produce histograms for each dataframe (--toSave is activated), then combine all histograms per sample (--toLoad is activated)")
    print(" - During the load step, two folders are created in --output=%s : 'histos' to save the histograms and 'jobs' (optionally) to store the information needed for processing this in batch. If several histos are to be done with the same dataframes (i.e. different cuts), and additional --tag=%s can be added"%(options.output,options.tag))
    print(" - Batch submission can be enabled with the --submit command. Otherwise it will run in a single local core which will be very very slow. Note that this will give you the actual command to run with batch submission but not submit the jobs themselves (for that you need to actually run it).\x1b[0m")
  print("-------------------------------------------")

  print("[PLOTS] saving step...")
  print("cd CMSSW_10_2_13/src/")
  print("cmsenv")
  print("cd -")
  print("cd plotting")
  print("python plotter_vh.py %s %s -l %1.1f --systFile %s --toSave %s/histos%s/ --batchsize 20 --jobname %s/jobs%s/ %s %s"%(options.samplefile, options.plotfile, theLumis[era],options.systfile, options.output, options.tag, options.output, options.tag, "" if not options.submit else "--queue %s"%options.queue, "--blind" if not options.unblind else ""))
  if options.detailed:
    print("\x1b[0;31;40m - If some of the previous jobs failed, the same plotter_vh.py with the --resubmit option can be run to only rerun the missing ones")
    print(" - Remember that all the jobs in the previous step need to finish before running the histogramming")
    print(" - The next step will produce all plots into the %s/plots%s folder, configurable again with the --output and --tag options\x1b[0m"%(options.output, options.tag))
  print("[PLOTS] loading and plotting step")
  print("cd CMSSW_10_2_13/src/")
  print("cmsenv")
  print("cd -")
  print("cd plotting")
  print("python plotter_vh.py %s %s -l %1.1f --systFile %s --toLoad %s/histos%s/ --batchsize 20 --jobname %s/jobs%s/ %s %s"%(options.samplefile, options.plotfile, theLumis[era], options.systfile, options.output, options.tag, options.output, options.tag, "" if not options.submit else "--queue %s"%options.queue, "--blind" if not options.unblind else ""))
  print("-------------------------------------------")
  print("-------------------------------------------")
  print("-------------------------------------------")

if doWhat == "all" or doWhat == "cards":
  if options.detailed:
    print("\x1b[0;31;40m This last command will take the histograms produced in the previous step and build a datacard based on the previous inputs:")
    print(" - Needs a configuration file for the samples (can reuse the one on the plots), --samplefile=%s. Additionally a configuration file with the uncertainties based on the --systfile=%s command"%(options.samplefile, options.systfile))
    print(" - Assumes that you have run plots in the 2D distribution case, for example (see instructions above):")
    print("python plotter_vh.py %s %s -l %1.1f --systFile %s --toSave %s/histos%s/ --batchsize 20 --jobname %s/jobs%s/ %s %s"%(options.samplefile, "ZH/plots_2D_SR.py", theLumis[era], options.systfile, options.output, options.tag, options.output, options.tag, "" if not options.submit else "--queue %s"%options.queue, "--blind" if not options.unblind else ""))
    print(" - This step is very fast, so no batch submission has been coded for it. Everything runs in local")
    print(" - Output will appear in %s/cards%s configurable with the --output and --tag commands")
    print(" - The variable that will be used for making the card is configured through --var=%s\x1b[0m"%options.var)
  print("-------------------------------------------")
  print("[DATACARDS] creation step...")
  print("cd CMSSW_10_2_13/src/")
  print("cmsenv")
  print("cd -")
  print("cd plotting")
  print("python datacardMaker.py %s %s %s/cards%s %s --rootfile %s/plots%s/%s.root --var %s"%(options.samplefile, options.systfile, options.output, options.tag, "--blind" if not options.unblind else "", options.output, options.tag, options.var, options.var))
  print("-------------------------------------------")
  print("-------------------------------------------")
  print("-------------------------------------------")

