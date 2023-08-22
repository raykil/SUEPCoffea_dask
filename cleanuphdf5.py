import os
import sys
import pandas as pd

fold = sys.argv[1]
strict = len(sys.argv) > 2
imin = -1
imax = 1e99
if len(sys.argv) > 4:
  imin = int(sys.argv[3])
  imax = int(sys.argv[4])
for f in os.listdir(fold):
  iBad  = 0
  iTot  = 0
  path = fold + "/" + f
  for ifil, fil in enumerate(os.listdir(path)):
    if (ifil %100) == 0: print("File %i/%i"%(ifil, len(os.listdir(path))))
    if len(sys.argv) > 4:
      if ifil < imin: continue
      if ifil > imax: break
    if not("hdf5" in fil):
      continue
    else:
      totfil = path + "/" + fil
      iTot += 1
      if os.path.getsize(totfil) == 0:
        iBad += 1
        os.system("rm %s"%totfil)
      elif strict:
        try:
          a = pd.HDFStore(totfil, "r")
          if not(sys.argv[2] in a.keys()):
            iBad += 1
            a.close()
            del a
            os.system("rm %s"%totfil)
        except:
          iBad += 1
          os.system("rm %s"%totfil)

  print("%i/%i files broken for process %s"%(iBad, iTot, f))