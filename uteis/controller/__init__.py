from uteis import interface,source


def escolhaCategoria():
    esc = escolhaServico()
    interface.menu2(source.lista[esc-1],source.servicos[esc -1])
    esc2 = escolhaServico()
    interface.detalhaItem(source.lista[esc -1],esc2)
  
    

def escolhaServico():
    esc = int(input('\033[32mEscolha uma opção: \033[m'))
    return esc
   
    
    
    
        
        

