import matplotlib.pyplot as plt
import numpy as np

phi = (1 + np.sqrt(5)) / 2

x = np.arange(1, 51, dtype=np.int64)

y1 = 2**x
y2 = phi**x.astype(float)

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(x, y2, marker='s', linestyle='--', color='red', label='$\phi^x$')

ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('f(x)', fontsize=12)

ax.grid(True, which="both", linestyle='--', linewidth=0.5)

nome_arquivo = 'grafico_2x_phix.png'
plt.savefig(nome_arquivo, dpi=300, bbox_inches='tight')

print(f"O gráfico foi gerado e salvo com sucesso como '{nome_arquivo}'")