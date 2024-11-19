# **Trabalho Prático 1 - Algoritmos 2**

![GitHub top language](https://img.shields.io/github/languages/top/IgorCrispim/Trabalho_Pratico1_ALG2)
![GitHub last commit](https://img.shields.io/github/last-commit/IgorCrispim/Trabalho_Pratico1_ALG2)
![License](https://img.shields.io/badge/license-MIT-blue)

O presente programa tem como objetivo a criação de um compressor e descompressor de arquivo utilizando o método Lempel-Ziv-Welch de compressão. Para isso, foi criado um algoritmo utilizando a linguagem Python e uma estrutura de dados de árvore de prefixo, permitindo a compressão de qualquer tipo de arquivo.

## **Lempel-Ziv-Welch**

### **Descrição**
Implementação do algoritmo **LZW** para compressão e descompressão de arquivos, utilizando a Compact Binary Trie como dicionário para realizar inserção e busca dos elementos. Este algoritmo permite:
- Reduzir o tamanho de arquivos por meio de codificação eficiente, utilizando códigos que indicam sequências de caracteres do texto para codifica-los e reduzir o espaço ocupado na memória com um conjunto de bits que o representa.
- Reconstruir o texto original de arquivos comprimidos, utilizando um sistesma inverso da compressão ao a partir dos códigos chegar aos valores armazenados na arvore durante a compressão sem ter acesso a essa árvore.
- Gerar estatísticas detalhadas sobre compressão e descompressão, como o tempo de execução e a variação da taxa de compressão durante o processo

---

### **Funcionalidades**
1. **Compressão:**
   - Codifica um arquivo de entrada lendo caractere por caractere e gerando uma codificação para as sequencias de caracteres que se repetem no texto, permitindo a redução do espaço ocupado na memória
   - A compressão pode ser realizada utilizando uma quantidade de bits dos códigos váriavel ou fixo. Nesse caso, quando é variável a quantidade de bits dos códigos irá variar conforme a necessidade do código entre 8 e a quantidade máxima de bits definida, enquanto na variável todos os códigos possuíram exatamente 12 bits. Caso não seja escolhida uma quantidade máxima de bits no caso variavel, será imposto que a quantidade máxima de bits será 12. 
2. **Descompressão:**
   - Decodifica o arquivo comprimido e reconstrói o texto original baseado no arquivo binário de entrada. A decoficação é feita lendo cada código sequencialmente do arquivo de entrada e definindo qual string deveria representar aquela entrada de código, assim gerando o arquivo de saída descomprimido. Para funcionamento correto, deve-se enviar para a descompressão a mesma quantidade máxima de bits e o mesmo modo de armazenamente de bits (variável ou fixo), gerando erro caso isso não seja feito corretamente. 
3. **Estatísticas:**
   - Caso o sistema esteja em modo de teste, ele irá calcular a variação da compressão do arquivo a cada caractere da string, memória usada na árvore, tempo total de execução e outras estatísticas úteis para a verificação da integradade da codificação. Os dados computados são tratados pelo sistema para gerar um gráfico sobre a variação da taxa de compressão e descompressão, além de uma tabela indicando as estatísticas finais mais importantes do processo de compressão ou descompressã
---

### **Decisões de projeto**
- Na implementação da compressão e descompressão limitada pela quantidade de bits começa a existir um problema quando é criado um novo código no qual precisaria de uma quantidade de bits maior que o máximo estabelecido. Nesse caso, foi decidido que o programa pararia de adicionar novas cadeias ao dicionário, assim comprimindo o resto do arquivo com a árvore criada até o momento sem inserir novas cadeias.

### **Saída dos arquivos**

- Na compressão o arquivo no formato binário será colocado na pasta Arquivos comprimidos
- Na descompressão o arquivo no formato txt será colocado na pasta Arquivos descomprimidos

### **Requesitos**
1. Python 3.8 ou superior
2. Biblioteca Compact Binary Trie (inclusa no projeto
3. Biblioteca do Python time
4. Biblioteca do Python sys

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

## **Como utilizar**

   Para executar o algoritmo será compilado o arquivo main.py adicionando os seguintes parametros na linha de comando:
'''python
main.py [-h] [-c] [-d] [-v] [-f] [-t] [max_bits] nome_arquivo
'''

Dado essa entrada, cada variável representa o seguinte conceito no programa

- -h: O comando indica Help, descrevendo separadamente o que significa cada parametro da entrada
- -c: A opção define que será realizado a compressão do arquivo
- -d: A opção define que será realizado uma descompressão do arquivo de entrada. O algoritmo não permite que não seja definido se ira utilizar compressão e descompressão
- -v: A opção define que será utilizado uma quantidade de bits dos códigos variável 
- -f: A opção define que será utilizado uma quantidade de bits dos códigos fixo. o Algoritmo não permite que não seja definido se a quantidade será variável ou fixa
- -t: A opção indica que o sitema funcionará em modo de teste, assim gerando valores de teste do algoritmo
- -max_bits: Recebe a quantidade de bits máxima na compressão/descompressão. Caso não seja informado será utilizado o padrão que é 12 bits
- -nome_arquivo: Recebe obrigatoriamente o nome do arquivo a ser descomprimido/comprimido. Caso não seja informada, o sistema indicará erro

## **Análise dos Testes **

   Dado o programa funcional foi realizado alguns testes em diferentes tipos de arquivo para demonstrar o funcionamento e a qualidade do algoritmo de compressão. A cada teste um script automático adiciona os dados analisados no Readme, gerando os testes representados nos relatórios da pasta "Dados de Teste". Dado os dados de teste, foi possível fazer a seguinte análise sobre o funciomento do programa:

