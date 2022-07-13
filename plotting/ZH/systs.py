systematicsAndShapes = {
 "yields": { # This always needs to be defined
           "name": "yields",
           "type": "yieldsWithShapes",
           "file": "/eos/user/c/cericeci/www/SUEP/stack_ncltracks40_eta1p5/jet1pt_5rebinned.root",
           "match": "jet1pt_$PROCESS"
  },
 "DYnorm": {
           "name" : "DYnorm",
           "type" : "lnN",
           "processes": ["DY.*"],
           "size" : 1.5,
 },
 "Othersnorm": {
           "name" : "Othersnorm",
           "type" : "lnN",
           "processes": ["tt.*","W.*","V.*"],
           "size" : 1.5,
 },
 "Signalnorm": {
            "name": "Signalnorm",
            "type": "lnN",
            "processes": ["SUEP.*"],
            "size" : 1.5,
 },
 "DummyCorr": {
            "name": "DummyCorr",
            "type": "lnN",
            "processes": [".*"],
            "size" : 1.1,
 },
}


