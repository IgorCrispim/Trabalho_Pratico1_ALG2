import sys

def inicializaDicionario():
    dicionario = {}
    for i in range(256):
        dicionario[chr(i)] = format(i, '012b')
    return dicionario

def inicializaDicionarioInverso():
    dicionario = {}
    for i in range(256):
        dicionario[format(i, '012b')] = chr(i)
    return dicionario   

def compressaoFixa(entrada):
    dicionario = inicializaDicionario()
    posicao = 256
    StringProvisoria = entrada[0]
    resultado = []
    for caractere in entrada[1:]:
        if (StringProvisoria + caractere) in dicionario:
            StringProvisoria += caractere
        else:
            #Verificar se a entrada está muito grande
            dicionario[StringProvisoria+caractere] = format(posicao, '012b')
            posicao+=1
            resultado.append(dicionario[StringProvisoria])
            StringProvisoria = caractere
    resultado.append(dicionario[StringProvisoria])
    return resultado    

def descompressaoFixa(comprimido):
    dicionario = inicializaDicionarioInverso()
    posicao = 256
    StringProvisoria = dicionario[comprimido[0]]
    StringSaida = StringProvisoria
    
    for codigo in comprimido[1:]:
        entrada = ""
        if codigo in dicionario:
            entrada = dicionario[codigo]
        else:
            entrada = StringProvisoria + StringProvisoria[0]
        StringSaida+=entrada
        dicionario[format(posicao, '012b')] = StringProvisoria + entrada[0]
        #Verificar se a posição ultrapassou o tamanho máximo
        posicao+=1
        StringProvisoria = entrada
    return StringSaida


entrada = sys.argv[1]      

arquivo = open(entrada)
texto = arquivo.read()

bitsVariado = sys.argv[2]     

if bitsVariado is None:
    bitsVariado = 12

#Implementar versão de tamanho fixo e tamanho variável

comprimido = compressaoFixa(texto)
descomprimido = descompressaoFixa(comprimido)

print(texto == descomprimido)

arquivo.close()

#Você também deverá implementar uma opção de teste em que o programa
#armazenará estatísticas da codificação/decodificação. Essas estatísticas deverão conter
#a taxa de compressão ao longo do processamento dos arquivos, tamanho do dicionário
#(número de elementos armazenados e espaço em memória), tempo total de execução,
#e outras estatísticas que você julgar importantes. 

