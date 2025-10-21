#sentiment using vader
from textblob import TextBlob
import matplotlib.pyplot as plt
import pandas as pd

#Read text file
with open('article.txt','r',encoding='utf-8') as f:
    lines = f.readlines()

#clean lines ( remove empty lines and whitespaces)
lines = [line.strip() for line in lines if line.strip()]
print("Sample lines:")
print(lines[:5])

sentiments = []

for line in lines:
    blob = TextBlob(line)
    polarity = blob.sentiment.polarity #-1 (Negative) - +1 (positive)
    subjectivity = blob.sentiment.subjectivity #0 (objective) - 1 (subjective )
    sentiments.append({'Text': line,'polarity': polarity,'subjectivity0': subjectivity})

#convert to dataframe
df = pd.DataFrame(sentiments)
print(df.head())
