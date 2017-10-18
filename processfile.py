import re

class ProcessFile:

    def __init__(self, name):
        self.file = open(name, 'r')
        self.string = self.file.read()
    def strip_string(self):
        self.stripped_string = re.sub('[^A-Za-z0-9 ]+', '', self.string)
        print(self.stripped_string)

f = ProcessFile("plik.txt")
f.strip_string()
