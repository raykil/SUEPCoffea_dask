import ROOT
import imp
import copy
import re 
class datacardMaker(object):
  def __init__(self, samples, systs, output, options):
    self.samples = samples
    self.systs   = systs
    self.output  = output
    self.options = options
    self.isCC    = False
    self.isShape = False
    self.signals = []
    self.backgr  = []
  def createDatacards(self):
    self.collectYields()
    for s in self.samples:
      if "isSig" in self.samples[s]:
        if self.samples[s]["isSig"]:
          print("Create card for signal process %s"%(s))
          self.createDatacard(s)
  def createDatacard(self, s):
    newcard = open(self.output + "/" + self.samples[s]["name"] + ".txt","w")
    newcard.write("imax *\njmax *\nkmax *\n")
    if self.isShape:
      newcard.write("shapes * * ./" + self.samples[s]["name"] + "_shapes.root $PROCESS\n")
    newcard.write("bin bin1\n")
    newcard.write("observation -1\n")
    newcard.write("bin " + " ".join(["bin1" for i in range(len(self.backgr)+1)])+ "\n")
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

  def collectYields(self):
    if self.systs["yields"]["type"] == "yields":
      self.collectYieldsCutAndCount()
    if self.systs["yields"]["type"] == "yieldsWithShapes":
      self.collectYieldsShapes()
  def collectYieldsCutAndCount(self): #TODO
    self.isCC = True
    pass
  def collectYieldsShapes(self):
    print("Collecting shape histograms...")
    self.isShape = True
    tf = ROOT.TFile(self.systs["yields"]["file"],"READ")
    self.th1s   = {}
    self.yields = {}
    toDelete = []
    for s in self.samples:
      print("....%s"%s)
      print(self.systs["yields"]["match"].replace("$PROCESS", self.samples[s]["name"]))
      newth1 = tf.Get(self.systs["yields"]["match"].replace("$PROCESS", self.samples[s]["name"]))
      self.th1s[s]   = copy.deepcopy("data_obs" if s=="data" else newth1.Clone(s))
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


if __name__ == "__main__":
  print("Starting plotting script...")
  from optparse import OptionParser
  parser = OptionParser(usage="%prog [options] samples.py systs.py output") 
  parser.add_option("--ms", dest="multisignal", action="store_true", default=False, help="Activate to have all signals in same card (default is different cards)")
  parser.add_option("--blind", dest="blind", action="store_true", default=False, help="Activate for blinding (no data)")

  (options, args) = parser.parse_args()
  samplesFile   = imp.load_source("samples",args[0])
  systsFile     = imp.load_source("systematicsAndShapes", args[1])
  outputFolder  = args[2]
  if options.blind:
    del samplesFile.samples["data"]
  dM = datacardMaker(samplesFile.samples, systsFile.systematicsAndShapes, outputFolder, options)
  dM.createDatacards()  
