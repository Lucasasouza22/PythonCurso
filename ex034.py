salario = float(input('Digite o valor do seu salario: R$'))
salariof = (salario*0.10)+salario if salario >= 1250 else (salario*0.15)+salario
print('O seu novo salario é R$ {}'.format(salariof))