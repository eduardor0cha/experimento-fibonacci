import os
import matplotlib.pyplot as plt

def plotar_graficos():
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, 'dados_testes/resultados/')
    imgpath = os.path.join(dirname, 'dados_testes/grafico.png')

    dados = []
    for entry in sorted(os.listdir(filepath)):
        posicoes = []
        resultados = []
        tempos_exec= []

        with open(os.path.join(filepath, entry)) as file:
            for linha in file.read().splitlines():
                [posicao, resultado, tempo_exec] = linha.split(",")
                posicoes.append(int(posicao))
                resultados.append(int(resultado))
                tempos_exec.append(float(tempo_exec))
        
        dados.append([entry.replace(".txt", ""), posicoes, tempos_exec])

    plt.figure()

    for dado in dados:
        plt.plot(dado[1], dado[2], label=dado[0])
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