class CompactBinaryTrieNode:
    def __init__(self):
        self.children = {} 
        self.is_end_of_prefix = False
        self.index = None  

class CompactBinaryTrie:
    def __init__(self, text):
        self.root = CompactBinaryTrieNode()
        self.prefix_list = []
        self.index_counter = 256  
        for i in range(1, len(text) + 1):
            self.insert_prefix(text[:i])

    def char_to_binary(self, char):
        return format(ord(char), '08b')

    def insert_prefix(self, prefix):
        node = self.root
        binary_path = ''.join(self.char_to_binary(char) for char in prefix)

        for bit in binary_path:
            if bit not in node.children:
                node.children[bit] = CompactBinaryTrieNode()
            node = node.children[bit]

        if not node.is_end_of_prefix:
            node.is_end_of_prefix = True
            node.index = self.index_counter  
            self.index_counter += 1  

        self.prefix_list.append(prefix)
        print(f"Inserção realizada: {prefix} (caminho binário: {binary_path})")

    def search(self, pattern):
        node = self.root
        binary_path = ''.join(self.char_to_binary(char) for char in pattern)

        for bit in binary_path:
            if bit not in node.children:
                return None  
            node = node.children[bit]

        return node.index if node.is_end_of_prefix else None

    def display_prefixes(self):
        print("\nPrefixos armazenados na árvore:")
        for index, prefix in enumerate(self.prefix_list):
            status = "Removido" if prefix is None else prefix
            print(f"Índice {index}: {status}")

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
                node.index = None  
            return len(node.children) == 0

        bit = binary_path[depth]
        if bit in node.children:
            can_delete = self._remove_from_trie(node.children[bit], binary_path, depth + 1)
            if can_delete:
                del node.children[bit]

        return len(node.children) == 0 and not node.is_end_of_prefix


# Lendo texto do arquivo
def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Arquivo de texto
file_path = "test.txt"
text = read_file(file_path)

# Criando a trie compacta em binário
compact_binary_trie = CompactBinaryTrie(text)

# Exibindo os prefixos inseridos
compact_binary_trie.display_prefixes()

# Testando busca
print("\nResultados das buscas:")
print(f"Buscando 'Oi': {compact_binary_trie.search('Oi')}")
print(f"Buscando 'Oi  ': {compact_binary_trie.search('Oi  ')}")
print(f"Buscando 'Oi sou um teste,': {compact_binary_trie.search('Oi sou um teste,')}")

# Testando remoção
print("\nRemovendo elementos:")
compact_binary_trie.remove_by_index(1)
compact_binary_trie.remove_by_index(5)

# Exibindo os prefixos após remoção
compact_binary_trie.display_prefixes()
