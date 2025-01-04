import json
from tokenizers.decoders import ByteLevel

with open("opinion-lexicon-English/positive-words.txt") as file_in_positive:
    positiveWords = []
    for line in file_in_positive:
        if (not ";" in line[0:1]):
           positiveWords.append(line[0:len(line)-1])

with open("opinion-lexicon-English/negative-words.txt") as file_in_negative:
    negativeWords = []
    for line in file_in_negative:
        if (not ";" in line[0:1]):
           negativeWords.append(line[0:len(line)-1])

d = None
with open(r"tokenizer.json", 'r', encoding='utf-8') as f:
    d = json.load(f)
#print(d)

vocab = []
decoder = ByteLevel()
countPositive = 0
countPositiveBingo = 0
countNegative = 0
countNegativeBingo = 0
for positiveWord in positiveWords:
    countPositive+=1
for negativeWord in negativeWords:
    countNegative+=1
for token in d['model']['vocab']:
    tokenDekoded = decoder.decode([token])
    if (" " in tokenDekoded[0:1]):
        tokenWord = tokenDekoded[1:len(tokenDekoded)]
    else:
        tokenWord = tokenDekoded
    for positiveWord in positiveWords:
        if tokenWord == positiveWord[0:len(tokenWord)]:
            countPositiveBingo+=1
    for negativeWord in negativeWords:
        if  tokenWord == negativeWord[0:len(tokenWord)]:
            countNegativeBingo+=1
print("countPositive ", countPositive)
print("countPositiveBingo ", countPositiveBingo)
print("countNegative ", countNegative)
print("countNegativeBingo ", countNegativeBingo)