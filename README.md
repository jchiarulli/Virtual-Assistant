# Virtual-Assistant
TensorFlow based Virtual Assistant

General flow 

Raw Text > Tokenization > Tokenized Words (list of strings) > 

Text Processing-RegEx, removing stopwords > 

Enitiy classifier > words with entity tags (list of tuples) > 

intent classifier > Respond with function/message

## Tokenizer

For the tokenizer make sure you create a directory in env called: nltk_data

This will be where we keep the corpus data

invoke the pthton3 shell command and download the data:

```
python3

import nltk

nltk.download('punkt')
```

However it may be easier to do the following
```
python3

import nltk

nltk.download_gui()
```
### Note 

I may have added to many corpi?
