from time import sleep


print('================================= \n| COD |     PRODUTO     | VALOR  | \n| 100 | Cachorro quente |R$ 8.00 | \n'
      '| 101 | Hamburguer      |R$ 25.00|\n| 102 | Suco            |R$ 3.00 |\n| 103 | Refrigerante 2l |R$ 6.00 | \n'
      '| 104 | Salgado         |R$ 4.00 |\n| 105 | Pizza           |R$ 35.00| \n| 106 | Batata Frita    |R$ 14.00|\n'
      '==================================\nFINALIZAR PEDIDO DIGITE 0')

menu = {

    '100': ['Cachorro quente', 8.00],
    '101': ['Hamburguer', 25.00],
    '102': ['Suco', 3.00],
    '103': ['Refrigerente 2L', 6.00],
    '104': ['Salgado', 4.00],
    '105': ['Pizza', 35.00],
    '106': ['Batata Frita', 14.00]
}
name = str(input('\nInforme o seu nome: '))
pedido = {}
while True:
    codigo = input('Informe o codigo Do seu pedido sr(a){}: '.format(name))
    if (codigo == '0'):
        break
    if codigo in menu:
        quantidade = int(input('Informe a quantidade: '))
        if quantidade > 0:
            valorItem = menu.get(codigo)
            pedido.update({codigo: (valorItem, quantidade)})

valorDoPedido = 0

for linha in pedido.items():
    valorDoPedido += linha[1][0][1] * linha[1][1]  # Preço * Quantidade

print('\nSEU PEDIDO: ')

for linha in pedido.items():
    print(str(linha[1][1]) + ' x ' + str(linha[1][0][0]) + ' --- ' + 'R$ ' + str(round(linha[1][0][1], 2)))

print('\nO VALOR TOTAL DO PEDIDO: R$ ' + str(round(valorDoPedido, 2)))

print('\nESCOLHA A FORMA DE PAGAMENTO !')
print('[1] á vista dinheiro \n[2]Cartão de Debito \n[3]Picpay\n[4]Cartão de Credito')

op = int(input('\nQual a opção acima escolhida: '))

if op == 1:
    print('Pagamento Confirmado !!')
if op == 2:
    print('Pagamento no Cartão de Debito...')
    sleep(2)
    print('Pagamento Confirmado !!')
if op == 3:
    print('Pagamento Picpay...')
    sleep(2)
    print('Pagamento Confirmado !!')
if op == 4:
    print('Pagamento Cartão De Credito...')
    sleep(2)
    print('Pagamento Confirmado !!')

print('\nOBRIGADO E VOLTE SEMPRE !!')
