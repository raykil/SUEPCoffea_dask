import uproot
import matplotlib.pyplot as plt

# Open the ROOT file using uproot
root_file = uproot.open("RunII/higgsCombine55_SR_Scan.MultiDimFit.mH120.root")

# Access the 'limit;1' tree
tree = root_file["limit;1"]

# Extract the 'nll' and 'r' branches as NumPy arrays
nll_values = tree["deltaNLL"].array()
r_values = tree["r"].array()

# Create a 2D plot using matplotlib
plt.figure(figsize=(8, 6))
plt.scatter(r_values, nll_values, marker='.', c='b', label='nll vs r')
plt.xlabel('r')
plt.ylabel('deltaNLL')
plt.title('2D Plot of deltaNLL vs r')
plt.grid(True)
plt.legend()

# Show the plot
plt.savefig('LikelihoodScan_Hadronic_5_5.png')
