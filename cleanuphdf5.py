import os
import sys
import pandas as pd
import h5py

fold = sys.argv[1]
strict = len(sys.argv) > 2
imin = -1
imax = 1e99
repeatedIndexFils = []
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
    try:
      test = 0
      with h5py.File(totfil, 'r') as h5file:
        #print("File Structure:")
        #print(h5file)
        
        #print("\nGroups:")
        for group_name in h5file:
            #print(group_name)
            test = group_name
        
        #print("\nAttributes:")
        for attr_name in h5file.attrs:
            #print(f"{attr_name}: {h5file.attrs[attr_name]}")
            test = attr_name

        #print("\nDatasets:")
        for group_name in h5file:
            group = h5file[group_name]
            for dataset_name in group:
                dataset = group[dataset_name]
                #print(f"{group_name}/{dataset_name}: {dataset.shape}, {dataset.dtype}")
      df = pd.read_hdf(totfil, key='/onecluster')
      if df.index.duplicated().any():
          print(f"File {totfil} may be corrupted: Repeated indices found!")
          repeatedIndexFils.append(totfil)

    except FileNotFoundError:
        print("Error: The specified file was not found.")
        iBad += 1
        os.system("rm %s"%totfil)
    except (IOError, OSError) as e:
        print("Error: An HDF5-related error occurred.")
        print(e)
        iBad += 1
        os.system("rm %s"%totfil)
    except Exception as e:
        print("An unexpected error occurred:")
        print(e)   
        iBad += 1
        os.system("rm %s"%totfil)

  print("%i/%i files broken for process %s"%(iBad, iTot, f))
  print(repeatedIndexFils)
