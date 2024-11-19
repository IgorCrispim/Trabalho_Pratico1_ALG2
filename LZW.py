from arvores import CompactBinaryTrie
import time
import sys

def inicializaArvore(arvore):
    for i in range(256):
        arvore.insert_prefix(chr(i),i)

def inicializaArvoreInvera(arvore):
    for i in range(256):
        arvore.insert_prefix(i,chr(i))

def compressao(entrada,bitsMaximo,variavel,teste):
    
    if teste:
        taxas_compressao = []
        numero_elementos_total = 0
        numero_nos_total = 0
        espaco_total = 0
        tempo_total = 0
        quantidade_caracteres = 1
        start_time = time.time()  
        
    
    arvore = CompactBinaryTrie()
    if variavel:
        tamanhoAtual = 8
    else:
        tamanhoAtual = 12
    
    inicializaArvore(arvore)
    
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
                
            
            if (posicao) < (2 ** bitsMaximo):
                if posicao >= (1 << tamanhoAtual) and tamanhoAtual < bitsMaximo:
                    tamanhoAtual += 1
                arvore.insert_prefix(StringProvisoria+caractere,posicao)
                posicao+=1

            StringProvisoria = caractere
        if teste:
            quantidade_caracteres += 1
            taxas_compressao.append(sys.getsizeof(entrada[:quantidade_caracteres])/(sys.getsizeof(bytes(encoded))))
    
    bit_buffer = (bit_buffer << tamanhoAtual) | arvore.search(StringProvisoria)
    bit_count += tamanhoAtual
    
    while bit_count >= 8:
        bit_count -= 8
        byte = (bit_buffer >> bit_count) & 0xFF
        encoded.append(byte)

    if bit_count > 0:
        byte = (bit_buffer << (8 - bit_count)) & 0xFF
        encoded.append(byte)

    if teste:
        tempo_total = (time.time()  - start_time)
        numero_nos_total,espaco_total,numero_elementos_total = arvore.get_tree_statistics()    
        return bytes(encoded), taxas_compressao, tempo_total, numero_nos_total,espaco_total,numero_elementos_total
    else:
        return bytes(encoded)

def descompressao(comprimido,bitsMaximo,variavel,teste):
    if variavel:
        tamanhoAtual = 8
    else:
        tamanhoAtual = 12
        
    if teste:
        taxas_compressao = []
        numero_elementos_total = 0
        numero_nos_total = 0
        espaco_total = 0
        tempo_total = 0
        quantidade_bytes = 1
        start_time = time.time()  
        
    arvore = CompactBinaryTrie()
    
    inicializaArvoreInvera(arvore)
    
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
                   
            StringProvisoria = entrada
        if teste:
            quantidade_bytes += 1
            taxas_compressao.append(sys.getsizeof(bytes(comprimido[:quantidade_bytes]))/(sys.getsizeof(StringSaida)))
        
    if teste:
        tempo_total = (time.time()  - start_time)
        numero_nos_total,espaco_total,numero_elementos_total = arvore.get_tree_statistics()    
        return StringSaida, taxas_compressao, tempo_total, numero_nos_total,espaco_total,numero_elementos_total
    else:
        return StringSaida
    