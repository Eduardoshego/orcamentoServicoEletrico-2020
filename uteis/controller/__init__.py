from uteis import interface,source


def escolha():
    esc = int(input('Escolha uma opção: '))
    if esc == 1:
        interface.menu2(source.iluminacao,source.servicos[esc -1])
    elif esc == 2:
        interface.menu2(source.pontoUtilizacao,source.servicos[esc -1])
    elif esc == 3:
        interface.menu2(source.qdc,source.servicos[esc -1])
    elif esc == 4 :
        interface.menu2(source.passagemcabo20m,source.servicos[esc -1])
    elif esc == 5:
        interface.menu2(source.soluceletrica,source.servicos[esc -1])
    elif esc == 6:
        interface.menu2(source.servicos,source.servicos[esc -1])
        
        

