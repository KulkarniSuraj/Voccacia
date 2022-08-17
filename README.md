# Voccacia
A simple tool to build your vocabulary
by effectively using

* Synonyms
* Antonyms
* Hyponyms
* Hypernyms
* Definitions
* Examples

of a word using popular lexical database for english called [wordnet](https://wordnet.princeton.edu/)
> _This project is currently under development_

## Installation

1. clone this repo `git clone https://github.com/KulkarniSuraj/Voccacia.git`
2. activate virtual environment if any
3. `pip3 install nltk`
4. Open python interactive shell
5.
```python
>>> import nltk
>>> nltk.download('wordnet') 
```
## Set up for Development
 ```sh
git clone https://github.com/KulkarniSuraj/Voccacia.git
python3 -m venv .venv
pip3 install -r requirements.txt
python3 -m nltk.downloader -d .venv/nltk_data wordnet
 ```

