#O usuário informa 2 listas, juntamos e exibimos na 3 lista
lista_1 = []
lista_2 = []
lista_3 = []
quantidade_na_lista_1 = int(input("Quantos valores na lista 1?"))

while len(lista_1) < quantidade_na_lista_1:
  valor = int(input('Valor:'))
  #Adicionar no final da lista
  lista_1.append(valor)
  print(lista_1)
