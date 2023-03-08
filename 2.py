#Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...).
#Escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
#IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;


def verifica_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    if b == num:
        return True
    else:
        return False

def sequencia_fibonacci(num):
    fibonacci = [0, 1]
    while fibonacci[-1] < num:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    if fibonacci[-1] == num:
        print(f"O número {num} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {num} não pertence à sequência de Fibonacci.")
    return fibonacci[:-1]

num = int(input("Digite um número: "))
sequencia = sequencia_fibonacci(num)
print(f"A sequência de Fibonacci até o número {num} é: {sequencia}")
