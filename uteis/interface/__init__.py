def menu(listas):
    print('*='*30)
    print('')
    print ('code                    Serviços')
    for c in range(0,len(listas)):
        print(f'  {c+1} - {listas[c]}')
    print('')
    print('*='*30)

    
def menu2(listas,txt):
    print('*='*30)
    print('')
    print (f'code                    {txt.upper()}')
    print('')
    print('*='*30)
    for k, v in enumerate(listas):
        print(f'  {k} - {listas[k]["item"]}')
    print('')
    print('*='*30)

    
    