"""Word Finder: finds random words from a dictionary."""

from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary.
    
    >>> wf = WordFinder("words.txt")
    235886 words read

    >>> wf.word_count
    235886

    >>> isinstance(wf, WordFinder)
    True

    wf.random() this will return a random word from the list

    """
    
    def __init__(self, dictionary):
        """Create a dictionary, establish word count, return word count string"""
        self.dictionary = self.create_dictionary(dictionary)
        self.word_count = self.count_words()
        print(self.announce_count())
    
    def __repr__(self):
        return f"<WordFinder random word generator with {self.word_count} words>"

    def create_dictionary(self, dictionary):
        """reads the file path, opens file, adds each line to a word List, returns List"""
        words = open(f"{dictionary}", "r")
        word_list = []
        for line in words:
            word = line.strip()
            word_list.append(word)
        words.close()
        return word_list

    def count_words(self):
        """returns count of words in the file"""
        count = len(self.dictionary)
        return count
    
    def announce_count(self):
        """prepares a string with the word count"""
        return f"{self.word_count} words read"
    
    def random(self):
        """returns a random word from the word List, using random.choice() import"""
        return choice(self.dictionary)

class SpecialWordFinder(WordFinder):

    """Special Word Finder: finds random words from a dictionary when the base file contains comments and line breaks.
    
    >>> wf2 = SpecialWordFinder("words2.txt")
    4 words read

    >>> wf2.word_count
    4

    >>> isinstance(wf2, WordFinder)
    True

    >>> isinstance(wf2, SpecialWordFinder)
    True

    wf.random() this will return a random word from the list

    """

    def __init__(self, dictionary):
        super().__init__(dictionary)

    
    def create_dictionary(self, dictionary):
        """reads the file path, opens file, filters out comments and line breaks
        and adds each line to a word List, returns List"""
        words = open(f"{dictionary}", "r")
        word_list = []
        for line in words:
            word = line.strip()
            if len(word) > 0 and not word.startswith("#"): 
                word_list.append(word)
        words.close()
        return word_list
