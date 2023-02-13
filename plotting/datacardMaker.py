import ROOT
import imp
import copy
import re 

ROOT.gErrorIgnoreLevel = ROOT.kError

class datacardMaker(object):
  def __init__(self, samples, systs, output, options, channel = "bin1"):
    self.samples = samples
    self.systs   = systs
    self.output  = output
    self.options = options
    self.isCC    = False
    self.isShape = False
    self.signals = []
    self.backgr  = []
    self.data    = []
    self.channel = channel
  def createDatacards(self):
    self.collectYields()
    for s in self.samples:
      if "isSig" in self.samples[s]:
        if self.samples[s]["isSig"]:
          print("Create card for signal process %s..."%(s))
          self.createDatacard(s)
  def createDatacard(self, s):
    if not(self.options.ABCD):
      newcard = open(self.output + "/" + self.samples[s]["name"] + ".txt","w")
      newcard.write("imax *\njmax *\nkmax *\n")

      if self.isShape:
        newcard.write("shapes * * ./" + self.samples[s]["name"] + "_shapes.root $PROCESS\n")
      newcard.write("bin %s\n"%self.channel)
      newcard.write("observation -1\n")
      newcard.write("bin " + " ".join(["%s"%self.channel for i in range(len(self.backgr)+1)])+ "\n")
      newcard.write("process " + s + " " + " ".join(self.backgr)+"\n")
      newcard.write("process " + " ".join([str(i) for i in range(len(self.backgr)+1)])+"\n")
      newcard.write("rate " + " ".join(["-1" for i in range(len(self.backgr)+1)])+"\n")
      for syst in self.systs:
        if self.systs[syst]["type"] == "lnN":
          effects = ["-" for i in range(len(self.backgr)+1)]
          for pr in self.systs[syst]["processes"]:
            if re.match(pr, s):
              effects[0] = str(self.systs[syst]["size"])
            for ib, b in enumerate(self.backgr):
              if re.match(pr, b):
                effects[ib+1] = str(self.systs[syst]["size"])
          # Now format the line
          newcard.write(self.systs[syst]["name"] + " lnN " + " ".join(effects)+ "\n")
      if self.isShape: 
        newcard.write("* autoMCStats 0\n")
        rout = ROOT.TFile(self.output + "/" + self.samples[s]["name"] + "_shapes.root", "RECREATE")
        rout.cd()
        for b in self.backgr:
          self.th1s[b].Write()
        self.th1s["data_obs"].Write()
        self.th1s[s].Write()
        rout.Close()
      newcard.close()
    else:
      newcard = open(self.output + "/%s"%self.channel + "_" + self.samples[s]["name"] + ".txt","w")
      newcard.write("imax *\njmax *\nkmax *\n")
      if self.isShape:
        newcard.write("shapes * * ./%s"%self.channel + "_" + self.samples[s]["name"] + "_shapes.root $PROCESS_$CHANNEL $PROCESS_$CHANNEL_$SYSTEMATIC \n")
      newcard.write("bin " + " ".join(["%sbin%i"%(self.channel, i) for i in range(1,self.nbins+1)])  + " \n")
      newcard.write("observation " + " ".join(["-1"  for ibin in range(1, self.nbins+1)]) + " \n")
      newcard.write("bin " + " ".join([ " ".join(["%sbin%i"%(self.channel, j) for i in range(2)]) for j in range(1,self.nbins+1)])+" \n")
      newcard.write("process " + " ".join([s + " total_background" for i in range(self.nbins)])+"\n")
      newcard.write("process " + " ".join(["0 1" for i in range(self.nbins)])+"\n")
      newcard.write("rate " + " ".join(["-1 -1" for ibin in range(1, self.nbins+1)])+" \n")
      processes = []
      bins      = []
      for ibin in range(1,self.nbins+1):
        processes.append(s)
        processes.append("total_background")
        bins.append("%sbin%i"%(self.channel, ibin))
        bins.append("%sbin%i"%(self.channel, ibin))

      empty = ["-"]*len(processes)
      for syst in self.systs: # Now the fun begins:
        #print(syst)
        if self.systs[syst]["type"] == "lnN" or self.systs[syst]["type"] == "gmN":
          onlychannel = None
          if hasattr(self.systs[syst], "onlychannel"): 
            onlychannel = self.systs[syst]["onlychannel"]
          if onlychannel:
            if self.channel != onlychannel: 
              continue
          size = "-"
          name = syst
          for corrScheme in self.systs[syst]["corrs"]:
            if options.year in self.systs[syst]["corrs"][corrScheme]:
              name = syst + "_" + corrScheme
              for iyear, yearcorr in enumerate(self.systs[syst]["corrs"][corrScheme]):
                if options.year == yearcorr:
                  if size == "-": 
                    if type(self.systs[syst]["size"]) == type({"a":1}):
                      size = "%1.2f"%self.systs[syst]["size"][corrScheme][iyear] 
                    else:
                      size = "%1.2f"%self.systs[syst]["size"]
          if len(self.systs[syst]["corrs"]) == 1: 
            name = syst

          perbin = False
          if hasattr(self.systs[syst], "perbin"): 
            perbin = self.systs[syst]["perbin"]
          if not(perbin):
            effect = [size if any([re.match(princfg, princard)  for princfg in self.systs[syst]["processes"]]) else "-" for princard in processes]
            #print(size, effect, processes,  self.systs[syst]["processes"])
            if effect == empty:
              print("......lnN/gmN Systematic %s has no effect, will skip it"%(name))
            else:
              newcard.write("%s %s "%(name, self.systs[syst]["type"]) + " ".join(effect)+ " \n")
          else:
            basename = name
            for ibin in range(1, self.nbins+1):
              name = basename + "_bin"+str(ibin)
              effect = [size if any([re.match(princfg, processes[ientry]) and "bin%i"%ibin == bins[ientry]  for princfg in self.systs[syst]["processes"]]) else "-" for ientry in range(len(processes))]
              if effect == empty:
                print("......lnN/gmN Systematic %s has no effect, will skip it"%(name))
                continue
              else:
                newcard.write("%s %s "%(name, self.systs[syst]["type"]) + " ".join(effect)+ " \n")

        elif self.systs[syst]["type"] == "shape":
          onlychannel = None
          name = syst
          if hasattr(self.systs[syst], "onlychannel"):
            onlychannel = self.systs[syst]["onlychannel"]
          if onlychannel:
            if self.channel != onlychannel:
              continue
          size = "-"
          for corrScheme in self.systs[syst]["corrs"]:
            if options.year in self.systs[syst]["corrs"][corrScheme]:
              name = syst + "_" + corrScheme
              size = "1"
          if len(self.systs[syst]["corrs"]) == 1: 
            name = syst
          effect = [size if any([re.match(princfg, princard)  for princfg in self.systs[syst]["processes"]]) else "-" for princard in processes]
          if effect == empty:
            print("......Shape Systematic %s has no effect, will skip it"%(name))
            continue
          #print(size, effect, processes,  self.systs[syst]["processes"])
          newcard.write("%s %s "%(name, self.systs[syst]["type"]) + " ".join(effect)+ " \n")
          for ientry, entry in enumerate(effect):
            if entry == "-": 
              continue #No effect
            # Else we have to get the shapes and save them
            #print(self.tf,self.systs[syst]["match"].replace("$PROCESS", self.samples[s]["name"]).replace("[VAR]", self.options.var).replace("$SYSTEMATIC",syst).replace("[CHANNEL]", self.channel) + self.systs[syst]["up"], self.systs[syst]["match"].replace("$PROCESS", self.samples[s]["name"]).replace("[VAR]", self.options.var).replace("$SYSTEMATIC",syst).replace("[CHANNEL]", self.channel) + self.systs[syst]["down"]) 
            newup = self.tf.Get(self.systs[syst]["match"].replace("$PROCESS", self.samples[s]["name"]).replace("[VAR]", self.options.var).replace("$SYSTEMATIC",syst).replace("[CHANNEL]", self.channel) + self.systs[syst]["up"])
            newdn = self.tf.Get(self.systs[syst]["match"].replace("$PROCESS", self.samples[s]["name"]).replace("[VAR]", self.options.var).replace("$SYSTEMATIC",syst).replace("[CHANNEL]", self.channel) + self.systs[syst]["down"])
            for ibin in range(1, self.nbins + 1):
              self.th1s_perbin[ibin][s + syst + "Up"] = ROOT.TH1F("%s_%sbin%i_%sUp"%(s, self.channel, ibin, name), "%s_%sbin%i_%sUp"%(s, self.channel, ibin, name), 1, 0 , 1)
              self.th1s_perbin[ibin][s + syst + "Up"].SetBinContent(1, max(0.0001, newup.GetBinContent(ibin)))
              self.th1s_perbin[ibin][s + syst + "Up"].SetBinError(ibin, newup.GetBinError(ibin))
              self.th1s_perbin[ibin][s + syst + "Down"] = ROOT.TH1F("%s_%sbin%i_%sDown"%(s, self.channel, ibin, name), "%s_%sbin%i_%sDown"%(s, self.channel, ibin, name), 1, 0 , 1)
              self.th1s_perbin[ibin][s + syst + "Down"].SetBinContent(1, max(0.0001, newdn.GetBinContent(ibin)))
              self.th1s_perbin[ibin][s + syst + "Down"].SetBinError(1, newdn.GetBinError(ibin))
      newcard.write("* autoMCStats 0 1")
      rout = ROOT.TFile(self.output + "/%s_"%self.channel + self.samples[s]["name"] + "_shapes.root", "RECREATE")
      rout.cd()
      for ibin in range(1, self.nbins+1):
        for h in self.th1s_perbin[ibin]:
          if s in h or "background" in h or "data" in h:
            self.th1s_perbin[ibin][h].Write()
      rout.Close()


  def collectYields(self):
    if self.systs["yields"]["type"] == "yields":
      self.collectYieldsCutAndCount()
      self.nbins = 1
    elif self.systs["yields"]["type"] == "yieldsWithShapes" and not(options.ABCD):
      self.collectYieldsShapes()
      self.nbins = 1
    elif options.ABCD:
      self.collectYieldsPerBin()
    
  def collectYieldsCutAndCount(self): #TODO
    self.isCC = True
    pass
  def collectYieldsShapes(self):
    print("Collecting shape histograms...")
    self.isShape = True
    self.tf = ROOT.TFile(self.systs["yields"]["file"].replace("[ROOTFILE]", self.options.rootfile).replace("[CHANNEL]", self.channel if self.channel != "bin1" else ""),"READ")
    self.th1s   = {}
    self.yields = {}
    toDelete = []
    for s in self.samples:
      print("....%s"%s)
      newth1 = self.tf.Get(self.systs["yields"]["match"].replace("$PROCESS", self.samples[s]["name"]).replace("[VAR]", options.var).replace("[CHANNEL]",self.channel))
      if s != "data" or "data_obs" in self.th1s:
        self.th1s[s]   = copy.deepcopy(self.th1s["data_obs"] if s=="data" else newth1.Clone(s))
      self.yields[s] = newth1.Integral()
      if self.yields[s] == 0: 
        print("Process %s has 0 yields, skipping..."%s)
        del self.th1s[s]
        del self.yields[s]
        toDelete.append(s)
        #del self.samples[s]
        continue
      if not( "isSig" in self.samples[s]):
        self.backgr.append(s)
      else:
        if self.samples[s]["isSig"]:
          self.signals.append(s)
          continue
        else:
          self.backgr.append(s)
      if self.options.blind:  
        if not("data_obs" in self.th1s):
          self.th1s["data_obs"] = copy.deepcopy(self.th1s[s].Clone("data_obs"))
        else:
          self.th1s["data_obs"].Add(self.th1s[s])
    for d in toDelete:
      del self.samples[d]

  def collectYieldsPerBin(self):
    print("Collecting shape histograms for channel %s..."%self.channel)
    self.isShape = True
    print("...file is %s"%(self.systs["yields"]["file"].replace("[ROOTFILE]", self.options.rootfile).replace("[CHANNEL]", self.channel if self.channel != "bin1" else "")))
    self.tf = ROOT.TFile(self.systs["yields"]["file"].replace("[ROOTFILE]", self.options.rootfile).replace("[CHANNEL]", self.channel if self.channel != "bin1" else ""),"READ")
    self.th1s        = {}
    self.th1s_perbin = {}
    self.yields      = {}
    self.nbins = -1
    # First the nominal yields
    for s in self.samples:
      if not(self.samples[s]["isSig"]) or self.samples[s]["name"] == "data": continue
      if self.samples[s]["name"] == "data" and self.options.blind: continue
      #print("......Getting %s"%(self.systs["yields"]["match"].replace("$PROCESS", self.samples[s]["name"]).replace("[VAR]", self.options.var).replace("[CHANNEL]", self.channel)))
      newth1 = self.tf.Get(self.systs["yields"]["match"].replace("$PROCESS", self.samples[s]["name"]).replace("[VAR]", self.options.var).replace("[CHANNEL]", self.channel))
      self.th1s[s]   = copy.deepcopy(newth1.Clone("data_obs") if s=="data" else newth1.Clone(s))
      self.nbins = self.th1s[s].GetNbinsX()
      if not( "isSig" in self.samples[s]):
        self.backgr.append(s)
      else:
        if self.samples[s]["isSig"]:
          self.signals.append(s)
          continue
        else:
          self.backgr.append(s)
    if self.options.ABCD:
      self.th1s["total_background"] = copy.deepcopy(self.tf.Get("total_background").Clone("total_background"))
      self.backgr.append("total_background")
    if self.options.blind: 
      self.th1s["data_obs"] = copy.deepcopy(self.tf.Get("total_background").Clone("data_obs"))
      self.data.append("data_obs")
       
    for ibin in range(1,self.nbins+1):
      self.yields[ibin] = {} 
      self.th1s_perbin[ibin] = {}
      for s in self.signals + self.backgr + self.data:
        self.yields[ibin][s]      = max(0.1 if s in self.backgr else 0.0001, self.th1s[s].GetBinContent(ibin))
        self.th1s_perbin[ibin][s] = ROOT.TH1F("%s_%sbin%i"%(s, self.channel, ibin), "%s_%sbin%i"%(s, self.channel, ibin), 1, 0 , 1)
        self.th1s_perbin[ibin][s].SetBinContent(1, self.yields[ibin][s])
        self.th1s_perbin[ibin][s].SetBinError(1, min(self.yields[ibin][s], max(0.,self.th1s[s].GetBinError(1) )))

        if s in self.backgr:
          self.th1s_perbin[ibin][s].SetBinError(1, 0.)

