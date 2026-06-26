def decalage(x, k):
    return (x + k) % 26

def c_cesar(mot, k):
    phrase_crypt = []

    for l in mot:
        if 65 <= ord(l) <= 90: #A = 65 Z = 90
            nb = ord(l) - 65
            nb_crypt = decalage(nb, k)
            lettre_crypt = chr(nb_crypt + 65)
            phrase_crypt.append(lettre_crypt)
        elif 97 <= ord(l) <= 122: #a = 97 z = 122
            nb = ord(l) - 97
            nb_crypt = decalage(nb, k)
            lettre_crypt = chr(nb_crypt + 97)
            phrase_crypt.append(lettre_crypt)
        else:
            phrase_crypt.append(l)

    return "".join(phrase_crypt) #TABLEAU --> CHAR

#EXEMPLE:
ph1 = c_cesar("ALEA JACTA EST",3)
print(ph1)

#SORTIE: DOHD MDFWD HVW
