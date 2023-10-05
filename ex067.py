while True:
    print('='*60)
    t = int(input('Quer ver a tabuada de qual valor: '))
    print('=' * 30)
    if t < 0:
        break
    for c in range(1 , 11):
        m = c*t
        print(f'{c} x {t} = {m}')
print('FIM')