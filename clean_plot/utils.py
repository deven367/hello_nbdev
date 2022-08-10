# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_utils.ipynb.

# %% auto 0
__all__ = ['STOPWORDS', 'get_data', 'load_pmi', 'loader', 'load_dictionary', 'normalize', 'download_nltk_dep', 'split_by_newline',
           'rm_useless_spaces', 'make_sentences', 'write_to_file_cleaned', 'clean', 'get_wordnet_pos',
           'remove_stopwords', 'remove_punctuations', 'remove_punc_clean', 'process_for_lexical']

# %% ../nbs/00_utils.ipynb 3
import pickle
import numpy as np
from pathlib import Path
from fastcore.foundation import L
from fastcore.xtras import globtastic
import pathlib
from fastcore.test import test_eq

# %% ../nbs/00_utils.ipynb 4
def get_data(
    fname: (str, Path) # path to the file
    )->str: # returns content of the file
    "Reads from a txt file"
    with open(fname, 'r') as f:
        all_text = f.read()
    return all_text

# %% ../nbs/00_utils.ipynb 5
def load_pmi(
    fname: (str, Path)  # name of pmi file
) -> np.ndarray:  # pmi matrix
    """
    Loads the PMI matrix
    """
    file_ = loader(fname, '.npy')
    pmi = np.load(file_)
    print(f'Loaded {name}')
    return pmi

# %% ../nbs/00_utils.ipynb 6
def loader(
    path: [str, pathlib.Path],  # path to a given folder,
    extension: str,  # extension of the file you want
) -> L:  # returns `L`
    "Given a Path and an extension, returns all files with the extension in the path"
    files = L([Path(f) for f in globtastic(path, file_glob=f'*{extension}')])

    return files

# %% ../nbs/00_utils.ipynb 7
def load_dictionary(
    fname: str , # path to the pkl file
    )->dict: # returns the contents 
    """
    Given a fname, function loads a `pkl` dictionary
    from the current directory
    """
    fname = open(fname, 'rb')
    data = pickle.load(fname)
    return data

# %% ../nbs/00_utils.ipynb 8
def normalize(
    data: np.ndarray,  # input array
) -> np.ndarray:  # normalized array
    """
    Given an input array, return normalized array
    """
    return (data - np.min(data)) / (np.max(data) - np.min(data))

# %% ../nbs/00_utils.ipynb 11
import re
from fastcore.script import call_parse

# %% ../nbs/00_utils.ipynb 13
def download_nltk_dep():
    """
    Downloads the `nltk` dependencies
    """
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')
    nltk.download('omw-1.4')

# %% ../nbs/00_utils.ipynb 14
def split_by_newline(
    text: str, # sentences separated by \n
    ) -> L: # list of sentences
    """
    Only use when sentences are already tokenized
    returns sentences split by '\\n' if len(line) > 0

    Args:
        all (str): tokenized string to be split by '\\n'

    Returns:
        list: list of sentences split by '\\n'
    """
    return L([line for line in text.split('\n') if len(line) > 0])

# %% ../nbs/00_utils.ipynb 16
def rm_useless_spaces(
    t: str, # sentence with extra spaces
    ) -> str: # sentence without extra spaces
    """
    Removes useless spaces
    """
    _re_space = re.compile(' {2,}')
    return _re_space.sub(' ', t).lstrip().rstrip()

# %% ../nbs/00_utils.ipynb 18
def make_sentences(
    text: str, # bulk text
    ) -> L: # list of sentences
    """
    Converts given bulk into sentences
    """
    try:
        sent_tokenize('')
    except Exception as error:
        download_nltk_dep()
        print(f'Run download_nltk_dep() first') 
#     all_cleaned = re.sub('\n', ' ', text)
    all_cleaned = text.replace('\n', ' ')
    all_cleaned = rm_useless_spaces(all_cleaned)
    all_cleaned = all_cleaned.strip()
    all_cleaned = unidecode.unidecode(all_cleaned)
    sentences = sent_tokenize(all_cleaned)
    return L(sentences)

# %% ../nbs/00_utils.ipynb 19
def write_to_file_cleaned(
    sentences: list, # list of sentences 
    fname: str, # name of output file
    ) -> None:
    """
    Writes the sentences to a .txt file
    """
    with open(f'{fname.stem}_cleaned.txt', 'w') as f:
        for line in sentences:
            f.write(f'{line}\n')
    f.close()

# %% ../nbs/00_utils.ipynb 20
@call_parse
def clean(
    fname: str, # name of input txt file
    ) -> None:
    """
    Takes name of a txt file and writes the tokenized sentences into a new txt file
    """
    fname = Path(fname)
    text = get_data(fname)
    sentences = make_sentences(text)
    print(f'{fname.name} contains {len(sentences)} sentences')
    write_to_file_cleaned(sentences, fname)

# %% ../nbs/00_utils.ipynb 21
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import wordnet, stopwords
from nltk.stem import WordNetLemmatizer

# %% ../nbs/00_utils.ipynb 25
import unidecode

# %% ../nbs/00_utils.ipynb 28
def get_wordnet_pos(
    word: str, # input word token
    ) -> str: # POS of the given word
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)

# %% ../nbs/00_utils.ipynb 29
from nltk.corpus import stopwords
STOPWORDS = set(stopwords.words('english'))

# %% ../nbs/00_utils.ipynb 30
def remove_stopwords(
    sentence: str, # input sentence
    ) -> str: # output sentence
    """
    Takes a sentence and removes stopwords from it
    """
    sentences = []
    
    for word in sentence.split():
        if word.lower() not in STOPWORDS:
            sentences.append(word)
    return ' '.join(sentences)

# %% ../nbs/00_utils.ipynb 31
def remove_punctuations(
    sentence: str, # input sentence
    ) -> str: # output sentence
    """
    Takes a sentence and removes punctuations from it
    """
    pat2 = re.compile('[^a-zA-Z0-9 ]+')
    pat1 = re.compile('[\s]+')

    doc = pat2.sub(' ', sentence)
    doc = pat1.sub(' ', doc)
    doc = doc.strip()
    return doc

# %% ../nbs/00_utils.ipynb 32
def remove_punc_clean(
    sentence: str, # input sentence
    lemmatize: bool = False, # flag to `lemmatize`
    ) -> str:
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

# %% ../nbs/00_utils.ipynb 34
def process_for_lexical(
    fname: str, # name of the input txt file
    ) -> L: # 
    "Given an input txt file, return removed sentences"
    fname = Path(fname)
    all_data = get_data(fname)
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
    print('Done processing', fname.name)
    return L(removed_sentences)