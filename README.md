# Sentiment analysis session at the UCREL summer school 2017

The sides associated to this session can be found [here](slides/ucrel-sentiment-analysis.pdf) and the latex associated to those slides are within the [latex folder](slides/latex), the latex when complied will not have the University logo due to copyright. The tutorial that accompied the slides is within this repository and is explained below:

# SentiLexTutorial
Sentiment lexicon creation tutorial for the sentiment analysis session at the UCREL summer school 2017.

This is based on the the sentiment lexicon creation defined in this [paper](http://aclweb.org/anthology/D16-1057) and uses the code from that paper as well which can be found [here](https://github.com/williamleif/socialsent), we actually manipulated the original code so that it is compatiable with python3 that code can be found [here](https://github.com/apmoore1/socialsent).

The tutorial is within the [IPython notebook](Tutorial.ipynb)

The code requires the following [PIPs](requirements.txt). To install them run the following:
`pip3 install -r requirements.txt`
And the following command needs running to download the stop words for NLTK:
`python3 -m nltk.downloader stopwords`
