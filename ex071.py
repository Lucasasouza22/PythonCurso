print('='*4,' Seja bem vindo ao Banco PAPACU! ','='*4)
saque = int(input('Qual valor você deseja sacar: R$ '))
cont50 = cont20 = cont2 = cont1 = resto = 0
while True:
    resto = saque
    if resto >= 50:
        while resto >= 50:
            resto -= 50
            cont50 += 1
    if resto >= 20:
        while resto >= 20:
            resto -= 20
            cont20 += 1
    if resto >= 2:
        while resto >= 2:
            resto -= 2
            cont2 += 1
    if resto >= 1:
        while resto >= 1:
            resto -= 1
            cont1 += 1
    if resto == 0:
        break
print(f'Total de {cont50} cedulas de R$ 50,00')
print(f'Total de {cont20} cedulas de R$ 20,00')
print(f'Total de {cont2} cedulas de R$ 2,00')
print(f'Total de {cont1} cedulas de R$ 1,00')
print('='*4,'Obrigado pela preferência. Volte sempre!','='*4)
