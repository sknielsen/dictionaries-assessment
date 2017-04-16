"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    # Separate phrase into a list of words in that phrase
    words_in_phrase = phrase.split(' ')
    # Initialize empty dictionary
    word_counts = {}
    # Iterate over words in list, adding them to dictionary or adding one to their count
    for word in words_in_phrase:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon.

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If melon name does not exist, return 'No price found'.

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """
    # Set dictionary of melon names and prices
    melon_prices = {'Watermelon': 2.95, 'Cantaloupe': 2.50, 'Musk': 3.25, 'Christmas': 14.25}
    # Search for melon name in the dictionary
    if melon_name in melon_prices:
        # Return the price if melon in dictionary
        return melon_prices[melon_name]
    else:
        return 'No price found'


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

        >>> word_length_sorted(["porcupine", "ok"])
        [(2, ['ok']), (9, ['porcupine'])]
    """

    # Initialize empty dictionary
    word_lengths = {}
    #  Iterate over words in given list
    for word in words:
        # Get word lenght
        length = len(word)
        # Add word length as key and list of words with that length as value
        word_lengths.setdefault(length, []).append(word)

    # Initialize empty list
    lengths_and_words = []
    # Iterate over key value pairs in dictionary
    for key, value in word_lengths.items():
        # Add key value pairs as tuple to list
        lengths_and_words.append((key, sorted(value)))

    # Sort list
    lengths_and_words.sort()

    return lengths_and_words


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
    # Initialize dictionary of english to pirate words
    english_to_pirate = {
        'sir': 'matey',
        'hotel': 'fleabag inn',
        'student': 'swabbie',
        'man': 'matey',
        'professor': 'foul blaggart',
        'restaurant': 'galley',
        'your': 'yer',
        'excuse': 'arr',
        'students': 'swabbies',
        'are': 'be',
        'restoom': 'head',
        'my': 'me',
        'is': 'be',
    }
    # Split phrase into list at spaces
    phrase_words = phrase.split(' ')
    # Iterate over indices in phrase words list
    for i in range(len(phrase_words)):
        english_word = phrase_words[i]
        # Search for word in dictionary and change word if found
        if english_word in english_to_pirate:
            phrase_words[i] = english_to_pirate[english_word]

    # Join list into a string with spaces
    pirate_phrase = ' '.join(phrase_words)

    return pirate_phrase


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
    #  Initialize empty dictionary for storing names and their first letter
    first_letters = {}
    # Iterate over names list
    for name in names:
        # Add first letter as key and name to the value list
        first_letters.setdefault(name[0], []).append(name)

    # Set new empty list
    new_names = []
    # Grab the first letter of the first word
    letter = names[0][0]
    # While the first letter is in the dictionary
    while letter in first_letters:
        # Remove name from value list in dict and save it
        next_name = first_letters[letter].pop(0)
        # Add name to the new list
        new_names.append(next_name)
        # If the value is now an empty list, remove the key from dict
        if first_letters[letter] == []:
            del first_letters[letter]
        # Grab last letter in the next name
        letter = next_name[-1]

    return new_names

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
