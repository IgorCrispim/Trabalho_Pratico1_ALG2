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
- Na implementação da compressão exista um problema gerado por valores da string original que não estavam na tabela ASCII, assim gerando erro. Por isso, foi escolhido substituir qualquer valor fora da tabela ASCII como " ", assim permitindo a compressão correta dos valores.

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
   - Relata o número total de nós, espaço ocupado (em KB) e número de prefixos adicionado

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


## **Relatório**

### **Descrição**

Este projeto implementa uma script de relatório em Python, projetada para gerar automaticamente o Readme com as estatísticas geradas pelo teste. A estrutura suporta:
- Criação de uma tabela com as estatísticas principais da compressão e descompressãol.
- Criação do gráfico da taxa de compressão ao longo do tempo.
- Geração de um arquivo markdown apresentado esses dados estatísticos.

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

---

## **Análise dos Testes **

   Dado o programa funcional foi realizado alguns testes em diferentes tipos de arquivo para demonstrar o funcionamento e a qualidade do algoritmo de compressão. A cada teste um script automático adiciona os dados analisados no Readme, gerando os testes representados nos relatórios da pasta "Dados de Teste". Dado os dados de teste, foi possível fazer a seguinte análise sobre o funciomento do programa:

### **Compressão e descompressão de Livro em txt com bit variavel de 12**

   Como primeiro teste foi analisado o funcionamento da compressão e descompressão em arquivos de texto. Para isso, foi pego um livro no site do [Projeto Gutenberg](https://www.gutenberg.org/cache/epub/52847/pg52847-images.html). Baixando o arquivo em txt e analisando via teste com 12 bits variável foi possível chegar aos resultados do [relatorio gerado](Dados_teste/Relatorio_de_testes_Compressao_variavel_12_livro.md)

   Observando os dados, percebe-se pelas estatísticas que a compressão funcionou bem, fazendo a compressão de um livro de tamanho extenso em 17 segundos e ocupando pouco espaço utilizando o dicionário. Além disso, observa-se pelo grafico que a taxa de compressão esteve alta durante toda a compressão do texto, gerando no final uma taxa de compressão ótimo de 4, indicando que o arquivo compactado ficou 4 vezes menor que o arquivo original

   Dado o arquivo comprimido gerado pelo livro, foi realizado a descompressão do arquivo com o mesmo máximo de bits e também variável, chegando aos resultados do [relatorio criado](Dados_teste/Relatorio_de_testes_Descompressao_variavel_12_livro.md)

   Analisando as estastísticas de descompressão é possível perceber que a descompressão foi eficiente, gerando o arquivo descomprimido em menos de 10 segundos, ocupando bem menos espaço no dicionário comparado com a compressão. Além disso, analisando o gráfico percebe-se que em relação a taxa de compressão ela diminui consideravelmente, já que ele retorna o valor ao formato original em caractere e perde as características de compressão. 

### **Compressão e descompressão de Livro em txt com bit variavel de 9**

   Dado o mesmo arquivo de livro utilizado na primeira análise, foi feito uma nova execução com uma quantidade de bits máxima menor para testar a eficiência da compressão com menos bits, chegando aos resultados representados no [relatorio criado](Dados_teste/Relatorio_de_testes_Compressao_variavel_9_livro.md)

   Observando os dados e comparando com a compressão anterior é possivel perceber que a compressão teve um desempenho menos eficiente comparado com a primeira compressão, apresentando um tempo de compressão de 26 segundos, mas economiza muito em relação ao espaço gasto pela árvore. Além disso, verica-se que a limitação está funcionando por limitar o número de elementos adicionados em 512, sendo esse a quantidade máxima de valores permitido definido pela quantidade máxima de bits. Em relação ao gráfico, observa-se que a compressão teve um desempenho estritamente pior que a compressão com 12 bits, gerando uma taxa de compressão de apenas 2.7.

   Dado o arquivo comprimido gerado pelo livro, foi realizado a descompressão do arquivo com o mesmo máximo de bits e também variável, chegando aos resultados do [relatorio criado](Dados_teste/Relatorio_de_testes_Descompressao_variavel_9_livro.md)   

   Observando as estatísticas da descompressão percebe-se que a descompressão também é afetada pela diminuição do máximo de bits, obtendo um desempenho menor comparado com a descompressão de 12 bits de 20 segundos, mas economiza muito em relação ao espaço gasto pela árvore. Em relação ao gráfico, observa-se que a compressão teve um desempenho maior, já que a taxa de compressão ao passar o arquivo foi baixa.

### **Compressão e descompressão de Livro em txt com bit fixo**

   Considerando que a quantidade de bits pode ser variável ou fixa, foi feito uma nova execução para a taxa com o tamanho máximo de bits padrão de 12 para verificar a diferença estatística para a compressão variável, chegando aos arquivos presentes no [relatorio gerado](Dados_teste/Relatorio_de_testes_Compressao_fixa_12_livro.md)

   Observando os dados e comparando com a compressão variável é possivel perceber que os dois métodos geraram estatísticas parecidas, indicando a proximidade do tipo de compressão nos dois casos. Por isso, o tempo gasto em segundos e o espaço ocupado nos dois casos foi basicamente igual. Além disso, observando o gráfico percebe-se ainda mais essa semelhança, já que os dois gráficos são basicamente iguais.

   Dado o arquivo comprimido gerado pelo livro, foi realizado a descompressão do arquivo com o mesmo máximo de bits e também fixa, chegando aos resultados do [relatorio criado](Dados_teste/Relatorio_de_testes_Descompressao_fixa_12_livro.md)  

   Observando as estatísticas da descompressão percebe-se que a descompressão também é pouco afetada pela mudança de variável para fixo, porém nesse caso existe uma pequena diferença devido ao tamanho dos bytes do codigo. Por isso, observa-se que teve um desempenho minimamente diferente na quantidade de valores, já que a opção fixa faz tratar mais bytes devido a diminuição de bytes necessário que a compressão faz. Além disso, observando o gráfico percebe-se que realmente são bem parecidos, possuindo apenas uma pequena diferença no inicio devido ao período em que a utilização variável teria bits menores.

## Problemas na implementação

-Não foi possível realizar a compressão de arquivos que não sejam arquivos de texto, assim o programa funciona apenas caso seja inserido arquivos de texto
