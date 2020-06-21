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


## `follow_the_economy.py`

A script to identify messages from `beginbotbot`, and parse them into economic events (which have been loosely categorized in beginbot.economic.events.txt).

The goal is to log economic events so we can discern market sentiment. We will log:
    - market participants expressing sentiment (love/hate) towards products (soundeffects)
    - market participants doing activism (proposing a coup, voting for/against a coup)
    - pro-social and anti-social behavior

From these news events, we can eventually plot market participants on a radar chart  of personality traits, and even assign a "social credit score".

Then, Blackwater bot can use this information to track and predict potential dissidents

## `construct_business_network.py`

Updates a Neo4j graph with any beginworld chat events related to commerce (e.g. !give, !steal, !props etc.)

Make sure you `docker-compose up` before running this script
