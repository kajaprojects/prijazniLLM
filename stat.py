import json
import pandas as pd
from tokenizers.decoders import ByteLevel

with open("opinion-lexicon-English/positive-words.txt") as file_in_positive:
    positiveWords = []
    for line in file_in_positive:
        line = line.strip()
        if line and not line.startswith(";"): #ce ni prazna plus ne zacne
           positiveWords.append(line)

with open("opinion-lexicon-English/negative-words.txt") as file_in_negative:
    negativeWords = []
    for line in file_in_negative:
        if line and not line.startswith(";"):
           negativeWords.append(line)

with open(r"tokenizer.json", 'r', encoding='utf-8') as f:
    d = json.load(f)
#print(d)

vocab = []
decoder = ByteLevel()
totalPositive = len(positiveWords) #vse pozitivne
#countPositiveBingo = 0 #koliko zetonov matcha
totalNegative = len(negativeWords) #vse negativne
#countNegativeBingo = 0
matchPositiveCount = 0
matchNegativeCount = 0
tokenStats = {}

for token in d['model']['vocab']:
    tokenDecoded = decoder.decode([token])
    tokenWord = tokenDecoded.lstrip()

    matchPositiveCount = sum(1 for positiveWord in positiveWords if tokenWord == positiveWord[:len(tokenWord)])
    matchNegativeCountCount = sum(1 for negativeWord in negativeWords if tokenWord == negativeWord[:len(tokenWord)])

    totalMatch = matchPositiveCount + matchNegativeCountCount

    tokenStats[tokenWord] = {
        "totalMatch": totalMatch,
        "positiveCount": matchPositiveCount,
        "negativeCount": matchNegativeCountCount,
        "stat_pos": matchPositiveCount / totalMatch if totalMatch > 0 else 0,
        "stat_neg": matchNegativeCountCount / totalMatch if totalMatch > 0 else 0,
    }

statistika = pd.DataFrame.from_dict(tokenStats, orient='index')
statistika.to_csv("tokenStats.csv")
#print("countPositive ", totalPositive)
#print("countPositiveBingo ", countPositiveBingo)
#print("countNegative ", totalNegative)
#print("countNegativeBingo ", countNegativeBingo)