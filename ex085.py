'''list = []
for c in range(0,7):
    n = float(input(f'Digite {c+1}º numeroex113: '))
    list.append(n)
print(f'Segue a lista de numeros pares: ', end='')
ordem = sorted(list)
for numeroex113 in ordem:
    if numeroex113 % 2 == 0:
        print(f'[{numeroex113:.0f}]',end=' ')
print()
print(f'Segue a lista de numeros impares: ', end='')
for numeroex113 in ordem:
    if numeroex113 % 2 != 0:
        print(f'[{numeroex113:.0f}]',end=' ')'''
#minha solução acima!

list = [[],[]]
for c in range(0,7):
    n = int(input(f'Digite {c+1}º numeroex113: '))
    calc = n % 2
    if calc == 0:
        list[0].append(n)
    else:
        list[1].append(n)
par = sorted(list[0][:])
impar = sorted(list[1][:])
print(f'Segue a lista de numeros pares: {par}')
print(f'Segue a lista de numeros impares: {impar}')

#Segunda solução minha