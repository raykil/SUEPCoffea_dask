import ROOT
import copy

def cut(x, extra=lambda x:  (x["njets"] >= 0)):
  return (x["njets"] >= 0) & (abs(x["Z_m"]-90) < 30) & (x["Z_pt"] >= 25) & (x["nBLoose"] == 0) & (x["leadcluster_pt"] >= 60) & extra(x)

def cuttight(x, extra=lambda x:  (x["njets"] >= 0)):
  return (x["njets"] >= 0) & (abs(x["Z_m"]-90) < 30) & (x["Z_pt"] >= 25) & (x["nBLoose"] == 0) & (x["leadcluster_pt"] >= 60) & (x["leadcluster_ntracks"] >= 40) & extra(x)

def cut2mu(x, extra=lambda x:  (x["njets"] >= 0)):
  return (x["njets"] >= 0) & (abs(x["Z_m"]-90) < 30) & (x["Z_pt"] >= 25) & (x["nBLoose"] == 0) & (x["leadcluster_pt"] >= 60) & (x["nmuons"] == 2) & extra(x)

def cut2mutight(x, extra=lambda x:  (x["njets"] >= 0)):
  return (x["njets"] >= 0) & (abs(x["Z_m"]-90) < 30) & (x["Z_pt"] >= 25) & (x["nBLoose"] == 0) & (x["leadcluster_pt"] >= 60) & (x["leadcluster_ntracks"] >= 40) & (x["nmuons"] == 2) & extra(x)

def cut2el(x, extra=lambda x: (x["njets"] >= 0)):
  return (x["njets"] >= 0) & (abs(x["Z_m"]-90) < 30) & (x["Z_pt"] >= 25) & (x["nBLoose"] == 0) & (x["leadcluster_pt"] >= 60) & (x["nelectrons"] == 2) & extra(x)

def cut2eltight(x, extra=lambda x: (x["njets"] >= 0)):
  return (x["njets"] >= 0) & (abs(x["Z_m"]-90) < 30) & (x["Z_pt"] >= 25) & (x["nBLoose"] == 0) & (x["leadcluster_pt"] >= 60) & (x["leadcluster_ntracks"] >= 40) & (x["nelectrons"] == 2) & extra(x)





