def decrypt(x, k):
    return (x - k) % 26

def d_cesar(crypt, k):
    phrase_decrypt = []

    for l in crypt:
        if 65 <= ord(l) <= 90: #A = 65 Z = 90
            nb = ord(l) - 65
            nb_decrypt = decrypt(nb, k)
            lettre_decrypt = chr(nb_decrypt + 65)
            phrase_decrypt.append(lettre_decrypt)
        elif 97 <= ord(l) <= 122: #a = 97 z = 122
            nb = ord(l) - 97
            nb_decrypt = decrypt(nb, k)
            lettre_decrypt = chr(nb_decrypt + 97)
            phrase_decrypt.append(lettre_decrypt)
        else:
            phrase_decrypt.append(l)

    return "".join(phrase_decrypt) #TABLEAU --> CHAR

ph1 = d_cesar("DOHD MDFWD HVW",3)
print(ph1)
