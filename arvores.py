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
        self.index_counter = 0  
        for i in range(1, len(text) + 1):
            self.insert_prefix(text[:i])
        self.compact_trie(self.root)

    def insert_prefix(self, prefix):
        node = self.root
        for char in prefix:
            ascii_val = ord(char)
            node = node.children[ascii_val]
        node.is_end_of_prefix = True
        self.index_counter += 1
        print(f"Inserção realizada: índice {self.index_counter}")

    def search(self, pattern):
        node = self.root
        for char in pattern:
            ascii_val = ord(char)
            if ascii_val not in node.children:
                return False
            node = node.children[ascii_val]
        return node.is_end_of_prefix

    def display_ascii(self):
        print("\nExibição em ASCII:\n")
        self._display_recursive_ascii(self.root, [])

    def _display_recursive_ascii(self, node, prefix):
        if node.is_end_of_prefix:
            print(" ".join(map(str, prefix)))
        for ascii_val, child_node in node.children.items():
            self._display_recursive_ascii(child_node, prefix + [ascii_val])

    def display_text(self):
        print("\nExibição traduzida para texto:\n")
        self._display_recursive_text(self.root, "")

    def _display_recursive_text(self, node, prefix):
        if node.is_end_of_prefix:
            print(prefix)
        for ascii_val, child_node in node.children.items():
            self._display_recursive_text(child_node, prefix + chr(ascii_val))

    def compact_trie(self, node):
        for ascii_val, child in list(node.children.items()):
            self.compact_trie(child)
            if len(child.children) == 1 and not child.is_end_of_prefix:
                next_ascii_val, next_node = next(iter(child.children.items()))
                node.children[ascii_val * 256 + next_ascii_val] = next_node
                del node.children[ascii_val]

    def remove_invalid_nodes(self):
        print("\nRemovendo nós inválidos...")
        self._remove_invalid_nodes_recursive(self.root)

    def _remove_invalid_nodes_recursive(self, node):
        invalid_keys = [ascii_val for ascii_val in node.children if ascii_val < 0 or ascii_val > 255]
        for key in invalid_keys:
            del node.children[key]
        for child_node in node.children.values():
            self._remove_invalid_nodes_recursive(child_node)


# Teste com texto
with open("test.txt", "r", encoding="utf-8") as file:
    text = file.read()

prefix_trie = PrefixTrie(text)

# Exibição antes e após a remoção
prefix_trie.display_ascii()
prefix_trie.display_text()

prefix_trie.remove_invalid_nodes()

prefix_trie.display_ascii()
prefix_trie.display_text()

# Testando buscas
print("\nResultados das buscas:\n")
print(prefix_trie.search("Oi"))
print(prefix_trie.search("Oi "))
print(prefix_trie.search("Oi  "))
print(prefix_trie.search("sou um texto"))
print(prefix_trie.search("Oi sou um teste, será que funcionou?"))
