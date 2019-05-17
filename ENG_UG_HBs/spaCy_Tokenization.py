import spacy
import random

nlp = spacy.load('en')

ECE_UG_HB = open('ECE_current-handbook.txt', mode='r', encoding='utf-8')

ECE_UG_HB_contents = ECE_UG_HB.read()

#print(ECE_UG_HB_contents)
doc = nlp(ECE_UG_HB_contents)

#for token in doc[100:110]:
#    print(token.text, token.lemma_, token.pos_, token.dep_,
#          token.shape_, token.is_alpha, token.is_stop)

#for ent in doc.ents[60:150]:
#    print(ent.text, ent.start_char, ent.end_char, ent.label_)

#print(spacy.explain('PROPN'))
#print(spacy.explain('Xxxxx'))

#print(len(doc))

train_data = [
    ("Handbook for Undergraduate Students", {'entities': [(0, 34, 'WORK_OF_ART')]}),
    ("This handbook describes the details of the undergraduate program offered by the Department of Electrical and Computer Engineering.", {'entities': [(80, 128, 'ORG')]}),
    ("Both options lead to the same B.S. Degree in Electrical and Computer Engineering (ECE).", {'entities': [(30, 80, 'PRODUCT')]}),
    ("A B.S. Degree in Electrical and Computer Engineering has the following requirements: Required Number of Degree Credits: Both Electrical Engineering and Computer Engineering options require 123 credits for graduation. Under certain circumstances, due to one reason or another, a student might be exempted from taking a required course.", {'entities': [(2, 52, 'PRODUCT')]})]

nlp = spacy.blank('en')
optimizer = nlp.begin_training()
for i in range(20):
    random.shuffle(train_data)
    for text, annotations in train_data:
        nlp.update([text], [annotations], sgd=optimizer)
nlp.to_disk('/home/jason/Repo/Virtual-Assistant/ENG_UG_HBs/model')
