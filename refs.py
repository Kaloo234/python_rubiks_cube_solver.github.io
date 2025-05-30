import numpy as np

CUBE_SOLVED = np.array([[[0,0,0],[0,0,0],[0,0,0]],
                        [[1,1,1],[1,1,1],[1,1,1]],
                        [[2,2,2],[2,2,2],[2,2,2]],
                        [[3,3,3],[3,3,3],[3,3,3]],
                        [[4,4,4],[4,4,4],[4,4,4]],
                        [[5,5,5],[5,5,5],[5,5,5]]])

SIDES = {
    0: {"l": 1,"r": 3,"u": 4,"d": 2},
    1: {"l": 4,"r": 2,"u": 0,"d": 5},
    2: {"l": 1,"r": 3,"u": 0,"d": 5},
    3: {"l": 2,"r": 4,"u": 0,"d": 5},
    4: {"l": 3,"r": 1,"u": 0,"d": 5},
    5: {"l": 1,"r": 3,"u": 2,"d": 4}
    }

COLORS = {
    0: "blue",
    1: "orange",
    2: "white",
    3: "red",
    4: "yellow",
    5: "green"
    }

MOVES = {
    "F":  [["tc",2]],
    "F2": [["tc",2],["tc",2]],
    "F'": [["ta",2]],

    "U":  [["tc",0]],
    "U2": [["tc",0],["tc",0]],
    "U'": [["ta",0]],

    "D":  [["tc",5]],
    "D2": [["tc",5],["tc",5]],
    "D'": [["ta",5]],

    "L":  [["tc",1]],
    "L2": [["tc",1],["tc",1]],
    "L'": [["ta",1]],

    "R":  [["tc",3]],
    "R2": [["tc",3],["tc",3]],
    "R'": [["ta",3]],

    "B":  [["tc",4]],
    "B2": [["tc",4],["tc",4]],
    "B'": [["ta",4]],

    "M":  [["tmx","c"]],
    "M2": [["tmx","c"],["tmx","c"]],
    "M'": [["tmx","a"]],

    "E":  [["tmy","c"]],
    "E2": [["tmy","c"],["tmy","c"]],
    "E'": [["tmy","a"]],

    "S":  [["tmz","c"]],
    "S2": [["tmz","c"],["tmz","c"]],
    "S'": [["tmz","a"]],

    "f":  [["tc",2],["tmz","c"]],
    "f2": [["tc",2],["tc",2],["tmz","c"],["tmz","c"]],
    "f'": [["ta",2],["tmz","a"]],

    "u":  [["tc",0],["tmy","a"]],
    "u2": [["tc",0],["tc",0],["tmy","a"],["tmy","a"]],
    "u'": [["ta",0],["tmy","c"]],

    "d":  [["tc",5],["tmy","c"]],
    "d2": [["tc",5],["tc",5],["tmy","c"],["tmy","c"]],
    "d'": [["ta",5],["tmy","a"]],

    "l":  [["tc",1],["tmx","c"]],
    "l2": [["tc",1],["tc",1],["tmx","c"],["tmx","c"]],
    "l'": [["ta",1],["tmx","a"]],

    "r":  [["tc",3],["tmx","a"]],
    "r2": [["tc",3],["tc",3],["tmx","a"],["tmx","a"]],
    "r'": [["ta",3],["tmx","c"]],

    "b":  [["tc",4],["tmz","a"]],
    "b2": [["tc",4],["tc",4],["tmz","a"],["tmz","a"]],
    "b'": [["ta",4],["tmz","c"]],

    "x":  [["ta",1],["tmx","a"],["tc",3]],
    "x2": [["ta",1],["ta",1],["tmx","a"],["tmx","a"],["tc",3],["tc",3]],
    "x'": [["tc",1],["tmx","c"],["ta",3]],

    "y":  [["tc",0],["tmy","a"],["ta",5]],
    "y2": [["tc",0],["tc",0],["tmy","a"],["tmy","a"],["ta",5],["ta",5]],
    "y'": [["ta",0],["tmy","c"],["tc",5]],

    "z":  [["tc",2],["tmz","c"],["ta",4]],
    "z2": [["tc",2],["tc",2],["tmz","c"],["tmz","c"],["ta",4],["ta",4]],
    "z'": [["ta",2],["tmz","a"],["tc",4]]
    }

OPPOSITE_MOVE = {
    "F":  "F'",
    "F2": "F2",
    "F'": "F",

    "U":  "U'",
    "U2": "U2",
    "U'": "U",

    "D":  "D'",
    "D2": "D2",
    "D'": "D",

    "L":  "L'",
    "L2": "L2",
    "L'": "L",

    "R":  "R'",
    "R2": "R2",
    "R'": "R",

    "B":  "B'",
    "B2": "B2",
    "B'": "B",

    "M":  "M'",
    "M2": "M2",
    "M'": "M",

    "E":  "E'",
    "E2": "E2",
    "E'": "E",

    "S":  "S'",
    "S2": "S2",
    "S'": "S",

    "f":  "f'",
    "f2": "f2",
    "f'": "f",

    "u":  "u'",
    "u2": "u2",
    "u'": "u",

    "d":  "d'",
    "d2": "d2",
    "d'": "d",

    "l":  "l'",
    "l2": "l2",
    "l'": "l",

    "r":  "r'",
    "r2": "r2",
    "r'": "r",

    "b":  "b'",
    "b2": "b2",
    "b'": "b",

    "x":  "x'",
    "x2": "x2",
    "x'": "x",

    "y":  "y'",
    "y2": "y2",
    "y'": "y",

    "z":  "z'",
    "z2": "z2",
    "z'": "z",
    }

CANCEL_MOVES = {
    0: {"cancel": ["U", "d'"], "result": "y"},
    1: {"cancel": ["U'", "d"], "result": "y'"},
    2: {"cancel": ["D", "u'"], "result": "y'"},
    3: {"cancel": ["D'", "u"], "result": "y"},
    2: {"cancel": ["R", "l'"], "result": "x"},
    3: {"cancel": ["R'", "l"], "result": "x'"},
    2: {"cancel": ["L", "r'"], "result": "x'"},
    3: {"cancel": ["L'", "r"], "result": "x"},
    2: {"cancel": ["F", "b'"], "result": "z"},
    3: {"cancel": ["F'", "b"], "result": "z'"},
    2: {"cancel": ["B", "f'"], "result": "z'"},
    3: {"cancel": ["B'", "f"], "result": "z"},
    }
