# -*-encoding utf-8 -*-

#First Program
name = input("What's your name?")
print(f"Hello {name}!")

#Python Challenge
# Tendo como dados de entrada a altura de uma pessoa,
# construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58

height = float(input("Altura:"))
weight = (72.7 * height) - 58.0
print(f"Peso ideal: {weight}")

#Conditional Challenge
# Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
# ou "Valor Inválido!", conforme o caso.#m@th10txf
shift = str(input("M - Matutino V-Vespertino N- Noturno"))

if shift == 'M':
    print("Bom dia!")
elif shift == 'V':
    print("Boa tarde!")
elif shift == 'N':
    print("Boa noite!")
else:
    print("Valor Inválido!")