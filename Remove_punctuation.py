import nltk
from nltk.corpus import stopwords

#nltk.download('./env/punkt')

sentence = "Some stupid sentence to be tokenized, also we should check things like didn't or wouldn't!"

tokens = nltk.word_tokenize(sentence)

# initialize 
output = []

# This will remove punctuation, really anything thats not alphanumeric
output = [k for k in tokens if k.isalpha()]

# address this issue TODO
print('There is an issue with the list below since it gets rid of the n\'t which changes wouldn\'t to would')
print(output)
