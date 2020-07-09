def menu(listas):
    print('\033[32m*=\033[m'*30)
    print('')
    print ('\033[33mcode                    Categoria\033[m')
    print('')
    print('\033[32m*=\033[m'*30)
    print('')
    for c in range(0,len(listas)):
        print(f'  \033[31m{c+1}\033[m - \033[34m{listas[c]}\033[m')
    print('')
    print('\033[32m*=\033[m'*30)
    

    
def menu2(listas,txt):
    print('\033[32m*=\033[m'*30)
    print('')
    print (f'\033[33mcode                    {txt.upper().center(10)}\033[m')
    print('')
    print('\033[32m*=\033[m'*30)
    print('')
    for k, v in enumerate(listas):
        print(f'  \033[31m{k}\033[m - \033[34m{listas[k]["item"]}\033[m')
    print('')
    print('\033[32m*=\033[m'*30)

def detalhaItem(lista, x):
    txt = lista[x]["item"]
    print('\033[32m*=\033[m'*30)
    print('')
    print(f'\033[33m{txt.center(60).upper()}\033[m')
    print('')
    print('\033[32m*=\033[m'*30)
    print('')
    print('\033[33mSem passagem de cabos\033[m')
    print('+='*15)
    print('')
    print(f'\033[31m 1 \033[m - \033[34m unidade:\033[m \033[31m R$ {lista[x]["preco"]:.2f}\033[m')
    print(f'\033[31m 3 \033[m - \033[34m unidades:\033[m \033[31mR$ {lista[x]["preco2"]:.2f}\033[m')
    print('')
    print('+='*15)
    print('\033[33mcom passagem de cabos\033[m')
    print('+='*15)
    print('')
    print(f'\033[31m 1 \033[m - \033[34munidade:\033[m \033[31m R$ {lista[x]["preco1"]:.2f}\033[m')
    print(f'\033[31m 3 \033[m - \033[34munidades:\033[m \033[31mR$ {lista[x]["preco3"]:.2f}\033[m')
    print('')
    print('+='*15)
    print('')
    print('\033[32m*=\033[m'*30)
    
    

    
    