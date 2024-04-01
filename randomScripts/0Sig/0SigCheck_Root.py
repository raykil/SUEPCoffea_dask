import ROOT
import os

def copy_and_modify_histograms(original_file_path, new_file_path):
    original_file = ROOT.TFile(original_file_path, "READ")
    new_file = ROOT.TFile(new_file_path, "RECREATE")
    
    for key in original_file.GetListOfKeys():
        obj = key.ReadObj()
        if isinstance(obj, ROOT.TH1F):
            new_hist = obj.Clone()
            if 'SUEP_hadronic_mS125_mD3.00_T3.00' in new_hist.GetName():
                for bin in range(1, new_hist.GetNbinsX() + 1):
                    new_hist.SetBinContent(bin, 0.000001)
                    new_hist.SetBinError(bin, 0.00000001)
            new_file.cd()
            new_hist.Write()
    
    # Close both files
    original_file.Close()
    new_file.Close()

def process_files(directory):
    for file_name in os.listdir(directory):
        if file_name.endswith('shapes.root') and file_name.startswith('CRTT') and 'SUEP_hadronic_mS125_mD3.00_T3.00' in file_name:
            original_file_path = os.path.join(directory, file_name)
            new_file_path = os.path.join(directory, file_name.replace('.root', '_0Sig.root'))
            copy_and_modify_histograms(original_file_path, new_file_path)

process_files('/eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats/2016APV')
process_files('/eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats/2016')
process_files('/eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats/2017')
process_files('/eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats/2018')
