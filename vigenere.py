ALPHABATES = list(map(chr,range(ord('A'),ord('Z')+1)))
def encryptShort(text,key="HEALTH"):
    return "".join([ALPHABATES[(ALPHABATES.index(text[i])+ALPHABATES.index(key[i%len(key)]))%len(ALPHABATES)] for i in range(len(text))])

print(encryptShort("LIFEISFULLOFSURPRISES"))