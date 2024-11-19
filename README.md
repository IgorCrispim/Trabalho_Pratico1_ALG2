# **Trabalho_Pratico1_ALG2**

## **Compact Binary Trie README**
### **Descrição**
####    Este projeto implementa uma Compact Binary Trie em Python, projetada para armazenar e manipular prefixos convertidos em formato binário. A estrutura oferece suporte a inserção, busca, remoção e análise estatística da árvore de maneira eficiente. A estrutura é útil para situações em que prefixos precisam ser organizados e manipulados em um formato compacto e eficiente, como compressão de dados ou aplicações de roteamento.

### **Funcionalidades**
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

### **Estrutura de Arquivo**
#### Classes Principais
##### CompactBinaryTrieNode:
###### Representa um nó na trie.
###### Atributos:
###### *children: Dicionário para armazenar os filhos;*
###### *index: Índice do prefixo armazenado.*
###### *is_end_of_prefix: Indica se é o fim de um prefixo.*
##### CompactBinaryTrie:
###### Controla a estrutura da trie e fornece métodos para manipulação e análise.

### **Métodos Principais**
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
###### *Número de nós na trie;*
###### *Espaço ocupado (em KB);*
###### *Tempo total de inserção.*

### **Requisitos:**
#### Python 3.8 ou superior
#### Biblioteca sys (inclusa no Python)


## **Lempel-Ziv-Welch**
### **Descrição :**
#### Este projeto implementa um algoritmo de compressão e descompressão baseado na estrutura de dados Compact Binary Trie. Ele utiliza conceitos de codificação baseados em LZW (Lempel-Ziv-Welch) para manipular cadeias de caracteres e reduzir o uso de memória. A implementação suporta modos de compressão com tamanho fixo e dinâmico de dicionário, além de gerar estatísticas úteis sobre o processo de compressão.

### **Funcionalidades**
#### Compressão:
##### Codifica um arquivo de entrada utilizando uma trie binária compacta;
##### Suporta tamanhos de dicionário fixos (até 12 bits) ou variáveis.
#### Descompressão:
##### Decodifica o arquivo comprimido, reconstruindo o texto original.
#### Inicialização de Dicionário:
##### Mapeamento de caracteres para índices (compressão);
##### Mapeamento de índices para caracteres (descompressão).
#### Estatísticas:
##### Memória usada pelo texto original e comprimido;
##### Taxa de compressão;
##### Validação de integridade do arquivo (compara texto original e descomprimido).

### **Estrutura de Arquivo**
#### Funções Principais
##### Compressão
###### compressao(entrada, bitsMaximo, variavel)
###### *entrada: Texto a ser comprimido;*
###### *bitsMaximo: Número máximo de bits para o tamanho do dicionário;*
###### *variavel: Define se o tamanho do dicionário é dinâmico (True) ou fixo (False);*
###### *Retorno: Arquivo comprimido como uma sequência de bytes.*
##### Descompressão
###### descompressao(comprimido, bitsMaximo, variavel)
###### *comprimido: Arquivo comprimido como uma sequência de bytes;*
###### *bitsMaximo: Número máximo de bits para o tamanho do dicionário;*
###### *variavel: Define se o tamanho do dicionário é dinâmico (True) ou fixo (False);*
###### *Retorno: Texto descomprimido como uma string.*
##### Inicialização de Dicionário
###### inicializaDicionario(arvore)
###### inicializaDicionarioInverso(arvore)
###### *Inicializam os dicionários de compressão e descompressão com os 256 caracteres ASCII.*

### **Como Usar**
#### Executar Compressão:
##### python script.py arquivo.txt [bitsMaximo]
###### arquivo.txt: Caminho do arquivo de texto a ser comprimido;
###### bitsMaximo (opcional): Número máximo de bits do dicionário (padrão: 12).

### **Requisitos** 
#### Python 3.8 ou superior
#### Arquivo arvores.py contendo a classe CompactBinaryTrie (implementação separada).

### **Observações**
#### A implementação pode ser estendida para incluir suporte a arquivos binários e métodos avançados de análise estatística.
#### Para realizar testes e armazenar as estatísticas, modifique o script para salvar as métricas em um arquivo de log.

## Índice
- [Sobre](#sobre)

