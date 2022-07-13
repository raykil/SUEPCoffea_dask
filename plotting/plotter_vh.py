import ROOT
import imp
import array 
import os
import pandas as pd
import CMS_lumi
from multiprocessing import Pool
import time
import copy
from contextlib import closing
import subprocess, sys
import math
import numpy as np

ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch(True)

class sample(object):
  def __init__(self, sampledict, options):
    self.config  = sampledict
    self.name    = sampledict["name"]
    self.hdfiles = []
    self.safefiles=[]
    self.nnorms = {}
    self.norms  = {}
    self.isData = ("data" in self.name) or ("Data" in self.name)
    iF = 0
    if options.queue: print("Loading sample %s"%self.name)
    for f in sampledict["files"]:
      iF +=1
      #if options.queue:
      print("Checking files %i/%i"%(iF, len(sampledict["files"])))
      try:
        filename = f.split("/")[-1].replace("out_","").replace(".hdf5","")
        if options.toSave: 
          fullfilename = options.toSave + "/" + self.name + "_" + filename + ".root"
        if options.toLoad:
          fullfilename = options.toLoad + "/" + self.name + "_" + filename + ".root"

        if options.resubmit:
          if os.path.isfile(fullfilename):
            if os.path.getsize(fullfilename) > 1000: #I.e., non corrupted
              print("Corrupted!")
              continue    
        if not(options.toLoad and (("skim" in self.config) or (self.isData)) and os.path.isfile(fullfilename)):
          a = pd.HDFStore(f, "r")

          if not("skim" in self.config) and not(self.isData):
            #print(a.get_storer("twoleptons").attrs.metadata)
            self.nnorms[f] = a.get_storer("twoleptons").attrs.metadata["gensumweight"]
          b = {}
          if len(a.keys()) == 0: #Empty file
            a.close()
            print("No keys!")
            continue
          if not(options.queue) and not(options.toLoad):
            for k in a.keys():
              #print(k)
              b[k.replace("/","")] = a[k]
            self.hdfiles.append(b)
          a.close()
        self.safefiles.append(f)
        #print("File %s loaded succesfully"%f)
      except Exception, e:
        print("File %s broken, will skip loading it"%f)
        print(str(e))

    print(self.name, self.safefiles)
    if "skim" in sampledict and not(self.isData):
      self.unskimmedyields, self.norm = self.getUnskimmedYields()
      
    self.histos  = {}
    self.plots   = {}
    self.channels= []
    self.plotsinchannel = {}
    self.varstoload = {}
    self.yields     = {}

  def getUnskimmedYields(self):
    rf = ROOT.TFile(self.config["skim"])
    out = {}
    norm = 0
    for f in self.safefiles:
       run, luminosityBlock, event= f.split("/")[-1].replace("out_","").replace(".hdf5","").split("_")
       
       #print("Runs_"+str(event)+ "_" + str(luminosityBlock) + "_" + str(run))
       #print(self.config["skim"])
       tt = rf.Get("Runs_"+str(event)+ "_" + str(luminosityBlock) + "_" + str(run))
       for ev in tt:
         out[f] = ev.genEventSumw
         norm += ev.genEventSumw
         break
    return out, norm

  def addPlot(self, plotdict):
    self.plots[plotdict["name"]] = plotdict
    if not(plotdict["channel"] in self.channels): 
      self.channels.append(plotdict["channel"])
      self.plotsinchannel[plotdict["channel"]] = [plotdict["name"]]
      self.varstoload[plotdict["channel"]]     = plotdict["vars"]
    else:
      self.plotsinchannel[plotdict["channel"]].append(plotdict["name"])
      for v in plotdict["vars"]:
        if not(v in self.varstoload[plotdict["channel"]]): 
          self.varstoload[plotdict["channel"]].append(v)

  def getRawHistogramsAndNorms(self, options):
    for plotName in self.plots:
      p = self.plots[plotName]
      if p["bins"][0] == "uniform": #Then it is nbins, minX, maxX
        self.histos[plotName] = {}
        self.histos[plotName]["total"] = ROOT.TH1F(plotName + "_" + self.name, plotName + "_" + self.name, p["bins"][1], p["bins"][2], p["bins"][3])
      elif p["bins"][0] == "limits":
        self.histos[plotName] = {}
        self.histos[plotName]["total"] = ROOT.TH1F(plotName + "_" + self.name, plotName + "_" + self.name, array.array('f', p["bins"][1])) 
      if not(self.isData): self.norms[plotName] = 0 if not("skim" in self.config) else self.norm

    print(self.name, "Pre-load")
    if not(options.toLoad):
      for iff, f in enumerate(self.hdfiles):
        print("Loading file %i/%i"%(iff, len(self.hdfiles)))
        self.getRawHistogramsAndNormsOneFile([f,self.safefiles[iff], options])
    else:
      for iff, f in enumerate(self.safefiles):
        print("Loading file %i/%i"%(iff, len(self.hdfiles)))
        self.getRawHistogramsAndNormsOneFile(["",self.safefiles[iff], options])

    """elif options.jobs >= 2:
      with closing(Pool(options.jobs)) as p:
        retlist1 = p.map_async(self.getRawHistogramsAndNormsOneFile, [[h, options] for h in self.hdfiles], 1)
        while not retlist1.ready():
          print("Jobs left: {}".format(retlist1._number_left ))
          time.sleep(1)
        retlist1 = retlist1.get()
        p.close()
        p.join()
        p.terminate()"""
    
    # After all is said and done, add up histograms and normalize to xsec
    if options.toSave: 
      return
    for c in self.channels:
      for plotName in self.plotsinchannel[c]:
        p = self.plots[plotName]
        for iff, f in enumerate(self.safefiles):
          if options.toLoad and not("skim" in self.config) and not(self.isData): # If loading and unskimmed, need to set the norm here
            self.norms[plotName] += self.nnorms[self.safefiles[iff]]
          filename = self.safefiles[iff].split("/")[-1].replace("out_","").replace(".hdf5","")
          print(plotName, filename, self.isData, "skim" in self.config, options.toLoad)
          self.histos[plotName]["total"].Add(self.histos[plotName][filename])
        self.histos[plotName]["total"].Sumw2() # To get proper stat. unc.
        print(plotName, self.safefiles, self.isData, "skim" in self.config, options.toLoad)
        if not(self.isData): self.histos[plotName]["total"].Scale(options.luminosity*self.config["xsec"]/self.norms[plotName])
        self.yields[plotName] = self.histos[plotName]["total"].Integral()
        print(self.name, plotName, self.yields[plotName])

  def getRawHistogramsAndNormsOneFile(self, g):
    f, safefile, options = g[0], g[1], g[2]
    
    filename = safefile.split("/")[-1].replace("out_","").replace(".hdf5","")
    if not(options.toLoad):  
      if options.toSave:
        rf = ROOT.TFile(options.toSave + "/" + self.name + "_" + filename + ".root", "RECREATE")

      for plotName in self.plots:
        self.histos[plotName][filename]  = self.histos[plotName]["total"].Clone(self.histos[plotName]["total"].GetName() + "_" + filename)
      for c in self.channels:
        #print(f, safefile)
        if not(self.isData): 
          weights = f[c]["genweight"]
        else: 
          weights = np.ones(len(f[c]))
        if "extraWeights" in self.config: 
          extraweights = self.config["extraWeights"](f[c])
          print(extraweights)
        for plotName in self.plotsinchannel[c]:
          print("...%s"%plotName)
          p = self.plots[plotName]
          if not("skim" in self.config) and not(self.isData):
            self.norms[plotName] += self.nnorms[safefile]
          values, weightsHere = p["value"](f[c], weights)
          if "extraWeights" in self.config: weightsHere = weightsHere*extraweights
          #print(p["value"])
          for idx in range(len(values)):
            if (idx+1)%100000 == 0: print("%i/%i"%(idx, len(values)))
            self.histos[p["name"]][filename].Fill(values[idx], weightsHere[idx])
          if options.toSave:
             rf.cd()
             self.histos[p["name"]][filename].Write()
      if options.toSave: rf.Close() 
    else:
      rf = ROOT.TFile(options.toLoad + "/" + self.name + "_" + filename + ".root", "READ")
      print(options.toLoad + "/" + self.name + "_" + filename + ".root")
      for plotName in self.plots:
        print(self.histos[plotName]["total"].GetName() + "_" + filename)
        self.histos[plotName][filename] = copy.copy(rf.Get(self.histos[plotName]["total"].GetName() + "_" + filename))
 
  def setStyleOptions(self):
    for key in self.histos:
      if "linecolor" in self.config: 
        self.histos[key]["total"].SetLineColor(self.config["linecolor"])
      if "fillcolor" in self.config:
        self.histos[key]["total"].SetFillColor(self.config["fillcolor"])
        self.histos[key]["total"].SetMarkerColor(self.config["fillcolor"])
      if "style" in self.config:
        self.histos[key]["total"].SetLineStyle(self.config["style"])
      if "markerstyle" in self.config:
        self.histos[key]["total"].SetMarkerStyle(self.config["markerstyle"])
      if "markersize" in self.config:
        self.histos[key]["total"].SetMarkerSize(self.config["markersize"])


  def isBackground(self):
    bkg = True
    if "isSig" in self.config: bkg = not(self.config["isSig"])
    if self.isData: return False
    return bkg

