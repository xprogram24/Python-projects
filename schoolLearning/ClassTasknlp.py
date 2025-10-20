#class task1



'''input and cleaninig 
'''
#text = '''Artificial intelligence(AI) is changing the way we live and work.
#AI helps in language translation, chatbots, and data analysis .'''

'''convert to lowercase, reomve punctuation and print the cleaned text'''

import re
from collections import Counter
import matplotlib.pyplot as plt
text = '''Artificial intelligence(AI) is changing the way we live and work.
AI helps in language translation, chatbots, and data analysis 😊😂👌.'''

token = text.lower()

clean_text = re.sub(r'[^\w\s]','',token)


print('clean text')
print(clean_text)



#class task2 
'''split the text into individaul words using .split( ) , print the list of tokens'''
token = clean_text.split()
print('tokens ')
print(token)


#class task3
#define stopwords
stopwords = ['and','is','in','the','we','of','a']
#using list comprehesion
filtered_words = [word for word in token if word not in stopwords]
print(f"stop words fillted out : {filtered_words}")

#class task 4
#count word frequency(task 4)
freq = Counter(filtered_words)
print(freq)

#class task 5
#visualization(task 5)
most_Common = freq.most_common(5)
words, counts = zip(*most_Common)

plt.bar(words,counts)
plt.title("Top 5 Most frequent Words")
plt.xlabel("words")
plt.ylabel("frequecy")
plt.show()