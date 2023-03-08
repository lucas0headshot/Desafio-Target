#Escreva um programa que inverta os caracteres de um string.
#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;


def inverter_string(palavra):
    x = len(palavra)
    i = 0
    palavra_invertida = ""

    for i in range(x):
        palavra_invertida += palavra[x - i - 1]
    
    print("Palavra: ",palavra)
    print("Invertida: ",palavra_invertida)

palavra = str(input("Digite uma palavra: "))
inverter_string(palavra)