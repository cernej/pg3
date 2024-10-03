# funkce demonstrujici cyklus while
def stars_while():
    print('zacatek')
    
    i = 0
    while i<5:
        print('*')
        i += 1

    print('konec')


# funkce demonstrujici cyklus for
def stars_for():
    print('zacatek')

    for i in range(5):
        print('*', i)

    print('konec')


# funkce urcujici, zda number lezi mezi min_number a max_number
def in_range(min_nuber, max_number, number):
    if number >= min_nuber and number <= max_number:
        print('Is in range')
    else:
        print('Is not in range')

#in_range(100, 1000, 2000)


# funkce vypise "Ahoj jmeno"
def zobraz_pozdrav(jmeno):
    print('Ahoj', jmeno)


jm = input("Zadej jmeno: ")
zobraz_pozdrav(jm)