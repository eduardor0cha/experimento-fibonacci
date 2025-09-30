import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

colunas = ['i-ésimo valor', 'Sist. 01', 'Sist. 02', 'Sist. 03', 'Sist. 04', 'Sist. 05']
df = pd.DataFrame(columns=colunas)
df['i-ésimo valor'] = list(range(1, 51))

# df['Título da Coluna'] = pd.read_csv('pwd/resultado', header=None)[2]
df['Sist. 01'] = pd.read_csv('dados_testes/resultados/01.txt', dtype=str, header=None)[2]
df['Sist. 02'] = pd.read_csv('dados_testes/resultados/02.txt', dtype=str, header=None)[2]
df['Sist. 03'] = pd.read_csv('dados_testes/resultados/03.txt', dtype=str, header=None)[2]
df['Sist. 04'] = pd.read_csv('dados_testes/resultados/04.txt', dtype=str, header=None)[2]
df['Sist. 05'] = pd.read_csv('dados_testes/resultados/05.txt', dtype=str, header=None)[2]

fig, ax = plt.subplots(figsize=(10, 14))
ax.axis('tight')
ax.axis('off')

tabela = ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center')
tabela.auto_set_font_size(False)
tabela.set_fontsize(10)
tabela.scale(1.2, 1.2)

nome_arquivo_saida = 'dados_testes/tabela_tempos.png'
plt.savefig(nome_arquivo_saida, bbox_inches='tight', dpi=200)

print(f"A tabela foi gerada com sucesso e salva como '{nome_arquivo_saida}'")
