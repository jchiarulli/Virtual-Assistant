import spacy

nlp = spacy.load('en')

ECE_UG_HB = open('ECE_current-handbook.txt', mode='r', encoding='utf-8')

ECE_UG_HB_contents = ECE_UG_HB.read()

#print(ECE_UG_HB_contents)
doc = nlp(ECE_UG_HB_contents)

#for token in doc[100:110]:
#    print(token.text, token.lemma_, token.pos_, token.dep_,
#          token.shape_, token.is_alpha, token.is_stop)

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

#print(spacy.explain('PROPN'))
#print(spacy.explain('Xxxxx'))

#print(len(doc))
