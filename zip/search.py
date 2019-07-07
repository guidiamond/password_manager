class Search:
    def __init__(self, search_word):
        self.search_word = search_word
    
    def linear_search(self, words_list):
        new_words_list = []
        for word in words_list:
            if self.search_word in word:
                new_words_list.append(word)
        return new_words_list