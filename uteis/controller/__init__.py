from uteis import interface,source

def escolhaServico():
    esc = int(input('\033[32mEscolha uma opção: \033[m'))
    return esc

def escolhaCategoria():
    esc = escolhaServico()
    if esc != 6 :
        interface.menu2(source.lista[esc-1],source.servicos[esc -1])
        esc2 = escolhaServico()
        interface.detalhaItem(source.lista[esc -1],esc2)
    else:
        interface.menu(source.servicos[0:-2])
        esc = escolhaServico()
        for c in range(0,len(source.lista[esc-1])):
            interface.detalhaItem(source.lista[esc-1],c)
    


   
    
    
    
        
        

