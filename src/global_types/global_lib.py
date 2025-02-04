import ctypes
import os
from enum import IntEnum

FILE_PATH = os.path.dirname(os.path.realpath(__file__))
GLOBAL_BIN_FILE_PATH = str(FILE_PATH) + "/global.so"
global_gate_convert = {
    "IDENTITY": 0,
    "HADAMARD": 1,
    "PAULIX": 2,
    "PAULIY": 3,
    "PAULIZ": 4,
    "PHASE": 5,
    "S": 6,
    "SDG": 7,
    "T": 8,
    "TDG": 9,
    "RZ": 10,
    "RY": 11,
    "RX": 12,
    "SX": 13,
    "SXDG": 14,
    "U": 15,
    "CX": 16,
    "CH": 17,
    "CY": 18,
    "CZ": 19,
    "CRX": 20,
    "CRY": 21,
    "CRZ": 22,
    "CR1": 23,
    "CCX": 24,
    "QFT": 25,
    "RCCX": 26,
    "RC3X": 27,
    "SWAP": 28,
    "RXX": 29,
    "RZZ": 30,
    "CUSTOM": 31,
    "CUSTOMCONTROLLED": 32,
    "MULTI": 33,
    "CUSTOMBLOCK": 34,
    "CUSTOMALGORITHM": 35,
}

global_type_convert = {
    "SINGLE": 0,
    "CONTROLLED": 1,
    "MULTI": 2,
    "BLOCK": 3,
    "ALGORITHM": 4,
}
