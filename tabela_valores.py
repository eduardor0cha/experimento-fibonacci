import os
import matplotlib.pyplot as plt

def gerar_tabela_grafica():
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, 'resultados_locais/resultados.txt')
    tablepath = os.path.join(dirname, 'resultados_locais/tabela.png')

    dados_tabela = []

    with open(filepath) as file:
        for linha in file.read().splitlines():
            [posicao, resultado, tempo_exec] = linha.split(",")
            dados_tabela.append([posicao, f"{int(resultado):,}"])
    
    colunas = ['Posição (n)', 'Resultado Fibonacci']

    fig, ax = plt.subplots(figsize=(10, 0.3 * len(dados_tabela))) 

    ax.axis('tight')
    ax.axis('off')

    tabela = ax.table(
        cellText=dados_tabela,      
        colLabels=colunas,          
        loc='center',               
        cellLoc='center'            
    )

    tabela.auto_set_font_size(False)
    tabela.set_fontsize(12)
    tabela.scale(1.1, 1.4) 

    for key, cell in tabela.get_celld().items():
        
        if key[0] == 0:
            cell.set_facecolor('#40466e') 
            cell.set_text_props(weight='bold', color='w') 

    plt.savefig(tablepath, bbox_inches='tight', dpi=450)
    print(f"Tabela salva em {tablepath}")
    plt.show()

if __name__ == '__main__':
    gerar_tabela_grafica()