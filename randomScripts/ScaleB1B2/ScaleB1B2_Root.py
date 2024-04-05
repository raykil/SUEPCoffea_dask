import ROOT
import os

def copy_and_modify_histograms(original_file_path, new_file_path):
    original_file = ROOT.TFile(original_file_path, "READ")
    new_file = ROOT.TFile(new_file_path, "RECREATE")
    
    for key in original_file.GetListOfKeys():
        obj = key.ReadObj()
        if isinstance(obj, ROOT.TH1F):
            new_hist = obj.Clone()
            if 'data_obs' in new_hist.GetName():
                for bin in range(1, new_hist.GetNbinsX() + 1):
                    original_content = new_hist.GetBinContent(bin)
                    original_error = new_hist.GetBinError(bin)
                    if 'B1' in new_hist.GetName():
                        new_hist.SetBinContent(bin, original_content*10)
                        new_hist.SetBinError(bin, original_error*10)
                    else:
                        new_hist.SetBinContent(bin, original_content*100)
                        new_hist.SetBinError(bin, original_error*100)           
            new_file.cd()
            new_hist.Write()
    
    # Close both files
    original_file.Close()
    new_file.Close()

def process_files(directory):
    for file_name in os.listdir(directory):
        if file_name.endswith('shapes_0Sig.root') and (file_name.startswith('CRDYB1') or file_name.startswith('CRDYB2')) and 'SUEP_hadronic_mS125_mD5.00_T5.00' in file_name:
            original_file_path = os.path.join(directory, file_name)
            new_file_path = os.path.join(directory, file_name.replace('.root', '_B1B2Scaled.root'))
            print(new_file_path)
            copy_and_modify_histograms(original_file_path, new_file_path)

process_files('/eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats/2016APV')
process_files('/eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats/2016')
process_files('/eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats/2017')
process_files('/eos/user/g/gdecastr/SUEPCoffea_dask/Cards/HighStats/2018')
