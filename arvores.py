import sys

class CompactBinaryTrieNode:
    def __init__(self):
        self.children = {}  
        self.is_end_of_prefix = False
        self.index = None  

class CompactBinaryTrie:
    def __init__(self):
        self.root = CompactBinaryTrieNode()
        self.prefix_list = []
        self.num_inserts = 0  
        self.total_insertion_time = 0 

    def char_to_binary(self, char):
        return format(ord(char), '08b')

    def insert_prefix(self, prefix, index):
        node = self.root
        binary_path = ''.join(self.char_to_binary(char) for char in str(prefix))

        for bit in binary_path:
            if bit not in node.children:
                node.children[bit] = CompactBinaryTrieNode()
            node = node.children[bit]

        if not node.is_end_of_prefix:
            node.is_end_of_prefix = True
            node.index = index  

        self.prefix_list.append(str(prefix))
        self.num_inserts += 1

    def search(self, pattern):
        node = self.root
        binary_path = ''.join(self.char_to_binary(char) for char in str(pattern))

        for bit in binary_path:
            if bit not in node.children:
                return None
            node = node.children[bit]

        end_time = time.time()
        #print(f"Tempo de busca para '{pattern}': {end_time - start_time:.6f} segundos")
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
        if prefix_to_remove is None:
            print(f"Índice {index} já foi removido.")
            return False

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

    def get_tree_statistics(self):
        # Calcula o número de nós e o espaço ocupado pela árvore
        num_nodes = self.count_nodes(self.root)
        space_usage = self.calculate_space_usage(self.root)
        space_occupied = space_usage / (1024)
        return num_nodes,space_occupied,self.num_inserts

    def count_nodes(self, node):
        # Conta o número de nós na árvore
        num_nodes = 1  
        for child in node.children.values():
            num_nodes += self.count_nodes(child)
        return num_nodes

    def calculate_space_usage(self, node):
        # Estima o espaço usado pela árvore
        node_size = sys.getsizeof(node) 
        children_size = sum(self.calculate_space_usage(child) for child in node.children.values())  
        return node_size + children_size


# Lendo texto do arquivo
#def read_file(file_path):
    #with open(file_path, "r", encoding="utf-8") as file:
        #return file.read()

# Arquivo de texto
#file_path = "test.txt"
#text = read_file(file_path)

# Criando a trie compacta em binário
#compact_binary_trie = CompactBinaryTrie()

# Inserindo prefixos com índices específicos
#compact_binary_trie.insert_prefix('Oi', 1)
#compact_binary_trie.insert_prefix('Oi sou', 2)
#compact_binary_trie.insert_prefix('Oi sou um', 3)
#compact_binary_trie.insert_prefix('Oi sou um teste', 4)

# Exibindo os prefixos inseridos
#compact_binary_trie.display_prefixes()

# Testando busca
#print("\nResultados das buscas:")
#print(f"Buscando 'Oi': {compact_binary_trie.search('Oi')}")
#print(f"Buscando 'Oi sou': {compact_binary_trie.search('Oi sou')}")
#print(f"Buscando 'Oi sou um teste,': {compact_binary_trie.search('Oi sou um teste,')}")

# Exibindo as estatísticas da árvore
#compact_binary_trie.get_tree_statistics()

# Testando remoção
#print("\nRemovendo elementos:")
#compact_binary_trie.remove_by_index(1)
#compact_binary_trie.remove_by_index(3)

# Exibindo os prefixos após remoção
#compact_binary_trie.display_prefixes()
