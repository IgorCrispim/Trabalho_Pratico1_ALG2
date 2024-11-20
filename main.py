import LZW
import argparse
import relatorio
import os

def leituraParametros():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', action='store_true', help="Indica que irá realizar a compressão de um arquivo")
    parser.add_argument('-d', action='store_true', help="Indica que irá realizar a descompressão de um arquivo")
    parser.add_argument('-v', action='store_true', help="A compressão/descompressão será com tamanho de bits variado")
    parser.add_argument('-f', action='store_true', help="A compressão/descompressão será com tamanho de bits fixo")
    parser.add_argument('-t', action='store_true', help="Indica que o sistema funcionará em modo de teste")
    parser.add_argument('max_bits', type=int, nargs='?', help="Tamanho máximo dos bits")
    parser.add_argument('nome_arquivo', type=str, help="Nome do arquivo a ser comprimido/descomprimido")
    args = parser.parse_args()

    if not (args.c or args.d):
        parser.error("Você deve especificar -c para compressão ou -d para descompressão.")
    
    if not (args.v or args.f):
        parser.error("Você deve especificar -f para fixo ou -v para variavel.")
    
    return args

def inicializaValores(args):
    compressao = args.c
    variavel = args.v
    teste = args.t
    bitsMaximo = args.max_bits if args.max_bits and variavel else 12
    
    if bitsMaximo < 8 or bitsMaximo > 16:
        print("Erro: O número de bits deve estar entre 8 e 16.")
        exit(1)

    entrada = args.nome_arquivo
    try:
        with open(entrada, 'r' if compressao else 'rb') as arquivo:
            texto = arquivo.read() if compressao else bytearray(arquivo.read())
    except FileNotFoundError:
        print(f"Erro: O arquivo '{entrada}' não foi encontrado.")
        exit(1)
    except IOError as e:
        print(f"Erro de I/O: {e}")
        exit(1)

    return compressao, variavel, teste, texto, bitsMaximo

if __name__ == '__main__':
    args = leituraParametros()
    compressao, variavel, teste, texto, bitsMaximo = inicializaValores(args)
    nome_arquivo, _ = os.path.splitext(os.path.basename(args.nome_arquivo))

    os.makedirs("Arquivos comprimidos", exist_ok=True)
    os.makedirs("Arquivos descomprimidos", exist_ok=True)

    if compressao:
        if teste:
            comprimido, taxas_compressao, tempo_total, numero_nos_total, espaco_total, numero_elementos_total = LZW.compressao(
                texto, bitsMaximo, variavel, teste)
            if variavel:
                relatorio.geraRelatorio(taxas_compressao, tempo_total, numero_nos_total, espaco_total, numero_elementos_total, len(texto), "Compressao_variavel_"+ str(bitsMaximo) +"_" + nome_arquivo)
            else:
                relatorio.geraRelatorio(taxas_compressao, tempo_total, numero_nos_total, espaco_total, numero_elementos_total, len(texto), "Compressao_fixa_"+ str(bitsMaximo) +"_" + nome_arquivo)
        else:
            comprimido = LZW.compressao(texto, bitsMaximo, variavel, teste)
        with open(f"Arquivos comprimidos/{nome_arquivo}.bin", "wb") as arquivo:
            arquivo.write(comprimido)
    else:
        if teste:
            descomprimido, taxas_compressao, tempo_total, numero_nos_total, espaco_total, numero_elementos_total = LZW.descompressao(
                texto, bitsMaximo, variavel, teste)
            if variavel:
                relatorio.geraRelatorio(taxas_compressao, tempo_total, numero_nos_total, espaco_total, numero_elementos_total, len(texto), "Descompressao_variavel_" + str(bitsMaximo) +"_" + nome_arquivo)
            else:
                relatorio.geraRelatorio(taxas_compressao, tempo_total, numero_nos_total, espaco_total, numero_elementos_total, len(texto), "Descompressao_fixa_" + str(bitsMaximo) +"_" + nome_arquivo)
        else:
            descomprimido = LZW.descompressao(texto, bitsMaximo, variavel, teste)
        with open(f"Arquivos descomprimidos/{nome_arquivo}.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write(descomprimido)
