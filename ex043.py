peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso/(altura**2)
print('Seu IMC é {:.2f}.'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc < 25:
    print('Você está no peso ideal.')
elif imc < 30:
    print('Você está com sobre peso.')
elif imc < 40:
    print('Você está com obesidade.')
elif imc >= 40:
    print('Você está MORBIDO.')