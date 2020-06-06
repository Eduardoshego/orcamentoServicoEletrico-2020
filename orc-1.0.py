print('Programa de orçamento de serviços eletricos /2020')
iluminacao = [

    {
        'item':'LÂMPADA FLUORESCENTE/ LED COMUM',
        'preco':'30.00',
        'preco1':'45.00',
        'preco2':'24.00',
        'preco3':'36.00'
    },
    {
        'item':'ARANDELA OU SPOT COMUM/ DUPLO/ TRIPLO',
        'preco':'30.00',
        'preco1':'45.00',
        'preco2':'24.00',
        'preco3':'36.00'
    },
    {
        'item':'LÂMPADA FLUORESCENTE/ LED (TUBULAR)',
        'preco':'30.00',
        'preco1':'45.00',
        'preco2':'24.00',
        'preco3':'36.00'
    },
    {
        'item':'LUSTRES SIMPLES / LUMINÁRIA',
        'preco':'40.00',
        'preco1':'60.00',
        'preco2':'32.00',
        'preco3':'48.00'
    },
    {
        'item':'LUSTRES GRANDES / LUMINÁRIA',
        'preco':'90.00',
        'preco1':'135.00',
        'preco2':'72.00',
        'preco3':'108.00'
    },
    {
        'item':'REFLETOR DE JARDIM',
        'preco':'40.00',
        'preco1':'60.00',
        'preco2':'32.00',
        'preco3':'48.00'
    },
    {
        'item':'REFLETOR DE POSTE COMUM',
        'preco':'50.00',
        'preco1':'75.00',
        'preco2':'40.00',
        'preco3':'60.00'
    },
    {
        'item':'REFLETOR DE POSTE COM LÂMPADA A VAPOR',
        'preco':'90.00',
        'preco1':'135.00',
        'preco2':'72.00',
        'preco3':'108.00'
    },
    {
        'item':'INTERRUPTOR SIMPLES',
        'preco':'20.00',
        'preco1':'30.00',
        'preco2':'16.00',
        'preco3':'24.00'
    },
    {
        'item':'INTERRUPTOR TREE-WAY/ FOUR WAY',
        'preco':'30.00',
        'preco1':'45.00',
        'preco2':'24.00',
        'preco3':'36.00'
    },
    {
        'item':'INTERRUPTOR DUPLO/ BIPOLAR',
        'preco':'30.00',
        'preco1':'45.00',
        'preco2':'24.00',
        'preco3':'36.00'
    },
    {
        'item':'INTERRUPTOR E TOMADA',
        'preco':'30.00',
        'preco1':'45.00',
        'preco2':'24.00',
        'preco3':'36.00'
    },
    {
        'item':'REATOR DE LÂMPADA A VAPOR',
        'preco':'50.00',
        'preco1':'75.00',
        'preco2':'40.00',
        'preco3':'60.00'
    },
    {
        'item':' FOTOCÉLULA / SENSOR PRESENÇA',
        'preco':'40.00',
        'preco1':'60.00',
        'preco2':'32.0  0',
        'preco3':'48.00 '
    },
    {
        'item':'REFLETOR LED + FOTOCÉLULA ou SENSOR DE PRESENÇA',
        'preco':'60.00',
        'preco1':'90.00',
        'preco2':'48.00',
        'preco3':'72.00'
    },
    {
        'item':'LUMINÁRIA DE EMERGÊNCIA DE SOBREPOR',
        'preco':'30.00',
        'preco1':'45.00',
        'preco2':'24.00',
        'preco3':'36.00'
    },
    {
        'item':'LUMINÁRIA DE EMERGÊNCIA DE EMBUTIR caixinha 2x4',
        'preco':'30.00',
        'preco1':'45.00',
        'preco2':'24.00',
        'preco3':'36.00'
    },
    {
        'item':' LUMINÁRIA TUBULAR - TROCA SISTEMA DE REATOR PARA LED',
        'preco':'40.00',
        'preco1':'60.00',
        'preco2':'32.00',
        'preco3':'48.00'
    }
]
# for itens in iluminacao:
#     print(f'Descrição {itens["item"]}')
#     print(f'sem passagem de cabo R${itens["preco"]}')
#     print(f'com passagem de cabo R${itens["preco1"]}')
#     print('')
#     print('Acima de 3 unidades')
#     print(f'Sem passagem de cabo R${itens["preco2"]}')
#     print(f'Com passagem de cabos R${itens["preco3"]}')
#     print('-='*30)


pontoUtilizacao = {}
qdc = {}
passagemcabo20m = {}
soluceletrica = {}
cond = 99
cont = 1

while True:
    if cond == 0:
        break
    print('Escolha uma opção abaixo para orçar ou digite 0 para sair:\n')
    print('1-Iluminação')
    print('2-Pontos de ultilização (tomadas)')
    print('3-QDC (Quadros de distribuição) ')
    print('4-Passagem de cabos (*circuitos até 20 metros)')
    print('5-Soluções de problemas')
    cond = int(input('Digite o número correspondente\n'))
    if cond == 1:
        while True:
            print('-=*'*30)
            print('cod            Serviço')
            print('-'*60)
            for k, v in enumerate(iluminacao):
               print(f'{k} - {v["item"]}')
            print('-=*'*30)
            esc = int(input('Digite o codigo de um serviço para iniciar o orçamento: '))
            if esc >= len(iluminacao):
                print('Erro esse código de serviço não existe.')
            while True:
                resp = str(input('Deseja continuar em iluminação[S/N]?')).upper()[0]
                if resp in 'SN':
                    break
                print('Erro responda S OU N')
            if resp == 'N':
                break     








