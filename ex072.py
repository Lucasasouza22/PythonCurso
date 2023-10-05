n = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
escolha = ' '
while True:
    mais = ' '
    escolha = int(input('Digite um numeroex113 inteiro de 0 ate 20 para ve-lo escrito na tela: '))
    if escolha < 0 or escolha > 20:
        print('\033[4:30:41mValor invalido! Digite um valor inteiro entre 0 e 20!\033[m')
    print(f'Você pediu por extenso o numeroex113 {n[escolha]}')
    mais = str(input('Deseja ver outro numeroex113 [S/N]: ')).strip().upper()[0]
    if mais == 'N':
        break
print('FIM')
