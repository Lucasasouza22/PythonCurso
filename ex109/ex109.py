import moedas109

n = float(input('Digite um numeroex113: '))
sif = moedas109.sifrao(n)
print(f'O dobro vale {sif} {moedas109.dobro(n):.2f}')
print(f'Com 10% de desconto vai valer {sif} {moedas109.desconta10(n,10):.2f}')
print(f'A metade vale {sif} {moedas109.metade(n):.2f}')
print(f'Aumentando 20% vai valer {sif} {moedas109.aumenta20(n,20):.2f}')
