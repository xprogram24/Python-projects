from textblob import TextBlob
import matplotlib.pyplot as plt
import pandas as pd

# Read text file task1
# task 4 create multiple files and analsye each file
with open('schoolLearning/article3.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Clean lines (remove empty lines and whitespace) task 2
lines = [line.strip() for line in lines if line.strip()]
print("Sample lines:")
print(lines[:5])

# Sentiment analysis task
sentiments = []
for line in lines:
    blob = TextBlob(line)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    sentiments.append({'Text': line, 'polarity': polarity, 'subjectivity': subjectivity})

# Convert to DataFrame
df = pd.DataFrame(sentiments)
print(df.head())

# Plot sentiment scores task 3
plt.figure(figsize=(10,5))
plt.plot(df.index, df['polarity'], marker='o')
plt.title('Sentiment Polarity per Line')
plt.ylabel('Polarity Score')
plt.grid(True)
plt.show()

