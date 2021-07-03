# AUTOGENERATED! DO NOT EDIT! File to edit: 05_lexical.ipynb (unless otherwise specified).

__all__ = ['interpolate', 'load_pmi', 'load_dictionary']

# Cell
import re
from clean_plot import *
import os
import unidecode
from collections import OrderedDict

# Cell
def interpolate(lex, removed_indices = []):
    """
    Method does interpolation based on the removed indices.
    Substitutes the missing values based on the previous value in the array
    """
    for index in removed_indices:
        if index < len(lex):
            lex = np.insert(lex, index, lex[index - 1])
    return lex

# Cell
def load_pmi(path):
    pmi = np.load(path)
    return pmi


# Cell
def load_dictionary(path):
    fname = open(path, 'rb')
    data = pickle.load(fname)
    return data