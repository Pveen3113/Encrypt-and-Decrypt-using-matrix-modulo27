import numpy as np
import sys

alpha_mapping = {" ": 0, "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
                 "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23,
                 "X": 24, "Y": 25, "Z": 26,
                 }
digits_mapping = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K", 12: "L",
                  13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U", 22: "V", 23: "W",
                  24: "X", 25: "Y", 26: "Z", 0: " "
                  }


def mulinv(key):

    size = len(key)

    if size == 2:
        deter = key[0][0] * key[1][1] - key[0][1] * key[1][0]
    elif size == 3:
        deter = (key[0][0]) * ((key[1][1] * key[2][2]) - (key[2][1] * key[1][2])) - ((key[0][1]) * ((key[1][0] * key[2][2]) - (key[2][0] * key[1][2]))) + ((key[0][2]) * ((key[1][0] * key[2][1]) - (key[2][0] * key[1][1])))
    elif size == 4:
        deter1 = key[1][1] * ((key[2][2] * key[3][3]) - (key[3][2] * key[2][3])) - key[1][2] * ((key[2][1] * key[3][3]) - (key[3][1] * key[2][3])) + key[1][3] * ((key[2][1] * key[3][2]) - (key[3][1] * key[2][2]))
        deter2 = key[1][0] * ((key[2][2] * key[3][3]) - (key[3][2] * key[2][3])) - key[1][2] * ((key[2][0] * key[3][3]) - (key[3][0] * key[2][3])) + key[1][3] * ((key[2][0] * key[3][2]) - (key[3][0] * key[2][2]))
        deter3 = key[1][0] * ((key[2][1] * key[3][3]) - (key[3][1] * key[2][3])) - key[1][1] * ((key[2][0] * key[3][3]) - (key[3][0] * key[2][3])) + key[1][3] * ((key[2][0] * key[3][1]) - (key[3][0] * key[2][1]))
        deter4 = key[1][0] * ((key[2][1] * key[3][2]) - (key[3][1] * key[2][2])) - key[1][1] * ((key[2][0] * key[3][2]) - (key[3][0] * key[2][2])) + key[1][2] * ((key[2][0] * key[3][1]) - (key[3][0] * key[2][1]))
        deter = key[0][0] * deter1 - key[0][1] * deter2 + key[0][2] * deter3 - key[0][3] * deter4

    inv = -1

    for i in range(27):
        temp_inv = deter * i
        if temp_inv % 27 == 1:
            inv = i
            break
        else:
            continue

    return inv


def extraction(word, wordmat, key):
    size = len(key)
    text = ""
    if size == 2:
        itr_count = int(len(word) / 2)
        for i in range(0, itr_count):
            temp1 = (key[0][0] * wordmat[0][i]) + (key[0][1] * wordmat[1][i])
            temp1 = temp1 % 27
            text += digits_mapping.get(temp1)

            temp2 = (key[1][0] * wordmat[0][i]) + (key[1][1] * wordmat[1][i])
            temp2 = temp2 % 27
            text += digits_mapping.get(temp2)
    elif size == 3:
        itr_count = int(len(word) / 3)
        for i in range(0, itr_count):
            temp1 = (key[0][0] * wordmat[0][i]) + (key[0][1] * wordmat[1][i]) + (key[0][2] * wordmat[2][i])
            temp1 = temp1 % 27
            text += digits_mapping.get(temp1)

            temp2 = (key[1][0] * wordmat[0][i]) + (key[1][1] * wordmat[1][i]) + (key[1][2] * wordmat[2][i])
            temp2 = temp2 % 27
            text += digits_mapping.get(temp2)

            temp3 = (key[2][0] * wordmat[0][i]) + (key[2][1] * wordmat[1][i]) + (key[2][2] * wordmat[2][i])
            temp3 = temp3 % 27
            text += digits_mapping.get(temp3)
    elif size == 4:
        itr_count = int(len(word) / 4)
        for i in range(0, itr_count):
            temp1 = (key[0][0] * wordmat[0][i]) + (key[0][1] * wordmat[1][i]) + (key[0][2] * wordmat[2][i]) + (key[0][3] * wordmat[3][i])
            temp1 = temp1 % 27
            text += digits_mapping.get(temp1)

            temp2 = (key[1][0] * wordmat[0][i]) + (key[1][1] * wordmat[1][i]) + (key[1][2] * wordmat[2][i]) + (key[1][3] * wordmat[3][i])
            temp2 = temp2 % 27
            text += digits_mapping.get(temp2)

            temp3 = (key[2][0] * wordmat[0][i]) + (key[2][1] * wordmat[1][i]) + (key[2][2] * wordmat[2][i]) + (key[2][3] * wordmat[3][i])
            temp3 = temp3 % 27
            text += digits_mapping.get(temp3)

            temp4 = (key[3][0] * wordmat[0][i]) + (key[3][1] * wordmat[1][i]) + (key[3][2] * wordmat[2][i]) + (key[3][3] * wordmat[3][i])
            temp4 = temp4 % 27
            text += digits_mapping.get(temp4)

    return text
