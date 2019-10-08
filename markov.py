"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    file = open(file_path)
    text = file.read()
   
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
    file_to_use = open_and_read_file(text_string)
    words = file_to_use.split()
    # print(words)

    for i in range(len(words) -2):
        pairs = (words[i], words[i + 1])
        print(pairs)
        # print(words[i], words[i + 1], words[i + 2])

    chains = {}
        
    chains[pairs] = next_word
    next_word = []
    
    print(chains)
    # print(make_chains)    

        # words[word] = words.get(word, 0) + 1
 
    # key = ()
    # value = []
    # print(key)
    # print(value)
    # for word in file_to_use:
    #     chains[word] = chains.get(word, 0) + 1


    # return chains

make_chains("green-eggs.txt")

def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
