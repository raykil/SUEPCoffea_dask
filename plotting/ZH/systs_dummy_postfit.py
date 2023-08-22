systematicsAndShapes = {
 "yields": { # This always needs to be defined
           "name": "yields",
           "type": "yieldsWithShapes",
           "file": "[ROOTFILE]",
           "match": "[VAR]_$PROCESS"
 },
 ""  : {
            "name": "",
            "type": "shape",
            "processes": [".*"],
            "match": "$PROCESS_$SYSTEMATIC",
            "up"  : "Up",
            "down": "Dn",
 },
}

