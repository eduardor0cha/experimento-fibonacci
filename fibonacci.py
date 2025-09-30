def seq_fibonacci(numero):
    # Caso base 1: fib(0) = 0
    # Caso base 2: fib(1) = 1
    if numero <= 1:
        return numero
    else:
        return seq_fibonacci(numero-1) + seq_fibonacci(numero-2)

if __name__ == '__main__':
    n = int(input("Posição: "))
    resultado = seq_fibonacci(n-1)
    #print("O número %d está na posição %d na sequência de fibonacci" % (resultado,n))
    print(resultado)
