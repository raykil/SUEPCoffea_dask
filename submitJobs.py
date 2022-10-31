#!/usr/bin/env python
import os
import sys

conda_source  = "/afs/cern.ch/user/%s/%s/miniconda3/etc/profile.d/conda.sh"%(os.getlogin()[0], os.getlogin())
doSingularity = True 
print()
print('START')
print()
########   YOU ONLY NEED TO FILL THE AREA BELOW   #########
########   customization  area #########
NumberOfJobs= int(sys.argv[1]) # number of jobs to be submitted
FileFolder  = sys.argv[2]      # File folder with all the files
OutputDir   = sys.argv[3]      # Where to put the stuff
queue       = sys.argv[4]      # Which queue to use: expresso (20min), microcentury (1h), longlunch (2h), workday (8h), tomorrow (1d), testmatch (3d), nextweek (1w)
doSubmit    = sys.argv[5]      # Whether to submit or not
analyzer    = sys.argv[6]
era         = sys.argv[7]
isData      = bool(int(sys.argv[8]))
interval    = int(sys.argv[9])
doSRonly    = bool(int(sys.argv[10]))
filt = None
isDY = False
resubmission = False
if len(sys.argv) > 11:
  filt = sys.argv[11]
if len(sys.argv) > 12:
  if int(sys.argv[12])==1:  
    isDY = True
files = [FileFolder + "/" + f for f in os.listdir(FileFolder)] # list with all the files  
if filt:
  newfiles = []
  for f in files:
    if filt in f: newfiles.append(f)
  print("Filtered files to %i/%i"%(len(newfiles), len(files)))
  files =  newfiles
if resubmission:
  newfiles = []
  import ROOT
  for iff, f in enumerate(files):
    print("%i/%i"%(iff, len(files)))
    tf = ROOT.TFile(f,"READ")
    tt = tf.Get("Events")
    run, lum, eve = 0, 0, 0
    for ev in tt:
      run = ev.run
      lum = ev.luminosityBlock
      eve = ev.event
      break
    tf.Close()
    testout = "out_%i_%i_%i.hdf5"%(eve, lum, run)
    if not(os.path.isfile(OutputDir +"/" + testout)):
      newfiles.append(f)
  files = newfiles

tag=OutputDir

if NumberOfJobs == -1: NumberOfJobs = len(files)

########   customization end   #########

path = os.getcwd()
print()
print('do not worry about folder creation:')
os.system("mkdir %s" %OutputDir)
os.system("rm -rf %s/tmp"%tag)
os.system("rm -rf %s/exec"%tag)
os.system("rm -rf %s/batchlogs"%tag)
os.system("mkdir %s/tmp"%tag)
os.system("mkdir %s/exec"%tag)
print()

##### loop for creating and sending jobs #####
ifile = 0
ijob  = 1
while ifile < NumberOfJobs:
    print(ifile)
    ##### creates jobs #######
    with open('%s/exec/job_'%tag+str(ijob)+'.sh', 'w') as fout:
        fout.write("#!/bin/bash\n")
        fout.write("echo 'START---------------'\n")
        fout.write("echo 'WORKDIR ' ${PWD}\n")
        fout.write("cd "+str(path)+"\n")
        if not(doSingularity): # If you are not running on singularity, need to load the coffea environment
          fout.write("source %s\n\n"%conda_source)
          fout.write("conda activate coffea\n")
        for i in range(interval):
          if ifile == NumberOfJobs: continue # Last one will have less
          fout.write("python condor_SUEP_WS.py  --isMC=%i --era=%s --dataset=DY --analyzer=%s --infile=%s --outputdir=%s %s %s\n"%(0 if isData else 1, era, analyzer, files[ifile], OutputDir, "--isDY" if isDY else "", "--SR" if doSRonly else "")) 
          ifile += 1

        fout.write("echo 'STOP---------------'\n")
        fout.write("echo\n")
        fout.write("echo\n")

    os.system("chmod 755 %s/exec/job_"%tag+str(ijob)+".sh")
    ijob += 1

###### create submit.sub file ####
    
os.mkdir("%s/batchlogs"%tag)
with open('submit.sub', 'w') as fout:
    fout.write("executable              = $(filename)\n")
    fout.write("arguments               = $(Proxy_path) $(ClusterId)$(ProcId)\n")
    fout.write("output                  = %s/batchlogs/$(ClusterId).$(ProcId).out\n"%tag)
    fout.write("error                   = %s/batchlogs/$(ClusterId).$(ProcId).err\n"%tag)
    fout.write("log                     = %s/batchlogs/$(ClusterId).log\n"%tag)
    if doSingularity: fout.write("+SingularityImage       = \"/cvmfs/unpacked.cern.ch/registry.hub.docker.com/coffeateam/coffea-dask:latest\"\n")
    fout.write('+JobFlavour = "%s"\n' %(queue))
    fout.write("\n")
    fout.write("queue filename matching (%s/exec/job_*sh)\n"%tag)
    
###### sends bjobs ######
if int(doSubmit) > 0:
  os.system("echo submit.sub")
  os.system("condor_submit -spool submit.sub")
   
print()
print("your jobs:")
os.system("condor_q")
print()
print('END')
print()
