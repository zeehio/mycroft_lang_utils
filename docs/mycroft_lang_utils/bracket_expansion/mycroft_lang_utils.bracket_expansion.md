
## Module mycroft_lang_utils.bracket_expansion


###  Fragment

(Abstract) empty sentence fragment

####  expand

```

def expand(self)

```

Expanded version of the fragment. In this case an empty sentence.

Returns:

    List<List<str>>: A list with an empty sentence (= token/string list)

####  tree

```

def tree(self)

```

Return the represented sentence tree as raw data.




###  Options

A Combination of possible sub-sentences.

Construct with List<Fragment> as argument.

####  expand

```

def expand(self)

```

Returns all of its options as seperated sub-sentences.

Returns:

    List<List<str>>: A list containing the sentences created by all
                        expansions of its sub-sentences




###  Sentence

A Sentence made of several concatenations/words.
Construct with a List<Fragment> as argument.

####  expand

```

def expand(self)

```

Creates a combination of all sub-sentences.

Returns:

    List<List<str>>: A list with all subsentence expansions combined in
                        every possible way




###  SentenceTreeParser

Generate sentence token trees from a list of tokens
['1', '(', '2', '|', '3, ')'] -> [['1', '2'], ['1', '3']]

####  expand\_parentheses

```

def expand_parentheses(self)

```





###  Word

Single word in the sentence tree.
Construct with a string as argument.

####  expand

```

def expand(self)

```

Creates one sentence that contains exactly that word.

Returns:

    List<List<str>>: A list with the given string as sentence
                        (= token/string list)


