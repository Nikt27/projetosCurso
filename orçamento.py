import random
salario=float(random.randint(400,900))
print(f'Seu salário desse mês é de {salario} reais')
gasto=float(input('Quanto você gastará do seu salário para pagar as contas mensais? '))
salAtual=(salario-gasto)
resp=lower(input('Deseja gastar mais? '))
if salAtual > 10:
    while = resp==('sim'):
        if salAtual > 10:
            resp=lower(print('Deseja gastar mais? '))
        else:
            print('Você não tem dinheiro.')
            upper(resp)
elif salAtual <=10 and >=0:
    print('Você gastou seu salário por esse mês')
else:
    print(f'Você gastou {salAtual*-1} mais do que deveria, sua dívida é de {salAtual}')