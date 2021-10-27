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

def encryption2d(word, key):

    if len(word) % 2 != 0:
        word += " "

    row = 2
    col = int(len(word) / 2)
    word2d = np.zeros((row, col), dtype=int)
    key2d = np.zeros((2, 2), dtype=int)
    itr1 = 0
    itr2 = 0

    for i in range(0, col):
        for j in range(0, row):
            word2d[j][i] = alpha_mapping.get(word[itr1])
            itr1 += 1

    for i in range(0, 2):
        for j in range(0, 2):
            key2d[j][i] = alpha_mapping.get(key[itr2])
            itr2 += 1

    mul_inv = mulinv(key2d)

    while mul_inv == -1:
        print("Invalid key")
        print("Key must only consist of 4 characters and all must be alphabets")
        key = input("Enter your key again: ").upper()
        while not key.isalpha() or len(key) > 4 or len(key) < 4:
            if ' ' in key and not any(str.isdigit(c) for c in key):
                break
            else:
                print("Key must only consist of 4 characters and all must be alphabets")
                key = input("Re-enter key: ").upper()
        key2d = np.zeros((2, 2), dtype=int)
        itr2 = 0
        for i in range(0, 2):
            for j in range(0, 2):
                key2d[j][i] = alpha_mapping.get(key[itr2])
                itr2 += 1
        mul_inv = mulinv(key2d)

    encryp_text = extraction(word, word2d, key2d)
    print("\n\n********************************************")
    print(f'Your encrypted text: {encryp_text}')
    print("\n\n********************************************")



def encryption3d(word, key):

    while len(word) % 3 != 0:
        word += " "

    row = 3
    col = int(len(word) / 3)
    word3d = np.zeros((row, col), dtype=int)
    key3d = np.zeros((3, 3), dtype=int)
    itr1 = 0
    itr2 = 0
    for i in range(0, col):
        for j in range(0, row):
            word3d[j][i] = alpha_mapping.get(word[itr1])
            itr1 += 1

    for i in range(0, 3):
        for j in range(0, 3):
            key3d[j][i] = alpha_mapping.get(key[itr2])
            itr2 += 1

    mul_inv = mulinv(key3d)

    while mul_inv == -1:
        print("Invalid key")
        print("Key must only consist of 9 characters and all must be alphabets")
        key = input("Enter your key again: ").upper()
        while not key.isalpha() or len(key) > 9 or len(key) < 9:
            if ' ' in key and not any(str.isdigit(c) for c in key):
                break
            else:
                print("Key must only consist of 9 characters and all must be alphabets")
                key = input("Re-enter key: ").upper()
        key3d = np.zeros((3, 3), dtype=int)
        itr2 = 0
        for i in range(0, 3):
            for j in range(0, 3):
                key3d[j][i] = alpha_mapping.get(key[itr2])
                itr2 += 1
        mul_inv = mulinv(key3d)

    encryp_text = extraction(word, word3d, key3d)
    print("\n\n***********************************************")
    print(f'Your encrypted text: {encryp_text}')
    print("\n\n***********************************************")


def decryption2d(word, key):

    if len(word) % 2 != 0:
        word += " "

    row = 2
    col = int(len(word) / 2)
    word2d = np.zeros((row, col), dtype=int)
    key2d = np.zeros((2, 2), dtype=int)
    itr1 = 0
    itr2 = 0

    for i in range(0, col):
        for j in range(0, row):
            word2d[j][i] = alpha_mapping.get(word[itr1])
            itr1 += 1

    for i in range(0, 2):
        for j in range(0, 2):
            key2d[j][i] = alpha_mapping.get(key[itr2])
            itr2 += 1

    mul_inv = mulinv(key2d)

    while mul_inv == -1:
        print("Invalid key")
        print("Key must only consist of 4 characters and all must be alphabets")
        key = input("Enter your key again: ").upper()
        while not key.isalpha() or len(key) > 4 or len(key) < 4:
            if ' ' in key and not any(str.isdigit(c) for c in key):
                break
            else:
                print("Key must only consist of 4 characters and all must be alphabets")
                key = input("Re-enter key: ").upper()
        key2d = np.zeros((2, 2), dtype=int)
        itr2 = 0
        for i in range(0, 2):
            for j in range(0, 2):
                key2d[j][i] = alpha_mapping.get(key[itr2])
                itr2 += 1

        mul_inv = mulinv(key2d)

    key2d[0][0], key2d[1][1] = key2d[1][1], key2d[0][0]
    key2d[0][1] *= -1
    key2d[1][0] *= -1
    key2d[0][1] = key2d[0][1] % 27
    key2d[1][0] = key2d[1][0] % 27

    for i in range(0, 2):
        for j in range(0, 2):
            key2d[j][i] = (key2d[j][i] * mul_inv)

    for i in range(0, 2):
        for j in range(0, 2):
            key2d[j][i] = key2d[j][i] % 27

    decryp_text = extraction(word, word2d, key2d)
    print("\n\n*************************************************")
    print(f'Your decrypted text: {decryp_text}')
    print("*****************************************************")