plots = {
  "leadclusterspher_base": {
             "name"     : "leadclusterspher_base",
             "bins"     : ["uniform", 50, 0, 1],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["leadclusterSpher_C"], y*cut(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "leadclusterspher_base",
             "xlabel"   : "S^{leadcluster}",
             "vars"     : ["leadclusterSpher_C"]
   },
"LeadMuon_mediumId": {
             "name"     : "LeadMuon_mediumId",
             "bins"     : ["uniform", 2, 0, 1],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["LeadMuon_mediumId"], y*cut2mu(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "LeadMuon_mediumId",
             "xlabel"   : "mediumId",
             "vars"     : ["LeadMuon_mediumId"]
   },
"SubLeadMuon_mediumId": {
             "name"     : "SubLeadMuon_mediumId",
             "bins"     : ["uniform", 2, 0, 1],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["SubLeadMuon_mediumId"], y*cut2mu(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "SubLeadMuon_mediumId",
             "xlabel"   : "mediumId",
             "vars"     : ["SubLeadMuon_mediumId"]
   },
"LeadMuon_mediumPromptId": {
             "name"     : "LeadMuon_mediumPromptId",
             "bins"     : ["uniform", 2, 0, 1],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["LeadMuon_mediumPromptId"], y*cut2mu(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "LeadMuon_mediumPromptId",
             "xlabel"   : "mediumPromptId",
             "vars"     : ["LeadMuon_mediumPromptId"]
   },
"SubLeadMuon_mediumPromptId": {
             "name"     : "SubLeadMuon_mediumPromptId",
             "bins"     : ["uniform", 2, 0, 1],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["SubLeadMuon_mediumPromptId"], y*cut2mu(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "SubLeadMuon_mediumPromptId",
             "xlabel"   : "mediumPromptId",
             "vars"     : ["SubLeadMuon_mediumPromptId"]
   },
"LeadMuon_miniIsoId": {
             "name"     : "LeadMuon_miniIsoId",
             "bins"     : ["uniform", 6, 0, 6],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["LeadMuon_miniIsoId"], y*cut2mu(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "LeadMuon_miniIsoId",
             "xlabel"   : "miniIsoId",
             "vars"     : ["LeadMuon_miniIsoId"]
   },
"SubLeadMuon_miniIsoId": {
             "name"     : "SubLeadMuon_miniIsoId",
             "bins"     : ["uniform", 6, 0, 6],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["SubLeadMuon_miniIsoId"], y*cut2mu(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "SubLeadMuon_miniIsoId",
             "xlabel"   : "miniIsoId",
             "vars"     : ["SubLeadMuon_miniIsoId"]
   },
"LeadMuon_multiIsoId": {
             "name"     : "LeadMuon_multiIsoId",
             "bins"     : ["uniform", 3, 0, 3],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["LeadMuon_multiIsoId"], y*cut2mu(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "LeadMuon_multiIsoId",
             "xlabel"   : "multiIsoId",
             "vars"     : ["LeadMuon_multiIsoId"]
   },
"SubLeadMuon_multiIsoId": {
             "name"     : "SubLeadMuon_multiIsoId",
             "bins"     : ["uniform", 3, 0, 3],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["SubLeadMuon_multiIsoId"], y*cut2mu(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "SubLeadMuon_multiIsoId",
             "xlabel"   : "multiIsoId",
             "vars"     : ["SubLeadMuon_multiIsoId"]
   },
"LeadMuon_mvaId": {
             "name"     : "LeadMuon_mvaId",
             "bins"     : ["uniform", 7, 0, 7],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["LeadMuon_mvaId"], y*cut2mu(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "LeadMuon_mvaId",
             "xlabel"   : "mvaId",
             "vars"     : ["LeadMuon_mvaId"]
   },
"SubLeadMuon_mvaId": {
             "name"     : "SubLeadMuon_mvaId",
             "bins"     : ["uniform", 7, 0, 7],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["SubLeadMuon_mvaId"], y*cut2mu(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "SubLeadMuon_mvaId",
             "xlabel"   : "mvaId",
             "vars"     : ["SubLeadMuon_mvaId"]
   },
"LeadMuon_pfIsoId": {
             "name"     : "LeadMuon_pfIsoId",
             "bins"     : ["uniform", 6, 0, 6],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["LeadMuon_pfIsoId"], y*cut2mu(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "LeadMuon_pfIsoId",
             "xlabel"   : "pfIsoId",
             "vars"     : ["LeadMuon_pfIsoId"]
   },
"SubLeadMuon_pfIsoId": {
             "name"     : "SubLeadMuon_pfIsoId",
             "bins"     : ["uniform", 6, 0, 6],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["SubLeadMuon_pfIsoId"], y*cut2mu(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "SubLeadMuon_pfIsoId",
             "xlabel"   : "pfIsoId",
             "vars"     : ["SubLeadMuon_pfIsoId"]
   },
"LeadMuon_tightId": {
             "name"     : "LeadMuon_tightId",
             "bins"     : ["uniform", 2, 0, 1],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["LeadMuon_tightId"], y*cut2mu(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "LeadMuon_tightId",
             "xlabel"   : "tightId",
             "vars"     : ["LeadMuon_tightId"]
   },
"SubLeadMuon_tightId": {
             "name"     : "SubLeadMuon_tightId",
             "bins"     : ["uniform", 2, 0, 1],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["SubLeadMuon_tightId"], y*cut2mu(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "SubLeadMuon_tightId",
             "xlabel"   : "tightId",
             "vars"     : ["SubLeadMuon_tightId"]
   },
"LeadMuon_genpart": {
             "name"     : "LeadMuon_genpart",
             "bins"     : ["uniform", 20, 0, 20],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["LeadMuon_genpart"], y*cut2mu(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "LeadMuon_genpart",
             "xlabel"   : "genpart",
             "vars"     : ["LeadMuon_genpart"]
   },
"SubLeadMuon_genpart": {
             "name"     : "SubLeadMuon_genpart",
             "bins"     : ["uniform", 20, 0, 20],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["SubLeadMuon_genpart"], y*cut2mu(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "SubLeadMuon_genpart",
             "xlabel"   : "genpart",
             "vars"     : ["SubLeadMuon_genpart"]
   },
"LeadElectron_cutBased": {
             "name"     : "LeadElectron_cutBased",
             "bins"     : ["uniform", 6, 0, 6],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["LeadElectron_cutBased"], y*cut2el(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "LeadElectron_cutBased",
             "xlabel"   : "cutBased",
             "vars"     : ["LeadElectron_cutBased"]
   },
"SubLeadElectron_cutBased": {
             "name"     : "SubLeadElectron_cutBased",
             "bins"     : ["uniform", 6, 0, 6],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["SubLeadElectron_cutBased"], y*cut2el(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "SubLeadElectron_cutBased",
             "xlabel"   : "cutBased",
             "vars"     : ["SubLeadElectron_cutBased"]
   },
"LeadElectron_mvaFall17V2Iso_WPL": {
             "name"     : "LeadElectron_mvaFall17V2Iso_WPL",
             "bins"     : ["uniform", 2, 0, 1],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["LeadElectron_mvaFall17V2Iso_WPL"], y*cut2el(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "LeadElectron_mvaFall17V2Iso_WPL",
             "xlabel"   : "mvaFall17V2Iso_WPL",
             "vars"     : ["LeadElectron_mvaFall17V2Iso_WPL"]
   },
"SubLeadElectron_mvaFall17V2Iso_WPL": {
             "name"     : "SubLeadElectron_mvaFall17V2Iso_WPL",
             "bins"     : ["uniform", 2, 0, 1],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["SubLeadElectron_mvaFall17V2Iso_WPL"], y*cut2el(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "SubLeadElectron_mvaFall17V2Iso_WPL",
             "xlabel"   : "mvaFall17V2Iso_WPL",
             "vars"     : ["SubLeadElectron_mvaFall17V2Iso_WPL"]
   },
"LeadElectron_mvaFall17V2Iso_WP90": {
             "name"     : "LeadElectron_mvaFall17V2Iso_WP90",
             "bins"     : ["uniform", 2, 0, 1],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["LeadElectron_mvaFall17V2Iso_WP90"], y*cut2el(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "LeadElectron_mvaFall17V2Iso_WP90",
             "xlabel"   : "mvaFall17V2Iso_WP90",
             "vars"     : ["LeadElectron_mvaFall17V2Iso_WP90"]
   },
"SubLeadElectron_mvaFall17V2Iso_WP90": {
             "name"     : "SubLeadElectron_mvaFall17V2Iso_WP90",
             "bins"     : ["uniform", 2, 0, 1],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["SubLeadElectron_mvaFall17V2Iso_WP90"], y*cut2el(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "SubLeadElectron_mvaFall17V2Iso_WP90",
             "xlabel"   : "mvaFall17V2Iso_WP90",
             "vars"     : ["SubLeadElectron_mvaFall17V2Iso_WP90"]
   },
"LeadElectron_mvaFall17V2Iso_WP80": {
             "name"     : "LeadElectron_mvaFall17V2Iso_WP80",
             "bins"     : ["uniform", 2, 0, 1],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["LeadElectron_mvaFall17V2Iso_WP80"], y*cut2el(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "LeadElectron_mvaFall17V2Iso_WP80",
             "xlabel"   : "mvaFall17V2Iso_WP80",
             "vars"     : ["LeadElectron_mvaFall17V2Iso_WP80"]
   },
"SubLeadElectron_mvaFall17V2Iso_WP80": {
             "name"     : "SubLeadElectron_mvaFall17V2Iso_WP80",
             "bins"     : ["uniform", 2, 0, 1],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["SubLeadElectron_mvaFall17V2Iso_WP80"], y*cut2el(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "SubLeadElectron_mvaFall17V2Iso_WP80",
             "xlabel"   : "mvaFall17V2Iso_WP80",
             "vars"     : ["SubLeadElectron_mvaFall17V2Iso_WP80"]
   },
"LeadElectron_mvaFall17V2noIso_WPL": {
             "name"     : "LeadElectron_mvaFall17V2noIso_WPL",
             "bins"     : ["uniform", 2, 0, 1],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["LeadElectron_mvaFall17V2noIso_WPL"], y*cut2el(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "LeadElectron_mvaFall17V2noIso_WPL",
             "xlabel"   : "mvaFall17V2noIso_WPL",
             "vars"     : ["LeadElectron_mvaFall17V2noIso_WPL"]
   },
"SubLeadElectron_mvaFall17V2noIso_WPL": {
             "name"     : "SubLeadElectron_mvaFall17V2noIso_WPL",
             "bins"     : ["uniform", 2, 0, 1],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["SubLeadElectron_mvaFall17V2noIso_WPL"], y*cut2el(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "SubLeadElectron_mvaFall17V2noIso_WPL",
             "xlabel"   : "mvaFall17V2noIso_WPL",
             "vars"     : ["SubLeadElectron_mvaFall17V2noIso_WPL"]
   },
"LeadElectron_mvaFall17V2noIso_WP90": {
             "name"     : "LeadElectron_mvaFall17V2noIso_WP90",
             "bins"     : ["uniform", 2, 0, 1],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["LeadElectron_mvaFall17V2noIso_WP90"], y*cut2el(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "LeadElectron_mvaFall17V2noIso_WP90",
             "xlabel"   : "mvaFall17V2noIso_WP90",
             "vars"     : ["LeadElectron_mvaFall17V2noIso_WP90"]
   },
"SubLeadElectron_mvaFall17V2noIso_WP90": {
             "name"     : "SubLeadElectron_mvaFall17V2noIso_WP90",
             "bins"     : ["uniform", 2, 0, 1],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["SubLeadElectron_mvaFall17V2noIso_WP90"], y*cut2el(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "SubLeadElectron_mvaFall17V2noIso_WP90",
             "xlabel"   : "mvaFall17V2noIso_WP90",
             "vars"     : ["SubLeadElectron_mvaFall17V2noIso_WP90"]
   },
"LeadElectron_mvaFall17V2noIso_WP80": {
             "name"     : "LeadElectron_mvaFall17V2noIso_WP80",
             "bins"     : ["uniform", 2, 0, 1],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["LeadElectron_mvaFall17V2noIso_WP80"], y*cut2el(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "LeadElectron_mvaFall17V2noIso_WP80",
             "xlabel"   : "mvaFall17V2noIso_WP80",
             "vars"     : ["LeadElectron_mvaFall17V2noIso_WP80"]
   },
"SubLeadElectron_mvaFall17V2noIso_WP80": {
             "name"     : "SubLeadElectron_mvaFall17V2noIso_WP80",
             "bins"     : ["uniform", 2, 0, 1],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["SubLeadElectron_mvaFall17V2noIso_WP80"], y*cut2el(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "SubLeadElectron_mvaFall17V2noIso_WP80",
             "xlabel"   : "mvaFall17V2noIso_WP80",
             "vars"     : ["SubLeadElectron_mvaFall17V2noIso_WP80"]
   },
"LeadElectron_miniIso": {
             "name"     : "LeadElectron_miniIso",
             "bins"     : ["uniform", 40, 0, 4],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["LeadElectron_miniIso"], y*cut2el(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "LeadElectron_miniIso",
             "xlabel"   : "miniIso",
             "vars"     : ["LeadElectron_miniIso"]
   },
"SubLeadElectron_miniIso": {
             "name"     : "SubLeadElectron_miniIso",
             "bins"     : ["uniform", 40, 0, 4],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["SubLeadElectron_miniIso"], y*cut2el(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "SubLeadElectron_miniIso",
             "xlabel"   : "miniIso",
             "vars"     : ["SubLeadElectron_miniIso"]
   },
"LeadElectron_pfRelIso": {
             "name"     : "LeadElectron_pfRelIso",
             "bins"     : ["uniform", 40, 0, 4],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["LeadElectron_pfRelIso"], y*cut2el(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "LeadElectron_pfRelIso",
             "xlabel"   : "pfRelIso",
             "vars"     : ["LeadElectron_pfRelIso"]
   },
"SubLeadElectron_pfRelIso": {
             "name"     : "SubLeadElectron_pfRelIso",
             "bins"     : ["uniform", 40, 0, 4],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["SubLeadElectron_pfRelIso"], y*cut2el(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "SubLeadElectron_pfRelIso",
             "xlabel"   : "pfRelIso",
             "vars"     : ["SubLeadElectron_pfRelIso"]
   },
"LeadElectron_genpart": {
             "name"     : "LeadElectron_genpart",
             "bins"     : ["uniform", 20, 0, 20],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["LeadElectron_genpart"], y*cut2el(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "LeadElectron_genpart",
             "xlabel"   : "genpart",
             "vars"     : ["LeadElectron_genpart"]
   },
"SubLeadElectron_genpart": {
             "name"     : "SubLeadElectron_genpart",
             "bins"     : ["uniform", 20, 0, 20],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["SubLeadElectron_genpart"], y*cut2el(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "SubLeadElectron_genpart",
             "xlabel"   : "genpart",
             "vars"     : ["SubLeadElectron_genpart"]
   },
"LeadLepton_dxy": {
             "name"     : "LeadLepton_dxy",
             "bins"     : ["uniform", 50, -1, 1],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["LeadLepton_dxy"], y*cut(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "LeadLepton_dxy",
             "xlabel"   : "dxy",
             "vars"     : ["LeadLepton_dxy"]
   },
"SubLeadLepton_dxy": {
             "name"     : "SubLeadLepton_dxy",
             "bins"     : ["uniform", 50, -1, 1],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["SubLeadLepton_dxy"], y*cut(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "SubLeadLepton_dxy",
             "xlabel"   : "dxy",
             "vars"     : ["SubLeadLepton_dxy"]
   },
"LeadLepton_dz": {
             "name"     : "LeadLepton_dz",
             "bins"     : ["uniform", 50, -1, 1],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["LeadLepton_dz"], y*cut(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "LeadLepton_dz",
             "xlabel"   : "dz",
             "vars"     : ["LeadLepton_dz"]
   },
"SubLeadLepton_dz": {
             "name"     : "SubLeadLepton_dz",
             "bins"     : ["uniform", 50, -1, 1],
             "channel"  : "SR",
             "value"    : lambda x, y : (x["SubLeadLepton_dz"], y*cut(x)),
             "logY"     : True,
             "normalize": False,
             "maxY"     : 1e9,
             "minY"     : 1e0,
             "ratiomaxY": 2.,
             "ratiominY": 0.,
             "plotname" : "SubLeadLepton_dz",
             "xlabel"   : "dz",
             "vars"     : ["SubLeadLepton_dz"]
   },
}

functions = {"2mu": cut2mu, "2mutight": cut2mutight, "2el": cut2el, "2eltight":cut2eltight, "2lep": cut, "2leptight": cuttight}
for tag in functions:
  newname = "leadclusterspher_base".replace("base", tag)
  plots[newname] = copy.deepcopy(plots["leadclusterspher_base"])
  plots[newname]["name"]     = newname
  plots[newname]["plotname"] = newname
  plots[newname]["value"]    = lambda x, y, tag=tag: (x["leadclusterSpher_C"], y*functions[tag](x))
  #print(newname)
mufunctions = {"Medium": lambda x: (x["LeadMuon_mediumId"]) & (x["SubLeadMuon_mediumId"]), "Tight": lambda x: (x["LeadMuon_tightId"]) & (x["SubLeadMuon_tightId"]), "MediumPrompt": lambda x: (x["LeadMuon_mediumPromptId"]) & (x["SubLeadMuon_mediumPromptId"]), "MiniIsoL": lambda x: (x["LeadMuon_miniIsoId"] >= 1) & (x["SubLeadMuon_miniIsoId"] >= 1), "MiniIsoM": lambda x: (x["LeadMuon_miniIsoId"] >= 2) & (x["SubLeadMuon_miniIsoId"] >= 2), "MiniIsoT": lambda x: (x["LeadMuon_miniIsoId"] >= 3) & (x["SubLeadMuon_miniIsoId"] >= 3), "MiniIsoVT": lambda x: (x["LeadMuon_miniIsoId"] >= 4) & (x["SubLeadMuon_miniIsoId"] >= 4), "MultiIsoL": lambda x: (x["LeadMuon_multiIsoId"] >= 1) & (x["SubLeadMuon_multiIsoId"] >= 1), "MultiIsoT": lambda x: (x["LeadMuon_multiIsoId"] >= 2) & (x["SubLeadMuon_multiIsoId"] >= 2), "MVAL": lambda x: (x["LeadMuon_mvaId"] >= 1) & (x["SubLeadMuon_mvaId"] >= 1) , "MVAM": lambda x: (x["LeadMuon_mvaId"] >= 3) & (x["SubLeadMuon_mvaId"] >= 3), "MVAT": lambda x: (x["LeadMuon_mvaId"] >= 5) & (x["SubLeadMuon_mvaId"] >= 5),  "pfIsoVL": lambda x: (x["LeadMuon_pfIsoId"] >= 1) & (x["SubLeadMuon_pfIsoId"] >= 1), "pfIsoL": lambda x: (x["LeadMuon_pfIsoId"] >= 2) & (x["SubLeadMuon_pfIsoId"] >= 2), "pfIsoM": lambda x: (x["LeadMuon_pfIsoId"] >= 3) & (x["SubLeadMuon_pfIsoId"] >= 3), "pfIsoT": lambda x: (x["LeadMuon_pfIsoId"] >= 4) & (x["SubLeadMuon_pfIsoId"] >= 4), "pfIsoVT": lambda x: (x["LeadMuon_pfIsoId"] >= 5) & (x["SubLeadMuon_pfIsoId"] >= 5), "pfIsoVVT": lambda x: (x["LeadMuon_pfIsoId"] >= 6) & (x["SubLeadMuon_pfIsoId"] >= 6)}


for mtag in mufunctions:
  for tag in ["2mu", "2mutight"]:
    newname = "leadclusterspher_base".replace("base", tag + "_" + mtag)
    plots[newname] = copy.deepcopy(plots["leadclusterspher_base"])
    plots[newname]["name"]     = newname
    plots[newname]["plotname"] = newname
    plots[newname]["value"]    = lambda x, y, tag=tag, mtag=mtag: (x["leadclusterSpher_C"], y*functions[tag](x, extra=mufunctions[mtag]))
    #print(newname)

elfunctions = {"Veto": lambda x: (x["LeadElectron_cutBased"] >= 0) & (x["SubLeadElectron_cutBased"] >= 0), "Loose": lambda x: (x["LeadElectron_cutBased"] >= 1) & (x["SubLeadElectron_cutBased"] >= 1), "Medium": lambda x: (x["LeadElectron_cutBased"] >= 2) & (x["SubLeadElectron_cutBased"] >= 2), "Tight": lambda x: (x["LeadElectron_cutBased"] >= 3) & (x["SubLeadElectron_cutBased"] >= 3), "VTight": lambda x: (x["LeadElectron_cutBased"] >= 4) & (x["SubLeadElectron_cutBased"] >= 4), "MVAIso_WPL": lambda x: (x["LeadElectron_mvaFall17V2Iso_WPL"] >= 1) & (x["SubLeadElectron_mvaFall17V2Iso_WPL"] >= 1), "MVAnoIso_WPL": lambda x: (x["LeadElectron_mvaFall17V2noIso_WPL"] >= 1) & (x["SubLeadElectron_mvaFall17V2noIso_WPL"] >= 1), "MVAIso_WP90": lambda x: (x["LeadElectron_mvaFall17V2Iso_WP90"] >= 1) & (x["SubLeadElectron_mvaFall17V2Iso_WP90"] >= 1), "MVAnoIso_WP90": lambda x: (x["LeadElectron_mvaFall17V2noIso_WP90"] >= 1) & (x["SubLeadElectron_mvaFall17V2noIso_WP90"] >= 1), "MVAIso_WP80": lambda x: (x["LeadElectron_mvaFall17V2Iso_WP80"] >= 1) & (x["SubLeadElectron_mvaFall17V2Iso_WP80"] >= 1), "MVAnoIso_WP80": lambda x: (x["LeadElectron_mvaFall17V2noIso_WP80"] >= 1) & (x["SubLeadElectron_mvaFall17V2noIso_WP80"] >= 1),"MiniIsoL": lambda x: (x["LeadElectron_miniIso"] <= 0.4) & (x["SubLeadElectron_miniIso"] <= 0.4), "MiniIsoM": lambda x: (x["LeadElectron_miniIso"] <= 0.2) & (x["SubLeadElectron_miniIso"] <= 0.2), "MiniIsoT": lambda x: (x["LeadElectron_miniIso"] <= 0.1) & (x["SubLeadElectron_miniIso"] <= 0.1), "MiniIsoVT": lambda x: (x["LeadElectron_miniIso"] <= 0.05) & (x["SubLeadElectron_miniIso"] <= 0.05), "PFIsoL": lambda x: (x["LeadElectron_pfRelIso"] <= 0.4) & (x["SubLeadElectron_pfRelIso"] <= 0.4), "PFIsoM": lambda x: (x["LeadElectron_pfRelIso"] <= 0.2) & (x["SubLeadElectron_pfRelIso"] <= 0.2), "PFIsoT": lambda x: (x["LeadElectron_pfRelIso"] <= 0.1) & (x["SubLeadElectron_pfRelIso"] <= 0.1), "PFIsoVT": lambda x: (x["LeadElectron_pfRelIso"] <= 0.05) & (x["SubLeadElectron_pfRelIso"] <= 0.05)}


for eltag in elfunctions:
  for tag in ["2el", "2eltight"]:
    newname = "leadclusterspher_base".replace("base", tag + "_" + eltag)
    plots[newname] = copy.deepcopy(plots["leadclusterspher_base"])
    plots[newname]["name"]     = newname
    plots[newname]["plotname"] = newname
    plots[newname]["value"]    = lambda x, y, tag=tag, eltag=eltag: (x["leadclusterSpher_C"], y*functions[tag](x, extra=elfunctions[eltag]))
    #print(newname)

lepfunctions = {"dxy0p5": lambda x: (abs(x["LeadLepton_dxy"]) < 0.5) & (abs(x["SubLeadLepton_dxy"]) < 0.5), "dxy0p25": lambda x: (abs(x["LeadLepton_dxy"]) < 0.25) & (abs(x["SubLeadLepton_dxy"]) < 0.25), "dxy0p1": lambda x: (abs(x["LeadLepton_dxy"]) < 0.1) & (abs(x["SubLeadLepton_dxy"]) < 0.1), "dxy0p05": lambda x: (abs(x["LeadLepton_dxy"]) < 0.05) & (abs(x["SubLeadLepton_dxy"]) < 0.05), "dz0p5": lambda x: (abs(x["LeadLepton_dz"]) < 0.5) & (abs(x["SubLeadLepton_dz"]) < 0.5), "dz0p25": lambda x: (abs(x["LeadLepton_dz"]) < 0.25) & (abs(x["SubLeadLepton_dz"]) < 0.25), "dz0p1": lambda x: (abs(x["LeadLepton_dz"]) < 0.1) & (abs(x["SubLeadLepton_dz"]) < 0.1), "dz0p05": lambda x: (abs(x["LeadLepton_dz"]) < 0.05) & (abs(x["SubLeadLepton_dz"]) < 0.05)}


for leptag in lepfunctions:
  for tag in ["2lep", "2leptight"]:
    newname = "leadclusterspher_base".replace("base", tag + "_" + leptag)
    plots[newname] = copy.deepcopy(plots["leadclusterspher_base"])
    plots[newname]["name"]     = newname
    plots[newname]["plotname"] = newname
    plots[newname]["value"]    = lambda x, y, tag=tag, leptag=leptag: (x["leadclusterSpher_C"], y*functions[tag](x, extra=lepfunctions[leptag]))
    #print(newname)

#print(plots.keys())
