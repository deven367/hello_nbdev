# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/01_functions.ipynb (unless otherwise specified).

__all__ = ['download_ntlk_dep', 'normalize', 'split_by_newline', 'rm_useless_spaces', 'make_sentences',
           'write_to_file_cleaned', 'clean', 'STOPWORDS', 'get_wordnet_pos', 'remove_stopwords', 'remove_punctuations',
           'remove_punc_clean', 'process']

# Cell
import nltk

# Cell
from .core import *
from pathlib import Path
import os
import pandas as pd
import pickle
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import wordnet, stopwords
import unidecode
import re
from nltk.stem import WordNetLemmatizer
from fastcore.foundation import L
from fastcore.test import test_eq, test_ne

# Cell
from typing import Callable, Iterator, Union, Optional, List

# Cell
def download_ntlk_dep():
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')

# Cell
download_ntlk_dep()

# Cell
def normalize(data: np.ndarray) -> np.ndarray:
    """
    The function takes an array, matrix as input and normalizes
    it between 0 and 1

    Args:
        data (ndarray): any 1-D, or 2-D numpy array

    Returns:
        (ndarray): normalized ndarray
    """
    return (data - np.min(data)) / (np.max(data) - np.min(data))

# Cell
def split_by_newline(text: str) -> List[str]:
    """
    Only use when sentences are already tokenized
    returns sentences split by '\\n' if len(line) > 0

    Args:
        all (str): tokenized string to be split by '\\n'

    Returns:
        list: list of sentences split by '\\n'
    """
    return L([line for line in text.split('\n') if len(line) > 0])

# Cell
def rm_useless_spaces(t: str) -> str:
    """
    Remove multiple spaces
    """
    _re_space = re.compile(' {2,}')
    return _re_space.sub(' ', t)

# Cell
def make_sentences(text: str) -> List[str]:
    """
    Converts given bulk into sentences
    """
#     all_cleaned = re.sub('\n', ' ', text)
    all_cleaned = text.replace('\n', ' ')
    all_cleaned = rm_useless_spaces(all_cleaned)
    all_cleaned = all_cleaned.strip()
    all_cleaned = unidecode.unidecode(all_cleaned)
    sentences = sent_tokenize(all_cleaned)
    return L(sentences)

# Cell
def write_to_file_cleaned(sentences: List[str], fname: str) -> None:
    """
    Writes the sentences to a .txt file
    """
    with open(f'{fname.stem}_cleaned.txt', 'w') as f:
        for line in sentences:
            f.write(f'{line}\n')
    f.close()

# Cell
def clean(fname: str) -> None:
    """
    Takes name of a txt file and writes the tokenized sentences into a new txt file
    """
    fname = Path(fname)
    text = get_data(fname)
    sentences = make_sentences(text)
    print(f'{fname.name} contains {len(sentences)} sentences')
    write_to_file_cleaned(sentences, fname)

# Cell
STOPWORDS = set(stopwords.words('english'))

# Cell
def get_wordnet_pos(word: str) -> str:
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)

# Cell
def remove_stopwords(sentence: str) -> str:
    """
    Takes a sentence and removes stopwords from it
    """
    sentences = []
    for word in sentence.split():
        if word.lower() not in STOPWORDS:
            sentences.append(word)
    return ' '.join(sentences)

# Cell
def remove_punctuations(sentence: str) -> str:
    """
    Takes a sentence and removes punctuations from it
    """
    pat2 = re.compile('[^a-zA-Z0-9 ]+')
    pat1 = re.compile('[\s]+')

    doc = pat2.sub(' ', sentence)
    doc = pat1.sub(' ', doc)
    doc = doc.strip()
    return doc

# Cell
def remove_punc_clean(sentence: str, lemmatize: bool = False) -> str:
    """
    Takes a sentence and removes punctuations and stopwords from it

    Will lemmatize words if `lemmatize = True`
    """
    doc = remove_punctuations(sentence)
    doc = remove_stopwords(doc)


    if lemmatize:
        lemmatizer = WordNetLemmatizer()
        doc = ' '.join([lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in doc.split()])
    return doc

# Cell
def process(fname: str) -> List[str]:

    all_data = get_data(fname)
    all_data = unidecode.unidecode(all_data)
    sentences = make_sentences(all_data)
    clean_sentences = []
    removed_sentences = []
    for i, sentence in enumerate(sentences):
        t = remove_punc_clean(sentence)
        if len(t) > 0:
            clean_sentences.append(t)
        else:
            removed_sentences.append(i)

    # write_to_file_lexical(clean_sentences, fname)
    print('Done processing', fname)
    return L(removed_sentences)