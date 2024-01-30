from wordfinder import WordFinder

class TheRandomWordFinder(WordFinder):
    def __init__ (self,filepath):
        super().__init__(filepath);

    def make_list_of_words(self,file):
        wordList = [];
        for line in file:
            line.strip();
            # how to eliminate the empty lines ?
            if len(line) != 1:  
                wordList.append(line);
                print (len(line));
        return wordList;