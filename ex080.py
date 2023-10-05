valores = []
for c in range(0, 5):
    n = int(input(f'Digite o {c+1}º numero:'))
    if c == 0 or n > valores[-1]:
        valores.append(n)
        print('O valor foi adicionado no final da fila.')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'O valor foi adicionado na posição \033[1:30:41m{pos}º\033[m!')
                break
            pos += 1
print(f'Segue a sua lista de valores: {valores}')