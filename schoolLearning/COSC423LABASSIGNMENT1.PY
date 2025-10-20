import re
import matplotlib.pyplot as plt
from collections import Counter
import nltk
from nltk.stem import PorterStemmer 

text = """
   Artificial Intelligence (AI) is no longer a futuristic concept—it's here, and it’s changing the world faster than we expected!
From voice assistants like Alexa and Siri, to recommendation systems on Netflix and YouTube, AI quietly powers much of our daily digital experience.
   However, as AI continues to grow, questions about ethics, fairness, and privacy are becoming louder. For instance, how do we ensure that AI systems make decisions that are transparent and unbiased?
   
Many organizations have started to use machine learning (ML) to predict customer behavior, detect fraud, and even diagnose diseases.
But not all AI systems are perfect—some models may make mistakes, especially when trained on poor-quality data. 
That’s why data preprocessing, cleaning, and normalization are essential steps before any AI model is built.

  In addition, researchers now talk about “Explainable AI” (XAI), which focuses on making AI decisions understandable to humans. 
This is particularly important in sensitive areas such as healthcare, education, and criminal justice, where wrong decisions can have serious consequences.

Interestingly, AI is not just about coding or mathematics—it’s also about human values, social responsibility, and understanding language. 
Natural Language Processing (NLP), for example, helps computers understand human text and speech, enabling chatbots, language translation, and sentiment analysis.

Overall, the success of AI depends on how responsibly we collect, process, and interpret data. 
As future data scientists and software engineers, your role is to build AI systems that are accurate, ethical, and human-centered. 
"""

#task 1. Text cleaning 
'''a. Convert the text to lowercase
b. Remove punctuation
c. Remove digits
d. Remove extra spaces and newline characters'''

lower_text = text.lower()

clean_text = re.sub(r'[^\w\s]','',lower_text)#remove anything that is not a word or white space
clean_text = re.sub(r'\d+','',clean_text) #remove digit
clean_text = re.sub(r'\s+',' ',clean_text) #remove newline characters
print("Text cleaning ")
print("\n")
print(clean_text)


#Task 2. Tokenization
'''a. Split the text into:
b. Words: using .split()
c. Sentences: using .split('.')
Challenge: Compare the number of tokens before and after cleaning.'''


wordtoken = clean_text.split()
sentencesToken = clean_text.split('.')
print(f"\nword token {wordtoken}")
print("\n")
print(f"\nsentences Token {sentencesToken}")

#challenge
word_before  = text.split() 
word_After = wordtoken
print(f"token before cleaning: {len(word_before)}" )
print(f"token after cleaning: {len(word_After)}")

#Task 3. Stopword Removal
'''Use a small list like:
stopwords = ['and', 'is', 'the', 'to', 'of', 'a', 'in', 'on', 'for', 'as', 'are', 'that', 'be', 'it', 'this']

And then print the filtered tokens'''


stopwords = ['and', 'is', 'the', 'to', 'of', 'a', 'in', 'on', 'for', 'as', 'are', 'that', 'be', 'it', 'this']
filtered_Token = [word for word in wordtoken if word not in stopwords]
print(f"\nstop words fillted out : {filtered_Token}")


#Task 4. Normalization
'''Demonstrate: Stemming (manually or using nltk.PorterStemmer) or simply remove plural endings (rstrip('s'))
Goal: reduce words like systems, decisions, models → system, decision, model.
'''

#create the portstemer instance
stemmer = PorterStemmer()
stemmer_Word  = [ stemmer.stem(word) for word in filtered_Token] 
print(f"\nstemmer_Word")

#Task 5. Word Frequency
'''Count the top 10 most frequent words. What does the frequency distribution tell you about the main topic?
'''
print("Top 10 most frequent word")
frequency =  Counter(stemmer_Word)
top_10Words = frequency.most_common(10)
print("\n Top ten word: ")
print(top_10Words)

'''the top ten word tells us the topic is on AI'''

#Task 6. Visualization
'''Plot a bar chart of the top 10 words'''
words, counts = zip(*top_10Words)

plt.bar(words,counts)
plt.title("Top 5 Most frequent Words")
plt.xlabel("words")
plt.ylabel("frequecy")
plt.show()

