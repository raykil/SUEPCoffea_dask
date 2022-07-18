import pandas as pd
import os
import sys

d = sys.argv[1] 
f = pd.HDFStore(d,"r")
a = f["onecluster"]
print(a.corr()["leadjet_pt"])
#print(a["leadclusterSpher_L"].corr(a["leadcluster_ntracks"]))
