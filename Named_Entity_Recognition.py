from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

ner_tagger = StanfordNERTagger("stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz", "stanford-ner/stanford-ner.jar")

text = "Jason has yet to commit to this repo, and Nick is ugly in Australia! \n I wonder if it notices things like football, baseball, soccer, Today, Monday, car"
tokens = word_tokenize(text)
ner_tags = ner_tagger.tag(tokens)

print(ner_tags)
