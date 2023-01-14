# x = 1

# while(x<=5):
#   print(x)
#   x+=1

  # Variável de controle é o x, também chamada de Iterador

# x=0

# while(x<=100):
#   if(x%2 == 0):
#    print(x)
#   x+=1


# soma = 0 
# cont = 1
# while(cont <= 5):
#   nota = float(input('Digite sua nota: '))
#   soma+=nota
#   cont+=1

# print(soma / 5)

# cont = 0
# numero = 0
# while(cont == 0):
#   numero = float(input('Digite um número: '))
#   if(numero <= 0 or numero ):
#     cont = 0
#   else:
#     print(numero)
#     cont+=1
    
# print('Para sair digite sair')
# while True: 
#   text = input('Digite: ')
#   if(text == 'Sair'):
#     break
#   print(text)

# print('Faça o Login')

# while True:
#   Nome = input('Nome do usuário: ')
#   if(Nome != 'Mateus'):
#     print('Usuário {} não existe'.format(Nome))
#     continue
#   Senha = input('Digite sua senha: ')
#   if(Senha != '123'):
#     print('Senha incorreta')
#     continue
#   print('Usuário Logado!')
#   break

# Para a variável i no intervalo de 6, comaçando com i=1 e acrescentando 1 em i a cada repetição
# for i in range (1, 6, 1):
#   print(i)
# soma=0
# qtd=0

# for i in range(1,101):
#   if(i%2==0):
#     soma+=i
#     qtd+=1
  
# print(soma/qtd)

# print('Tabuada')
# for x in range(0,11,1):
#   print('Tabuada do {}'.format(x))
#   for y in range(0,11,1):
#     print(x, ' x ', y, '= ', x*y)
# n=3
# while(n <=12):
#   print(n)
#   n+=1
# for i in range(0, 9, 2):
#   print(i)

# while True:
#   n1 = float(input('Escolha um número: '))
#   n2 = float(input('Escolha outro número: '))
#   op = input('Escolha a operação que deseja realizar: ')
#   if(op == '*'):
#     print(n1 * n2)
#   if(op == '/'):
#     print(n1 / n2)
#   if(op == '+'):
#     print(n1 + n2)
#   if(op == '-'):
#     print(n1 - n2)

#   exit = input('Para sair, digite y: ')
#   if(exit == 'y'):
#     break
#   continue

# dinheiro = 0 
# pessoas = 0
# print("Para sair, digite 'sair' ou digite a idade do cliente: ")
# while True:
  
#   age = input('Digite sua idade: ')
#   if(age == 'sair'):
#     print('Total: {}'.format(dinheiro))
#     print(pessoas, ' Pessoas')
#     break
#   pessoas+=1
#   age = int(age)

#   if(age<3):
#     print('Ingresso gratuito')
#   elif(age>=3 and age<=12):
#     print('Entrada: R$15,00')
#     dinheiro+=15
#   elif(age>12):
#     print('Entrada: R$30,00')
#     dinheiro+=30