if __name__ == "__main__":
  print("Starting plotting script...")
  from optparse import OptionParser
  parser = OptionParser(usage="%prog [options] samples.py systs.py output") 
  parser.add_option("--ms", dest="multisignal", action="store_true", default=False, help="Activate to have all signals in same card (default is different cards)")
  parser.add_option("--blind", dest="blind", action="store_true", default=False, help="Activate for blinding (no data)")
  parser.add_option("--rootfile", dest="rootfile", default="", help="ROOT file with the input shapes")
  parser.add_option("--var", dest="var", default="", help="Variable name in the plots file used to produce the rootfile")
  parser.add_option("--ABCD", dest="ABCD", default=False, action="store_true", help="Use ABCD background instead of directly MC")
  parser.add_option("--year", dest="year", default="2018", help="Which year the card is from")
  (options, args) = parser.parse_args()
  samplesFile   = imp.load_source("samples",args[0])
  systsFile     = imp.load_source("systematicsAndShapes", args[1])
  outputFolder  = args[2]
  if options.blind and "data" in samplesFile.samples:
    del samplesFile.samples["data"]
  if not (options.ABCD): #Build MC based cards, simple and direct
    dM = datacardMaker(samplesFile.samples, systsFile.systematicsAndShapes, outputFolder, options)
    dM.createDatacards()
  else: # If ABCD, one card per channel
    for ch in systsFile.systematicsAndShapes["yields"]["extendedABCD"]:
      dM =  datacardMaker(samplesFile.samples, systsFile.systematicsAndShapes, outputFolder, options, channel = ch)
      dM.createDatacards()
      del dM
