from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
import string

class ProcessFile:

    def __init__(self, name):
        self.file = open(name, 'r', encoding="utf-8")
        self.string_in = self.file.read()
        self.file.close()
    def strip_string(self):
        translator = str.maketrans('', '', string.punctuation + '\u2013')
        self.stripped_string = self.string_in.translate(translator)
        self.stripped_string = self.stripped_string.lower()
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

        #x_data = np.arange(0, len(self.words), 0.1 )
        x_data = np.linspace(0, 20, num=100, endpoint=True)
        
        y2 = []
        for i in range(len(x_data)):
            y2.append(self.counters[0]/(i+1))
        f = interp1d(x_data, y2, kind='cubic')
        plt.plot(self.counters, 'o', label="Number of occurences")
        plt.plot(x_data, y2, label="Number of occurences according to Zipf Law")
        plt.xticks(range(len(self.words)), self.words, rotation=50, horizontalalignment='right')
        plt.xlabel('First 20 words')
        plt.ylabel('Number of appearance of each word')
        plt.title("Top 20 most common words")
        plt.legend()
        plt.savefig("out.png")
        plt.show()
        
f = ProcessFile("plik.txt")
f.strip_string()
plot = Plotter(f.count_words())
plot.draw_plot()
