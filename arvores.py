# Definição dos nós sufixo
class SuffixTrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_suffix = False

# Definição da árvore de sufixo
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
            ascii_val = ord(char)  
            if ascii_val not in node.children:
                node.children[ascii_val] = SuffixTrieNode()
            node = node.children[ascii_val]
        node.is_end_of_suffix = True

    def search(self, pattern):
        node = self.root
        for char in pattern:
            ascii_val = ord(char)
            if ascii_val not in node.children:
                return False
            node = node.children[ascii_val]
        return node.is_end_of_suffix

    def display(self):
        self._display_recursive(self.root, [])

    def _display_recursive(self, node, prefix):
        if node.is_end_of_suffix:
            print(" ".join(map(str, prefix)))  
        for ascii_val, child_node in node.children.items():
            self._display_recursive(child_node, prefix + [ascii_val])  

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
            ascii_val = ord(char)
            if ascii_val not in node.children:
                node.children[ascii_val] = PrefixTrieNode()
            node = node.children[ascii_val]
        node.is_end_of_prefix = True

    def search(self, pattern):
        node = self.root
        for char in pattern:
            ascii_val = ord(char)
            if ascii_val not in node.children:
                return False
            node = node.children[ascii_val]
        return node.is_end_of_prefix

    def display(self):
        self._display_recursive(self.root, [])

    def _display_recursive(self, node, prefix):
        if node.is_end_of_prefix:
            print(" ".join(map(str, prefix))) 
        for ascii_val, child_node in node.children.items():
            self._display_recursive(child_node, prefix + [ascii_val])


with open("test.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Testes com a árvore de prefixo
print("\nTestes dos prefixos (em ASCII)\n")
prefix_trie = PrefixTrie(text)
prefix_trie.display()
print(prefix_trie.search("Incredible"))  
print(prefix_trie.search("Incr"))  
print(prefix_trie.search("ble"))  
print(prefix_trie.search("2019"))  
print(prefix_trie.search("Michigan"))

# Testes com a árvore de sufixo
print("\nTestes dos sufixos (em ASCII)\n")
suffix_trie = SuffixTrie(text)
suffix_trie.display()
print(suffix_trie.search("Incredible"))  
print(suffix_trie.search("Incr"))  
print(suffix_trie.search("ble")) 
print(suffix_trie.search("2019"))
print(suffix_trie.search("Michigan"))
