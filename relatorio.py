import matplotlib.pyplot as plt
import numpy as np

def geraRelatorio(taxas_compressao, tempo_total, numero_nos_total,espaco_total,numero_elementos_total, tamanho_inicial,nome_arquivo):
    nome_arquivo = nome_arquivo.replace(" ", "_")
    x = np.arange(0, len(taxas_compressao))

    descricoes = ['Quantidade de valores','Tempo de execução em segundos','Espaço gasto na árvore em kb','Numero total de nós','Numero de elementos adicionados', 'Taxa final de compressão/descompressão']
    valores = [tamanho_inicial,f"{tempo_total:.2f}",f"{espaco_total:.2f}",numero_nos_total,numero_elementos_total,f"{taxas_compressao[len(taxas_compressao)-1]:.2f}"]
    
    plt.figure()
    plt.plot(x,taxas_compressao)
    plt.title('Variação da taxa de compressão')
    plt.xlabel('Numero de bytes')
    plt.ylabel('Taxa de compressão')
    
    saida = 'Grafico_' + nome_arquivo +'.png'
    repositorio = "Dados_teste/"
    
    plt.savefig(repositorio + saida, format='png')
    plt.close() 
    
    cabecalho = ["Descrições", "Estatísticas"]
    tabela_markdown = "| " + " | ".join(cabecalho) + " |\n"
    tabela_markdown += "| " + " | ".join("---" for _ in cabecalho) + " |\n"
    
    for descricao, estatistica in zip(descricoes,valores):
        tabela_markdown += f"| {descricao} | {estatistica} |\n"
        
    markdown = f"""
# Relatório dos testes no arquivo {nome_arquivo.replace("_", " ")}
    
## Tabela dos dados
    
{tabela_markdown}
    
## Gráfico da taxa de compressão
    
![Grafico da compressão](./{saida})

    """
    with open(repositorio +"Relatorio_de_testes_" + nome_arquivo + ".md", "a") as readme:
        readme.write(markdown)