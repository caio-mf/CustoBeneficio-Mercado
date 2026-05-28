print('\n\nCompare os produtos e descubra qual vale mais a pena\n')

peso1 = int(input('Digite o peso do 1º Produto: '))
valor1 = float(input('Agora digite o valor do 1º Produto: '))
peso2 = int(
    input('Certo, agora vamos comparar com o 2º Produto, digite o peso: '))
valor2 = float(input('Pra finalizar o valor deste 2º Produto: '))

pkilo1 = 1000*(valor1/peso1) # Preço do kg do 1º Produto
pkilo2 = 1000*(valor2/peso2) # Preço do kg do 2º Produto

print(f'\n\nO 1º Produto está custando {pkilo1:.2f} reais o kg')

print(f'\nEnquanto o 2º Produto está {pkilo2:.2f} reais o kg')
