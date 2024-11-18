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

    def char_to_binary(self, char):
        return format(ord(char), '08b')

    def insert_prefix(self, prefix):
        node = self.root
        binary_path = ''.join(self.char_to_binary(char) for char in prefix)
        for bit in binary_path:
            node = node.children[bit]
        node.is_end_of_prefix = True
        self.node_pointers.append(node)
        self.prefix_list.append(prefix)
        print(f"Inserção realizada: {prefix} (caminho binário: {binary_path})")

    def compact_trie(self, node):
        # Compactar a árvore recursivamente
        for char, child in list(node.children.items()):
            self.compact_trie(child)
            if len(child.children) == 1 and not child.is_end_of_prefix:
                grandchild_char, grandchild_node = next(iter(child.children.items()))
                combined_char = char + grandchild_char
                node.children[combined_char] = grandchild_node
                del node.children[char]

    def search(self, pattern):
        node = self.root
        binary_path = ''.join(self.char_to_binary(char) for char in pattern)
        for bit in binary_path:
            if bit not in node.children:
                return False
            node = node.children[bit]
        return node.is_end_of_prefix

    def remove_by_index(self, index):
        if index < 0 or index >= len(self.prefix_list):
            print(f"Índice {index} fora do intervalo.")
            return False

        prefix_to_remove = self.prefix_list[index]
        binary_path = ''.join(self.char_to_binary(char) for char in prefix_to_remove)
        print(f"Removendo prefixo no índice {index}: {prefix_to_remove} (caminho binário: {binary_path})")
        self._remove_from_trie(self.root, binary_path, 0)
        self.prefix_list[index] = None  
        return True

    def _remove_from_trie(self, node, binary_path, depth):
        if depth == len(binary_path):
            if node.is_end_of_prefix:
                node.is_end_of_prefix = False
            return len(node.children) == 0

        bit = binary_path[depth]
        if bit in node.children:
            can_delete = self._remove_from_trie(node.children[bit], binary_path, depth + 1)
            if can_delete:
                del node.children[bit]
        return len(node.children) == 0 and not node.is_end_of_prefix

    def display_prefixes(self):
        print("\nPrefixos armazenados no vetor:")
        for index, prefix in enumerate(self.prefix_list):
            status = "Removido" if prefix is None else prefix
            print(f"Índice {index}: {status}")

    def get_index(self, value):
        if value.isdigit():
            index = int(value)
            if index < len(self.prefix_list):
                return self.prefix_list[index]
            else:
                return f"Valor numérico {value} não encontrado na árvore."
        if value in self.prefix_list:
            return self.prefix_list.index(value)
        return -1

    def display_text(self):
        print("\nExibição traduzida para texto:\n")
        self._display_recursive_text(self.root, "")

    def _display_recursive_text(self, node, prefix):
        if node.is_end_of_prefix:
            print(prefix)
        for bit, child_node in node.children.items():
            self._display_recursive_text(child_node, prefix + bit)


# Teste com texto vindo de arquivo
with open("test.txt", "r", encoding="utf-8") as file:
    text = file.read()

prefix_trie = PrefixTrie(text)

prefix_trie.display_prefixes()

# Testando remoção
print("\nRemovendo elementos:")
prefix_trie.remove_by_index(1) 
prefix_trie.remove_by_index(5)  

prefix_trie.display_prefixes()
