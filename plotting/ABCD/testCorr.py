import pandas as pd
import os
import sys

d = sys.argv[1] 
f = pd.HDFStore(d,"r")
a = f["SR"]
print(a.corr()[sys.argv[2]])
#print(a["leadclusterSpher_L"].corr(a["leadcluster_ntracks"]))
