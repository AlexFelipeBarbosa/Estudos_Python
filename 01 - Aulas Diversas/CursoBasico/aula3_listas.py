# listas 
vendas = [100, 50, 14, 20, 30, 700]

# soma dos elementos da lista
total_vendas = sum(vendas)
print(total_vendas)

# tamanho da lista
quantidade_vendas = len(vendas)
print(quantidade_vendas)

# maximo e minimo
print(max(vendas))
print(min(vendas))

# pegar a primeira venda
print(vendas[0])

lista_produtos = ['iphone', 'airpod', 'ipad', 'macbook']

# Verificando se um produto existe na lista
print("aplle watch" in lista_produtos) # retorna: TRUE ou FALSE
print("iphone" in lista_produtos)

produto_procurado = input("Pesquise pelo nome do produto: ")
produto_procurado = produto_procurado.lower()
print(produto_procurado in lista_produtos)

