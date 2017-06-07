from operator import xor

def encrypt(plaintext,key):

    keyascii = [None] * len(key)
    for i in range(0,len(key)):
        keyascii[i] = ord(key[i])

    key0 = [None] * 4
    key1 = [None] * 4

    j=0
    for i in range(0,len(keyascii)):
        if i <= 3:
            key0[i] = keyascii[i]
        else:
            key1[j] = keyascii[i]
            j = j + 1

    recur = len(plaintext)/4
    kosong = 4 - (len(plaintext)%4)
    if kosong > 0:
        recur = recur + 1

    asciitext = [None] * (recur*4)
    for i in range(0,len(asciitext)):
        if i < len(plaintext):
            asciitext[i] = ord(plaintext[i])
        else:
            asciitext[i] = ord(' ');

    diisi = (recur*4)

    x = 0
    for i in range(0,recur):
        for j in range(0,4):
            asciitext[x] = xor(asciitext[x], key0[j])
            x = x + 1

    x = 0
    hasilEncryp = [None] * len(asciitext)
    for i in range(0,recur):
        for j in range(0,4):
            hasilEncryp[x] = asciitext[x] + key1[j]
            x = x + 1

    hasilEncrypted = [None] * (len(hasilEncryp) - kosong)
    for i in range(0,len(hasilEncrypted)):
        hasilEncrypted[i] = chr(hasilEncryp[i])

    return hasilEncrypted


def decrypt(hasilEnkripsi, kunci):
    asciikey = [None] * len(kunci)
    for i in range(0, len(kunci)):
        asciikey[i] = ord(kunci[i])

    key0 = [None] * 4
    key1 = [None] * 4

    j = 0
    for i in range(0, len(asciikey)):
        if i <= 3:
            key0[i] = asciikey[i]
        else:
            key1[j] = asciikey[i]
            j = j + 1

    recur = len(hasilEnkripsi) / 4
    sisa = len(hasilEnkripsi) % 4
    ukuranEncryp = ((4*recur) + sisa)
    asciiEncryp = [None] * ukuranEncryp
    for i in range(0, len(asciiEncryp)):
        asciiEncryp[i] = ord(hasilEnkripsi[i])

    for i in range(0,ukuranEncryp):
        asciiEncryp[i] = asciiEncryp[i] - key1[i%4]

    hasilDecryp = [None] * len(asciiEncryp)
    for i in range(0,ukuranEncryp):
        hasilDecryp[i] = xor(asciiEncryp[i],key0[i%4])

    hasilDecrypted = [None] * len(hasilDecryp)
    for i in range(0,len(hasilDecrypted)):
        hasilDecrypted[i] = chr(hasilDecryp[i])

    return hasilDecrypted

text = raw_input("Masukkan text untuk di encrypt: ")
key = 'makanasi'

encrypted = encrypt(text,key)
print "Hasil enkripsi dari " + text + ":" + str(encrypted)

decrypted = decrypt(encrypted,key)
print "Hasil dekripsi dari" + text +  ":" + str(decrypted)


# nafiar rahmansyah