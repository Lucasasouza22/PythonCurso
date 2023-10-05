f = str(input('Digite uma frase: ')).strip().upper()
separa = f.split()
print(separa)
junta = ''.join(separa)
print(junta)
reverso = junta[::2]
print(reverso)

'''for c in range(1):
    rev = reversed(junta)
    print(rev)
    if f == rev:
        print('É UM PALINDROMO.')
    else:
        print('NÃO É UM PALINDROMO')'''