def classificacao():
  if idade >= 18:
    print(genero["18"], genero["16"], genero["14"], genero["12"], genero["10"], genero["Livre"])
  elif idade >= 16:
    print(genero["16"], genero["14"], genero["12"], genero["10"], genero["Livre"])
  elif idade >= 14:
    print(genero["14"], genero["12"], genero["10"], genero["Livre"])
  elif idade >= 12:
    print(genero["12"], genero["10"], genero["Livre"])
  elif idade >= 10:
    print(genero["10"], genero["Livre"])
  elif idade < 10:
    print(genero["Livre"])

Drama = {}

Drama["18"] = "13 - O Jogador"
Drama["16"] = "127 Horas"
Drama["14"] = "1917"
Drama["12"] = "Creed: Nascido Para Lutar"
Drama["10"] = "As Aventuras de PI"
Drama["Livre"] = "A Felicidade Não Se Compra"

Comedia = {}

Comedia["18"] = "Kick-Ass: Quebrando Tudo"
Comedia["16"] = "Rick e Morty"
Comedia["14"] = "A Noite do Jogo"
Comedia["12"] = "Gente Grande"
Comedia["10"] = "O Retorno de Johnny English"
Comedia["Livre"] = "O Mentiroso"

Terror = {}

Terror["18"] = "Esta é a sua morte"
Terror["16"] = "A Hora do Pesadelo"
Terror["14"] = "O Silêncio dos Inocentes"
Terror["12"] = "Poltergeist"
Terror["10"] = "ParaNorman"
Terror["Livre"] = "A Casa Monstro"

Açao = {}

Açao["18"] = "Rambo: Até o Fim"
Açao["16"] = "Lucy"
Açao["14"] = "Venom"
Açao["12"] = "Duro de Matar: Um Bom Dia Para Morrer"
Açao["10"] = "Bumblebee"
Açao["Livre"] = "Pequenos Espiões"

Animaçao = {}

Animaçao["18"] = "para 18"
Animaçao["16"] = "para 16"
Animaçao["14"] = "para 14"
Animaçao["12"] = "para 12"
Animaçao["10"] = "para 10"
Animaçao["Livre"] = "Livre"

Ficçao_Cientifica = {}

Ficçao_Cientifica["18"] = "para 18"
Ficçao_Cientifica["16"] = "para 16"
Ficçao_Cientifica["14"] = "para 14"
Ficçao_Cientifica["12"] = "para 12"
Ficçao_Cientifica["10"] = "para 10"
Ficçao_Cientifica["Livre"] = "Livre"

Romance = {}

Romance["18"] = "Jogo Perigoso"
Romance["16"] = "Cinquenta Tons de Cinza"
Romance["14"] = "Titanic"
Romance["12"] = "Nerve - Um jogo Sem Regras"
Romance["10"] = "O Amor Não Tira Férias"
Romance["Livre"] = "Legalmente Loira"

Suspense = {}

Suspense["18"] = "Scarface"
Suspense["16"] = "Parasita"
Suspense["14"] = "Tubarão"
Suspense["12"] = "Truque de Mestre"
Suspense["10"] = "O Mistério das Palavras Cruzadas"
Suspense["Livre"] = "para todos"

idade = int(input("qual a sua idade? "))
tipo = input("insira o tipo ")

if tipo == "Drama":
  genero = Drama
  classificacao()

if tipo == "comedia":
  genero = Comedia
  classificacao()

if tipo == "terror":
  genero = Terror
  classificacao()

if tipo == "açao":
  genero = Açao
  classificacao()

if tipo == "animaçao":
  genero = Animaçao
  classificacao()

if tipo == "ficçao cientifica":
  genero = Ficçao_Cientifica
  classificacao()

if tipo == "romance":
  genero = Romance
  classificacao()

if tipo == "suspense":
  genero = Suspense
  classificacao()
 
#http://www.w3schools.com/colors/colors_names.asp site mudar cor
  
