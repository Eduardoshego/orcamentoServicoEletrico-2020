from uteis import interface,source


def escolhaCategoria():
    esc = int(input('Escolha uma opção: '))
    if esc == 1:
        interface.menu2(source.iluminacao,source.servicos[esc -1])
        escolhaServico(source.iluminacao)
    elif esc == 2:
        interface.menu2(source.pontoUtilizacao,source.servicos[esc -1])
        escolhaServico(source.pontoUtilizacao)
    elif esc == 3:
        interface.menu2(source.qdc,source.servicos[esc -1])
        escolhaServico(source.qdc)
    elif esc == 4 :
        interface.menu2(source.passagemcabo20m,source.servicos[esc -1])
        escolhaServico(source.passagemcabo20m)
    elif esc == 5:
        interface.menu2(source.soluceletrica,source.servicos[esc -1])
        escolhaServico(source.soluceletrica)
    elif esc == 6:
        interface.menu2(source.servicos,source.servicos[esc -1])
        escolhaServico(source.s)
    

def escolhaServico(lista):
    esc = int(input('\033[32mEscolha uma opção: \033[m'))
    interface.detalhaItem(lista,esc)
    
    
    
        
        