class plotter(object):
  def __init__(self, plotdicts, sampledicts, options):
    self.plots      = plotdicts #[plotdicts[d] for d in plotdicts]
    self.samples    = [sample(sampledicts[d], options) for d in sampledicts]
    print("...Initializing")
    print("...Will run over %i samples"%(sum([len(s.safefiles) for s in self.samples])))
    for p in self.plots:
      for s in self.samples:
        s.addPlot(self.plots[p])

  def createJobs(self, options, command):
    iJob = 0
    for s in self.samples:
      sname = s.name
      nfiles = len(s.safefiles)
      options.batchsize = int(options.batchsize)
      chunks = int(math.ceil(nfiles*1./(options.batchsize)))
      jobfile = open("%s/exec/_%i.sh"%(options.jobname, iJob),"w")
      jobfile.write("#!/bin/bash\n")
      jobfile.write("cd /eos/home-c/cericeci/SUEP/SUEPCoffea_dask/plotting/\n")
      if chunks == 1:
        jobfile = open("%s/exec/_%i.sh"%(options.jobname, iJob),"w")
        jobfile.write("#!/bin/bash\n")
        jobfile.write("source /afs/cern.ch/cms/cmsset_default.sh\n")
        jobfile.write("cd /eos/user/c/cericeci/CMSSW_10_6_29/src/\n")
        jobfile.write("cmsenv\n")
        jobfile.write("cd /eos/home-c/cericeci/SUEP/SUEPCoffea_dask/plotting/\n")
        jobfile.write(command + " --sample %s --files %s"%(sname, ",".join(s.safefiles)))
        jobfile.close()
        iJob += 1
      else:
        for i in range(chunks-1):
          jobfile = open("%s/exec/_%i.sh"%(options.jobname, iJob),"w")
          jobfile.write("#!/bin/bash\n")
          jobfile.write("source /afs/cern.ch/cms/cmsset_default.sh\n")
          jobfile.write("cd /eos/user/c/cericeci/CMSSW_10_6_29/src/\n")
          jobfile.write("cmsenv\n")

          jobfile.write("cd /eos/home-c/cericeci/SUEP/SUEPCoffea_dask/plotting/\n")
          jobfile.write(command + " --sample %s --files %s"%(sname, ",".join(s.safefiles[i*options.batchsize:(i+1)*options.batchsize])))
          iJob += 1
          jobfile.close()

        jobfile = open("%s/exec/_%i.sh"%(options.jobname, iJob),"w")
        jobfile.write("#!/bin/bash\n")
        jobfile.write("source /afs/cern.ch/cms/cmsset_default.sh\n")
        jobfile.write("cd /eos/user/c/cericeci/CMSSW_10_6_29/src/\n")
        jobfile.write("cmsenv\n")
        jobfile.write("cd /eos/home-c/cericeci/SUEP/SUEPCoffea_dask/plotting/\n")
        jobfile.write(command + " --sample %s --files %s"%(sname, ",".join(s.safefiles[(chunks-1)*options.batchsize:])))
        jobfile.close()
        iJob += 1
    return iJob
  def doPlots(self, options):
    self.getRawHistogramsAndNorms(options)
    if not options.toSave: self.doStackPlots(options)

  def getRawHistogramsAndNorms(self, options):
    for s in self.samples:
      print("...Processing histograms for %s"%s.name)
      s.getRawHistogramsAndNorms(options)
      s.setStyleOptions()

  def doStackPlots(self, options):
    for plotName in self.plots:
      print("...Plotting %s"%plotName)
      mode = "stack"
      if "mode" in self.plots[plotName]: mode = self.plots[plotName]["mode"]

      if mode == "stack": self.doStackPlot(plotName, options)
      ## More to be implemented

  def doStackPlot(self, pname, options):
    p = self.plots[pname]
    c = ROOT.TCanvas(pname,pname, 800,1050)
    # Set pads
    p1 = ROOT.TPad("mainpad", "mainpad", 0, 0.30, 1, 1)
    p1.SetBottomMargin(0.025)
    p1.SetTopMargin(0.14)
    p1.SetLeftMargin(0.12)
    if "margins" in p:
      p1.SetBottomMargin(p["margins"][0])
      p1.SetTopMargin(p["margins"][1])
      p1.SetLeftMargin(p["margins"][2])
      p1.SetRightMargin(p["margins"][3])
    p1.Draw()
    p1.SetLogy(True)
    if "logY" in p:
      p1.SetLogy(p["logY"])

    p2 = ROOT.TPad("ratiopad", "ratiopad", 0, 0, 1, 0.30)
    p2.SetTopMargin(0.01)
    p2.SetBottomMargin(0.45)
    p2.SetLeftMargin(0.12)
    p2.SetFillStyle(0)
    if "margins" in p:
      p1.SetLeftMargin(p["margins"][2])
      p1.SetRightMargin(p["margins"][3])
    p2.Draw()
    p1.cd()
    tl = ROOT.TLegend(0.5,0.55,0.9,0.85)
    if "legendPosition" in p:
      tl = ROOT.TLegend(p["legendPosition"][0], p["legendPosition"][1], p["legendPosition"][2], p["legendPosition"][3])  

    # Now get the histograms and build the stack
    theStack = ROOT.THStack(pname+"_stack", pname)
    theIndivs= []
    theData  = []
    # Background go into the stack
    stacksize = 0
    back = False
    if options.ordered:
      self.samples.sort(key= lambda x: x.yields[pname], reverse=False)

    for s in self.samples:
      if s.isBackground():
        if options.rebin: s.histos[pname]["total"] = s.histos[pname]["total"].Rebin(options.rebin)
        theStack.Add(s.histos[pname]["total"])
        tl.AddEntry(s.histos[pname]["total"], s.config["label"], "f")
        if not(back): back = s.histos[pname]["total"].Clone("total_background")
        else: back.Add(s.histos[pname]["total"])
        #print(pname, s.name)
        #s.histos[pname]["total"].Print("all")
        stacksize += s.histos[pname]["total"].Integral()
      elif s.isData:
        if options.rebin: s.histos[pname]["total"] = s.histos[pname]["total"].Rebin(options.rebin)
        tl.AddEntry(s.histos[pname]["total"], s.config["label"], "pl")
        theData.append(s.histos[pname]["total"])
      else:
        if options.rebin: s.histos[pname]["total"] = s.histos[pname]["total"].Rebin(options.rebin)
        s.histos[pname]["total"].SetFillStyle(0)
        s.histos[pname]["total"].SetLineWidth(3)
        s.histos[pname]["total"].SetLineStyle(1)
        theIndivs.append(s.histos[pname]["total"])
        tl.AddEntry(s.histos[pname]["total"], s.config["label"], "l")

    if p["normalize"]:
      for index in range(len(theIndivs)):
        theIndivs[index].Scale(1./theIndivs[index].Integral())
      theStack = ROOT.THStack(pname+"_stack_norm", pname+ "_norm")
      for s in self.samples:
        if s.isBackground():
          s.histos[pname]["total"].Scale(1./stacksize)
          theStack.Add(s.histos[pname]["total"])
        
    # Now plotting stuff
    theStack.SetTitle("") 
    theStack.Draw("hist")
    theStack.GetXaxis().SetLabelSize(0)
    theStack.GetYaxis().SetLabelSize(0.04)
    theStack.GetYaxis().SetTitleSize(0.08)
    theStack.GetYaxis().SetTitleOffset(0.72)

    theStack.GetYaxis().SetTitle("Normalized events" if p["normalize"] else "Events")
    theStack.GetXaxis().SetTitle("") # Empty, as it goes into the ratio plot
    if "maxY" in p: 
      theStack.SetMaximum(p["maxY"])
    if "minY" in p:
      theStack.SetMinimum(p["minY"])

    theStack.Draw("hist")
    for ind in theIndivs:
      ind.Draw("hist same")
    # Last, draw the data
    for d in theData:
      d.Draw("P0 same")

    tl.Draw("same")

    # Now we go to the ratio
    p2.cd()

    # By default S/B, TODO: add more options
    den  = back.Clone("back_ratio")
    nums = [ind.Clone(ind.GetName()+ "_ratio") for ind in  theIndivs + theData]
    #den.Divide(den)
    for num in nums: 
      num.Divide(den)
    den.Divide(den)
    den.SetLineColor(ROOT.kBlack)
    den.SetTitle("")
    den.GetYaxis().SetTitle(options.ratioylabel)
    den.GetXaxis().SetTitle(p["xlabel"])
    den.GetYaxis().SetTitleSize(0.12)
    den.GetYaxis().SetTitleOffset(0.32)
    den.GetXaxis().SetTitleSize(0.12)
    den.GetXaxis().SetLabelSize(0.1)
    den.GetYaxis().SetLabelSize(0.06)

    if "ratiomaxY" in p:
      den.SetMaximum(p["ratiomaxY"])
    if "ratiominY" in p:
      den.SetMinimum(p["ratiominY"])
    den.Draw("")
    for num in nums:
      num.Draw("same") if not("data" in num.GetName()) else num.Draw("Psame")
    CMS_lumi.writeExtraText = True
    CMS_lumi.lumi_13TeV = "%.0f fb^{-1}" % options.luminosity
    CMS_lumi.extraText  = "Preliminary"
    CMS_lumi.lumi_sqrtS = "13"
    CMS_lumi.CMS_lumi(c, 4, 0, 0.122)

    if options.rebin:
      p["plotname"] = p["plotname"] + "_" + str(options.rebin) + "rebinned"

    c.SaveAs(options.plotdir + "/" + p["plotname"] + ".pdf")
    c.SaveAs(options.plotdir + "/" + p["plotname"] + ".png")
    # Also save as TH1 in root file 
    tf = ROOT.TFile(options.plotdir + "/" + p["plotname"] + ".root", "RECREATE")
    for s in self.samples:
      if s.isBackground():
        s.histos[pname]["total"].Write()
      else:
        s.histos[pname]["total"].Write()
    theStack.Write()
    tf.Close()


