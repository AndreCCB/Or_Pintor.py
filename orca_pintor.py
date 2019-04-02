#! user/bin/env/python
#coding: UTF-8
#irc.vircio.org
#phacker
#https://www.facebook.com/profile.php?id=100030877832029

print("FAÇA SEU ORÇAMENTO DE PINTURA GRATIS by:Phacker")
print("Caso use numeros decimais use ponto!\n")
try:   
    altura = float(input("Digite a altura da parede: "))
    comprimento = float(input("Digite o comprimento da parede: "))
    valor = float(input("Digite o valor de  cada lata de tinta R$: "))
    rendimento = int(input("Digite quantos metros 1 lata rende: "))
    paredes_metro = altura * comprimento
    red_latas = paredes_metro / rendimento
    print("Quantidade de latas: %.3f "%red_latas)
    qtd_latas = red_latas * valor
    print("Valor orcamento R$: %.2f "%qtd_latas)
    print("Gostou deseja doar qualquer quantia: http://vaka.me/468135")
except:
 	print("Você digitou um valor errado!\n")
