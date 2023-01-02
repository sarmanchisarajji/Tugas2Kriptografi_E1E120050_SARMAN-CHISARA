s = []
for i in range(256):
    s.append(i)
print("Array S :")
print(s)

print("")
    
plaintext = "2050"

i = 0;
j = 0;
keystream = []
for idx in range(len(plaintext)):
    i = (i + 1) % 256
    j = (j + s[i]) % 256
    s[i] , s[j] = s[j], s[i] ## swap

    t = (s[i] + s[j]) % 256
    u = s[t]
    keystream.append(u)
print("Keystream : ")
print(keystream)

print("")
    
xor = []
for idx in range(len(plaintext)):
    c = chr(keystream[idx] ^ ord(plaintext[idx]))
    xor.append(c)

print("Plaintext      :", plaintext)
print("Hasil xor pgra :",xor ,end='')