if __name__ == "__main__":
  print("Starting plotting script...")
  from optparse import OptionParser
  parser = OptionParser(usage="%prog [options] samples.py plots.py") 
  parser.add_option("-l","--luminosity", dest="luminosity", type="float", default=137, help="Luminosity")
  parser.add_option("-j","--jobs", dest="jobs", type="int", default=-1, help="Number of jobs (cores to use)")
  parser.add_option("--toSave", dest="toSave", type="str", default=None, help="If active, instead of plotting save per file histograms in this folder")
  parser.add_option("--toLoad", dest="toLoad", type="str", default=None, help="If active, instead of reading hdf5 load per file histograms from this folder")
  parser.add_option("-p","--plotdir", dest="plotdir", type="string", default="./", help="Where to put the plots")
  parser.add_option("--strict-order", dest="ordered", action="store_true", default=False, help="If true, will stack samples in the order of yields")

  parser.add_option("--sample", dest ="sample", default=None, help="If not none, process only this specific sample")
  parser.add_option("--files", dest="files", default=None, help="If not none, process only these set of comma separated files")
  parser.add_option("--queue", dest="queue", default=None, help="If not none, submit jobs to this queue")
  parser.add_option("--batchsize", dest="batchsize", default=1, help="Run this many files per batch job")
  parser.add_option("--jobname", dest="jobname", default="batchjobs", help="Folder in which to create the executable jobs")
  parser.add_option("--resubmit", dest="resubmit", default=False, action="store_true", help="If true, only run jobs that failed before (missing root files)")
  parser.add_option("--rebin", dest="rebin", default=None, type="int", help="Collapse bins by this factor")
  parser.add_option("--ratioylabel", dest="ratioylabel", type="string", default="S/B", help="Title of the Y axis of the ratio plot")

  (options, args) = parser.parse_args()
  samplesFile = imp.load_source("samples",args[0])
  plotsFile   = imp.load_source("plots",  args[1])
  if not(os.path.isdir(options.plotdir)):
    os.system("mkdir %s"%options.plotdir)
  if options.toSave and not(os.path.isdir(options.toSave)):
    os.system("mkdir %s"%options.toSave)
  os.system("cp %s %s %s"%(args[0], args[1], options.plotdir))
  samples = samplesFile.samples
  if options.sample:
    newsamples = {}
    newsamples[options.sample] = samples[options.sample]
    samples = newsamples
  if options.files:
    for s in samples:
      newfiles = []
      for f in samples[s]["files"]:
        print(f)
        if f in options.files:
          newfiles.append(f)
      samples[s]["files"] = newfiles

  plots   = plotsFile.plots
  thePlotter = plotter(plots, samples, options)
  if options.queue:
    print(options.jobname, os.path.isdir(options.jobname))
    if not(os.path.isdir(options.jobname)):
      print("mkdir %s"%options.jobname) 
      os.system("mkdir %s"%options.jobname)
    if not(os.path.isdir(options.jobname+"/exec")):
      os.system("mkdir %s/exec"%options.jobname)
    if not(os.path.isdir(options.jobname+"/batchlogs")):
      os.system("mkdir %s/batchlogs"%options.jobname)

    command = "python plotter_vh.py " + subprocess.list2cmdline(sys.argv[1:]).replace("--queue %s"%options.queue,"")
    savecommand = open("%s/command.txt"%options.toSave,"w")
    savecommand.write(command)
    savecommand.close()
    nJobs = thePlotter.createJobs(options, command)
    os.system("rm submit.sub")
    subfile = open("submit.sub", "w")
    subfile.write("executable              = $(filename)\n")
    subfile.write("arguments               = $(ClusterId)$(ProcId)\n")
    subfile.write("output                  = %s/$(ClusterId).$(ProcId).out\n"%("%s/batchlogs"%options.jobname))
    subfile.write("error                   = %s/$(ClusterId).$(ProcId).err\n"%("%s/batchlogs"%options.jobname))
    subfile.write("log                     = %s/$(ClusterId).log\n"%("%s/batchlogs"%options.jobname))
    subfile.write("+JobFlavour = \"%s\"\n"%(options.queue))
    subfile.write("queue filename matching (%s/exec/_*sh)\n"%("%s"%options.jobname))
    subfile.close()
    os.system("condor_submit -spool submit.sub")

  else:
    thePlotter.doPlots(options)
