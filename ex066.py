s = cont = 0
while True:
    n = int(input('Digite um numeroex113 [999 para o programa]: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'A soma dos {cont} valores digitados é {s}.')