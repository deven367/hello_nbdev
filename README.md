Welcome to clean_plot
================

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

![CI](https://github.com/deven367/clean_plot/actions/workflows/test.yaml/badge.svg)
![Deploy to GitHub
Pages](https://github.com/deven367/clean_plot/actions/workflows/deploy.yml/badge.svg)

## Install

The easiest way to install the library is to simply do a `pip` install.

    pip install clean-plot

Another way to install the library would be to build from source. It is
more likely that the released version may contain bugs. The source would
get updated more often. If you plan to add features to `clean_plot`
yourself, or want to be on the cutting edge, you can use an editable
install.

    git clone https://github.com/deven367/clean_plot.git
    cd clean_plot
    pip install -e . 

## How to use

The library contains easy to use methods for cleaning text, tokenizing
and lemmatizing sentences. These sentences can then be easily fed to a
sentence encoder to create sentence embeddings.

``` python
fname = '../files/dummy.txt'
text = get_data(fname)
print(text)
```

    MARLEY was dead: to begin with. There is no doubt
    whatever about that. The register of his burial was
    signed by the clergyman, the clerk, the undertaker,
    and the chief mourner. Scrooge signed it: and
    Scrooge's name was good upon 'Change, for anything he
    chose to put his hand to. Old Marley was as dead as a
    door-nail.

    Mind! I don't mean to say that I know, of my
    own knowledge, what there is particularly dead about
    a door-nail. I might have been inclined, myself, to
    regard a coffin-nail as the deadest piece of ironmongery
    in the trade. But the wisdom of our ancestors
    is in the simile; and my unhallowed hands
    shall not disturb it, or the Country's done for. You
    will therefore permit me to repeat, emphatically, that
    Marley was as dead as a door-nail.

    This is a new sentence.

``` python
sentences = make_sentences(text)
```

``` python
sentences
```

    (#11) ['MARLEY was dead: to begin with.','There is no doubt whatever about that.','The register of his burial was signed by the clergyman, the clerk, the undertaker, and the chief mourner.',"Scrooge signed it: and Scrooge's name was good upon 'Change, for anything he chose to put his hand to.",'Old Marley was as dead as a door-nail.','Mind!',"I don't mean to say that I know, of my own knowledge, what there is particularly dead about a door-nail.",'I might have been inclined, myself, to regard a coffin-nail as the deadest piece of ironmongery in the trade.',"But the wisdom of our ancestors is in the simile; and my unhallowed hands shall not disturb it, or the Country's done for.",'You will therefore permit me to repeat, emphatically, that Marley was as dead as a door-nail.'...]

``` python
no_punctuations = []
for sentence in sentences:
    new_sentence = remove_punctuations(sentence)
    no_punctuations.append(new_sentence)
```

``` python
no_punctuations
```

    ['MARLEY was dead to begin with',
     'There is no doubt whatever about that',
     'The register of his burial was signed by the clergyman the clerk the undertaker and the chief mourner',
     'Scrooge signed it and Scrooge s name was good upon Change for anything he chose to put his hand to',
     'Old Marley was as dead as a door nail',
     'Mind',
     'I don t mean to say that I know of my own knowledge what there is particularly dead about a door nail',
     'I might have been inclined myself to regard a coffin nail as the deadest piece of ironmongery in the trade',
     'But the wisdom of our ancestors is in the simile and my unhallowed hands shall not disturb it or the Country s done for',
     'You will therefore permit me to repeat emphatically that Marley was as dead as a door nail',
     'This is a new sentence']

## Help

To see the various CLI available in the library, use the function
`cp_help`

``` python
!cp_help
```

    check_len                       Takes name of a txt file and writes the tokenized sentences into a new txt file
    corr_hm                         Generates correlation plots from normalized SSMs
    cp_help                         Show help for all console scripts
    heatmaps                        Generates plots for embeddings in the folder
    heatmaps_pkl                    Generates SSMs from pkl files
    histograms                      Generates histograms for embeddings in the folder
    lex_ts                          Generate lexical TS from Lexical SSM
    make_pkl                        Create pkl for time series from embeddings
    ts_pkl                          Plot timeseries from the pkl file

## Contributing

This library has come into existence because of
[nbdev](https://nbdev.fast.ai/) (one of many amazing tools made by
[fast.ai](https://www.fast.ai/)). PRs and Issues are encouraged.

After you clone this repository, please run `nbdev_install_hooks` in
your terminal. This sets up git hooks, which clean up the notebooks to
remove the extraneous stuff stored in the notebooks (e.g. which cells
you ran) which causes unnecessary merge conflicts.

Before submitting a PR, check that the local library and notebooks
match. The script `nbdev_fix` can let you know if there is a difference
between the local library and the notebooks.

If you made a change to the notebooks in one of the exported cells, you
can export it to the library with `nbdev_export`.

If you made a change to the library, you can export it back to the
notebooks with `nbdev_update`.
