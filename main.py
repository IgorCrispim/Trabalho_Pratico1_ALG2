
import LZW
import argparse
import relatorio
import os

def leituraParametros():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', action='store_true',help = "Indica que ira realizar a compressão de um arquivo")
    parser.add_argument('-d', action='store_true', help = "Indica que ira realizar a descompressão de um arquivo")
    parser.add_argument('-v', action='store_true', help = "A compressão/descompressão será com tamanho de bits variado")
    parser.add_argument('-f', action='store_true', help = "A compressão/descompressão será com tamanho de bits fixo")
    parser.add_argument('-t', action='store_true', help = "Indica que o sistema funcionará em modo de teste")
    parser.add_argument('max_bits', type=int, nargs='?', help = "Tmamanho máximo dos bits")
    parser.add_argument('nome_arquivo', type=str, help = "Nome do arquivo a ser comprimido/descomprimido")
    args = parser.parse_args()
    return args

def inicializaValores(args):
  
    if args.c:
        compressao = True
    elif args.d:
        compressao = False
  
    if args.v:
        variavel = True
    elif args.f:
        variavel = False
        
    teste = args.t

    if args.max_bits is None or not variavel:
        bitsMaximo = 12
    else:
        bitsMaximo =  args.max_bits
        
    entrada = args.nome_arquivo    
    if compressao:  
        with open(entrada, 'r') as arquivo:
            texto = arquivo.read() 
        arquivo.close()
    else:
        with open(entrada, 'rb') as arquivo:
            texto = bytearray(arquivo.read())
        arquivo.close()
    
    return compressao,variavel,teste,texto, bitsMaximo
    

if __name__ == '__main__':
    args = leituraParametros()
    compressao,variavel,teste,texto, bitsMaximo = inicializaValores(args)
    nome_arquivo, extensao = os.path.splitext(os.path.basename(args.nome_arquivo))   
    if compressao:
        if(teste):
            comprimido, taxas_compressao, tempo_total, numero_nos_total,espaco_total,numero_elementos_total = LZW.compressao(texto,bitsMaximo,variavel, teste)
            relatorio.geraRelatorio(taxas_compressao, tempo_total, numero_nos_total,espaco_total,numero_elementos_total, len(texto),"Compressao - " + nome_arquivo)
        else:
            comprimido = LZW.compressao(texto,bitsMaximo,variavel, teste)
        with open("Arquivos comprimidos/" + nome_arquivo + ".bin", "wb") as arquivo:
            arquivo.write(comprimido)
        arquivo.close()
    else:
        if(teste):
            descomprimido, taxas_compressao, tempo_total, numero_nos_total,espaco_total,numero_elementos_total = LZW.descompressao(texto,bitsMaximo,variavel, teste)
            relatorio.geraRelatorio(taxas_compressao, tempo_total, numero_nos_total,espaco_total,numero_elementos_total, (len(texto)),"Descompressao - " + nome_arquivo)
        else:
            descomprimido = LZW.descompressao(texto,bitsMaximo,variavel, teste)
        with open("Arquivos descomprimidos/" + nome_arquivo + ".txt", "w") as arquivo:
            arquivo.write(descomprimido)
        arquivo.close()