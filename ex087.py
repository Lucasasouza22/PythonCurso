matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um numero para a  matriz [{l},{c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end=' ')
    print()
par = []
somapar = 0
impar = []
somaimpar = 0
for l in range(0,3):
    for c in range(0,3):
        calc = matriz[l][c] % 2
        if calc == 0:
            par.append(matriz[l][c])
            somapar += matriz[l][c]
print(f'A lista de numeros pares dessa matriz são: {par} e a soma vale {somapar}!')
print(f'Lista de valores da 3º coluna é {matriz[0][2],matriz[1][2],matriz[2][2]} e a soma vale {matriz[0][2]+matriz[1][2]+matriz[2][2]}')
print(f'Lista de valores da 3º linha é {matriz[2][0],matriz[2][1],matriz[2][2]} e o maior valor é {max(matriz[2][0],matriz[2][1],matriz[2][2])}')
