#Ler todos os nomes que o usuário digitar até que ele não 
#deseja mais continuar. Exibir todos os nomes da lista, em ordem
#alfabética

#Cria uma lista vazia para os nomes
nomes = []

#Cria uma repeticao que pergunta se o usuario deseja continuar
continuar = True

while continuar == True:
  nome = input('Informe um nome:')
  #Coloca o nome no final da lista
  nomes.append(nome)
  #Exibe a parcial da lista com os nomes
  print(nomes)
  if input('Deseja continuar (s/n)?') == 's':
    continuar = True
  else:
    continuar = False
