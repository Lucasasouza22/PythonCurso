numero = int(input('Escolha um numeroex113 inteiro: '))
base = int(input('Escolha qual sera a base de conversão: \n[1] BINARIO\n[2] OCTAL \n[3] HEXADECIMAL\nSua opção: '))
if base == 1:
    print('{} convertido em um numeroex113 BINARIO vale {}.'.format(numero, bin(numero)[2:]))
elif base == 2:
    print('{} convertido em um numeroex113 OCTAL vale {}.'.format(numero, oct(numero)[2:]))
elif base == 3:
    print('{} convertido em um numeroex113 HEXADECIMAL vale {}.'.format(numero, hex(numero)[2:]))
else:
    print('Esta opção é ivalida! Tente novamente.')