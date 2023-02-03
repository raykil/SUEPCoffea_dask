import os
import pathlib
import shutil
import awkward as ak
import pandas as pd
import numpy as np
import fastjet
from coffea import hist, processor
import vector
from typing import List, Optional
vector.register_awkward()

class SUEP_cluster(processor.ProcessorABC):
    def __init__(self, isMC: int, era: int, sample: str,  do_syst: bool, syst_var: str, weight_syst: bool, SRonly: bool, output_location: Optional[str], doOF: Optional[bool], isDY: Optional[bool]) -> None:
        self.SRonly = SRonly
        self.output_location = output_location
        self.doOF = doOF
        self.isDY = isDY # We need to save this to remove the overlap between the inclusive DY sample and the pT binned ones
        self.do_syst = do_syst
        self.gensumweight = 1.0
        self.era = era
        self.isMC = isMC
        self.sample = sample
        self.syst_var, self.syst_suffix = (syst_var, f'_sys_{syst_var}') if do_syst and syst_var else ('', '')
        self.weight_syst = weight_syst
        self.prefixes = {"SUEP": "SUEP"}
        #Set up for the histograms
        self._accumulator = processor.dict_accumulator({})

    @property
    def accumulator(self):
        return self._accumulator

    def ak_to_pandas(self, jet_collection: ak.Array) -> pd.DataFrame:
        output = pd.DataFrame()
        for field in ak.fields(jet_collection):
            prefix = self.prefixes.get(field, "")
            if len(prefix) > 0:
                for subfield in ak.fields(jet_collection[field]):
                    output[f"{prefix}_{subfield}"] = ak.to_numpy(
                        jet_collection[field][subfield]
                    )
            else:
                if not(isinstance(ak.to_numpy(jet_collection[field])[0],np.ndarray)):
                    output[field] = ak.to_numpy(jet_collection[field])
                else:
                    temp =  ak.to_numpy(jet_collection[field])
                    output[field] = [[k for k in kk] for kk in temp]
        return output

    def h5store(self, store: pd.HDFStore, df: pd.DataFrame, fname: str, gname: str, **kwargs: float) -> None:
        store.put(gname, df)
        store.get_storer(gname).attrs.metadata = kwargs
        
    def save_dfs(self, dfs, df_names, fname=None):
        if not(fname): fname = "out.hdf5"
        subdirs = []
        store = pd.HDFStore(fname)
        if self.output_location is not None:
            # pandas to hdf5
            for out, gname in zip(dfs, df_names):
                if self.isMC:
                    metadata = dict(gensumweight=self.gensumweight,era=self.era, mc=self.isMC,sample=self.sample)
                    #metadata.update({"gensumweight":self.gensumweight})
                else:
                    metadata = dict(era=self.era, mc=self.isMC,sample=self.sample)    
                    
                store_fin = self.h5store(store, out, fname, gname, **metadata)

            store.close()
            self.dump_table(fname, self.output_location, subdirs)
        else:
            print("self.output_location is None")
            store.close()

    def dump_table(self, fname: str, location: str, subdirs: Optional[List[str]] = None) -> None:
        subdirs = subdirs or []
        xrd_prefix = "root://"
        pfx_len = len(xrd_prefix)
        xrootd = False
        if xrd_prefix in location:
            try:
                import XRootD
                import XRootD.client

                xrootd = True
            except ImportError:
                raise ImportError(
                    "Install XRootD python bindings with: conda install -c conda-forge xroot"
                )
        local_file = (
            os.path.abspath(os.path.join(".", fname))
            if xrootd
            else os.path.join(".", fname)
        )
        merged_subdirs = "/".join(subdirs) if xrootd else os.path.sep.join(subdirs)
        destination = (
            location + merged_subdirs + f"/{fname}"
            if xrootd
            else os.path.join(location, os.path.join(merged_subdirs, fname))
        )
        if xrootd:
            copyproc = XRootD.client.CopyProcess()
            copyproc.add_job(local_file, destination)
            copyproc.prepare()
            copyproc.run()
            client = XRootD.client.FileSystem(
                location[: location[pfx_len:].find("/") + pfx_len]
            )
            status = client.locate(
                destination[destination[pfx_len:].find("/") + pfx_len + 1 :],
                XRootD.client.flags.OpenFlags.READ,
            )
            assert status[0].ok
            del client
            del copyproc
        else:
            dirname = os.path.dirname(destination)
            if not os.path.exists(dirname):
                pathlib.Path(dirname).mkdir(parents=True, exist_ok=True)
            if os.path.isfile(destination):
                if not os.path.samefile(local_file, destination):
                    shutil.copy2(local_file, destination)
                else:
                  fname = "condor_" + fname
                  destination = os.path.join(location, os.path.join(merged_subdirs, fname))
                  shutil.copy2(local_file, destination)
            else:
                shutil.copy2(local_file, destination)
            assert os.path.isfile(destination)
        pathlib.Path(local_file).unlink()


    def selectByFilters(self, events):
        ### Apply MET filter selection (see https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2)
        if self.era == 2018 or self.era == 2017:
           cutAnyFilter = (events.Flag.goodVertices) | (events.Flag.globalSuperTightHalo2016Filter) | (events.Flag.HBHENoiseFilter) | (events.Flag.HBHENoiseIsoFilter) | (events.Flag.EcalDeadCellTriggerPrimitiveFilter) | (events.Flag.BadPFMuonFilter) | (events.Flag.BadPFMuonDzFilter) | (events.Flag.eeBadScFilter) | (events.Flag.ecalBadCalibFilter)
        if self.era == 2016 or self.era == 2015: # 2015==2016APV
           cutAnyFilter = (events.Flag.goodVertices) | (events.Flag.globalSuperTightHalo2016Filter) | (events.Flag.HBHENoiseFilter) | (events.Flag.HBHENoiseIsoFilter) | (events.Flag.EcalDeadCellTriggerPrimitiveFilter) | (events.Flag.BadPFMuonFilter) | (events.Flag.BadPFMuonDzFilter) | (events.Flag.eeBadScFilter)
        return events[cutAnyFilter]


    def selectByTrigger(self, events, extraColls = []):
        ### Apply trigger selection
        if self.era == 2018:
           cutAnyHLT = (events.HLT.IsoMu24) | (events.HLT.Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8) | (events.HLT.Ele32_WPTight_Gsf) | (events.HLT.Ele23_Ele12_CaloIdL_TrackIdL_IsoVL) #| (events.HLT.Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ) | (events.HLT.Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL)
           return events[cutAnyHLT], [coll[cutAnyHLT] for coll in extraColls]
        if self.era == 2017:
           cutAnyHLT = (events.HLT.IsoMu27) | (events.HLT.Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8) | (events.HLT.Ele35_WPTight_Gsf) | (events.HLT.Ele23_Ele12_CaloIdL_TrackIdL_IsoVL) #| (events.HLT.Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ) | (events.HLT.Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ)
           return events[cutAnyHLT], [coll[cutAnyHLT] for coll in extraColls]
        if self.era == 2016 or self.era == 2015: # 2015==2016APV
           cutAnyHLT = (events.HLT.IsoMu24) | (events.HLT.Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ) | (events.HLT.Ele27_WPTight_Gsf) | (events.HLT.Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ) #| (events.HLT.Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ) | (events.HLT.Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ)
           return events[cutAnyHLT], [coll[cutAnyHLT] for coll in extraColls]
        return events, [coll[cutAnyHLT] for coll in extraColls]

    def selectByLeptons(self, events, extraColls = []):
    ###lepton selection criteria--4momenta collection for plotting

        muons = ak.zip({
            "pt": events.Muon.pt,
            "eta": events.Muon.eta,
            "phi": events.Muon.phi,
            "mass": events.Muon.mass,
            "charge": events.Muon.pdgId/(-13),
        }, with_name="Momentum4D")
	
        electrons = ak.zip({
            "pt": events.Electron.pt,
            "eta": events.Electron.eta,
            "phi": events.Electron.phi,
            "mass": events.Electron.mass,
            "charge": events.Electron.pdgId/(-11),
        }, with_name="Momentum4D")

        ###  Some very simple selections on ID ###
        ###  Muons: loose ID + dxy dz cuts mimicking the medium prompt ID https://twiki.cern.ch/twiki/bin/viewauth/CMS/SWGuideMuonIdRun2
        ###  Electrons: loose ID + dxy dz cuts for promptness https://twiki.cern.ch/twiki/bin/view/CMS/EgammaCutBasedIdentification
        cutMuons     = (events.Muon.looseId) & (events.Muon.pt >= 10) & (abs(events.Muon.dxy) <= 0.02) & (abs(events.Muon.dz) <= 0.1) & (events.Muon.pfIsoId >= 2)
        cutElectrons = (events.Electron.cutBased >= 2) & (events.Electron.pt >= 15) & (events.Electron.mvaFall17V2Iso_WP90) & ( abs(events.Electron.dxy) < 0.05 + 0.05*(events.Electron.eta > 1.479)) & (abs(events.Electron.dz) <  0.10 + 0.10*(events.Electron.eta > 1.479)) & ((abs(events.Electron.eta) < 1.444) | (abs(events.Electron.eta) > 1.566))

        ### Apply the cuts
        # Object selection. selMuons contain only the events that are filtered by cutMuons criteria.
        selMuons     = muons[cutMuons]
        selElectrons = electrons[cutElectrons]

        ### Now global cuts to select events. Notice this means exactly two leptons with pT >= 10, and the leading one pT >= 25

        # cutHasTwoMuons imposes three conditions:
        #  First, number of muons (axis=1 means column. Each row is an event.) in an event is 2.
        #  Second, pt of the muons is greater than 25.
        #  Third, Sum of charge of muons should be 0. (because it originates from Z)
        if self.doOF:
            # Only for the OF sideband for tt/WW/Fakes estimation
            templeps = ak.concatenate([selMuons,selElectrons], axis=1)
            cutHasOFLeps =  (ak.num(templeps, axis=1)==2) & (ak.max(templeps.pt, axis=1, mask_identity=False) >= 25) & (ak.sum(templeps.charge,axis=1) == 0) 
            events = events[cutHasOFLeps]
            selElectrons = selElectrons[cutHasOFLeps]
            selMuons = selMuons[cutHasOFLeps]
            cutOneAndOne = (ak.num(selElectrons) == 1) & (ak.num(selMuons) == 1)
            events = events[cutOneAndOne]
            selElectrons = selElectrons[cutOneAndOne]
            selMuons     = selMuons[cutOneAndOne] 

        else:
            cutHasTwoMuons = (ak.num(selMuons, axis=1)==2) & (ak.max(selMuons.pt, axis=1, mask_identity=False) >= 25) & (ak.sum(selMuons.charge,axis=1) == 0)
            cutHasTwoElecs = (ak.num(selElectrons, axis=1)==2) & (ak.max(selElectrons.pt, axis=1, mask_identity=False) >= 25) & (ak.sum(selElectrons.charge,axis=1) == 0)
            cutTwoLeps     = ((ak.num(selElectrons, axis=1)+ak.num(selMuons, axis=1)) < 4)
            cutHasTwoLeps  = ((cutHasTwoMuons) | (cutHasTwoElecs)) & cutTwoLeps
            ### Cut the events, also return the selected leptons for operation down the line
            events = events[cutHasTwoLeps]
            selElectrons = selElectrons[cutHasTwoLeps]
            selMuons = selMuons[cutHasTwoLeps]
          
        return events, selElectrons, selMuons #, [coll[cutHasTwoLeps] for coll in extraColls]

    def selectByJets(self, events, leptons = [],  extraColls = []):
        # These are just standard jets, as available in the nanoAOD
        if self.isMC:
            Jets = ak.zip({
              "pt": events.Jet.pt,
              "eta": events.Jet.eta,
              "phi": events.Jet.phi,
              "mass": events.Jet.mass,
              "btag": events.Jet.btagDeepFlavB,
              "jetId": events.Jet.jetId,
              "hadronFlavour": events.Jet.hadronFlavour
            }, with_name="Momentum4D")

        else:
            Jets = ak.zip({
              "pt": events.Jet.pt,
              "eta": events.Jet.eta,
              "phi": events.Jet.phi,
              "mass": events.Jet.mass,
              "btag": events.Jet.btagDeepFlavB,
              "jetId": events.Jet.jetId
            }, with_name="Momentum4D")
 
        # Minimimum pT, eta requirements + jet-lepton recleaning
        jetCut = (Jets.pt > 30) & (abs(Jets.eta)<2.5) & (Jets.deltaR(leptons[:,0])>= 0.4) & (Jets.deltaR(leptons[:,1])>= 0.4) & (Jets.jetId >= 6)
        jets = Jets[jetCut]
        # The following is the collection of events and of jets
        return events, jets, [coll for coll in extraColls]

    def selectByTracks(self, events, leptons, extraColls = []):
        ### PARTICLE FLOW CANDIDATES ###
        # Every particle in particle flow (clean PFCand matched to tracks collection)
        Cands = ak.zip({
            "pt": events.PFCands.trkPt,
            "eta": events.PFCands.trkEta,
            "phi": events.PFCands.trkPhi,
            "mass": events.PFCands.mass
        }, with_name="Momentum4D")

        cutPF = (events.PFCands.fromPV > 1) & \
            (events.PFCands.trkPt >= 1) & \
            (abs(events.PFCands.trkEta) <= 2.5) & \
            (abs(events.PFCands.dz) < 10) & \
            (abs(events.PFCands.d0) < 0.05) & \
            (events.PFCands.puppiWeight > 0.1)
            #(events.PFCands.dzErr < 0.05)
        Cleaned_cands = ak.packed(Cands[cutPF])

	### LOST TRACKS ###
        # Unidentified tracks, usually SUEP Particles
        LostTracks = ak.zip({
            "pt": events.lostTracks.pt,
            "eta": events.lostTracks.eta,
            "phi": events.lostTracks.phi,
            "mass": 0.0
        }, with_name="Momentum4D")

        cutLost = (events.lostTracks.fromPV > 1) & \
            (events.lostTracks.pt >= 1) & \
            (abs(events.lostTracks.eta) <= 2.5) \
            & (abs(events.lostTracks.dz) < 0.05) & \
            (abs(events.lostTracks.d0) < 0.05) & \
            (events.lostTracks.puppiWeight > 0.1)
            #(events.lostTracks.dzErr < 0.05)
        Lost_Tracks_cands = ak.packed(LostTracks[cutLost])

        # dimensions of tracks = events x tracks in event x 4 momenta
        totalTracks = ak.concatenate([Cleaned_cands, Lost_Tracks_cands], axis=1)

        # Sorting out the tracks that overlap with leptons
        totalTracks = totalTracks[(totalTracks.deltaR(leptons[:,0])>= 0.4) & (totalTracks.deltaR(leptons[:,1])>= 0.4)]
        nTracks = ak.num(totalTracks,axis=1)
        return events, totalTracks, nTracks, [coll for coll in extraColls]

    def clusterizeTracks(self, events, tracks):
        # anti-kt, dR=1.5 jets
        jetdef = fastjet.JetDefinition(fastjet.antikt_algorithm, 1.5)        
        cluster = fastjet.ClusterSequence(tracks, jetdef)
        ak15_jets   = ak.with_name(cluster.inclusive_jets(min_pt=0),"Momentum4D") # These are the ak15_jets
        ak15_consts = ak.with_name(cluster.constituents(min_pt=0),"Momentum4D")   # And these are the collections of constituents of the ak15_jets

        return events, ak15_jets, ak15_consts

    def selectByGEN(self, events):
        GenParts = ak.zip({
            "pt": events.GenPart.pt,
            "eta": events.GenPart.eta,
            "phi": events.GenPart.phi,
            "mass": events.GenPart.mass,
            "pdgId": events.GenPart.pdgId,
        }, with_name="Momentum4D")
        if self.isDY:
            # Build the Zpt from leptons. Somehow awkward but needed as gammastar is not saved...
            cutgenLepsNeg = (events.GenPart.pdgId >= 11) & (events.GenPart.pdgId <= 16) & (abs(events.GenPart.status - 25) < 6) # Leptons from the hard scattering
            cutgenLepsPos = (events.GenPart.pdgId >= -16) & (events.GenPart.pdgId <= -11) & (abs(events.GenPart.status - 25) < 6) # Antileptons from the hard scattering
            cutgenZ    = (events.GenPart.pdgId == 23) & (events.GenPart.status == 22)
            genlepsPos = ak.pad_none(GenParts[cutgenLepsPos], 1, clip=True)
            genlepsNeg = ak.pad_none(GenParts[cutgenLepsNeg], 1, clip=True)
            genZfromZ  = GenParts[cutgenZ]
            genZfromZpadded = ak.pad_none(genZfromZ, 1, clip=True)[:,0]
            genZfromleps = genlepsPos[:,0] + genlepsNeg[:,0]
            Zpt = ak.where(ak.num(genZfromZ) >= 1, genZfromZpadded.pt, genZfromleps.pt)
            return events, Zpt
        else:
            cutgenZ    = (events.GenPart.pdgId == 23) & ((events.GenPart.status == 62) | (events.GenPart.status == 22))
            cutgenH    = (events.GenPart.pdgId == 25) & ((events.GenPart.status == 62) | (events.GenPart.status == 22))
            cutgenSUEP = (events.GenPart.pdgId == 999999) & (events.GenPart.status == 2)
            return events, GenParts[cutgenZ], GenParts[cutgenH], GenParts[cutgenSUEP]

    def shouldContinueAfterCut(self, events, out):
        #if debug: print("Conversion to pandas...")
        if len(events) == 0:
            outdfs  = []
            outcols = []
            print("No events pass cut, stopping...")
            for channel in out.keys():
                outcols.append(channel)
                if out[channel][0] == {}:   
                    outdfs = pd.DataFrame(['empty'], columns=['empty'])
                else:              
                    if self.isMC:
                        out[channel][0]["genweight"] = out[channel][1].genWeight[:]

                if not isinstance(out[channel][0], pd.DataFrame): 
                   out[channel][0] = self.ak_to_pandas(out[channel][0])
            self.save_dfs([out[key][0] for key in out], [key for key in out], self.chunkTag)

            return False
        else: 
            return True


    def process(self, events):
        np.random.seed(events.event[0]) # This ensures reproducibility of results (i.e. for the random track dropping), while also getting different random numbers per file to avoid biases (like always dropping the first track, etc.
        debug    = True  # If we want some prints in the middle
        self.chunkTag = "out_%i_%i_%i.hdf5"%(events.event[0], events.luminosityBlock[0], events.run[0]) #Unique tag to get different outputs per tag
        fullFile = self.output_location + "/" + self.chunkTag
        print("Check file %s"%fullFile)
        if os.path.isfile(fullFile): 
            print("SKIP")
            return self.accumulator.identity()

        self.doTracks   = True  # Make it false, and it will speed things up but not run the tracks
        self.doClusters = True  # Make it false, and it will speed things up but not run the clusters
        self.doGen      = False if not(self.isDY) else True # In case we want info on the gen level, we do need it for the buggy DY samples (to get proper stitching)

        # Main processor code
        # ------------------------------------------------------------------------------------
        # ------------------------------- DEFINE OUTPUTS -------------------------------------
        # ------------------------------------------------------------------------------------

        accumulator    = self.accumulator.identity()
        # Each track is one selection level
        outputs = {
            "SR"          :[{},[]],   # Only the SR
        }

        # Data dependant stuff
        dataset = events.metadata['dataset']
        if self.isMC: self.gensumweight = ak.sum(events.genWeight)

        if not(self.isMC): doGen = False

        # ------------------------------------------------------------------------------------
        # ------------------------------- OBJECT LOADING -------------------------------------
        # ------------------------------------------------------------------------------------
        # MET filters
        if debug: print("Applying MET requirements.... %i events in"%len(events))
        self.events = self.selectByFilters(events)
        if not(self.shouldContinueAfterCut(self.events, outputs)): return accumulator # If we have no events, we simply stop
        if debug: print("%i events pass METFilter cuts. Applying lepton requirements...."%len(self.events))

        # Lepton selection
        self.events, self.electrons, self.muons = self.selectByLeptons(self.events)[:3]
        if not(self.shouldContinueAfterCut(self.events, outputs)): return accumulator # If we have no events, we simply stop

        # Trigger selection
        if debug: print("%i events pass lepton cuts. Applying trigger requirements...."%len(self.events))
        self.events, [self.electrons, self.muons] = self.selectByTrigger(self.events,[self.electrons, self.muons])
        # Here we join muons and electrons into leptons and sort them by pT
        self.leptons = ak.concatenate([self.electrons, self.muons], axis=1)
        highpt_leptons = ak.argsort(self.leptons.pt, axis=1, ascending=False, stable=True)
        self.leptons = self.leptons[highpt_leptons]
        if not(self.shouldContinueAfterCut(self.events, outputs)): return accumulator
        if debug: print("%i events pass trigger cuts. Selecting jets..."%len(self.events))

        # Jet selection
        self.events, self.jets = self.selectByJets(self.events, self.leptons)[:2] # Leptons are needed to do jet-lepton cleaning
	# Sorting jets by pt.
        highpt_jets = ak.argsort(self.jets.pt, axis=1, ascending=False, stable=True)
        self.jets   = self.jets[highpt_jets]
        if not(self.shouldContinueAfterCut(self.events, outputs)): return accumulator
        if debug: print("%i events pass jet cuts. Selecting tracks..."%len(self.events))
        
        if self.doTracks:
            # Right now no track cuts, only selecting tracks
            self.events, self.tracks = self.selectByTracks(self.events, self.leptons)[:2] # Again, we need leptons to clean the tracks
            if not(self.shouldContinueAfterCut(self.events, outputs)): return accumulator
            if debug: print("%i events pass track cuts. Doing track clustering..."%len(self.events))
            if self.doClusters:
                self.events, self.clusters, self.constituents  = self.clusterizeTracks(self.events, self.tracks)[:3]
                highpt_clusters = ak.argsort(self.clusters.pt, axis=1, ascending=False, stable=True)
                self.clusters   = self.clusters[highpt_clusters]
                self.constituents = self.constituents[highpt_clusters]

        if self.doGen:
            print("Do gen!")
            if self.isDY: self.events, self.Zpt = self.selectByGEN(self.events)[:2]
            else: self.events, self.genZ, self.genH, self.genSUEP = self.selectByGEN(self.events)[:4]
            if not(self.shouldContinueAfterCut(self.events, outputs)): return accumulator
            if debug: print("%i events pass gen cuts. Doing more stuff..."%len(self.events))

        ##### Finally, build additional composite objects
        # First the Z candidates
        self.Zcands = self.leptons[:,0] + self.leptons[:,1]
        
        # ------------------------------------------------------------------------------
        # ------------------------------- UNCERTAINTIES --------------------------------
        # ------------------------------------------------------------------------------
        self.jetsVar   = {"": self.jets} # If not activated, always central jet collection
        self.tracksVar = {"": self.tracks} # If not activated, always central jet collection

        self.varsToDo = [""]           # If not activated just do nominal yields

        # ------------------------------------------------------------------------------
        # ------------------------------- SELECTION + PLOTTING -------------------------
        # ------------------------------------------------------------------------------
        self.var = "" # To keep track of the systematic variation: "" == nominal
        if len(self.varsToDo) > 1:
            self.saveAllCollections()
        for var in self.varsToDo:
            self.var = var
            # Reset collections for syst variation
            if var != "": 
                self.resetAllCollections()
                if var in self.jetsVar:
                  self.jets   = self.jetsVar[var]
                if var in self.tracksVar:
                  self.tracks = self.tracksVar[var]

            self.isSpherable   = False # So we don't do sphericity plots until we have clusters
            self.isClusterable = False # So we don't try to compute sphericity if clusters are empty
            if not(self.shouldContinueAfterCut(self.events, outputs)): return accumulator
            if debug: print("%i events pass twoleptons cuts. Doing more stuff..."%len(self.events))

            if self.doTracks:
                cutOneTrack = (ak.num(self.tracks) != 0)
                self.applyCutToAllCollections(cutOneTrack)
                self.isSpherable = True # So we do sphericity plots
                if not(self.shouldContinueAfterCut(self.events, outputs)): return accumulator
                if debug: print("%i events pass onetrack cuts. Doing more stuff..."%len(self.events))
                if self.doClusters:
                    cutOneCluster = (ak.num(self.clusters) != 0)
                    self.applyCutToAllCollections(cutOneCluster)
                    self.isClusterable = True # So we do cluster plots
                    if not(self.shouldContinueAfterCut(self.events, outputs)): return accumulator
                    if debug: print("%i events pass onecluster cuts. Doing more stuff..."%len(self.events))
                    cutclusterpt60 = (self.clusters.pt[:,0] >= 60)
                    self.applyCutToAllCollections(cutclusterpt60)
                    if not(self.shouldContinueAfterCut(self.events, outputs)): return accumulator
                    if debug: print("%i events pass clusterpt cuts. Doing more stuff..."%len(self.events))
                    outputs["SR"+var] = [self.doAllPlots("SR"+var, debug), self.events]

        # ------------------------------------------------------------------------------
        # -------------------------------- SAVING --------------------------------------
        # ------------------------------------------------------------------------------
        todel = []
        if self.SRonly: # Lightweight, save only SR stuff
            for out in outputs:
                if not("SR"==out): 
                    todel.append(out)
            for t in todel:
                del outputs[t]

        for out in outputs:
            if out in todel: continue 
            if self.isMC:
                outputs[out][0]["genweight"] = outputs[out][1].genWeight[:]
            if debug: print("Conversion to pandas...")
            if not isinstance(outputs[out][0], pd.DataFrame):
                if debug: print("......%s"%out)
                outputs[out][0] = self.ak_to_pandas(outputs[out][0])

        if debug: print("DFS saving....")

        self.save_dfs([outputs[key][0] for key in outputs], [key for key in outputs], self.chunkTag)

        return accumulator
   

    def applyCutToAllCollections(self, cut): # Cut has to by a selection applicable across all collections, i.e. something defined per event
        self.events    = self.events[cut]
        self.electrons = self.electrons[cut]
        self.muons     = self.muons[cut]
        self.leptons   = self.leptons[cut]
        self.jets      = self.jets[cut]
        self.Zcands    = self.Zcands[cut]
        if self.doTracks:
            self.tracks  = self.tracks[cut]
            if self.doClusters:
                self.clusters     = self.clusters[cut]
                self.constituents = self.constituents[cut]

        if self.doGen:
            if self.isDY:
                self.Zpt = self.Zpt[cut]
            else:
                self.genZ    = self.genZ[cut]
                self.genH    = self.genH[cut]
                self.genSUEP = self.genSUEP[cut]

    def saveAllCollections(self): # Save collections before cutting, to reset when dealing with systematics
        self.safeevents    = self.events
        self.safeelectrons = self.electrons
        self.safemuons     = self.muons
        self.safeleptons   = self.leptons
        self.safejets      = self.jets
        self.safeZcands    = self.ZCands
        if self.doTracks:
            self.safetracks  = self.tracks
            if self.doClusters:
                self.safeclusters     = self.clusters
                self.safeconstituents = self.constituents

        if self.doGen:
            if self.isDY:
                self.safeZpt = self.Zpt
            else:
                self.safegenZ    = self.genZ
                self.safegenH    = self.genH
                self.safegenSUEP = self.genSUEP
        
    def resetAllCollections(self): # Reset collections to before cutting, useful when dealing with systematics
        self.events    = self.safeevents
        self.electrons = self.safeelectrons
        self.muons     = self.safemuons
        self.leptons   = self.safeleptons
        self.jets      = self.safejets
        self.Zcands    = self.safeZCands
        if self.doTracks:
            self.tracks  = self.safetracks
            if self.doClusters:
                self.clusters     = self.safeclusters
                self.constituents = self.safeconstituents

        if self.doGen:
            if self.isDY:
                self.Zpt = self.safeZpt
            else:
                self.genZ    = self.safegenZ
                self.genH    = self.safegenH
                self.genSUEP = self.safegenSUEP

    def btagcuts(self, WP, era):
        print("Era", era)
        if era == 2015: #2016APV
          if WP == "Loose":  return 0.0480
          if WP == "Medium": return 0.2489
          if WP == "Tight":  return 0.6377
        if era == 2016:
          if WP == "Loose":  return 0.0508
          if WP == "Medium": return 0.2598
          if WP == "Tight":  return 0.6502
        if era == 2017: 
          if WP == "Loose":  return 0.0532
          if WP == "Medium": return 0.3040
          if WP == "Tight":  return 0.7476
        if era == 2018: 
          if WP == "Loose":  return 0.0490
          if WP == "Medium": return 0.2783
          if WP == "Tight":  return 0.7100
        


    def doAllPlots(self, channel, debug=True):
        # ------------------------------------------------------------------------------
        # ------------------------------- PLOTTING -------------------------------------
        # ------------------------------------------------------------------------------
        out = {}
        # Define outputs for plotting
        if debug: print("Saving reco variables for channel %s"%channel)

        # Object: jets, a bit tricky as number varies per event!
        out["njets"]          = ak.num(self.jets, axis=1)[:]
        maxnjets = ak.max(ak.num(self.jets, axis=1))
        out["jet_pt"]     = ak.fill_none(ak.pad_none(self.jets.pt,  maxnjets, axis=1, clip=True), 0.)[:,:] # So take all events, if there is no jet_pt fill it with none, then replace none with 0
        out["jet_eta"]    = ak.fill_none(ak.pad_none(self.jets.eta, maxnjets, axis=1, clip=True), -999)[:,:] # So take all events, if there is no jet_pt fill it with none, then replace none with -999
        out["jet_flavour"]= ak.fill_none(ak.pad_none(self.jets.hadronFlavour, maxnjets, axis=1, clip=True), -1)[:,:] 
        out["jet_btag"]   = ak.fill_none(ak.pad_none(self.jets.btag >= self.btagcuts("Loose", self.era), maxnjets, axis=1, clip=True), -1)[:,:]
        if self.doGen:
            if debug: print("Saving gen variables")
            if self.isDY:
                out["genZpt"]  = self.Zpt

        return out

    def postprocess(self, accumulator):
        return accumulator
 
