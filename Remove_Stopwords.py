import nltk
from nltk.corpus import stopwords

#nltk.download('./env/punkt')

sentence = "Some stupid sentence to be tokenized, also we should check things like didn't or wouldn't!"

tokens = nltk.word_tokenize(sentence)

stop_words = set(stopwords.words('english'))

output = []

for k in tokens:
    if k not in stop_words:
        output.append(k)
print('Original ' + sentence)
print(output)

