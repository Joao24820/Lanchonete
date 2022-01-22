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
