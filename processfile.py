import re
from collections import Counter

class ProcessFile:

    def __init__(self, name):
        self.file = open(name, 'r')
        self.string = self.file.read()
    def strip_string(self):
        self.stripped_string = re.sub('[^A-Za-z0-9 ]+', ' ', self.string)
    def count_words(self):
        self.words = self.stripped_string.split()
        self.counted_words = Counter(self.words)
        print(self.counted_words)
        
f = ProcessFile("plik.txt")
f.strip_string()
f.count_words()
