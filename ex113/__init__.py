def leiainteiro(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO! Digite um valor inteiro!\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[0;31mUsuario não quis fornecer esse valor.\033[m')
            return 0
        else:
            return n
def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO! Digite um valor inteiro!\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[0;31mUsuario não quis fornecer esse valor.\033[m')
            return 0
        else:
            return n
