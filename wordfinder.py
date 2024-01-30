"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    
    def __init__(self,filepath):
        file = open(filepath,"r")
        self.lst = self.make_list_of_words(file);
        print(f"{len(self.lst)} words read");
        file.close();

    def make_list_of_words(self,file):
        wordList = [];
        for line in file:
            wordList.append(line);
        return wordList;
    
    def random(self):
        str = choice(self.lst);
        list1 = list(str)[:-1];
        return "".join(list1);

