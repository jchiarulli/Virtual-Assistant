import plac # wrapper over argparse
import random
from pathlib import Path
import spacy
from spacy.matcher import PhraseMatcher

# Utility Function

# This function converts the output of the PhraseMatcher to something usable in
# training. The training data needs a string index of characters (start, end, label)
# while the matched output uses index of words from an nlp document.

def offseter(lbl, doc, matchitem):
    o_one = len(str(doc[0:matchitem[1]]))
    subdoc = doc[matchitem[1]:matchitem[2]]
    o_two = o_one + len(str(subdoc))
    return (o_one, o_two, lbl)

# load spacy and setup pipes for training

nlp = spacy.load('en')

if 'ner' not in nlp.pipe_names:
    ner = nlp.create_pipe('ner')
    nlp.add_pipe(ner)
else:
    ner = nlp.get_pipe('ner')
    
# Instead setting up by hand, we can use PhraseMatcher class from spacy to locate the
# text we want to label.
    
label = 'DEGREE'
matcher = PhraseMatcher(nlp.vocab)
for i in ['B.S. Degree in Electrical and Computer Engineering', 'B.S.',
          'B.S. Degree in ECE']:
    matcher.add(label, None, nlp(i))
    
#one = nlp('Both options lead to the same B.S. Degree in Electrical and Computer Engineering (ECE).')
#matches = matcher(one)

# prints the representation of the label and the word position in the document

#print([match for match in matches])

# Gather training data from Rutgers reddit, Rutgers FAQs, Handbooks, webreg, etc.
# Use spacy to parse paragraphs of texts into sentences then use the PhraseMatcher
# Design our own webcrawler to gather data

# Format the data

res = []
to_train_ents = []
with open('ECE_current-handbook.txt') as ece_chb:
    line = True
    while line:
        line = ece_chb.readline()
        mnlp_line = nlp(line)
        matches = matcher(mnlp_line)
        res = [offseter(label, mnlp_line, x)
              for x
              in matches]
        to_train_ents.append((line, dict(entities=res)))
        
# Train the Recognizer

optimizer = nlp.begin_training()   # spacy's built in optimizer

# Go through the pipes to make sure only the ner pipe is there for the training

other_pipes = [pipe
              for pipe
              in nlp.pipe_names
              if pipe != 'ner']

# The update function takes the loaded model and updates dates it with new information
# about the token, the position of the token, and the string you are trying to parse
# Every time it is updated it is going to move down the gradient using the optimizer
# The error appears to bounce around, but the error rate is from the last run
# So when it is going up, it is not going up gobally, it is going up along the minimum
# for the path you are currently walking

# Using 20 as the number of iterations is taken from the documentation
# If you loop too many times it will forget everything it knows now i.e.
# catastrophic memory loss
# The documentation does not specify how many times to run the loop

with nlp.disable_pipes(*other_pipes):   # Only train ner
    for itn in range(20):
        losses = {}
        random.shuffle(to_train_ents)
        for item in to_train_ents:
            nlp.update([item[0]],
                      [item[1]],
                      sgd=optimizer,
                      drop=0.35,
                      losses = losses)
        print(losses)