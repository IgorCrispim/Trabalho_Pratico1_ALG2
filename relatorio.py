import matplotlib.pyplot as plt
import numpy as np

def geraRelatorio(taxas_compressao, tempo_total, numero_nos_total,espaco_total,numero_elementos_total, tamanho_inicial,nome_arquivo):
    x = np.arange(1, tamanho_inicial + 1)
    table = {
        'Descrições': ['Quantidade de valores','Tempo de execução em segundos','Espaço gasto na árvore em kb','Numero total de nós','Numero de elementos adicionados'],
        'Estatísticas':[tamanho_inicial,f"{tempo_total:.2f}",f"{espaco_total:.2f}",numero_nos_total,numero_elementos_total]
    }
    plt.figure()
    plt.plot(x,taxas_compressao)
    plt.title('Variação da taxa de compressão')
    plt.xlabel('Numero de bytes')
    plt.ylabel('Taxa de compressão')
    
    saida = 'Dados de teste/Grafico ' + nome_arquivo + '.png'
    
    plt.savefig(saida, format='png')
    plt.close() 

    fig, ax = plt.subplots()  
    ax.axis('tight')
    ax.axis('off')  
    table = ax.table(cellText=list(zip(*table.values())), colLabels=list(table.keys()), cellLoc='center', loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    
    saida = 'Dados de teste/Tabela ' + nome_arquivo + '.png'
    
    plt.savefig(saida, format='png')
    plt.close() 