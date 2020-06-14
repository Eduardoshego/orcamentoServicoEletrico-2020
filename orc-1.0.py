print('Programa de orçamento de serviços eletricos /2020')
iluminacao = [

    {
        'item':'LÂMPADA FLUORESCENTE/ LED COMUM',
        'preco':30.00,
        'preco1':45.00,
        'preco2':24.00,
        'preco3':36.00
    },
    {
        'item':'ARANDELA OU SPOT COMUM/ DUPLO/ TRIPLO',
        'preco':30.00,
        'preco1':45.00,
        'preco2':24.00,
        'preco3':36.00
    },
    {
        'item':'LÂMPADA FLUORESCENTE/ LED (TUBULAR)',
        'preco':30.00,
        'preco1':45.00,
        'preco2':24.00,
        'preco3':36.00
    },
    {
        'item':'LUSTRES SIMPLES / LUMINÁRIA',
        'preco':40.00,
        'preco1':60.00,
        'preco2':32.00,
        'preco3':48.00
    },
    {
        'item':'LUSTRES GRANDES / LUMINÁRIA',
        'preco':90.00,
        'preco1':135.00,
        'preco2':72.00,
        'preco3':108.00
    },
    {
        'item':'REFLETOR DE JARDIM',
        'preco':40.00,
        'preco1':60.00,
        'preco2':32.00,
        'preco3':48.00
    },
    {
        'item':'REFLETOR DE POSTE COMUM',
        'preco':50.00,
        'preco1':75.00,
        'preco2':40.00,
        'preco3':60.00
    },
    {
        'item':'REFLETOR DE POSTE COM LÂMPADA A VAPOR',
        'preco':90.00,
        'preco1':135.00,
        'preco2':72.00,
        'preco3':108.00
    },
    {
        'item':'INTERRUPTOR SIMPLES',
        'preco':20.00,
        'preco1':30.00,
        'preco2':16.00,
        'preco3':24.00
    },
    {
        'item':'INTERRUPTOR TREE-WAY/ FOUR WAY',
        'preco':30.00,
        'preco1':45.00,
        'preco2':24.00,
        'preco3':36.00
    },
    {
        'item':'INTERRUPTOR DUPLO/ BIPOLAR',
        'preco':30.00,
        'preco1':45.00,
        'preco2':24.00,
        'preco3':36.00
    },
    {
        'item':'INTERRUPTOR E TOMADA',
        'preco':30.00,
        'preco1':45.00,
        'preco2':24.00,
        'preco3':36.00
    },
    {
        'item':'REATOR DE LÂMPADA A VAPOR',
        'preco':50.00,
        'preco1':75.00,
        'preco2':40.00,
        'preco3':60.00
    },
    {
        'item':'FOTOCÉLULA / SENSOR PRESENÇA',
        'preco':40.00,
        'preco1':60.00,
        'preco2':32.00,
        'preco3':48.00
    },
    {
        'item':'REFLETOR LED + FOTOCÉLULA ou SENSOR DE PRESENÇA',
        'preco':60.00,
        'preco1':90.00,
        'preco2':48.00,
        'preco3':72.00
    },
    {
        'item':'LUMINÁRIA DE EMERGÊNCIA DE SOBREPOR',
        'preco':30.00,
        'preco1':45.00,
        'preco2':24.00,
        'preco3':36.00
    },
    {
        'item':'LUMINÁRIA DE EMERGÊNCIA DE EMBUTIR caixinha 2x4',
        'preco':30.00,
        'preco1':45.00,
        'preco2':24.00,
        'preco3':36.00
    },
    {
        'item':'LUMINÁRIA TUBULAR - TROCA SISTEMA DE REATOR PARA LED',
        'preco':40.00,
        'preco1':60.00,
        'preco2':32.00,
        'preco3':48.00
    }
]
pontoUtilizacao = [
    {
        'item':'TOMADA SIMPLES',
        'preco':20.00,
        'preco1':30.00,
        'preco2':16.00,
        'preco3':24.00
    },
    {
        'item':'TOMADA DUPLA',
        'preco':30.00,
        'preco1':45.00,
        'preco2':24.00,
        'preco3':36.00
    },
    {
        'item':'TOMADA TRIPLA',
        'preco':40.00,
        'preco1':60.00,
        'preco2':32.00,
        'preco3':48.00
    },
    {
        'item':'TOMADA DE PISO E/OU TELEFONE',
        'preco':40.00,
        'preco1':60.00,
        'preco2':32.00,
        'preco3':48.00
    },
    {
        'item':'INSTALAÇÃO TOMADA DE SOBREPOR COM CANALETA',
        'preco':40.00,
        'preco1':60.00,
        'preco2':32.00,
        'preco3':48.00
    },
    {
        'item':'CHAVE DE BÓIA SUPERIOR E INFERIOR ( EM RESIDÊNCIA )',
        'preco':60.00,
        'preco1':90.00,
        'preco2':48.00,
        'preco3':72.00
    },
    {
        'item':'VENTILADOR DE TETO',
        'preco':  90.00,
        'preco1':135.00,
        'preco2': 72.00,
        'preco3':108.00
    },
    {
        'item':'VENTILADOR DE PAREDE',
        'preco':50.00,
        'preco1':75.00,
        'preco2':40.00,
        'preco3':60.00
    },
    {
        'item':'CHUVEIRO ELÉTRICO SIMPLES',
        'preco':50.00,
        'preco1':75.00,
        'preco2':40.00,
        'preco3':60.00
    },
    {
        'item':'CHUVEIRO LUXO (Eletrônico/ Pressurizado/ Ducha)',
        'preco':100.00,
        'preco1':150.00,
        'preco2':80.00,
        'preco3':120.00
    },
    {
        'item':'TORNEIRA ELÉTRICA',
        'preco':50.00,
        'preco1':75.00,
        'preco2':40.00,
        'preco3':60.00
    },
    {
        'item':'CAMPAINHA ATÉ 20 MTS',
        'preco':50.00,
        'preco1':75.00,
        'preco2':40.00,
        'preco3':60.00
    },
    {
        'item':'INTERFONE 1 CHAMADA',
        'preco':90.00,
        'preco1':135.00,
        'preco2':72.00,
        'preco3':108.00
    },
    {
        'item':'INTERFONE 2 CHAMADAS',
        'preco':170.00,
        'preco1':255.00,
        'preco2':136.00,
        'preco3':204.00
    },
    {
        'item':'INTERFONE 4 CHAMADAS',
        'preco':300.00,
        'preco1':450.00,
        'preco2':240.00,
        'preco3':360.00
    },
    {
        'item':'VIDEO PORTEIRO',
        'preco':150.00,
        'preco1':225.00,
        'preco2':120.00,
        'preco3':180.00
    },
    {
        'item':'CÂMERAS CFTV 1 CÂMERA',
        'preco':80.00,
        'preco1':120.00,
        'preco2':64.00,
        'preco3':96.00
    },
    {
        'item':'CÂMERAS CFTV 3 CÂMERAS + DVR',
        'preco':150.00,
        'preco2':225.00
    },
    {
        'item':'PORTAO ELETRÔNICO DESLIZANTE',
        'preco':200.00,
        'preco1':300.00,
        'preco2':160.00,
        'preco3':240.00
    },
    {
        'item':'PORTAO ELETRÔNICO PIVONTANTE E / OU BASCULANTE',
        'preco':370.00,
        'preco1':555.00,
        'preco2':296.00,
        'preco3':444.00
    },
    {
        'item':'BOTOEIRA para FECHADURA ELETRÔNICA ( Portão Social )',
        'preco':40.00,
        'preco1':60.00,
        'preco2':32.00,
        'preco3':48.00
    },
    
    {
    'item':'FECHADURA ELETRÔNICA ( Portão Social )',
        'preco':120.00,
        'preco1':180.00,
        'preco2':96.00,
        'preco3':144.00
    },
    {
    'item':'EXAUSTOR COZINHA OU BANHEIRO',
        'preco':170.00,
        'preco1':255.00,
        'preco2':136.00,
        'preco3':204.00
    }
]
qdc = {}
passagemcabo20m = {}
soluceletrica = {}
cond = 99
cont = 1
dados = list()
orc = list()
total = 0

