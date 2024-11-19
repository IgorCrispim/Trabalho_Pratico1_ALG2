import sys
from arvores import CompactBinaryTrie

def inicializaDicionario(arvore):
    for i in range(256):
        arvore.insert_prefix(chr(i),i)

def inicializaDicionarioInverso(arvore):
    for i in range(256):
        arvore.insert_prefix(i,chr(i))

def compressao(entrada,bitsMaximo,variavel):
    arvore = CompactBinaryTrie()
    if variavel:
        tamanhoAtual = 8
    else:
        tamanhoAtual = 12
    
    inicializaDicionario(arvore)
    
    posicao = 256
    StringProvisoria = entrada[0]
    
    encoded = bytearray()
    bit_buffer = 0
    bit_count = 0

    for caractere in entrada[1:]:
        if ((arvore.search(StringProvisoria + caractere)) is not None):
            StringProvisoria += caractere
        else:
            
            bit_buffer = (bit_buffer << tamanhoAtual) | arvore.search(StringProvisoria)
            bit_count += tamanhoAtual
            
            while bit_count >= 8:
                bit_count -= 8
                byte = (bit_buffer >> bit_count) & 0xFF
                encoded.append(byte)
                
            
            if posicao < (2 ** bitsMaximo):
                if posicao >= (1 << tamanhoAtual) and tamanhoAtual < bitsMaximo:
                    tamanhoAtual += 1
                arvore.insert_prefix(StringProvisoria+caractere,posicao)
                posicao+=1
            #else:
                #dicionario.clear()
                #tamanhoAtual = 8 if variavel else 12
                #dicionario = inicializaDicionario(arvore)
                #posicao = 256

            StringProvisoria = caractere
    
    bit_buffer = (bit_buffer << tamanhoAtual) | arvore.search(StringProvisoria)
    bit_count += tamanhoAtual
    
    while bit_count >= 8:
        bit_count -= 8
        byte = (bit_buffer >> bit_count) & 0xFF
        encoded.append(byte)

    if bit_count > 0:
        byte = (bit_buffer << (8 - bit_count)) & 0xFF
        encoded.append(byte)

    return bytes(encoded)

def descompressao(comprimido,bitsMaximo,variavel):
    if variavel:
        tamanhoAtual = 8
    else:
        tamanhoAtual = 12
        
    arvore = CompactBinaryTrie()
    
    inicializaDicionarioInverso(arvore)
    
    StringProvisoria = ""
    StringSaida = StringProvisoria
    
    bit_buffer = 0
    bit_count = 0
    posicao = 256
        
    for byte in comprimido:
        bit_buffer = (bit_buffer << 8) | byte
        bit_count += 8       
        while bit_count >= tamanhoAtual:
            bit_count -= tamanhoAtual
            numero = (bit_buffer >> bit_count) & ((1 << tamanhoAtual) - 1)
            #print(numero)
            entrada = ""
            if (arvore.search(numero) is not None):
                entrada = arvore.search(numero)
            else:
                entrada = StringProvisoria + StringProvisoria[0]
            StringSaida+=entrada
            
            if posicao < (2 ** bitsMaximo):
                if StringProvisoria:
                    arvore.insert_prefix(posicao,(StringProvisoria + entrada[0]))
                    posicao += 1

                if posicao >= (1 << tamanhoAtual) and tamanhoAtual < bitsMaximo:
                    tamanhoAtual += 1
            #else
                #print(dicionario)
                #print(entrada)
                #dicionario.clear()
                #tamanhoAtual = 8 if variavel else 12
                #dicionario = inicializaDicionarioInverso(arvore)
                #posicao = 256                 
        
            StringProvisoria = entrada
    #print(dicionario)
    return StringSaida

entrada = sys.argv[1]      

arquivo = open(entrada)
texto = arquivo.read() 

variavel = False

if len(sys.argv) < 3 or not variavel:
    bitsMaximo = 12
else:
    bitsMaximo =  int(sys.argv[2])

comprimido = compressao(texto,bitsMaximo,variavel)

print(f"Memória usada pelo original: {sys.getsizeof(texto)} bytes")

print(f"Memória usada pelo comprimido: {sys.getsizeof(comprimido)} bytes")

descomprimido = descompressao(comprimido,bitsMaximo,variavel)

print("O arquivo descomprimido é igual ao original :", (descomprimido == texto))

arquivo.close()

#Você também deverá implementar uma opção de teste em que o programa
#armazenará estatísticas da codificação/decodificação. Essas estatísticas deverão conter
#a taxa de compressão ao longo do processamento dos arquivos, tamanho do dicionário
#(número de elementos armazenados e espaço em memória), tempo total de execução,
#e outras estatísticas que você julgar importantes. 