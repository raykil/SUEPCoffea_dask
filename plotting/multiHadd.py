import os
from multiprocessing import Pool
from contextlib import closing
import time
import ROOT

def uniformizeNames(x):
  output = x[0]
  inputF = x[1]
  tfIn  = ROOT.TFile(inputF, "READ")
  tfOut = ROOT.TFile(output, "RECREATE") 
  for h in tfIn.GetListOfKeys(): 
    oldName = h.GetName()
    newName = "_".join(oldName.split("_")[:-3])
    hObj = tfIn.Get(oldName).Clone(newName)
    tfOut.cd()
    hObj.Write()
  tfIn.Close()
  tfOut.Close()
  return x[0]

def haddFiles(x):
  output = x[0]
  inputs = x[1]
  os.system("hadd %s %s >> /dev/null "%(output, " ".join(inputs))) # Verbose log is destroyed
  return output

def haddAll(inputFiles, outputFil, nThreads = 10):
  if len(inputFiles) == 1:
    print("One file, automatic merge")
    uniformizeNames([outputFil,inputFiles[0]])
    return
  tStart = time.time()
  nSteps   = max(10, min(len(inputFiles)/(nThreads**2), 100))  # This means we will run always 3 iterations of the hadder N => N/nStep => N/nStep**2 => 1
  tmpdir = "tmp_%1.5f"%time.time() # Temporary folder where we can store all the trash we are about to produce
  os.system("mkdir %s"%tmpdir)
  here = os.getcwd()
  os.chdir(tmpdir)
  toHaddFiles = inputFiles

  # Uniformize TH1 names
  toUniformize = [["temp_%i.root"%i,f] for i, f in enumerate(toHaddFiles)]

  with closing(Pool(nThreads)) as p:
    totjobs    = len(toUniformize)
    printEvery = 100
    nextprint  = totjobs
    retlist1 = p.map_async(uniformizeNames, toUniformize, 1)
    tin = time.time()
    while not retlist1.ready():
      if retlist1._number_left < nextprint:
        dt = time.time() - tin
        print("....Files left for uniformization: {}".format(retlist1._number_left ) + " with %i input files, ellapsed time %1.1f s"%(len(toUniformize), dt))
        nextprint = retlist1._number_left - printEvery
      time.sleep(1)
    retlist1 = retlist1.get()
    p.close()
    p.join()
    p.terminate()

  toHaddFiles = retlist1

  # Now do the merging in several steps to profit from parallelization and not saturate I/O
  subidx = 0
  while len(toHaddFiles) > 1:
    subidx += 1
    chunks  = []
    for f in toHaddFiles:
      if len(chunks) == 0:
        chunks.append([f])
      elif len(chunks[-1]) < nSteps:
        chunks[-1].append(f)
      else:
        chunks.append([f])
    toProcess = [["temp_sub%i_%i.root"%(subidx, i), chunks[i]] for i in range(len(chunks))]
    with closing(Pool(nThreads)) as p:
      totjobs    = len(toUniformize)/nSteps
      printEvery = 1
      nextprint  = totjobs
      retlist1 = p.map_async(haddFiles, toProcess, 1)
      tin = time.time()
      while not retlist1.ready():
        if retlist1._number_left < nextprint: 
          dt = time.time() - tin
          print("....Files left for hadding: {}".format(retlist1._number_left ) + " Run %i with %i input files, ellapsed time %1.1f s"%(subidx, len(toHaddFiles), dt))
          nextprint = retlist1._number_left - printEvery
        time.sleep(1)
      retlist1 = retlist1.get()
      p.close()
      p.join()
      p.terminate()
    for index in range(10): 
      if subidx == 1:
        os.system("rm temp_%i*"%index)
      else:
        os.system("rm temp_sub%i_%i*"%(subidx-1,index))

    toHaddFiles = retlist1
  if len(toHaddFiles) == 1:
    os.system("mv %s %s"%(toHaddFiles[0], outputFil))
    os.chdir(here) # Go back where we were
    os.system("rm -r %s"%tmpdir)
  print("Done in %1.1f"%(time.time()-tStart))
