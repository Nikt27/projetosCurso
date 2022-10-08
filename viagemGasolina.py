viagem=int(input('Qual a distância da sua viagem? '))
if viagem<200:
    print(f'O preço da viagem de {viagem}Km/h será {(viagem*0.5)}')
elif viagem>=200:
    print(f'O preço da viagem de {viagem}Km/h será {(viagem * 0.45)}')
else:
    print('Acredito que você não entendeu o que fazer, tente novamente')