def decryption3d(word, key):

    while len(word) % 3 != 0:
        word += " "

    row = 3
    col = int(len(word) / 3)
    word3d = np.zeros((row, col), dtype=int)
    key3d = np.zeros((3, 3), dtype=int)
    ikey3d = np.zeros((3, 3), dtype=int)
    itr1 = 0
    itr2 = 0

    for i in range(0, col):
        for j in range(0, row):
            word3d[j][i] = alpha_mapping.get(word[itr1])
            itr1 += 1

    for i in range(0, 3):
        for j in range(0, 3):
            key3d[j][i] = alpha_mapping.get(key[itr2])
            itr2 += 1

    mul_inv = mulinv(key3d)

    while mul_inv == -1:
        print("Invalid key")
        print("Key must only consist of 9 characters and all must be alphabets")
        key = input("Enter your key again: ").upper()
        while not key.isalpha() or len(key) > 9 or len(key) < 9:
            if ' ' in key and not any(str.isdigit(c) for c in key):
                break
            else:
                print("Key must only consist of 9 characters and all must be alphabets")
                key = input("Re-enter key: ").upper()
        key3d = np.zeros((3, 3), dtype=int)
        itr2 = 0
        for i in range(0, 3):
            for j in range(0, 3):
                key3d[j][i] = alpha_mapping.get(key[itr2])
                itr2 += 1
        mul_inv = mulinv(key3d)

    key3d[0][1], key3d[0][2], key3d[2][1], key3d[1][0], key3d[2][0], key3d[1][2] = key3d[1][0], key3d[2][0], key3d[1][2], key3d[0][1], key3d[0][2], key3d[2][1]

    ikey3d[0][0] = (key3d[1][1] * key3d[2][2] - key3d[2][1] * key3d[1][2])
    ikey3d[0][1] = -(key3d[1][0] * key3d[2][2] - key3d[2][0] * key3d[1][2])
    ikey3d[0][2] = (key3d[1][0] * key3d[2][1] - key3d[2][0] * key3d[1][1])
    ikey3d[1][0] = -(key3d[0][1] * key3d[2][2] - key3d[2][1] * key3d[0][2])
    ikey3d[1][1] = (key3d[0][0] * key3d[2][2] - key3d[2][0] * key3d[0][2])
    ikey3d[1][2] = -(key3d[0][0] * key3d[2][1] - key3d[2][0] * key3d[0][1])
    ikey3d[2][0] = (key3d[0][1] * key3d[1][2] - key3d[1][1] * key3d[0][2])
    ikey3d[2][1] = -(key3d[0][0] * key3d[1][2] - key3d[1][0] * key3d[0][2])
    ikey3d[2][2] = (key3d[0][0] * key3d[1][1] - key3d[1][0] * key3d[0][1])

    for i in range(0, 3):
        for j in range(0, 3):
            ikey3d[j][i] = (ikey3d[j][i] * mul_inv)

    for i in range(0, 3):
        for j in range(0, 3):
            ikey3d[j][i] = ikey3d[j][i] % 27

    decryp_text = extraction(word, word3d, ikey3d)
    print("\n\n**************************************************")
    print(f'Your decrypted text: {decryp_text}')
    print("******************************************************")
