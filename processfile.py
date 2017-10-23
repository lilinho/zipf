import re
from collections import Counter
import matplotlib.pyplot as plt
import string

class ProcessFile:

    def __init__(self, name):
        self.file = open(name, 'r', encoding="utf-8")
        self.string_in = self.file.read()
        self.file.close()
    def strip_string(self):
        translator = str.maketrans('', '', string.punctuation + '\u2013')
        self.stripped_string = self.string_in.translate(translator)
    def count_words(self):
        self.words = self.stripped_string.split()
        self.counted_words = Counter(self.words)
        self.counted_words = dict(self.counted_words.most_common(20))
        print(self.counted_words)
        return self.counted_words

class Plotter:

    def __init__(self, data):
        self.words = []
        self.counters = []
        for word, count in data.items():
            self.words.append(word)
            self.counters.append(count)

    def func(self, x, i):
        return x/i
    
    def draw_plot(self):

        xticks = self.words
        y2 = []
        for i in range(100):
            y2.append(self.counters[0]/(i+1))
        plt.figure(1)
        plt.subplot(211)
        plt.plot(self.words, self.counters, 'o')
        plt.show()
        """
        fig = plt.figure()
        pl = fig.add_subplot(111)
        pl.plot(self.counters, 'o')
        pl.set_xticklabels(self.words)
        fig.savefig("out.png")

        fig.show()
        """
f = ProcessFile("plik.txt")
f.strip_string()
plot = Plotter(f.count_words())
plot.draw_plot()
