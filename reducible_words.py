__author__ = 'qi'

#A program to find all words that remain a valid English word, as you remove its letters one at a time
#Currently working on optimizing the algorithm

def compile_word(filename):
    word_list = []
    for line in open(filename):
        t = line.strip().lower()
        word_list.append(t)
    word_list.extend(["i","a",""])
    word_dict = dict(zip(word_list, range(len(word_list))))
    return word_dict

def gather_childern(word, word_dict):
    children_list = []
    for i in range(len(word)):
        t = list(word)
        del t[i]
        s = "".join(t)
        if s in word_dict:
            children_list.append(s)
    children_dict = dict(zip(children_list, range(len(children_list))))
    return children_list

global reducible_dict
reducible_dict = {'':0}

def reducible(word, word_dict):
    if word in reducible_dict:
        return True
    else:
        children_list = gather_childern(word, word_dict)
        for children in children_list:
            if reducible(children, word_dict):
                reducible_dict[word] = 0
                return True
        return False

if __name__ == '__main__':
    word_dict = compile_word("words.txt")
    for keys in word_dict:
        reducible(keys, word_dict)
    word_list = []
    for words in reducible_dict:
        word_list.append((len(words), words))
    word_list.sort(reverse=True)
    print word_list