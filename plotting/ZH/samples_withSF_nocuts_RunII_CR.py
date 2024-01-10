import os
import ROOT
from auxiliars import *
from ZH.samples_withSF_nocuts_UL18_CR import samples as samplesUL18
from ZH.samples_withSF_nocuts_UL17_CR import samples as samplesUL17
from ZH.samples_withSF_nocuts_UL16_CR import samples as samplesUL16
from ZH.samples_withSF_nocuts_UL16APV_CR import samples as samplesUL16APV

def hdf5inpath(path):
  ret = []
  for f in os.listdir(path):
    if "hdf5" in f: 
      ret.append(path + "/" + f)
  return ret

theLumis = {"18": 59.9, "17": 41.6, "16": 16.4, "16APV": 19.9}
# Main path where samples are stored
samples = {
}

for sample in samplesUL18:
  newname = sample +"_UL18"
  #samplesUL18[sample]["name"] = newname
  samplesUL18[sample]["partialLumi"] = theLumis["18"]
  samplesUL18[sample]["year"]        = "18"
  samples[newname] = samplesUL18[sample]

for sample in samplesUL17:
  newname = sample +"_UL17"
  #samplesUL17[sample]["name"] = newname
  samplesUL17[sample]["partialLumi"] = theLumis["17"]
  samplesUL17[sample]["year"]        = "17"
  samples[newname] = samplesUL17[sample]

for sample in samplesUL16:
  newname = sample +"_UL16"
  #samplesUL16[sample]["name"] = newname
  samplesUL16[sample]["partialLumi"] = theLumis["16"]
  samplesUL16[sample]["year"]        = "16"
  samples[newname] = samplesUL16[sample]

for sample in samplesUL16APV:
  newname = sample +"_UL16APV"
  #samplesUL16APV[sample]["name"] = newname
  samplesUL16APV[sample]["partialLumi"] = theLumis["16APV"]
  samplesUL16APV[sample]["year"]        = "16APV"
  samples[newname] = samplesUL16APV[sample]

