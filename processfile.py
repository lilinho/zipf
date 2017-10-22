import re
from collections import Counter
import matplotlib.pyplot as plt

class ProcessFile:

    def __init__(self, name):
        self.file = open(name, 'r')
        self.string = self.file.read()
    def strip_string(self):
        self.stripped_string = re.sub('[^A-Za-z0-9 ]+', ' ', self.string, re.UNICODE)
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


    def draw_plot(self):

        y2 = []
        for i in range(len(self.counters)):
            y2.append(self.counters[i]/(i+1))

        fig = plt.figure()
        pl = fig.add_subplot(111)
        pl.plot(self.counters, 'o')
        pl.set_xticklabels(self.words)
        pl.plot(y2)

        #plt.plot(self.words, self.counters)
        #pl.show()
        fig.show()
        
f = ProcessFile("plik.txt")
f.strip_string()
plot = Plotter(f.count_words())
plot.draw_plot()
