class TrieNode:
    def __init__(self):
        self.children = {}
        self.Last = False

class spell_checker:
    
    
    def __init__(self, file_path):
        """it take the file path as input to store the whole text into trie data structure.
        """
        self.root = TrieNode()
        with open(file_path) as f:
            for line in f:
                word = line.strip().lower()
                self.add_word(word)


    
    def add_word(self, word):
        """it adds a new word to the trie 
            Time complexity: O(n)

        Args:
            word (string): word to be added to the trie
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.Last = True
        
        
    def find_nearest_words(self, word):
        """if the word that pass is in the trie it returns it 
           if not it return the nearest 4 word to it.
           Time complexity: O(n)
        Returns:
            list: it holds the word if it exists in the trie and if not it return the nearest 4 words to it 
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return self.get_nearest_words(word, node)
                
            node = node.children[char]
        if node.Last:
            return [word]
        return self.get_nearest_words(word, node)

    def get_nearest_words(self, word, node):
        nearest_words = []
        stack = [(node, word)]
        while stack and len(nearest_words) < 4:
            node, word = stack.pop()
            if node.Last:
                nearest_words.append(word)
            for char, child in node.children.items():
                stack.append((child, word+char))
        return nearest_words

    
    
    
    
checking = spell_checker("dictionary.txt")

# try a findaa word
print(checking.find_nearest_words("findaa"))

# add it to the trie
checking.add_word("findaa")

# now it just return the actual word
print(checking.find_nearest_words("findaa"))
