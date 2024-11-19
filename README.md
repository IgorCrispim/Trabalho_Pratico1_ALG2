# **Trabalho Prático 1 - Algoritmos 2**

![GitHub top language](https://img.shields.io/github/languages/top/IgorCrispim/Trabalho_Pratico1_ALG2)
![GitHub last commit](https://img.shields.io/github/last-commit/IgorCrispim/Trabalho_Pratico1_ALG2)
![License](https://img.shields.io/badge/license-MIT-blue)

## **Compact Binary Trie**

### **Descrição**
Este projeto implementa uma **Compact Binary Trie** em Python, projetada para armazenar prefixos convertidos em binário. A estrutura suporta:
- Inserção e busca de prefixos.
- Remoção de prefixos por índice.
- Geração de estatísticas como tempo de execução e espaço ocupado.

A trie é útil em cenários como compressão de dados ou aplicações de roteamento, onde prefixos precisam ser organizados de forma compacta.

---

### **Funcionalidades**
1. **Conversão para Binário:**
   - Cada caractere é convertido em um caminho de 8 bits usando a tabela ASCII.
2. **Inserção:**
   - Insere prefixos na trie em formato binário e calcula o tempo de execução.
3. **Busca:**
   - Verifica se um padrão (prefixo) existe e retorna seu índice correspondente.
4. **Remoção:**
   - Remove um prefixo com base no índice.
5. **Estatísticas:**
   - Relata o número total de nós, espaço ocupado (em KB) e tempo de execução.

---

### **Estrutura de Arquivo**
| Classe                   | Função                                             |
|--------------------------|----------------------------------------------------|
| `CompactBinaryTrieNode`  | Representa os nós da trie.                         |
| `CompactBinaryTrie`      | Controla a manipulação e análise da estrutura.     |

**Atributos principais de `CompactBinaryTrieNode`:**
| Atributo         | Descrição                                     |
|------------------|-----------------------------------------------|
| `children`       | Dicionário que armazena os filhos do nó.      |
| `index`          | Índice do prefixo armazenado.                 |
|`is_end_of_prefix`| Indica se o nó é o fim de um prefixo.         |

### **Requesitos**
1. Python 3.8 ou superior
2. Biblioteca sys (inclusa no Python)

---

## **Lempel-Ziv-Welch**

### **Descrição**
Implementação do algoritmo **LZW** para compressão e descompressão de arquivos, utilizando a Compact Binary Trie como base. Este algoritmo permite:
- Reduzir o tamanho de arquivos por meio de codificação eficiente.
- Reconstruir o texto original de arquivos comprimidos.
- Gerar estatísticas detalhadas sobre compressão e descompressão.

---

### **Funcionalidades**
1. **Compressão:**
   - Codifica um arquivo de entrada utilizando uma Compact Binary Trie.
   - Suporta tamanhos de dicionário fixos (até 12 bits) ou dinâmicos.
2. **Descompressão:**
   - Decodifica o arquivo comprimido e reconstrói o texto original.
3. **Estatísticas:**
   - Calcula a memória usada, a taxa de compressão e valida a integridade do arquivo.

---

### **Requesitos**
1. Python 3.8 ou superior
2. Arquivo arvores.py contendo a implementação da classe CompactBinaryTrie.

### **Observações**
1. A implementação pode ser estendida para incluir suporte a arquivos binários e métodos avançados de análise estatística.
2. Para armazenar estatísticas, modifique o script para salvar as métricas em um arquivo de log.

