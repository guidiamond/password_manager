class Search:
    def __init__(self, searched_word):
        self.searched_word = searched_word
    
    def linear_search(self, words_list):
        new_words_list = []
        for word in words_list:
            if self.searched_word in word:
                new_words_list.append(word)
        return new_words_list

    def select_file(self, files_list):
        for file in files_list:
            print(file + " " + "[" + str(files_list.index(file)) + "]")
