import sys

def inicializaDicionario(tamanho):
    dicionario = {}
    for i in range(256):
        dicionario[chr(i)] = format(i, tamanho)
    return dicionario

def inicializaDicionarioInverso(tamanho):
    dicionario = {}
    for i in range(256):
        dicionario[format(i, tamanho)] = chr(i)
    return dicionario   

def compressao(entrada,bitsMaximo,variavel):
    
    if variavel:
        tamanhoAtual = 8
    else:
        tamanhoAtual = 12
        
    dicionario = inicializaDicionario(f'0{tamanhoAtual}b')
    posicao = 256
    StringProvisoria = entrada[0]
    resultado = ""

    for caractere in entrada[1:]:
        if (StringProvisoria + caractere) in dicionario:
            StringProvisoria += caractere
        else:
            tamanhoAnterior = tamanhoAtual
            if posicao == (2 ** tamanhoAtual):
                if tamanhoAtual < bitsMaximo:
                    tamanhoAtual += 1
                else:
                    dicionario.clear()
                    dicionario = inicializaDicionario(f'0{tamanhoAtual}b')
                    posicao = 256
                    tamanhoAtual = 8
                    print(bitsMaximo)
            
            dicionario[StringProvisoria+caractere] = format(posicao, f'0{tamanhoAtual}b')
            posicao+=1
            resultado += dicionario[StringProvisoria].zfill(tamanhoAnterior)
            StringProvisoria = caractere
    resultado += dicionario[StringProvisoria].zfill(tamanhoAtual)
    return resultado    

def descompressao(comprimido,bitsMaximo,variavel):
    if variavel:
        tamanhoAtual = 8
    else:
        tamanhoAtual = 12
    
    dicionario = inicializaDicionarioInverso(f'0{tamanhoAtual}b')
    posicao = 256
    StringProvisoria = dicionario[comprimido[0:0+tamanhoAtual]]
    StringSaida = StringProvisoria
    inicio = tamanhoAtual 
    
    while inicio < len(comprimido):
        if posicao == (2 ** tamanhoAtual):
            if tamanhoAtual < bitsMaximo:
                tamanhoAtual += 1
            else:
                dicionario.clear()
                dicionario = inicializaDicionarioInverso(f'0{tamanhoAtual}b')
                posicao = 256
        codigo = comprimido[inicio:inicio+tamanhoAtual]
        
        entrada = ""
        while (len(codigo) >= 8): #Provisorio, na Trie provavelmente existe jeitos melhores
            if codigo in dicionario:
                entrada = dicionario[codigo]
                break
            else:
                entrada = StringProvisoria + StringProvisoria[0]
                if (codigo[0] == '0'):
                    codigo = codigo[1:]
                else:
                    break
        StringSaida+=entrada
        
        dicionario[format(posicao, f'0{tamanhoAtual}b')] = StringProvisoria + entrada[0]
        posicao+=1
        StringProvisoria = entrada
        inicio += tamanhoAtual
    return StringSaida

entrada = sys.argv[1]      

arquivo = open(entrada)
texto = arquivo.read() 
bitsMaximo = int(sys.argv[2])   

if bitsMaximo is None:
    bitsMaximo = 12
    
variavel = True

comprimido = compressao(texto,bitsMaximo,variavel)

print(f"Memória usada pelo original: {sys.getsizeof(texto)} bytes")

print(f"Memória usada pelo comprimido: {sys.getsizeof(comprimido)} bytes")

descomprimido = descompressao(comprimido,bitsMaximo,variavel)

print(descomprimido == texto)
    
arquivo.close()

#Você também deverá implementar uma opção de teste em que o programa
#armazenará estatísticas da codificação/decodificação. Essas estatísticas deverão conter
#a taxa de compressão ao longo do processamento dos arquivos, tamanho do dicionário
#(número de elementos armazenados e espaço em memória), tempo total de execução,
#e outras estatísticas que você julgar importantes. 