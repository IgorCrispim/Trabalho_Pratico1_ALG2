import sys
from arvores import PrefixTrie

def inicializaDicionario(arvore):
    dicionario = {}
    for i in range(256):
        dicionario[chr(i)] = i
        arvore.insert_prefix(chr(i))
    return dicionario

def inicializaDicionarioInverso(arvore):
    dicionario = {}
    for i in range(256):
        dicionario[i] = chr(i)
        arvore.insert_prefix(i)
    return dicionario   

def compressao(entrada,bitsMaximo,variavel):
    arvore = PrefixTrie(chr(0))
    if variavel:
        tamanhoAtual = 8
    else:
        tamanhoAtual = 12
        
    dicionario = inicializaDicionario(arvore)
    
    posicao = 256
    StringProvisoria = entrada[0]
    
    encoded = bytearray()
    bit_buffer = 0
    bit_count = 0

    for caractere in entrada[1:]:
        print(arvore.search(StringProvisoria + caractere))
        print((StringProvisoria + caractere) in dicionario)
        if (StringProvisoria + caractere) in dicionario:
            StringProvisoria += caractere
        else:
            
            bit_buffer = (bit_buffer << tamanhoAtual) | dicionario[StringProvisoria]
            bit_count += tamanhoAtual
            
            print(dicionario[StringProvisoria])
            print(arvore.get_index(StringProvisoria))
            
            while bit_count >= 8:
                bit_count -= 8
                byte = (bit_buffer >> bit_count) & 0xFF
                encoded.append(byte)
                
            
            if posicao < (2 ** bitsMaximo):
                if posicao >= (1 << tamanhoAtual) and tamanhoAtual < bitsMaximo:
                    tamanhoAtual += 1
                arvore.insert_prefix(StringProvisoria+caractere)
                dicionario[StringProvisoria+caractere] = posicao
                posicao+=1
            #else:
                #dicionario.clear()
                #tamanhoAtual = 8 if variavel else 12
                #dicionario = inicializaDicionario(arvore)
                #posicao = 256

            StringProvisoria = caractere
    
    bit_buffer = (bit_buffer << tamanhoAtual) | dicionario[StringProvisoria]
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
        
    arvore = PrefixTrie(chr(0))
    
    dicionario = inicializaDicionarioInverso(arvore)
    
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
            #print(arvore.search(codigo))
            #print(codigo in dicionario)
            if numero in dicionario:
                entrada = dicionario[numero]
            else:
                entrada = StringProvisoria + StringProvisoria[0]
            StringSaida+=entrada
            #valor = arvore.insert_prefix(format(posicao, f'0{tamanhoAtual}b'))
            
            if len(dicionario) < (1 << bitsMaximo):
                if StringProvisoria:
                    dicionario[posicao] = StringProvisoria + entrada[0]
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

variavel = True

if len(sys.argv) < 3 or not variavel:
    bitsMaximo = 12
else:
    bitsMaximo =  int(sys.argv[2])

comprimido = compressao(texto,bitsMaximo,variavel)

print(f"Memória usada pelo original: {sys.getsizeof(texto)} bytes")

print(f"Memória usada pelo comprimido: {sys.getsizeof(comprimido)} bytes")

descomprimido = descompressao(comprimido,bitsMaximo,variavel)

print(descomprimido == texto)

arquivo.close()

print(descomprimido)

#Você também deverá implementar uma opção de teste em que o programa
#armazenará estatísticas da codificação/decodificação. Essas estatísticas deverão conter
#a taxa de compressão ao longo do processamento dos arquivos, tamanho do dicionário
#(número de elementos armazenados e espaço em memória), tempo total de execução,
#e outras estatísticas que você julgar importantes. 