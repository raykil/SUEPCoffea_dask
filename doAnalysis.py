from optparse import OptionParser
import os
import json 
import re

print("Running analysis parsing helper...")
parser = OptionParser(usage="%prog [all OR dataframes OR plots OR cards OR ABCDtests OR ZptCorrections] [options] [--detailed will get you a rundown of what you are running]")
parser.add_option("-y","--year", dest="year", type="int", default=2018, help="Year")
parser.add_option("-s","--samples", dest="samples", action="append", type="string", default=[], help="Only run these samples (accepts regexp matching)")
parser.add_option("-d","--detailed", dest="detailed", default=False, action="store_true", help="Print some more details on what is going on")
parser.add_option("-o","--output", dest="output", type="string", default=os.getcwd(), help="Where to put the output of what you are running")
parser.add_option("-q","--queue", dest="queue", type="string", default="longlunch", help="Which condor queue to use, the default is longlunch (2h)")
parser.add_option("-i","--interval", dest="interval", type="int", default=20, help="When submitting jobs, each one runs this many samples")
parser.add_option("--SR", dest="SR", action="store_true", help="If activated, the analyzer only saves yields up to SR to save space")
parser.add_option("--submit", dest="submit", action="store_true", help="If activated, do submission of jobs on top of printing the commands")
parser.add_option("--unblind", dest="unblind", action="store_true", help="Unless you activate this, data won't appear")
(options, args) = parser.parse_args()

doWhat = args[0]
if not(os.path.exists(options.output)):
    os.system("mkdir %s"%(options.output))

if doWhat == "all" or doWhat == "dataframes":
  if options.detailed:
    print("The first analysis step is producing dataframes with reduced event content. By default this will use the SUEP_ZH_simple.py analyzer")
    print("  - The following commands will generate a folder per sample on --output=%s containing the reduced .hdf5 files"%(options.output))
    print("  - The default behaviour is to run all of the samples for the given year (--year option), this can be modified with the -s argument")
    print("  - By default commands will be given for batch submission as this should not be run locally. Which queue can be regulated with the -q option")
    print("  - On lxplus, monitoring of the jobs can be done with the condor_q command")
  print("[DATAFRAMES] creation step...")
  samples = open(os.getcwd() +  "/data/samples_%i.json"%options.year)
  samplesjson = json.loads(samples.read())
  for sample in samplesjson:
    if (samplesjson[sample]["isData"] > 0) and not(options.unblind): continue
    if len(options.samples) == 0:
      print("python submitJobs.py -1 %s %s/%s/ %s 1 ZH_simple %i %i %s %s %s"%(samplesjson[sample]["path"], options.output, sample, options.queue, samplesjson[sample]["isData"], options.interval, "1" if options.SR else "", "" if samplesjson[sample]["filter"] == 0 else samplesjson[sample]["filter"], "1" if samplesjson[sample]["isDYinclusive"] == 1 else ""))
      if options.submit: os.system("python submitJobs.py -1 %s %s/%s/ %s 1 ZH_simple %i %i %s %s %s"%(samplesjson[sample]["path"], options.output, sample, options.queue, samplesjson[sample]["isData"], options.interval, "1" if options.SR else "", "" if samplesjson[sample]["filter"] == 0 else samplesjson[sample]["filter"], "1" if samplesjson[sample]["isDYinclusive"] == 1 else ""))
    else:
      for filt in options.samples:
        if re.match(filt, sample):
          print("python submitJobs.py -1 %s %s/%s/ %s 1 ZH_simple %i %i %s %s"%(samplesjson[sample]["path"], options.output, sample, options.queue, samplesjson[sample]["isData"], options.interval, "" if samplesjson[sample]["filter"] == 0 else samplesjson[sample]["filter"], "1" if samplesjson[sample]["isDYinclusive"] == 1 else ""))
          if options.submit: os.system("python submitJobs.py -1 %s %s/%s/ %s 1 ZH_simple %i %i %s %s"%(samplesjson[sample]["path"], options.output, sample, options.queue, samplesjson[sample]["isData"], options.interval, "" if samplesjson[sample]["filter"] == 0 else samplesjson[sample]["filter"], "1" if samplesjson[sample]["isDYinclusive"] == 1 else ""))
