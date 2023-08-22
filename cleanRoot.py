import os
import sys

inF = sys.argv[1]
minS= int(sys.argv[2])
for f in os.listdir(inF):
  if not("root" in f): continue
  #if "data" in f: continue
  #print(f, os.path.getsize(inF + "/" + f), minS)
  if os.path.getsize(inF + "/" + f) < minS:
    os.system("rm %s"%(inF+"/"+ f))
    print(f)