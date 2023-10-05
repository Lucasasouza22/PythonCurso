import moedas

n = float(input('Digite um numeroex113: '))
sif = moedas.sifrao(n)
print(f'O dobro vale {sif} {moedas.dobro(n):.2f}')
print(f'Com 10% de desconto vai valer {sif} {moedas.desconta10(n):.2f}')
print(f'A metade vale {sif} {moedas.metade(n):.2f}')
print(f'Aumentando 20% vai valer {sif} {moedas.aumenta20(n):.2f}')
