def leiadinheiro(msg):
    while True:
        k = str(input(msg))
        k = k.replace(',','.')
        if k.isnumeric():
            return float(k)
        else:
            print(f'\033[0;31mERRO! O valor digitado não é valido!\033[m')




