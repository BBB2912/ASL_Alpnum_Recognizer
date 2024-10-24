# trie_module.py

import nltk
from nltk.corpus import stopwords

# Download stopwords only once
nltk.download('stopwords', quiet=True)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def load_words(self, filePath="wlasl_class_list.txt"):
        with open(filePath, 'r') as file:
            lines = file.readlines()

            word_list = []
            for line in lines:
                word = line.strip()
                word_list.append(word)

        stopwords_set = set(stopwords.words('english'))
        words = word_list + list(stopwords_set)
        return set(words)

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def suggest(self, prefix, context):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []  # No suggestions found
            node = node.children[char]
        return self._get_words(node, prefix, context)

    def _get_words(self, node, prefix, context):
        words = []
        if node.is_word:
            words.append((prefix, self._calculate_rank(prefix, context)))
        for char, child_node in node.children.items():
            words.extend(self._get_words(child_node, prefix + char, context))
        return sorted(words, key=lambda x: (len(x[0]), -x[1]))[:10]

    def _calculate_rank(self, word, context):
        frequency = context.count(word)
        return frequency

# Create a trie and load words once
trie = Trie()
words = trie.load_words(r"C:\Users\MAHIREDDY\Desktop\Internships2024\Al-Zira\ASL_Alpnum_Recognizer\ASL_alnum_recognizer\nltk_words.txt")

for word in words:
    trie.insert(word)

if __name__=="__main__":
    print(len(words))
    
