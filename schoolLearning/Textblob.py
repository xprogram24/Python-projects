#class task1: setup enviroment
from textblob import TextBlob
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#nltk.download('vader_lexicon')

#class task 2: sentiment analysis with textblob
sentences = [
    "I love studying Artificial intelligence",
    "This project is really difficult and frustrating",
    "the movie was okay, not great but not terrible either",
    "Our Ai model performed exceptionally well on the dataset!",
    "i hate when my code doesn't run",
    "I HATE mondays",
    "I Really love Music ",
    
]

for text in sentences:
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    print(f"Text:{text}")
    print(f"sentiment score: {sentiment}")
    if sentiment > 0:
        print("- postive 😊\n")
    elif sentiment<0:
        print("--Negative 😒\n")
    else:
        print("--Neutral😐")

#task 3 INteractive Mini Sentiment Analyzer
print("=== Mini Sentiment Analyzer ===")
print("Type 'exit' to Quit.\n")
while True:
    text = input("Enter a sentence or paragraph: ")
    if text.lower() == 'exit':
        print("goodbye")
        break
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    print(f"\nSentiment Score: {polarity:2f}")
    if polarity > 0:
        print("Semtiment: postive 😊\n")
    elif polarity <0:
        print("Semtiment: Negative 😒\n")
    else:
        print("Semtiment: Neutral😐\n")