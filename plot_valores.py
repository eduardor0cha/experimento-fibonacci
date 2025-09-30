import os
import matplotlib.pyplot as plt

def plotar_graficos():
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, 'resultados_locais/resultados.txt')
    imgpath = os.path.join(dirname, 'resultados_locais/grafico.png')
    
    posicoes = []
    resultados = []
    tempos_exec= []

    with open(filepath) as file:
        for linha in file.read().splitlines():
            [posicao, resultado, tempo_exec] = linha.split(",")
            posicoes.append(int(posicao))
            resultados.append(int(resultado))
            tempos_exec.append(float(tempo_exec))

    fig, ax = plt.subplots()

    # Gráfico 1: Crescimento da Sequência de Fibonacci
    ax.plot(posicoes, resultados, marker='o', linestyle='-', color='b')
    ax.set_xlabel('Posição (n)')
    ax.set_ylabel('Valor de Fibonacci')
    ax.grid(True)

    ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(imgpath, dpi=450)
    print(f"Gráfico salvo em {imgpath}")
    plt.show()

if __name__ == '__main__':
    plotar_graficos()