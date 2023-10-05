from datetime import date
ano = int(input('Qual é o ano que você nasceu? '))
opcao = int(input('Você é do sexo: \n[1] Masculino \n[2] Feminino \nSua opção: '))
idade = date.today().year - ano
if opcao == 1 and idade == 18:
    print('Você é do sexo masculino!')
    print('Você tem {} anos.'.format(idade))
    print('Chegou a hora de se alistar. Procure a junta militar mais proxima.')
elif opcao == 1 and idade > 18:
    print('Você é do sexo masculino!')
    print('Você tem {} anos.'.format(idade))
    print('Chegou a hora de se alistar. Procure a junta militar mais proxima.')
elif opcao == 1 and idade < 18:
    print('Você é do sexo masculino!')
    print('Você tem {} anos.'.format(idade))
    print('Seu alistamento sera no ano {}.'.format(ano + 18))
elif opcao == 2 and idade == 18:
    print('Você é do sexo feminino!')
    print('Você tem {} anos.'.format(idade))
    print('Seu alistamento não é obrigatorio, mas caso queira servir chegou a hora. Procure a junta militar mais proxima.')
elif opcao == 2 and idade > 18:
    print('Você é do sexo feminino!')
    print('Você tem {} anos.'.format(idade))
    print('Seu alistamento seria no ano de {}, mas não era obrigatorio por você ser do sexo feminino!'.format(ano + 18))
elif opcao == 2 and idade < 18:
    print('Você é do sexo feminino!')
    print('Você tem {} anos.'.format(idade))
    print('Seu alistamento sera no ano de {}, mas não é obrigatorio por você ser do sexo feminino!'.format(ano + 18))

