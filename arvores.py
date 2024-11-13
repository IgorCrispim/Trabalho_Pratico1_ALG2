#Definição dos nós sufixo
class SuffixTrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_suffix = False
#Definição da arvore de sufixo 
class SuffixTrie:
    def __init__(self, text):
        self.root = SuffixTrieNode()
        words = text.split()
        for word in words:
            for i in range(len(word)):
                self.insert_suffix(word[i:])

    def insert_suffix(self, suffix):
        node = self.root
        for char in suffix:
            if char not in node.children:
                node.children[char] = SuffixTrieNode()
            node = node.children[char]
        node.is_end_of_suffix = True

    def search(self, pattern):
        node = self.root
        for char in pattern:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_suffix

    def display(self):
        self._display_recursive(self.root, "")

    def _display_recursive(self, node, prefix):
        if node.is_end_of_suffix:
            print(prefix)
        for char, child_node in node.children.items():
            self._display_recursive(child_node, prefix + char)

# Definição dos nós prefixo
class PrefixTrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_prefix = False

# Definição da árvore de prefixo
class PrefixTrie:
    def __init__(self, text):
        self.root = PrefixTrieNode()
        words = text.split()
        for word in words:
            for i in range(1, len(word) + 1):
                self.insert_prefix(word[:i])

    def insert_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                node.children[char] = PrefixTrieNode()
            node = node.children[char]
        node.is_end_of_prefix = True

    def search(self, pattern):
        node = self.root
        for char in pattern:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_prefix

    def display(self):
        self._display_recursive(self.root, "")

    def _display_recursive(self, node, prefix):
        if node.is_end_of_prefix:
            print(prefix)
        for char, child_node in node.children.items():
            self._display_recursive(child_node, prefix + char)


text = "banana bobora nabat"
print("\ntestes dos prefixos\n")
prefix_trie = PrefixTrie(text)
prefix_trie.display()
print(prefix_trie.search("ban"))  
print(prefix_trie.search("bob"))  
print(prefix_trie.search("nab"))  
print(prefix_trie.search("bat"))  
print(prefix_trie.search("ora"))

print("\nteste dos prefixos\n")
print("")
suffix_trie = SuffixTrie(text)
suffix_trie.display()
print(suffix_trie.search("ana"))  
print(suffix_trie.search("bat"))  
print(suffix_trie.search("ora")) 
print(suffix_trie.search("obora"))
print(suffix_trie.search("otra"))  


