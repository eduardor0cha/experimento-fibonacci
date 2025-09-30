import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 51, dtype=np.int64)

y1 = 2**x

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(x, y1, marker='o', linestyle='-', color='blue', label='$2^x$')

ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('f(x)', fontsize=12)

ax.grid(True, which="both", linestyle='--', linewidth=0.5)

nome_arquivo = 'grafico_2x.png'
plt.savefig(nome_arquivo, dpi=450, bbox_inches='tight')

print(f"O gráfico foi gerado e salvo com sucesso como '{nome_arquivo}'")