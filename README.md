# Trabalho_Pratico1_ALG2

## Compact Binary Trie README
### Descrição
####    Este projeto implementa uma Compact Binary Trie em Python, projetada para armazenar e manipular prefixos convertidos em formato binário. A estrutura oferece suporte a inserção, busca, remoção e análise estatística da árvore de maneira eficiente. A estrutura é útil para situações em que prefixos precisam ser organizados e manipulados em um formato compacto e eficiente, como compressão de dados ou aplicações de roteamento.

### Funcionalidades
#### Conversão de Caracteres em Binário:
##### Cada caractere é representado como um caminho de 8 bits usando a tabela ASCII.
#### Inserção de Prefixos:
##### Os prefixos são convertidos para binário e armazenados na trie;
##### O tempo de inserção é calculado e acumulado para estatísticas.
#### Busca de Padrões:
##### Permite buscar se um padrão (prefixo) existe na trie, retornando seu índice correspondente.
#### Exibição de Prefixos:
##### Lista todos os prefixos armazenados e indica aqueles removidos.
#### Remoção por Índice:
##### Remove um prefixo da trie baseado no índice armazenado na lista.
#### Estatísticas da Árvore:
##### Total de nós;
##### Espaço estimado ocupado (em KB);
##### Número de prefixos armazenados;
##### Tempo total gasto na inserção.

### Estrutura de Arquivo
#### Classes Principais
##### CompactBinaryTrieNode:
###### Representa um nó na trie.
###### Atributos:
###### children: Dicionário para armazenar os filhos;
###### index: Índice do prefixo armazenado.
###### is_end_of_prefix: Indica se é o fim de um prefixo.
##### CompactBinaryTrie:
###### Controla a estrutura da trie e fornece métodos para manipulação e análise.

### Métodos Principais
#### Inserção
##### insert_prefix(prefix, index)
###### Insere um prefixo na trie em formato binário.
#### Busca
##### search(pattern)
###### Retorna o índice do prefixo se encontrado, ou None.
#### Remoção
##### remove_by_index(index)
###### Retorna True se removido com sucesso, False caso contrário.
#### Estatísticas
##### get_tree_statistics()
###### Calucula e exibe :
###### Número de nós na trie;
###### Espaço ocupado (em KB);
###### Tempo total de inserção.

### Exemplos de uso:
####  Instanciar a trie
#### trie = CompactBinaryTrie()

#### Inserir prefixos
#### trie.insert_prefix("AB", 0)
#### trie.insert_prefix("CD", 1)

#### Buscar prefixos
#### print(trie.search("AB"))  # Output: 0
#### print(trie.search("EF"))  # Output: None

#### Exibir prefixos armazenados
#### trie.display_prefixes()

#### Remover prefixo pelo índice
#### trie.remove_by_index(0)

#### Exibir estatísticas da árvore
#### trie.get_tree_statistics()





