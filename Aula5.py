# def Myname(x, y):
#   return print(x + y)

# Myname(2, 3)


# def box(name):
#   tam = len(name)
#   if tam:
#     print('-'*(tam+4))
#     print('|',name,'|')
#     print('-'*(tam+4))


# box("Mateus")

# def baricuti(baricutil, pinguin = 0):
#   print(baricutil)
#   return print(pinguin)

# nome = baricuti('mateus', 'Costa')
# print(nome)

# def PrintName(fullName):
#       print(fullName)
# def Name():
#   fullName = input('Escreva seu nome completo: ')
#   tam = len(fullName)
#   if(tam > 10):
#     Name()
#   else:
#     PrintName(fullName)
# Name()
# help(print)
# def soma(x,y):
#   """
#   """


#   return print(x+y)

# soma(5,5)
# help(soma)

# def fatorial(n):
#   fat = 1
#   if(n==0):
#     return print(fat)

#   for i in range(1, n+1):
#     fat*=i
#   return print(fat)

# n = int(input('Digite um número para ver o fatorial do mesmo: '))
# if(n<0):
#   print('Numero inválido')

# else: 
#   fatorial(n)







# EXERCÍCIO LENDO ARQUIVO 

def validaInput(pergunta, max, min):
  n = int(input(pergunta))
  while (n<min or n>max):
    n = int(input(pergunta))
  return n


def existeArquivo(nomeArquivo):
  try:
    a = open(nomeArquivo, 'rt')
    a.close()
  except FileNotFoundError:
    return False
  else:
    return True


def criarArquivo(NomeArquivo):
  try:
    a = open(NomeArquivo, 'wt+')
    a.close()
  except:
    print('Erro na criação do arquivo!')
  else:
    print('Arquivo {} foi criado com sucesso'.format(NomeArquivo))

def cadastrarJogo(NomeArquivo, NomeJogo, NomeVideoGame):
  try:
    a = open(NomeArquivo, 'at')
  except:
    print('Erro ao abrir o arquivo')
  else:
    a.write('{}  {}\n'.format(NomeJogo, NomeVideoGame))
    print('Cadastro realizado com sucesso!')
  finally:
    a.close()

def listarArquivo(NomeArquivo):
  try:
    a = open(NomeArquivo, 'rt')
  except:
    print('Erro ao ler o arquivo')
  else: 
    print(a.read())
  finally:
    a.close()

arquivo = 'Games Txt'

if existeArquivo(arquivo):
  print('Arquivo localizado com sucesso!')
else: 
  # print('Não existe arquivo!')
  criarArquivo(arquivo)



while True:
  print('MENU')
  print('1- Cadastrar novo ítem')
  print('2- Listar ítens')
  print('3- Sair')
  op = validaInput('Escolha a opção desejada: ', 3, 1)
  if(op == 1):
    jogo = input('Digite o nome do Jogo: ')
    videoGame = input('Digite o nome do Video Game:')
    if(jogo and videoGame):
      cadastrarJogo(arquivo, jogo, videoGame)
      break
    else: 
      print('Insira os dados corretamente!!!!!')
      continue
  elif(op == 2):
    listarArquivo(arquivo)
    break
  elif(op == 3):
    print('Encerrando o programa')
    break