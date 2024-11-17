from collections import defaultdict

# Definição dos nós prefixo
class PrefixTrieNode:
    def __init__(self):
        self.children = defaultdict(PrefixTrieNode)
        self.is_end_of_prefix = False

# Definição da árvore de prefixo
class PrefixTrie:
    def __init__(self, text):
        self.root = PrefixTrieNode()
        self.node_pointers = []  
        self.prefix_list = []  
        for i in range(1, len(text) + 1):
            self.insert_prefix(text[:i])
        self.compact_trie(self.root) 
    def insert_prefix(self, prefix):
        node = self.root
        for char in prefix:
            ascii_val = ord(char)
            node = node.children[ascii_val]
        node.is_end_of_prefix = True
        self.node_pointers.append(node)
        self.prefix_list.append(prefix)
        print(f"Inserção realizada: {prefix} (índice {len(self.node_pointers) - 1})")

    def compact_trie(self, node):
        for char, child in list(node.children.items()):
            self.compact_trie(child)
            if len(child.children) == 1 and not child.is_end_of_prefix:
                grandchild_char, grandchild_node = next(iter(child.children.items()))
                combined_char = chr(char) + chr(grandchild_char)
                node.children[ord(combined_char)] = grandchild_node
                del node.children[char]

    def search(self, pattern):
        node = self.root
        for char in pattern:
            ascii_val = ord(char)
            if ascii_val not in node.children:
                return False
            node = node.children[ascii_val]
        return node.is_end_of_prefix

    def display_prefixes(self):
        print("\nPrefixos armazenados no vetor:")
        for index, prefix in enumerate(self.prefix_list):
            print(f"Índice {index}: {prefix}")

    def display_text(self):
        print("\nExibição traduzida para texto:\n")
        self._display_recursive_text(self.root, "")

    def _display_recursive_text(self, node, prefix):
        if node.is_end_of_prefix:
            print(prefix)
        for ascii_val, child_node in node.children.items():
            self._display_recursive_text(child_node, prefix + chr(ascii_val))


# Teste com texto
with open("test.txt", "r", encoding="utf-8") as file:
    text = file.read()

prefix_trie = PrefixTrie(text)

# Exibindo vetor de prefixos
prefix_trie.display_prefixes()

# Testando buscas
print("\nResultados das buscas:")
print(prefix_trie.search("Oi"))
print(prefix_trie.search("Oi "))
print(prefix_trie.search("Oi  "))
print(prefix_trie.search("sou um texto"))
