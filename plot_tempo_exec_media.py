import os
import matplotlib.pyplot as plt

def plotar_graficos():
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, 'dados_testes/resultados/')
    imgpath = os.path.join(dirname, 'dados_testes/grafico-media.png')

    dados = dict()
    for entry in sorted(os.listdir(filepath)):

        with open(os.path.join(filepath, entry)) as file:
            for linha in file.read().splitlines():
                [posicao, resultado, tempo_exec] = linha.split(",")

                if (str(posicao) not in dados):
                    dados[str(posicao)] = []
                dados[str(posicao)].append(float(tempo_exec))


    posicoes = sorted(map(int, dados.keys()))
    medias = []
    for k in posicoes:
        medias.append(sum(dados[str(k)]) / len(dados[str(k)]))

    plt.plot(posicoes, medias, marker='o')
    plt.xlabel('Posição (n)')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.legend()
    plt.grid(True)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(imgpath, dpi=450)
    print(f"Gráfico salvo em {imgpath}")
    plt.show()

if __name__ == '__main__':
    plotar_graficos()