nome= input("escreva seu nome?:")
valor= input("valor do produto?:")
quantidade=input("quantidade do produto?:")

with open("produtos.txt", "a" ) as produto:
    produto.write( nome + "|" + valor + "|"  + quantidade + "\n")
    print("Parabéns!!!!!!")