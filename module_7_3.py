from pprint import pprint
import io

class WordsFinder:
    file_names = ''

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                file = file.read().lower()
                words = []
                punc = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for p in punc:
                    file = file.replace(p, '')
                    words = file.split()
                all_words[file_name] = words
            return all_words

    def find(self, word):
        res = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                res[key] = value.index(word.lower()) + 1
        return res

    def count(self, word):
        res_ = {}
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            res_[value] = words_count
        return res_








finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего