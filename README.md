# Virtual-Assistant
TensorFlow based Virtual Assistant

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

