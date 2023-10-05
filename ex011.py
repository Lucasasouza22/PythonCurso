n1 = float(input('Digite a largura metros: '))
n2 = float(input('Digite a altura em metros: '))
print(('Sua parede tem uma largura de {}m e uma altura de {}m, obtendo apartir desses parametros a seguinte area {:.2f}m²'.format(n1, n2, n1*n2)))
print('Como a nossa tinta tem um rendimento de 2m² por litro, será necessario {:.2f}L de tinta.'.format((n1*n2)/2))