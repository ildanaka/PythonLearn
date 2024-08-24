import re

class WordsFinder:
    all_files = {}

    def __init__(self, *args):
        self.all_files = args


    def get_all_words(self):
        all_words = {}
        for fileName in self.all_files:
            with open(fileName, 'r') as file:
                content: str = file.read()
                all_words[file.name] = re.split(r'[,\.\=\!\?\;\:\-\s]+', content.lower())
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        for key, values in all_words.items():
            for w in values:
                if word in w:
                    index = values.index(w)
                    return {key: index}

    def count(self, word):
        all_words = self.get_all_words()
        for key, values in all_words.items():
            for w in values:
                if word in w:
                    len_ = len(values)
                    return {key: len_}


finder = WordsFinder('file1.txt', 'file2.txt', 'file3.txt')
print(finder.find('word'))
print(finder.count('word'))

