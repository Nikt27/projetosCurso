limitVel = int(80)
print('--------------------------------------')
print('-- O limite de velocidade para essa --')
print('--         80         Km/h          --')
print('--------------------------------------')
velAt=int(input('Digite sua velocidade atual: '))
if velAt>limitVel:
    multa=(limitVel-velAt)*6.85
    print(f'Você foi multado por excesso de velocidade. Pague a taxa de {round(multa,2)} rapidamente!')
elif velAt<40:
    multa=(40-velAt)*6.85
    print(f'Você foi multado por baixa velocidade. Pague a taxa de {round(multa, 5)} rapidamente!')
else:
    print('Pode continuar na estrada, amigo')