while True:
    if cond == 0:
        break
    print('Escolha uma opção abaixo para orçar ou digite 0 para encerrar o orçamento:\n')
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
            print()
            if esc > len(iluminacao):
                print(f'Erro! Não existe serviço com o codigo {esc}')
            else:
                print('-='*30)
                print(f'codigo do serviço: {esc} ')
                print(f'Descrição do serviço:{iluminacao[esc]["item"]}')
                print('-='*30)
                print('')
                print(f'Valor de 1 unidade sem passagem de cabos R${iluminacao[esc]["preco"]:.2f}')
                print(f'Valor de 3 unidades sem passagem de cabos R${iluminacao[esc]["preco2"]:.2f}')
                print(f'Valor de 1 unidade com passagem de cabos R${iluminacao[esc]["preco1"]:.2f}')
                print(f'Valor de 3 unidades com passagem de cabosR${iluminacao[esc]["preco3"]:.2f}')
                print('')
                print('-='*30)
                print('')
                while True:
                    print('')
                    op = int(input(f'Digite a quantidade de {iluminacao[esc]["item"]} a serem intalados '))
                    while True:
                        print('')
                        op2 = str(input(f'Total de {op} {iluminacao[esc]["item"]} a serem instaladas a quantidade está correta[S/N]? ')).upper()[0]
                        if op2 in "SN":
                            break
                        else:
                            print('Erro! Digite apenas sim ou não ')
                    if op2 == "S":
                        break
            
                while True:
                    print('')
                    op3 = str(input('Com passagem de cabos [S/N]')).upper()[0]
                        
                    if op3 in 'SN':
                        break
                    else:
                        print('Erro! Digite apenas sim ou não.')
                  
                if op > 2 and op3 == 'N' :
                    result = op * iluminacao[esc]["preco2"]
                    print(iluminacao[esc]["preco2"])
                elif op > 2 and op3 == "S":
                    result = op * iluminacao[esc]["preco1"]
                elif op3 == 'N':
                    result = iluminacao[esc]["preco"]
                else:
                    result = iluminacao[esc]["preco3"]
                dados.append(iluminacao[esc]["item"])
                dados.append(op)
                dados.append(op3)
                dados.append(result)
                orc.append(dados[:])
                dados.clear()


            while True:
                print('')
                resp = str(input('Deseja continuar em iluminação[S/N]?')).upper()[0]
                if resp in "SN":
                    break
            if resp == 'N':
                break 
    elif cond == 2:
        print('cod            Serviço')
        print('-=*'*30)
        for k, v in enumerate(pontoUtilizacao):
            print(f'{k} - {v["item"]}')
        print('')
        print('-=*'*30)
        print('')
        # while True:
        #     op = int(input('Digite um codigo para o serviço'))
        #     if op > len(pontoUtilizacao):
        #         print('Erro! não existe serviço com esse código')
        #     else:
        #         break
        # while True:
        #     op2 = int(input(f'Digite a quantidade de {pontoUtilizacao[op]["item"]}'))
        #     op3 = str(input(f'Total de {op} - {pontoUtilizacao[op]["item"]} esta correta[S/N]?')).upper()[0]
        #     if op3 == "S":
        #         break
       

print('-='*30)
print('')           
print('Itens com passagem de cabos')
print('-'*60)
print('')                   
for i in orc:
    if i[2] == 'S':
        print(f'{i[0]} x {i[1]} = {i[3]}')
        total += i[3]
print('-'*60)
print('')
print('Itens sem passagem de cabos')
print('-'*60)
print('')
for i in orc:
    if i[2] == 'N':
        print(f'{i[0]} x {i[1]} = {i[3]}')
        total += i[3]
print('-'*60)
print('')
print('-='*30)
print('')
print(f'Valor total da mão de obra R${total:.2f}')
print('')
print('-='*30)


                     
    