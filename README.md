# Streaming Topics

## INSTALLATION
```
pip3 install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.2.0/en_core_web_sm-2.2.0.tar.gz
pip install -r requirements
```


Construct a graph of topics discussed in a chat stream

Perform NLP on an IRC stream:
- NER to derive salient entities
- disentanglement to "connect" messages to overall conversation


## ~~Proof of Concept~~
1. set up NER and run it on an IRC stream, printing a running list of entities 
	* entities that appear in the [same messages](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/jupyter/4-%20Entity%20Recognizer%20DL.ipynb) are likely related, so we can draw an edge between them
```

```
