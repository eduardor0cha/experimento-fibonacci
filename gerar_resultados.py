import time
import os
import sys
from fibonacci import seq_fibonacci

def gerar_resultados():
  dirname = os.path.dirname(__file__)
  filepath = os.path.join(dirname, 'resultados_locais/resultados.txt')
  open(filepath, "a+").close()

  n = 0
  with open(filepath) as f:
    l = f.read().splitlines()

    if (len(l) > 0):
      ultima_l = l[-1].split(",")
      if (len(ultima_l) == 3 and ultima_l[0].isdigit()):
        n = int(ultima_l[0])
        print(f"Continuando a geração a partir da posição {n+1}.")


  print(f"Calculando a sequência de Fibonacci e o tempo de execução.")

  while True:
    n += 1
    start_time = time.time()
    resultado = seq_fibonacci(n - 1)
    end_time = time.time()
    
    tempo_gasto = end_time - start_time
    
    with open(filepath, 'a') as f:
      f.write(f"{n},{resultado},{tempo_gasto:.6f}\n")
    
    print(f"Posição: {n}, Resultado: {resultado}, Tempo: {tempo_gasto:.6f}s")

if __name__ == "__main__":
  try:
    gerar_resultados()
  except KeyboardInterrupt:
    print("Geração de resultados finalizada.")
    sys.exit(0)
