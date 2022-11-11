ALPHABATES = list(map(chr, range(ord('a'), ord('z')+1))) + list(map(chr, range(ord('A'), ord('Z')+1)))


def EncodeShort(text, key=2):
    return "".join([ALPHABATES[(ALPHABATES.index(i)+key) % len(ALPHABATES)] if i != " " else "$" for i in text])

def DecodeShort(text, key=2):
    return  "".join([ALPHABATES[(ALPHABATES.index(i)-key) % len(ALPHABATES)] if i != "$" else " " for i in text])

text = "Hello Arena"
encoded = EncodeShort(text)
print("Encoded ",encoded)
decoded = DecodeShort(encoded)
print("Decoded ",decoded)