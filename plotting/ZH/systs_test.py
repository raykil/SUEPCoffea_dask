systematicsAndShapes = {
 "yields": { # This always needs to be defined
           "name": "yields",
           "type": "yieldsWithShapes",
           "file": "[ROOTFILE]",
           "match": "[VAR]_$PROCESS"
 },
 #"syst0": {
 #          "name" : "DYnorm",
 #          "type" : "lnN",
 #          "processes": [".*"],
 #          "size" : 1.05,
 #},
 #"syst1": {
 #           "name": "syst1_shape",
 #           "type": "shape",
 #           "processes": [".*"],
 #           "match": "$PROCESS_$SYSTEMATIC",
 #           "up"  : "Up",
 #           "down": "Dn",
 #},
 #"syst2": {
 #            "name": "syst2_shape",
 #           "type": "shape",
 #           "processes": [".*"],
 #           "match": "$PROCESS_$SYSTEMATIC",
 #           "up"  : "Up",
 #           "down": "Dn",
 #},
 "syst3": {
            "name": "syst3_shape",
            "type": "shape",
            "processes": [".*"],
            "match": "$PROCESS_$SYSTEMATIC",
            "up"  : "Up",
            "down": "Dn",
 },

}
