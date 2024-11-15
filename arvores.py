# Definição dos nós prefixo
class PrefixTrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_prefix = False

# Definição da árvore de prefixo
class PrefixTrie:
    def __init__(self, text):
        self.root = PrefixTrieNode()
        for i in range(1, len(text) + 1):
            self.insert_prefix(text[:i]) 

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

    # Método para exibir a árvore em ASCII
    def display_ascii(self):
        print("Exibição em ASCII:")
        self._display_recursive_ascii(self.root, [])

    def _display_recursive_ascii(self, node, prefix):
        if node.is_end_of_prefix:
            print(" ".join(map(str, prefix))) 
        for ascii_val, child_node in node.children.items():
            self._display_recursive_ascii(child_node, prefix + [ascii_val])

    # Método para exibir a árvore traduzida para texto
    def display_text(self):
        print("Exibição traduzida para texto:")
        self._display_recursive_text(self.root, "")

    def _display_recursive_text(self, node, prefix):
        if node.is_end_of_prefix:
            print(prefix)
        for ascii_val, child_node in node.children.items():
            self._display_recursive_text(child_node, prefix + chr(ascii_val))


with open("test.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Testes com a árvore de prefixo
print("\nTestes dos prefixos\n")
prefix_trie = PrefixTrie(text)

# Exibição em ASCII
prefix_trie.display_ascii()

# Exibição traduzida para texto
prefix_trie.display_text()

# Testando buscas
print("\nResultados das buscas:")
print(prefix_trie.search("Oi"))
print(prefix_trie.search("Oi "))
print(prefix_trie.search("Oi  "))  
print(prefix_trie.search("sou um texto"))  
print(prefix_trie.search("Oi sou um teste, será que funcionou?"))  
print(prefix_trie.search("2019"))  
print(prefix_trie.search("Michigan"))
print(prefix_trie.search("The Incredible"))
