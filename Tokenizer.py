import nltk

#nltk.download('./env/punkt')

sentence = "Some stupdi sentence to be tokenizes also we should check things like didn't or wouldn't"

tokens = nltk.word_tokenize(sentence)

print(tokens)
