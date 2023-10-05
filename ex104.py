def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! O valor digitado não é um numeroex113.\033[m')
        if ok:
            break
    return valor


n = leiaint('Digite um numeroex113: ')
print(f'Você digitou o numeroex113 {n}.')

