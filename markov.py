"""Generate Markov text from text files."""
import sys
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    file = open(file_path)
    text = file.read()
    file.close()
   
    return text
# open_and_read_file("green-eggs.txt")

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]

       
    """
    chains = {} 
    
    words = text_string.split()

    # To set a stop point, append None to the end of our word list.
    words.append(None)

    print(words)
    
    for word in range(len(words) - 2):
        key = (words[word], words[word + 1])
        value = words[word + 2]

        if key not in chains: 
           chains[key] = []

        chains[key].append(value)
    
    return chains


def make_text(chains):
    """Return text from chains."""

    # To check a value ends in punctuation.
    punct = ([".", "?", "!"])

    keys = list(chains.keys())

    key = choice(keys)

    # Check if the first character of the first item in the key is uppercase
    while not key[0][0].isupper():
        key = choice(keys)

    words = list(key)
    word = choice(list(chains[key]))

    while word is not None:
        key = key[1:] + (word,)

        words.append(word)

        # If word ends in punctuation, break out of the loop
        if word[-1] in punct:
            break

        word = choice(chains[key])

    return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
