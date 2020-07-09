from uteis import interface,source,controller

interface.menu(source.servicos)
controller.escolhaCategoria()







    
# def mostrarLista(lista,msg):
#     menuCima()
#     print(f'          {msg}')
#     menuBaixo()
#     for v in range (0,len(lista)):
#         menuCima()
#         print(f'{lista[v]["item"]}')
#         menuBaixo()
#         print(f'sem passagem de cabos')
#         separaCima()
#         print(f'1 - UNIDADE R${lista[v]["preco"]:.2f}')
#         print(f'3 - ou + UNIDADES R${lista[v]["preco2"]:.2f}')
#         separaBaixo()
#         separaCima()
#         print('Com passagem de cabos')
#         print(f'1 - UNIDADE R${lista[v]["preco1"]:.2f}')
#         print(f'3 - ou + UNIDADES R${lista[v]["preco3"]:.2f}')
#         separaBaixo()
#     print('* Os preços acima são apenas uma base para orientação de valor por serviço dos profissionais da área elétrica.')
#     print('* Os valores podem variar de acordo com a região de cada profissional, é importante fazer uma pesquisa de mercado na sua região!')
#     print('* Os preços acima são o resultado de uma pesquisa com 2 mil votos de vários profissionais da área em diferentes regiões do país.')
#     print('* Os preços acima são referentes apenas ao valor da mão de obra, NÃO ESTÁ INCLUSO O MATERIAL necessário para execução.')
#     menuBaixo()

# def menu(lista,msg):
#     menuCima()
#     print(f'          {msg}')
#     menuBaixo()
#     for k, v in enumerate(lista):
#         print(f'{k} - {v["item"]}')
#     menuBaixo()
#     s = int(input('Digite o código do serviço para orçar: '))
#     return s


# def calcula(lista,s,msg):
#     dados = list()
#     dados.append(lista[s]["item"])
#     while True:
#         while True:
#             quant = int(input(f'Digite a quantidade de {lista[s]["item"]}: '))
#             resp = str(input(f'São no total {quant} {lista[s]["item"]}. Está correta?[S/N]? ')).upper()[0]
#             if resp in "SN":
#                 break
#             else:
#                 erro()

#         if resp == 'S':
#             break
#     while True:
#         resp = str(input('Com passagem de cabos[S/N]')).upper()[0]
#         if resp in 'SN':
#             break
#         else:
#             erro()
#     dados.append(resp)
#     if quant > 2 and resp == 'S':
#         dados.append(quant)
#         dados.append(lista[s]["preco3"])
#         dados.append(lista[s]["preco3"]*quant)
#     elif quant > 2 and resp == 'N':
#         dados.append(quant)
#         dados.append(lista[s]["preco1"])
#         dados.append(lista[s]["preco1"]*quant)
#     elif quant <= 2 and resp == 'N':
#         dados.append(quant)
#         dados.append(lista[s]["preco"])
#         dados.append(lista[s]["preco"]*quant)
#     else:
#         dados.append(quant)
#         dados.append(lista[s]["preco2"])
#         dados.append(lista[s]["preco2"]*quant)
#     orc.append(dados[:])
#     dados.clear()
#     while True:
#         resp = str(input(f'Para continuar em {msg} Digite sim, para retornar ao meu principal digite não: ')).upper()[0]
#         if resp in 'SN':
#             break
#         else:
#             erro()
#     return resp

# def mostrarOrc():
#     menuCima()

#     print('Itens com passagem de cabos')
#     menuBaixo()
#     separaCima()
#     for c in range(0,len(orc)):
#         if orc[c][1] == 'S':
#             print(f'Item:{orc[c][0]} quantidade = {orc[c][2]} valor unitário = {orc[c][3]} valor total = {orc[c][4]}')
#     separaBaixo()
#     menuCima()
#     print('Itens sem passagem de cabos')
#     menuBaixo()
#     for c in range(0,len(orc)):
#         if orc[c][1] == 'N':
#             print(f'Item:{orc[c][0]} quantidade = {orc[c][2]} valor unitário = {orc[c][3]} valor total = {orc[c][4]}')
#     separaBaixo()
#     menuBaixo()
#     total = 0
#     for c in range(0,len(orc)):
#         total += orc[c][4]
#     print(f'Valor total = {total}')
    
  
# while True:
#     if cond == 0:
#         break
#     menuCima()
#     print('              Menu principal')
#     menuBaixo()
#     print('Cod        Tabela Serviços')
#     separaCima()
#     for c in range(0,len(source.servicos)):
#         print(f'{c} - {servicos[c]}')
#     separaBaixo()
#     cond = int(input('Digite o número correspondente\n'))
#     if cond == 1:
#         while True:
#             s = menu(iluminacao,'iluminação')
#             resp = calcula(iluminacao,s,servicos[1])
#             if resp == 'N':
#                 break
#     elif cond == 2:
#         while True:
#             s = menu(pontoUtilizacao,'Ponto de ultilização')
#             resp = calcula(pontoUtilizacao,s,servicos[2])
#             if resp == 'N':
#                 break

#     elif cond == 3:
#         while True:
#             s = menu(qdc,'QDC')
#             resp = calcula(qdc,s,servicos[3])
#             if resp == 'N':
#                 break
#     elif cond == 4:
#         while True:
#             s = menu(passagemcabo20m, 'Passagem de cabos até 20m')
#             resp = calcula(passagemcabo20m,s,servicos[4])
#             if resp == 'N':
#                 break
#     elif cond == 5:
#         while True:
#             s = menu(soluceletrica,'solução de problemas elétricos')
#             resp = calcula(soluceletrica,s,servicos[5])
#             if resp == 'N':
#                 break
#     elif cond == 6:
#         c = detalhaPreco(servicos)
#         msg = servicos[c]
#         if c == 1:
#             mostrarLista(iluminacao,msg)
#         elif c ==2:
#                 mostrarLista(pontoUtilizacao,msg)
#         elif c == 3:
#             mostrarLista(qdc,msg)
#         elif c == 4:
#             mostrarLista(passagemcabo20m,msg)
#         elif c == 5:
#             mostrarLista(soluceletrica,msg)
# mostrarOrc()
# mostrarOrc()


    