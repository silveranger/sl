def calculateFrequencyShort(text):
    unique = set(text.replace(" ",""))
    return {i:100*text.count(i)/len(text) for i in unique}

print(calculateFrequencyShort("Hello World"))